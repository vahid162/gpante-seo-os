import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_repository import ValidationResult, format_result, validate_repository  # noqa: E402


def front(data):
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n# Body\n"


def read_front(path):
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---\n", 2)[1])


def write_front(path, data):
    path.write_text(front(data), encoding="utf-8")


class RepositoryValidatorTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        ignore = shutil.ignore_patterns(".git", ".venv", "__pycache__", "*.pyc")
        shutil.copytree(ROOT, self.root, ignore=ignore)

    def tearDown(self):
        self.tmp.cleanup()

    def result(self):
        return validate_repository(self.root)

    def assertInvalidContains(self, fragment):
        result = self.result()
        self.assertNotEqual(0, result.exit_code)
        self.assertIn(fragment, format_result(result))
        return result

    def records_in_run(self, result, run_id, record_type):
        return [record for record in result.records if record.run_id == run_id and record.record_type == record_type]

    def add_run(self, run_id="2026-07-24-test-run", evidence_id="EV-001", finding_id="FND-001"):
        run = self.root / "runs" / run_id
        (run / "evidence").mkdir(parents=True)
        (run / "findings").mkdir()
        (run / "evidence" / "README.md").write_text("# Evidence directory\n", encoding="utf-8")
        (run / "findings" / "README.md").write_text("# Findings directory\n", encoding="utf-8")
        (run / "state.yaml").write_text(yaml.safe_dump({
            "schema_version": 1,
            "record_type": "run_state",
            "is_template": False,
            "run_id": run_id,
            "status": "initialized",
            "workflow_stage": "intake",
            "mode": {"audit_only": True, "production_write": False},
            "approval": {"required": True, "status": "pending"},
            "owner": "repo-owner",
            "created_at": "2026-07-24",
            "updated_at": "2026-07-24",
        }, sort_keys=False), encoding="utf-8")
        write_front(run / "evidence" / "ev-001.md", {
            "schema_version": 1,
            "record_type": "evidence",
            "is_template": False,
            "evidence_id": evidence_id,
            "title": "Synthetic evidence",
            "owner": "repo-owner",
            "collected_at": "2026-07-24",
            "source_type": "repository_document",
            "scope": "Synthetic fixture",
            "classification": "repository-safe",
            "sanitized": False,
            "storage": "markdown_summary",
            "related_run": run_id,
            "related_findings": [],
        })
        write_front(run / "findings" / "fnd-001.md", {
            "schema_version": 1,
            "record_type": "finding",
            "is_template": False,
            "finding_id": finding_id,
            "title": "Synthetic finding",
            "status": "confirmed",
            "owner": "repo-owner",
            "related_run": run_id,
            "evidence": [evidence_id],
            "severity": "Medium",
            "risk": "Medium",
            "confidence": "Medium",
            "related_decisions": [],
            "related_tasks": [],
            "supersedes": None,
            "superseded_by": None,
        })
        return run

    def add_task(self, task_id="TSK-2026-123", filename="TSK-2026-123-fix-canonical-routing.md"):
        path = self.root / "tasks" / filename
        write_front(path, {
            "schema_version": 1,
            "record_type": "task",
            "is_template": False,
            "task_id": task_id,
            "title": "Synthetic task",
            "status": "proposed",
            "priority": "Medium",
            "owner": "repo-owner",
            "implementation_owner": "repo-owner",
            "related_run": None,
            "related_findings": [],
            "related_decisions": [],
            "approval": {"required": True, "status": "pending"},
            "risk": "Medium",
            "implementation_mode": "manual",
            "dependencies": [],
            "validation_result": "pending",
            "backup_required": False,
            "backup_verified": False,
        })
        return path

    def snapshot(self):
        return {
            path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(item for item in self.root.rglob("*") if item.is_file())
        }

    def test_current_repository_validates(self):
        result = validate_repository(ROOT)
        self.assertEqual([], result.sorted_errors, format_result(result))
        self.assertEqual(0, result.exit_code)

    def test_real_run_evidence_readme_is_ignored(self):
        run = self.add_run()
        result = self.result()
        self.assertEqual(0, result.exit_code, format_result(result))
        records = self.records_in_run(result, run.name, "evidence")
        self.assertEqual(["runs/2026-07-24-test-run/evidence/ev-001.md"], [record.relative_path for record in records])

    def test_real_run_findings_readme_is_ignored(self):
        run = self.add_run()
        result = self.result()
        self.assertEqual(0, result.exit_code, format_result(result))
        records = self.records_in_run(result, run.name, "finding")
        self.assertEqual(["runs/2026-07-24-test-run/findings/fnd-001.md"], [record.relative_path for record in records])

    def test_known_evidence_template_filename_inside_real_run_is_ignored(self):
        run = self.add_run()
        (run / "evidence" / "_evidence-template.md").write_text("# Not a record\n", encoding="utf-8")
        result = self.result()
        self.assertEqual(0, result.exit_code, format_result(result))
        self.assertEqual(1, len(self.records_in_run(result, run.name, "evidence")))

    def test_known_finding_template_filename_inside_real_run_is_ignored(self):
        run = self.add_run()
        (run / "findings" / "_finding-template.md").write_text("# Not a record\n", encoding="utf-8")
        result = self.result()
        self.assertEqual(0, result.exit_code, format_result(result))
        self.assertEqual(1, len(self.records_in_run(result, run.name, "finding")))

    def test_finding_template_filename_under_evidence_is_not_silently_ignored(self):
        run = self.add_run()
        (run / "evidence" / "_finding-template.md").write_text("# Misplaced\n", encoding="utf-8")
        result = self.assertInvalidContains("_finding-template.md")
        self.assertEqual(1, result.exit_code)

    def test_evidence_template_filename_under_findings_is_not_silently_ignored(self):
        run = self.add_run()
        (run / "findings" / "_evidence-template.md").write_text("# Misplaced\n", encoding="utf-8")
        result = self.assertInvalidContains("_evidence-template.md")
        self.assertEqual(1, result.exit_code)

    def test_missing_project_yaml_fails_as_configuration_error(self):
        (self.root / "project.yaml").unlink()
        result = self.assertInvalidContains("project.yaml")
        self.assertEqual(2, result.exit_code)
        self.assertTrue(any(error.category == "configuration" and error.path == "project.yaml" for error in result.errors))

    def test_missing_run_template_state_fails_as_configuration_error(self):
        (self.root / "runs" / "_template" / "state.yaml").unlink()
        result = self.assertInvalidContains("runs/_template/state.yaml")
        self.assertEqual(2, result.exit_code)
        self.assertTrue(any(error.category == "configuration" for error in result.errors))

    def test_missing_canonical_record_template_fails_as_configuration_error(self):
        (self.root / "tasks" / "task-template.md").unlink()
        result = self.assertInvalidContains("tasks/task-template.md")
        self.assertEqual(2, result.exit_code)
        self.assertTrue(any(error.category == "configuration" for error in result.errors))

    def test_real_run_missing_state_yaml_fails_as_record_error(self):
        run = self.add_run()
        (run / "state.yaml").unlink()
        result = self.assertInvalidContains("Real Run is missing required machine-readable state.yaml")
        self.assertEqual(1, result.exit_code)
        self.assertTrue(any(error.category == "record" and error.path == "runs/2026-07-24-test-run/state.yaml" for error in result.errors))

    def test_path_record_type_mismatch_fails(self):
        cases = [
            (self.root / "decisions" / "DEC-2026-001-site-knowledge-canonical-location.md", "task", "decision"),
            (self.add_task(), "decision", "task"),
            (self.add_run() / "evidence" / "ev-001.md", "finding", "evidence"),
            (self.root / "runs" / "2026-07-24-test-run" / "findings" / "fnd-001.md", "evidence", "finding"),
            (self.root / "tasks" / "task-template.md", "decision", "task"),
        ]
        for path, actual, expected in cases:
            data = read_front(path)
            data["record_type"] = actual
            write_front(path, data)
            result = self.result()
            self.assertTrue(any(error.category == "semantic" and error.field == "record_type" and expected in error.message and actual in error.message for error in result.errors), format_result(result))
            data["record_type"] = expected
            write_front(path, data)

    def test_real_paths_cannot_masquerade_as_templates(self):
        self.add_run()
        self.add_task()
        paths = [
            self.root / "runs" / "2026-07-24-test-run" / "state.yaml",
            self.root / "decisions" / "DEC-2026-001-site-knowledge-canonical-location.md",
            self.root / "tasks" / "TSK-2026-123-fix-canonical-routing.md",
            self.root / "runs" / "2026-07-24-test-run" / "evidence" / "ev-001.md",
            self.root / "runs" / "2026-07-24-test-run" / "findings" / "fnd-001.md",
        ]
        for path in paths:
            if path.suffix == ".yaml":
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
                data["is_template"] = True
                path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
            else:
                data = read_front(path)
                data["is_template"] = True
                write_front(path, data)
        result = self.assertInvalidContains("is_template must match canonical path")
        self.assertEqual(1, result.exit_code)

    def test_template_paths_must_remain_templates(self):
        paths = [
            self.root / "runs" / "_template" / "state.yaml",
            self.root / "decisions" / "decision-template.md",
            self.root / "tasks" / "task-template.md",
            self.root / "runs" / "_template" / "evidence" / "_evidence-template.md",
            self.root / "runs" / "_template" / "findings" / "_finding-template.md",
        ]
        for path in paths:
            if path.suffix == ".yaml":
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
                data["is_template"] = False
                path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
            else:
                data = read_front(path)
                data["is_template"] = False
                write_front(path, data)
        result = self.assertInvalidContains("Expected True, found False")
        self.assertEqual(1, result.exit_code)

    def test_task_filename_and_task_id_agree_is_valid(self):
        self.add_task()
        self.assertEqual(0, self.result().exit_code, format_result(self.result()))

    def test_task_filename_with_another_task_id_fails(self):
        self.add_task(task_id="TSK-2026-123", filename="TSK-2026-124-fix-canonical-routing.md")
        self.assertInvalidContains("Real Task filename must use TSK-2026-123-")

    def test_task_filename_without_descriptive_suffix_fails(self):
        self.add_task(task_id="TSK-2026-123", filename="TSK-2026-123.md")
        self.assertInvalidContains("lowercase-kebab-case-title")

    def test_task_filename_suffix_must_be_lowercase_kebab_case(self):
        self.add_task(task_id="TSK-2026-123", filename="TSK-2026-123-Fix_Canonical.md")
        self.assertInvalidContains("lowercase-kebab-case-title")

    def test_task_without_canonical_filename_is_discovered_and_fails(self):
        self.add_task(filename="fix-canonical-routing.md")

        result = self.result()

        self.assertIn(
            "tasks/fix-canonical-routing.md",
            [record.relative_path for record in result.records],
        )
        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.path == "tasks/fix-canonical-routing.md"
            and error.field == "filename"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertEqual(
            "Real Task filename must use TSK-2026-123-<lowercase-kebab-case-title>.md.",
            errors[0].message,
        )

    def test_misnamed_decision_is_discovered_and_checked_for_uniqueness(self):
        path = self.root / "decisions" / "misnamed-decision.md"
        source = self.root / "decisions" / "DEC-2026-001-site-knowledge-canonical-location.md"
        write_front(path, read_front(source))

        result = self.result()

        real_decision_paths = {
            record.relative_path
            for record in result.records
            if record.expected_record_type == "decision"
            and record.expected_is_template is False
        }
        self.assertIn("decisions/misnamed-decision.md", real_decision_paths)
        self.assertTrue(
            {
                "decisions/README.md",
                "decisions/index.md",
                "decisions/decision-template.md",
            }.isdisjoint(real_decision_paths)
        )
        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.category == "semantic"
            and error.path == "decisions/misnamed-decision.md"
            and error.record_id == "DEC-2026-001"
            and "Decision ID must be repository-unique." in error.message
        ]
        self.assertEqual(1, len(errors), format_result(result))

    def test_valid_front_matter_parses(self):
        self.add_run()
        self.assertEqual(0, self.result().exit_code, format_result(self.result()))

    def test_missing_exact_closing_front_matter_delimiter_fails(self):
        path = self.root / "decisions" / "DEC-2026-999-no-close.md"
        path.write_text("---\nrecord_type: decision\nis_template: false\n# no closing delimiter\n", encoding="utf-8")
        self.assertInvalidContains("missing closing YAML front matter delimiter")

    def test_non_delimiter_line_does_not_close_front_matter(self):
        path = self.root / "decisions" / "DEC-2026-999-bad-close.md"
        path.write_text("---\nrecord_type: decision\n---not-a-delimiter\n# Body\n", encoding="utf-8")
        self.assertInvalidContains("missing closing YAML front matter delimiter")

    def test_invalid_json_schema_fails(self):
        (self.root / "schemas" / "bad.schema.json").write_text('{"$schema": "https://json-schema.org/draft/2020-12/schema", "type": 7}', encoding="utf-8")
        self.assertInvalidContains("JSON Schema check failed")

    def test_missing_schema_dialect_returns_controlled_error(self):
        path = self.root / "schemas" / "task.schema.json"
        schema = json.loads(path.read_text(encoding="utf-8"))
        del schema["$schema"]
        path.write_text(json.dumps(schema), encoding="utf-8")

        result = self.result()

        self.assertIsInstance(result, ValidationResult)
        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.path == "schemas/task.schema.json" and error.field == "$schema"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertEqual(
            "Schema must declare JSON Schema Draft 2020-12 in $schema.",
            errors[0].message,
        )

    def test_unsupported_schema_dialect_returns_controlled_error(self):
        path = self.root / "schemas" / "task.schema.json"
        schema = json.loads(path.read_text(encoding="utf-8"))
        schema["$schema"] = "https://json-schema.org/draft/2019-09/schema"
        path.write_text(json.dumps(schema), encoding="utf-8")

        result = self.result()

        self.assertIsInstance(result, ValidationResult)
        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.path == "schemas/task.schema.json" and error.field == "$schema"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertEqual(
            "Schema must declare JSON Schema Draft 2020-12 in $schema.",
            errors[0].message,
        )

    def test_non_object_json_schema_returns_controlled_error(self):
        path = self.root / "schemas" / "task.schema.json"
        path.write_text("[]", encoding="utf-8")

        result = self.result()

        self.assertIsInstance(result, ValidationResult)
        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.category == "schema"
            and error.path == "schemas/task.schema.json"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertEqual(
            "Schema document must be a JSON object.",
            errors[0].message,
        )
        self.assertNotIn("[]", format_result(result))

    def test_markdown_without_front_matter_fails(self):
        (self.root / "decisions" / "DEC-2026-999-no-front-matter.md").write_text("# No front matter\n", encoding="utf-8")
        self.assertInvalidContains("must start with YAML front matter")

    def test_bad_front_matter_fails(self):
        (self.root / "decisions" / "DEC-2026-999-bad-yaml.md").write_text("---\nrecord_type: [\n---\n", encoding="utf-8")
        self.assertInvalidContains("YAML front matter parse failed")

    def test_unknown_record_type_fails(self):
        (self.root / "decisions" / "DEC-2026-999-unknown.md").write_text(front({"record_type": "unknown", "is_template": False}), encoding="utf-8")
        self.assertInvalidContains("Unknown record_type")

    def test_duplicate_evidence_id_in_same_run_fails(self):
        run = self.add_run()
        shutil.copy(run / "evidence" / "ev-001.md", run / "evidence" / "ev-dup.md")
        self.assertInvalidContains("Evidence ID must be unique within its Run")

    def test_same_evidence_id_in_different_runs_allowed(self):
        self.add_run("2026-07-24-test-one")
        self.add_run("2026-07-25-test-two")
        self.assertEqual(0, self.result().exit_code, format_result(self.result()))

    def test_duplicate_finding_id_in_same_run_fails(self):
        run = self.add_run()
        shutil.copy(run / "findings" / "fnd-001.md", run / "findings" / "fnd-dup.md")
        self.assertInvalidContains("Finding ID must be unique within its Run")

    def test_same_finding_id_in_different_runs_allowed(self):
        self.add_run("2026-07-24-test-one")
        self.add_run("2026-07-25-test-two")
        self.assertEqual(0, self.result().exit_code, format_result(self.result()))

    def test_missing_finding_evidence_fails(self):
        run = self.add_run()
        path = run / "findings" / "fnd-001.md"
        path.write_text(path.read_text(encoding="utf-8").replace("EV-001", "EV-999"), encoding="utf-8")
        self.assertInvalidContains("Finding evidence reference must resolve within the same Run")

    def test_finding_cannot_resolve_evidence_from_other_run(self):
        run = self.add_run("2026-07-24-test-one", "EV-002")
        self.add_run("2026-07-25-test-two", "EV-001")
        path = run / "findings" / "fnd-001.md"
        path.write_text(path.read_text(encoding="utf-8").replace("EV-002", "EV-001"), encoding="utf-8")
        self.assertInvalidContains("same Run")

    def test_malformed_relationship_values_return_controlled_schema_errors(self):
        path = self.root / "decisions" / "DEC-2026-001-site-knowledge-canonical-location.md"
        for malformed in (123, [{}]):
            with self.subTest(malformed=malformed):
                data = read_front(path)
                data["related_tasks"] = malformed
                write_front(path, data)

                result = self.result()

                self.assertIsInstance(result, ValidationResult)
                self.assertNotEqual(0, result.exit_code)
                self.assertTrue(
                    any(
                        error.category == "record"
                        and error.path == "decisions/DEC-2026-001-site-knowledge-canonical-location.md"
                        and error.field.startswith("related_tasks")
                        for error in result.errors
                    ),
                    format_result(result),
                )
                self.assertFalse(
                    any(error.category == "configuration" for error in result.errors),
                    format_result(result),
                )
                self.assertFalse(
                    any(
                        error.category == "reference"
                        and error.field.startswith("related_tasks")
                        for error in result.errors
                    ),
                    format_result(result),
                )

    def test_evidence_related_run_mismatch_fails(self):
        run = self.add_run("2026-07-24-test-one")
        path = run / "evidence" / "ev-001.md"
        path.write_text(path.read_text(encoding="utf-8").replace("related_run: 2026-07-24-test-one", "related_run: 2026-07-25-test-two"), encoding="utf-8")
        result = self.assertInvalidContains("Expected '2026-07-24-test-one', found '2026-07-25-test-two'")
        self.assertTrue(any(error.category == "semantic" and error.field == "related_run" for error in result.errors))

    def test_finding_related_run_mismatch_fails(self):
        run = self.add_run("2026-07-24-test-one")
        path = run / "findings" / "fnd-001.md"
        path.write_text(path.read_text(encoding="utf-8").replace("related_run: 2026-07-24-test-one", "related_run: 2026-07-25-test-two"), encoding="utf-8")
        result = self.assertInvalidContains("Expected '2026-07-24-test-one', found '2026-07-25-test-two'")
        self.assertTrue(any(error.category == "semantic" and error.field == "related_run" for error in result.errors))

    def test_related_findings_without_related_run_fails(self):
        self.add_task(task_id="TSK-2026-999", filename="TSK-2026-999-related.md")
        path = self.root / "tasks" / "TSK-2026-999-related.md"
        data = read_front(path)
        data["related_findings"] = ["FND-001"]
        write_front(path, data)
        self.assertInvalidContains("related_findings requires related_run")

    def test_decision_missing_related_task_fails(self):
        path = self.root / "decisions" / "DEC-2026-001-site-knowledge-canonical-location.md"
        data = read_front(path)
        data["related_tasks"] = ["TSK-2026-999"]
        write_front(path, data)

        result = self.result()

        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.category == "reference"
            and error.path == "decisions/DEC-2026-001-site-knowledge-canonical-location.md"
            and error.field == "related_tasks:TSK-2026-999"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertIn("real Task record", errors[0].message)

    def test_task_missing_related_decision_fails(self):
        path = self.add_task()
        data = read_front(path)
        data["related_decisions"] = ["DEC-2026-999"]
        write_front(path, data)

        result = self.result()

        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.category == "reference"
            and error.path == "tasks/TSK-2026-123-fix-canonical-routing.md"
            and error.field == "related_decisions:DEC-2026-999"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertIn("real Decision record", errors[0].message)

    def test_repository_wide_decision_task_relationships_resolve(self):
        decision_path = self.root / "decisions" / "DEC-2026-001-site-knowledge-canonical-location.md"
        decision_data = read_front(decision_path)
        decision_data["related_tasks"] = ["TSK-2026-123"]
        write_front(decision_path, decision_data)

        task_path = self.add_task()
        task_data = read_front(task_path)
        task_data["related_decisions"] = ["DEC-2026-001"]
        write_front(task_path, task_data)

        result = self.result()

        self.assertEqual(0, result.exit_code, format_result(result))

    def test_evidence_missing_related_finding_fails(self):
        run = self.add_run()
        path = run / "evidence" / "ev-001.md"
        data = read_front(path)
        data["related_findings"] = ["FND-999"]
        write_front(path, data)

        result = self.result()

        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.category == "reference"
            and error.path == "runs/2026-07-24-test-run/evidence/ev-001.md"
            and error.field == "related_findings:FND-999"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertEqual(
            "Evidence related_finding must resolve within the same Run.",
            errors[0].message,
        )

    def test_finding_missing_related_decision_fails(self):
        run = self.add_run()
        path = run / "findings" / "fnd-001.md"
        data = read_front(path)
        data["related_decisions"] = ["DEC-2026-999"]
        write_front(path, data)

        result = self.result()

        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.category == "reference"
            and error.path == "runs/2026-07-24-test-run/findings/fnd-001.md"
            and error.field == "related_decisions:DEC-2026-999"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertEqual(
            "Finding related_decision must resolve to a real Decision record in this repository.",
            errors[0].message,
        )

    def test_finding_missing_related_task_fails(self):
        run = self.add_run()
        path = run / "findings" / "fnd-001.md"
        data = read_front(path)
        data["related_tasks"] = ["TSK-2026-999"]
        write_front(path, data)

        result = self.result()

        self.assertNotEqual(0, result.exit_code)
        errors = [
            error
            for error in result.errors
            if error.category == "reference"
            and error.path == "runs/2026-07-24-test-run/findings/fnd-001.md"
            and error.field == "related_tasks:TSK-2026-999"
        ]
        self.assertEqual(1, len(errors), format_result(result))
        self.assertEqual(
            "Finding related_task must resolve to a real Task record in this repository.",
            errors[0].message,
        )

    def test_explicit_relationship_targets_resolve(self):
        run = self.add_run()
        evidence_path = run / "evidence" / "ev-001.md"
        evidence_data = read_front(evidence_path)
        evidence_data["related_findings"] = ["FND-001"]
        write_front(evidence_path, evidence_data)

        finding_path = run / "findings" / "fnd-001.md"
        finding_data = read_front(finding_path)
        finding_data["related_decisions"] = ["DEC-2026-001"]
        finding_data["related_tasks"] = ["TSK-2026-123"]
        write_front(finding_path, finding_data)
        self.add_task()

        result = self.result()

        self.assertEqual(0, result.exit_code, format_result(result))

    def test_missing_related_finding_fails(self):
        self.add_run()
        write_front(self.root / "decisions" / "DEC-2026-999-related.md", {
            "schema_version": 1,
            "record_type": "decision",
            "is_template": False,
            "decision_id": "DEC-2026-999",
            "title": "Decision",
            "status": "proposed",
            "date": "2026-07-24",
            "owner": "repo-owner",
            "related_run": "2026-07-24-test-run",
            "related_findings": ["FND-999"],
            "related_tasks": [],
            "supersedes": None,
            "superseded_by": None,
        })
        self.assertInvalidContains("related_finding must resolve inside related_run")

    def test_run_id_mismatch_fails(self):
        run = self.add_run()
        data = yaml.safe_load((run / "state.yaml").read_text(encoding="utf-8"))
        data["run_id"] = "2026-07-24-other"
        (run / "state.yaml").write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
        self.assertInvalidContains("run_id must match")

    def test_self_reference_fails(self):
        write_front(self.root / "decisions" / "DEC-2026-999-self.md", {
            "schema_version": 1,
            "record_type": "decision",
            "is_template": False,
            "decision_id": "DEC-2026-999",
            "title": "Decision",
            "status": "proposed",
            "date": "2026-07-24",
            "owner": "repo-owner",
            "related_run": None,
            "related_findings": [],
            "related_tasks": [],
            "supersedes": "DEC-2026-999",
            "superseded_by": None,
        })
        self.assertInvalidContains("must not directly reference itself")

    def test_templates_remain_valid(self):
        result = self.result()
        template_errors = [error for error in result.sorted_errors if "template" in error.path]
        self.assertEqual([], template_errors)

    def test_error_order_and_summary_are_deterministic(self):
        self.add_run()
        (self.root / "decisions" / "DEC-2026-999-no-front-matter.md").write_text("# bad\n", encoding="utf-8")
        first = format_result(self.result())
        second = format_result(self.result())
        self.assertEqual(first, second)

    def test_validator_is_read_only(self):
        before = self.snapshot()
        validate_repository(self.root)
        after = self.snapshot()
        self.assertEqual(before, after)

    def test_cli_valid_repository_exit_zero(self):
        completed = subprocess.run([sys.executable, str(ROOT / "tools" / "validate_repository.py"), str(ROOT)], text=True, capture_output=True, check=False)
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)

    def test_cli_invalid_repository_exit_one(self):
        (self.root / "decisions" / "DEC-2026-999-no-front-matter.md").write_text("# bad\n", encoding="utf-8")
        completed = subprocess.run([sys.executable, str(ROOT / "tools" / "validate_repository.py"), str(self.root)], text=True, capture_output=True, check=False)
        self.assertEqual(1, completed.returncode, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
