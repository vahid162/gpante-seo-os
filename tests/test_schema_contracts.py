import datetime as dt
import json
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker, exceptions
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
FORMAT_CHECKER = FormatChecker()


def load_json(path):
    return json.loads(path.read_text())


def load_yaml(path):
    return yaml.safe_load(path.read_text())


def load_front_matter(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        raise AssertionError(f"missing YAML front matter: {path}")
    return yaml.safe_load(text.split("---\n", 2)[1])


def registry():
    resources = []
    for path in SCHEMAS.glob("*.schema.json"):
        schema = load_json(path)
        resources.append((schema["$id"], Resource.from_contents(schema)))
        resources.append((schema["$id"].removeprefix("./"), Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def validator(schema_name):
    schema = load_json(SCHEMAS / schema_name)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, registry=registry(), format_checker=FORMAT_CHECKER)


class SchemaContractsTest(unittest.TestCase):
    def test_all_schemas_parse_check_and_local_references_resolve(self):
        reg = registry()
        for path in SCHEMAS.glob("*.schema.json"):
            schema = load_json(path)
            self.assertEqual("https://json-schema.org/draft/2020-12/schema", schema["$schema"])
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema, registry=reg, format_checker=FORMAT_CHECKER)

        refs = []
        def collect_refs(node):
            if isinstance(node, dict):
                if "$ref" in node:
                    refs.append(node["$ref"])
                for value in node.values():
                    collect_refs(value)
            elif isinstance(node, list):
                for value in node:
                    collect_refs(value)
        for path in SCHEMAS.glob("*.schema.json"):
            collect_refs(load_json(path))
        resolver = reg.resolver()
        for ref in refs:
            resolver.lookup(ref)

        instances = [
            ("project.schema.json", load_yaml(ROOT / "project.yaml")),
            ("run-state.schema.json", load_yaml(ROOT / "runs/_template/state.yaml")),
            ("decision.schema.json", load_front_matter(ROOT / "decisions/decision-template.md")),
            ("task.schema.json", load_front_matter(ROOT / "tasks/task-template.md")),
            ("evidence.schema.json", load_front_matter(ROOT / "runs/_template/evidence/_evidence-template.md")),
            ("finding.schema.json", load_front_matter(ROOT / "runs/_template/findings/_finding-template.md")),
        ]
        for schema_name, instance in instances:
            validator(schema_name).validate(instance)

    def assert_valid(self, schema_name, instance):
        validator(schema_name).validate(instance)

    def assert_invalid(self, schema_name, instance, expected_fragment):
        with self.assertRaises(exceptions.ValidationError) as ctx:
            validator(schema_name).validate(instance)
        self.assertIn(expected_fragment, ctx.exception.message)

    def test_project_yaml_validates_against_project_schema(self):
        self.assert_valid("project.schema.json", load_yaml(ROOT / "project.yaml"))

    def test_run_state_template_validates_against_run_state_schema(self):
        self.assert_valid("run-state.schema.json", load_yaml(ROOT / "runs/_template/state.yaml"))

    def test_real_decisions_validate_against_decision_schema(self):
        for path in [
            ROOT / "decisions/DEC-2026-001-site-knowledge-canonical-location.md",
            ROOT / "decisions/DEC-2026-002-record-first-machine-validation-architecture.md",
        ]:
            self.assert_valid("decision.schema.json", load_front_matter(path))

    def test_record_templates_validate_against_record_schemas(self):
        cases = [
            ("decision.schema.json", ROOT / "decisions/decision-template.md"),
            ("task.schema.json", ROOT / "tasks/task-template.md"),
            ("evidence.schema.json", ROOT / "runs/_template/evidence/_evidence-template.md"),
            ("finding.schema.json", ROOT / "runs/_template/findings/_finding-template.md"),
        ]
        for schema_name, path in cases:
            self.assert_valid(schema_name, load_front_matter(path))

    def test_quoted_iso_date_fixture_validates(self):
        instance = load_yaml(ROOT / "tests/fixtures/schema/valid/quoted_iso_date_decision.yaml")
        self.assertIsInstance(instance["date"], str)
        self.assert_valid("decision.schema.json", instance)

    def test_real_records_with_findings_require_related_run(self):
        cases = [
            ("decision.schema.json", "decision_findings_without_related_run.yaml"),
            ("task.schema.json", "task_findings_without_related_run.yaml"),
        ]
        for schema_name, fixture in cases:
            with self.assertRaises(exceptions.ValidationError) as ctx:
                validator(schema_name).validate(
                    load_yaml(ROOT / "tests/fixtures/schema/invalid" / fixture)
                )
            self.assertEqual(["related_run"], list(ctx.exception.absolute_path))
            self.assertEqual("None is not of type 'string'", ctx.exception.message)

    def test_real_records_with_findings_validate_with_related_run(self):
        cases = [
            ("decision.schema.json", "decision_findings_with_related_run.yaml"),
            ("task.schema.json", "task_findings_with_related_run.yaml"),
        ]
        for schema_name, fixture in cases:
            instance = load_yaml(ROOT / "tests/fixtures/schema/valid" / fixture)
            self.assert_valid(schema_name, instance)

            instance["related_run"] = None
            instance["related_findings"] = []
            self.assert_valid(schema_name, instance)

    def test_invalid_fixtures_fail_with_expected_causes(self):
        cases = [
            ("decision.schema.json", "invalid_record_type.yaml", "'decision' was expected"),
            ("task.schema.json", "invalid_status.yaml", "is not one of"),
            ("decision.schema.json", "malformed_id.yaml", "does not match"),
            ("decision.schema.json", "placeholder_in_real_record.yaml", "does not match"),
            ("decision.schema.json", "owner_required_in_real_record.yaml", "should not be valid"),
            ("finding.schema.json", "missing_required_metadata.yaml", "is a required property"),
            ("decision.schema.json", "invalid_calendar_date.yaml", "is not a 'date'"),
        ]
        for schema_name, fixture, expected in cases:
            self.assert_invalid(schema_name, load_yaml(ROOT / "tests/fixtures/schema/invalid" / fixture), expected)

    def test_unquoted_yaml_date_is_not_silently_normalized(self):
        instance = load_yaml(ROOT / "tests/fixtures/schema/invalid/unquoted_yaml_date.yaml")
        self.assertIsInstance(instance["date"], dt.date)
        self.assert_invalid("decision.schema.json", instance, "is not of type 'string'")


if __name__ == "__main__":
    unittest.main()
