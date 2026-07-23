import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def parse_scalar(value):
    value = value.strip()
    if value == "null":
        return None
    if value == "[]":
        return []
    if value == "true":
        return True
    if value == "false":
        return False
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if re.fullmatch(r"[0-9]+", value):
        return int(value)
    return value


def parse_simple_yaml(text):
    root = {}
    stack = [(-1, root)]
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if stripped.startswith("- "):
            parent = stack[-1][1]
            parent.append(parse_scalar(stripped[2:]))
            i += 1
            continue
        key, value = stripped.split(":", 1)
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value.strip():
            parent[key] = parse_scalar(value)
            i += 1
            continue
        # choose list if next meaningful line is a list item at deeper indent
        j = i + 1
        next_is_list = False
        while j < len(lines):
            nxt = lines[j]
            if nxt.strip() and not nxt.lstrip().startswith("#"):
                next_is_list = nxt.strip().startswith("- ")
                break
            j += 1
        node = [] if next_is_list else {}
        parent[key] = node
        stack.append((indent, node))
        i += 1
    return root


def load_yaml(path):
    return parse_simple_yaml(path.read_text())


def load_front_matter(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        raise AssertionError(f"missing YAML front matter: {path}")
    return parse_simple_yaml(text.split("---\n", 2)[1])


def assert_keys(testcase, data, required, allowed):
    testcase.assertEqual([], [k for k in required if k not in data])
    testcase.assertEqual([], [k for k in data if k not in allowed])


def is_real_id(kind, value):
    patterns = {
        "decision": r"^DEC-[0-9]{4}-[0-9]{3}$",
        "task": r"^TSK-[0-9]{4}-[0-9]{3}$",
        "evidence": r"^EV-[0-9]{3}$",
        "finding": r"^FND-[0-9]{3}$",
        "run": r"^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*$",
    }
    return isinstance(value, str) and re.match(patterns[kind], value)


DECISION_STATUSES = {"proposed", "approved", "rejected", "superseded"}
TASK_STATUSES = {"proposed", "approved", "ready", "in_progress", "validation_pending", "completed", "blocked", "rejected", "cancelled", "rolled_back"}
FINDING_STATUSES = {"draft", "confirmed", "deferred", "resolved", "rejected", "superseded"}
RUN_STATUSES = {"initialized", "in_progress", "blocked", "completed", "cancelled", "archived"}
STAGES = {"intake", "scope", "evidence", "analysis", "findings", "prioritization", "decisions", "task_definition", "approval", "implementation", "validation", "monitoring", "closed"}


class SchemaContractsTest(unittest.TestCase):
    def test_all_schemas_parse_and_local_references_resolve(self):
        ids = {}
        for path in SCHEMAS.glob("*.schema.json"):
            schema = json.loads(path.read_text())
            self.assertEqual("https://json-schema.org/draft/2020-12/schema", schema["$schema"])
            self.assertIn("$id", schema)
            ids[schema["$id"]] = schema
        refs = re.findall(r'"\$ref"\s*:\s*"([^"]+)"', "\n".join(p.read_text() for p in SCHEMAS.glob("*.schema.json")))
        for ref in refs:
            target = ref.split("#", 1)[0]
            self.assertIn(target if target in ids else "./" + target, ids)

    def test_project_yaml_validates(self):
        data = load_yaml(ROOT / "project.yaml")
        self.assertEqual(1, data["schema_version"])
        self.assertEqual("gpante-seo-os", data["repository"]["name"])
        self.assertEqual("1.0.0-alpha.1", data["repository"]["version"])
        self.assertEqual("foundation", data["maturity"]["stage"])
        self.assertFalse(data["maturity"]["first_real_run_started"])
        self.assertFalse(data["maturity"]["production_operational"])
        self.assertEqual("read_only", data["agent_mode"]["default_access"])
        self.assertEqual("pull_request_only", data["agent_mode"]["repository_write"])
        self.assertEqual("prohibited_by_default", data["agent_mode"]["production_write"])

    def validate_run_state(self, data):
        assert_keys(self, data, {"schema_version","record_type","is_template","run_id","status","workflow_stage","mode","approval","owner","created_at","updated_at"}, set(data))
        self.assertEqual(1, data["schema_version"])
        self.assertEqual("run_state", data["record_type"])
        self.assertIn(data["status"], RUN_STATUSES)
        self.assertIn(data["workflow_stage"], STAGES)
        if data["is_template"]:
            self.assertEqual("YYYY-MM-DD-short-slug", data["run_id"])
            self.assertEqual("OWNER_REQUIRED", data["owner"])
        else:
            self.assertTrue(is_real_id("run", data["run_id"]))
            self.assertNotEqual("OWNER_REQUIRED", data["owner"])

    def validate_decision(self, data):
        required = {"schema_version","record_type","is_template","decision_id","title","status","date","owner","related_run","related_findings","related_tasks","supersedes","superseded_by"}
        assert_keys(self, data, required, required)
        self.assertEqual("decision", data["record_type"])
        self.assertIn(data["status"], DECISION_STATUSES)
        if data["is_template"]:
            self.assertIn(data["decision_id"], ["DEC-YYYY-NNN"])
        else:
            self.assertTrue(is_real_id("decision", data["decision_id"]))
            self.assertNotEqual("OWNER_REQUIRED", data["owner"])

    def validate_task(self, data):
        self.assertEqual("task", data["record_type"])
        self.assertIn(data["status"], TASK_STATUSES)
        self.assertIn(data["validation_result"], {"pending","passed","failed","inconclusive","not_applicable"})
        if data["is_template"]:
            self.assertEqual("TSK-YYYY-NNN", data["task_id"])
        else:
            self.assertTrue(is_real_id("task", data["task_id"]))
            self.assertNotEqual("OWNER_REQUIRED", data["owner"])

    def validate_evidence(self, data):
        self.assertEqual("evidence", data["record_type"])
        if data["is_template"]:
            self.assertEqual("EV-NNN", data["evidence_id"])
        else:
            self.assertTrue(is_real_id("evidence", data["evidence_id"]))

    def validate_finding(self, data):
        required = {"schema_version","record_type","is_template","finding_id","title","status","owner","related_run","evidence","risk","confidence","related_decisions","related_tasks","supersedes","superseded_by"}
        assert_keys(self, data, required, required)
        self.assertEqual("finding", data["record_type"])
        self.assertIn(data["status"], FINDING_STATUSES)
        if data["is_template"]:
            self.assertEqual("FND-NNN", data["finding_id"])
        else:
            self.assertTrue(is_real_id("finding", data["finding_id"]))

    def test_run_state_template_validates(self):
        self.validate_run_state(load_yaml(ROOT / "runs/_template/state.yaml"))

    def test_real_decisions_validate(self):
        for path in [ROOT / "decisions/DEC-2026-001-site-knowledge-canonical-location.md", ROOT / "decisions/DEC-2026-002-record-first-machine-validation-architecture.md"]:
            self.validate_decision(load_front_matter(path))

    def test_record_templates_validate(self):
        self.validate_decision(load_front_matter(ROOT / "decisions/decision-template.md"))
        self.validate_task(load_front_matter(ROOT / "tasks/task-template.md"))
        self.validate_evidence(load_front_matter(ROOT / "runs/_template/evidence/_evidence-template.md"))
        self.validate_finding(load_front_matter(ROOT / "runs/_template/findings/_finding-template.md"))

    def test_invalid_fixtures_fail(self):
        validators = {
            "invalid_record_type.yaml": self.validate_decision,
            "invalid_status.yaml": self.validate_task,
            "malformed_id.yaml": self.validate_decision,
            "placeholder_in_real_record.yaml": self.validate_decision,
            "missing_required_metadata.yaml": self.validate_finding,
        }
        for fixture, validate in validators.items():
            with self.assertRaises(AssertionError, msg=fixture):
                validate(load_yaml(ROOT / "tests/fixtures/schema/invalid" / fixture))


if __name__ == "__main__":
    unittest.main()
