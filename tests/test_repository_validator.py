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
from validate_repository import format_result, validate_repository  # noqa: E402


def front(data):
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n# Body\n"


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
        rendered = format_result(result)
        self.assertIn(fragment, rendered)

    def add_run(self, run_id="2026-07-24-test-run", evidence_id="EV-001", finding_id="FND-001"):
        run = self.root / "runs" / run_id
        (run / "evidence").mkdir(parents=True)
        (run / "findings").mkdir()
        (run / "state.yaml").write_text(yaml.safe_dump({
            "schema_version": 1, "record_type": "run_state", "is_template": False, "run_id": run_id,
            "status": "initialized", "workflow_stage": "intake", "mode": {"audit_only": True, "production_write": False},
            "approval": {"required": True, "status": "pending"}, "owner": "repo-owner", "created_at": "2026-07-24", "updated_at": "2026-07-24",
        }, sort_keys=False), encoding="utf-8")
        (run / "evidence" / "ev-001.md").write_text(front({
            "schema_version": 1, "record_type": "evidence", "is_template": False, "evidence_id": evidence_id, "title": "Synthetic evidence", "owner": "repo-owner", "collected_at": "2026-07-24", "source_type": "repository_document", "scope": "Synthetic fixture", "classification": "repository-safe", "sanitized": False, "storage": "markdown_summary", "related_run": run_id, "related_findings": []}), encoding="utf-8")
        (run / "findings" / "fnd-001.md").write_text(front({
            "schema_version": 1, "record_type": "finding", "is_template": False, "finding_id": finding_id, "title": "Synthetic finding", "status": "confirmed", "owner": "repo-owner", "related_run": run_id, "evidence": [evidence_id], "severity": "Medium", "risk": "Medium", "confidence": "Medium", "related_decisions": [], "related_tasks": [], "supersedes": None, "superseded_by": None}), encoding="utf-8")
        return run

    def snapshot(self):
        snap = {}
        for path in sorted(p for p in self.root.rglob("*") if p.is_file()):
            rel = path.relative_to(self.root).as_posix()
            snap[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
        return snap

    def test_current_repository_validates(self):
        result = validate_repository(ROOT)
        self.assertEqual([], result.sorted_errors, format_result(result))
        self.assertEqual(0, result.exit_code)

    def test_invalid_json_schema_fails(self):
        (self.root / "schemas" / "bad.schema.json").write_text('{"$schema": "https://json-schema.org/draft/2020-12/schema", "type": 7}', encoding="utf-8")
        self.assertInvalidContains("JSON Schema check failed")

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
        self.add_run("2026-07-24-test-one"); self.add_run("2026-07-25-test-two")
        self.assertEqual(0, self.result().exit_code, format_result(self.result()))

    def test_duplicate_finding_id_in_same_run_fails(self):
        run = self.add_run()
        shutil.copy(run / "findings" / "fnd-001.md", run / "findings" / "fnd-dup.md")
        self.assertInvalidContains("Finding ID must be unique within its Run")

    def test_same_finding_id_in_different_runs_allowed(self):
        self.add_run("2026-07-24-test-one"); self.add_run("2026-07-25-test-two")
        self.assertEqual(0, self.result().exit_code, format_result(self.result()))

    def test_missing_finding_evidence_fails(self):
        run = self.add_run(); p = run / "findings" / "fnd-001.md"; text = p.read_text(encoding="utf-8").replace("EV-001", "EV-999"); p.write_text(text, encoding="utf-8")
        self.assertInvalidContains("Finding evidence reference must resolve within the same Run")

    def test_finding_cannot_resolve_evidence_from_other_run(self):
        run = self.add_run("2026-07-24-test-one", "EV-002"); self.add_run("2026-07-25-test-two", "EV-001")
        p = run / "findings" / "fnd-001.md"; p.write_text(p.read_text(encoding="utf-8").replace("EV-002", "EV-001"), encoding="utf-8")
        self.assertInvalidContains("same Run")

    def test_related_findings_without_related_run_fails(self):
        (self.root / "tasks" / "TSK-2026-999-related.md").write_text(front({"schema_version":1,"record_type":"task","is_template":False,"task_id":"TSK-2026-999","title":"Task","status":"proposed","priority":"Medium","owner":"repo-owner","implementation_owner":"repo-owner","related_run":None,"related_findings":["FND-001"],"related_decisions":[],"approval":{"required":True,"status":"pending"},"risk":"Medium","implementation_mode":"manual","dependencies":[],"validation_result":"pending","backup_required":False,"backup_verified":False}), encoding="utf-8")
        self.assertInvalidContains("related_findings requires related_run")

    def test_missing_related_finding_fails(self):
        self.add_run()
        (self.root / "decisions" / "DEC-2026-999-related.md").write_text(front({"schema_version":1,"record_type":"decision","is_template":False,"decision_id":"DEC-2026-999","title":"Decision","status":"proposed","date":"2026-07-24","owner":"repo-owner","related_run":"2026-07-24-test-run","related_findings":["FND-999"],"related_tasks":[],"supersedes":None,"superseded_by":None}), encoding="utf-8")
        self.assertInvalidContains("related_finding must resolve inside related_run")

    def test_run_id_mismatch_fails(self):
        run = self.add_run(); data = yaml.safe_load((run / "state.yaml").read_text(encoding="utf-8")); data["run_id"] = "2026-07-24-other"; (run / "state.yaml").write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
        self.assertInvalidContains("run_id must match")

    def test_self_reference_fails(self):
        (self.root / "decisions" / "DEC-2026-999-self.md").write_text(front({"schema_version":1,"record_type":"decision","is_template":False,"decision_id":"DEC-2026-999","title":"Decision","status":"proposed","date":"2026-07-24","owner":"repo-owner","related_run":None,"related_findings":[],"related_tasks":[],"supersedes":"DEC-2026-999","superseded_by":None}), encoding="utf-8")
        self.assertInvalidContains("must not directly reference itself")

    def test_templates_remain_valid(self):
        result = self.result()
        template_errors = [e for e in result.sorted_errors if "template" in e.path]
        self.assertEqual([], template_errors)

    def test_error_order_and_summary_are_deterministic(self):
        self.add_run(); (self.root / "decisions" / "DEC-2026-999-no-front-matter.md").write_text("# bad\n", encoding="utf-8")
        first = format_result(self.result()); second = format_result(self.result())
        self.assertEqual(first, second)

    def test_validator_is_read_only(self):
        before = self.snapshot(); validate_repository(self.root); after = self.snapshot()
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
