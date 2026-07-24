#!/usr/bin/env python3
"""Read-only repository validator for current machine-readable records."""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker, exceptions
from referencing import Registry, Resource

DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"
SCHEMA_BY_RECORD_TYPE = {"decision": "decision.schema.json", "task": "task.schema.json", "evidence": "evidence.schema.json", "finding": "finding.schema.json"}
ID_FIELD_BY_TYPE = {"decision": "decision_id", "task": "task_id", "evidence": "evidence_id", "finding": "finding_id", "run_state": "run_id", "project": None}
REQUIRED_REPOSITORY_RECORDS = {
    Path("project.yaml"): "project.schema.json",
    Path("runs/_template/state.yaml"): "run-state.schema.json",
    Path("decisions/decision-template.md"): "decision.schema.json",
    Path("tasks/task-template.md"): "task.schema.json",
    Path("runs/_template/evidence/_evidence-template.md"): "evidence.schema.json",
    Path("runs/_template/findings/_finding-template.md"): "finding.schema.json",
}
IGNORED_REAL_RUN_MARKDOWN = {"README.md", "_evidence-template.md", "_finding-template.md"}

@dataclass(frozen=True)
class ValidationErrorItem:
    category: str; path: str; record_id: str = ""; field: str = ""; message: str = ""
    def sort_key(self) -> tuple[str, str, str, str, str]: return (self.category, self.path, self.record_id, self.field, self.message)
    def render(self) -> str:
        parts = [f"[{self.category}]", self.path]
        if self.record_id: parts.append(f"id={self.record_id}")
        if self.field: parts.append(f"field={self.field}")
        parts.append(f"- {self.message}")
        return " ".join(parts)

@dataclass
class Record:
    path: Path; relative_path: str; data: dict[str, Any]; record_type: str; schema_name: str; is_template: bool; run_id: str | None = None; record_id: str = ""

@dataclass
class ValidationResult:
    root: Path; schema_count: int = 0; records: list[Record] = field(default_factory=list); real_run_ids: set[str] = field(default_factory=set); errors: list[ValidationErrorItem] = field(default_factory=list)
    @property
    def sorted_errors(self) -> list[ValidationErrorItem]: return sorted(self.errors, key=lambda error: error.sort_key())
    @property
    def record_counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for record in self.records: counts[record.record_type] = counts.get(record.record_type, 0) + 1
        return dict(sorted(counts.items()))
    @property
    def exit_code(self) -> int:
        return 2 if any(error.category == "configuration" for error in self.errors) else 1 if self.errors else 0

def _rel(root: Path, path: Path) -> str: return path.relative_to(root).as_posix()
def _add_error(result: ValidationResult, category: str, path: Path, message: str, record_id: str = "", field: str = "") -> None:
    result.errors.append(ValidationErrorItem(category, _rel(result.root, path), str(record_id or ""), field, message))

def _load_yaml_file(result: ValidationResult, path: Path) -> dict[str, Any] | None:
    try: data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        _add_error(result, "record", path, f"YAML parse failed: {exc.__class__.__name__}"); return None
    if not isinstance(data, dict): _add_error(result, "record", path, "YAML document must be a mapping."); return None
    return data

def _load_front_matter(result: ValidationResult, path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        _add_error(result, "record", path, "Markdown record must start with YAML front matter delimiter '---'."); return None
    closing = text.find("\n---", 4)
    if closing == -1:
        _add_error(result, "record", path, "Markdown record is missing closing YAML front matter delimiter '---'."); return None
    try: data = yaml.safe_load(text[4:closing])
    except yaml.YAMLError as exc:
        _add_error(result, "record", path, f"YAML front matter parse failed: {exc.__class__.__name__}"); return None
    if not isinstance(data, dict): _add_error(result, "record", path, "YAML front matter must be a mapping."); return None
    return data

def _load_schemas(result: ValidationResult) -> tuple[dict[str, dict[str, Any]], Registry]:
    schemas: dict[str, dict[str, Any]] = {}; resources = []
    for path in sorted((result.root / "schemas").glob("*.schema.json")):
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            if schema.get("$schema") != DRAFT_2020_12: _add_error(result, "schema", path, "Schema must declare JSON Schema Draft 2020-12 in $schema.", field="$schema")
            Draft202012Validator.check_schema(schema)
            schema_id = schema.get("$id")
            if not isinstance(schema_id, str): _add_error(result, "schema", path, "Schema must declare string $id.", field="$id"); continue
            schemas[path.name] = schema; resource = Resource.from_contents(schema); resources.extend([(schema_id, resource), (schema_id.removeprefix("./"), resource)])
        except json.JSONDecodeError as exc: _add_error(result, "schema", path, f"JSON parse failed at line {exc.lineno}, column {exc.colno}.")
        except exceptions.SchemaError as exc: _add_error(result, "schema", path, f"JSON Schema check failed: {exc.message}", field="/".join(str(p) for p in exc.absolute_path))
    result.schema_count = len(schemas); registry = Registry().with_resources(resources); resolver = registry.resolver()
    for name, schema in sorted(schemas.items()):
        refs: list[str] = []
        def collect(node: Any) -> None:
            if isinstance(node, dict):
                if isinstance(node.get("$ref"), str): refs.append(node["$ref"])
                for value in node.values(): collect(value)
            elif isinstance(node, list):
                for value in node: collect(value)
        collect(schema)
        for ref in sorted(refs):
            try: resolver.lookup(ref)
            except Exception as exc: _add_error(result, "schema", result.root / "schemas" / name, f"Local $ref does not resolve: {ref} ({exc.__class__.__name__})", field="$ref")
    return schemas, registry

def _record_from_data(result: ValidationResult, path: Path, data: dict[str, Any], schema_name: str, run_id: str | None = None) -> Record:
    record_type = str(data.get("record_type", "project" if path.name == "project.yaml" else "")); id_field = ID_FIELD_BY_TYPE.get(record_type); record_id = str(data.get(id_field, "")) if id_field else ""
    return Record(path, _rel(result.root, path), data, record_type, schema_name, bool(data.get("is_template", False)), run_id, record_id)

def _real_run_markdown_records(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(path for path in directory.glob("*.md") if path.name not in IGNORED_REAL_RUN_MARKDOWN)

def _discover_records(result: ValidationResult) -> list[Record]:
    root = result.root
    candidates: list[tuple[Path, str, str | None]] = []
    for relative_path, schema_name in sorted(REQUIRED_REPOSITORY_RECORDS.items(), key=lambda item: item[0].as_posix()):
        path = root / relative_path
        if path.exists():
            candidates.append((path, schema_name, None))
        else:
            _add_error(result, "configuration", path, "Required machine-readable repository file is missing.")
    candidates += [(p, "decision.schema.json", None) for p in sorted((root / "decisions").glob("DEC-*.md"))]
    candidates += [(p, "task.schema.json", None) for p in sorted((root / "tasks").glob("TSK-*.md"))]
    if (root / "runs").exists():
        for run_dir in sorted(p for p in (root / "runs").iterdir() if p.is_dir() and p.name != "_template"):
            state_path = run_dir / "state.yaml"
            if state_path.exists():
                candidates.append((state_path, "run-state.schema.json", run_dir.name))
            else:
                _add_error(result, "record", state_path, "Real Run is missing required machine-readable state.yaml.")
            candidates += [(p, "evidence.schema.json", run_dir.name) for p in _real_run_markdown_records(run_dir / "evidence")]
            candidates += [(p, "finding.schema.json", run_dir.name) for p in _real_run_markdown_records(run_dir / "findings")]
    records: list[Record] = []
    for path, schema_name, run_id in sorted(candidates, key=lambda item: _rel(root, item[0])):
        data = _load_yaml_file(result, path) if path.suffix in {".yaml", ".yml"} else _load_front_matter(result, path)
        if data is None: continue
        if path.suffix == ".md":
            expected = SCHEMA_BY_RECORD_TYPE.get(str(data.get("record_type", "")))
            if expected is None: _add_error(result, "record", path, f"Unknown record_type: {data.get('record_type')!r}.", field="record_type"); continue
            schema_name = expected
        records.append(_record_from_data(result, path, data, schema_name, run_id))
    return records

def _validate_instances(result: ValidationResult, schemas: dict[str, dict[str, Any]], registry: Registry) -> None:
    for record in result.records:
        schema = schemas.get(record.schema_name)
        if not schema: _add_error(result, "configuration", record.path, f"Schema file is missing: {record.schema_name}."); continue
        validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
        for error in sorted(validator.iter_errors(record.data), key=lambda e: (list(e.absolute_path), e.message)):
            _add_error(result, "record", record.path, error.message, record.record_id, "/".join(str(part) for part in error.absolute_path))

def _unique(result: ValidationResult, seen: dict[str, Path], record: Record, message: str) -> None:
    if record.record_id in seen: _add_error(result, "semantic", record.path, f"{message} First seen at {_rel(result.root, seen[record.record_id])}.", record.record_id)
    else: seen[record.record_id] = record.path

def _semantic_validation(result: ValidationResult) -> None:
    decisions: dict[str, Path] = {}; tasks: dict[str, Path] = {}; evidence: dict[str, dict[str, Path]] = {}; findings: dict[str, dict[str, Path]] = {}
    for r in result.records:
        if r.record_type == "run_state" and not r.is_template:
            if r.run_id: result.real_run_ids.add(r.run_id)
            if r.data.get("run_id") != r.run_id: _add_error(result, "semantic", r.path, "run_id must match the containing Run directory name.", r.record_id, "run_id")
            if r.data.get("is_template") is not False: _add_error(result, "semantic", r.path, "Real Run state must set is_template to false.", r.record_id, "is_template")
        elif r.relative_path == "runs/_template/state.yaml" and r.data.get("is_template") is not True:
            _add_error(result, "semantic", r.path, "Run state template must set is_template to true.", r.record_id, "is_template")
        if r.is_template: continue
        if r.record_type in {"evidence", "finding"} and r.run_id and r.data.get("related_run") != r.run_id:
            _add_error(result, "semantic", r.path, f"related_run must match containing Run directory. Expected {r.run_id!r}, found {r.data.get('related_run')!r}.", r.record_id, "related_run")
        if r.record_type == "decision" and r.record_id: _unique(result, decisions, r, "Decision ID must be repository-unique.")
        if r.record_type == "task" and r.record_id: _unique(result, tasks, r, "Task ID must be repository-unique.")
        if r.record_type == "evidence" and r.run_id and r.record_id: _unique(result, evidence.setdefault(r.run_id, {}), r, "Evidence ID must be unique within its Run.")
        if r.record_type == "finding" and r.run_id and r.record_id: _unique(result, findings.setdefault(r.run_id, {}), r, "Finding ID must be unique within its Run.")
    for r in result.records:
        if r.is_template: continue
        for field_name in ("supersedes", "superseded_by"):
            if r.record_id and r.data.get(field_name) == r.record_id: _add_error(result, "semantic", r.path, "Record must not directly reference itself.", r.record_id, field_name)
        if r.record_type == "finding" and r.run_id:
            for ev_id in r.data.get("evidence") or []:
                if ev_id not in evidence.get(r.run_id, {}): _add_error(result, "reference", r.path, "Finding evidence reference must resolve within the same Run.", r.record_id, f"evidence:{ev_id}")
        if r.record_type in {"decision", "task"}:
            related_run = r.data.get("related_run"); related_findings = r.data.get("related_findings") or []
            if related_run and related_run not in result.real_run_ids: _add_error(result, "reference", r.path, "related_run must resolve to a real Run state in this repository.", r.record_id, "related_run")
            if related_findings and not related_run: _add_error(result, "reference", r.path, "related_findings requires related_run so Finding IDs resolve in Run scope.", r.record_id, "related_findings")
            if related_run:
                for fnd_id in related_findings:
                    if fnd_id not in findings.get(str(related_run), {}): _add_error(result, "reference", r.path, "related_finding must resolve inside related_run.", r.record_id, f"related_findings:{fnd_id}")

def validate_repository(root: Path) -> ValidationResult:
    result = ValidationResult(root.resolve()); schemas, registry = _load_schemas(result); result.records = _discover_records(result); _validate_instances(result, schemas, registry); _semantic_validation(result); return result

def format_result(result: ValidationResult) -> str:
    lines = ["Repository validation summary", f"Schema count: {result.schema_count}"]
    for record_type, count in result.record_counts.items(): lines.append(f"Record count ({record_type}): {count}")
    lines += [f"Real Run count: {len(result.real_run_ids)}", f"Validation error count: {len(result.errors)}"]
    if result.errors: lines += ["Errors:"] + [error.render() for error in result.sorted_errors]
    lines += [f"Final status: {'valid' if not result.errors else 'invalid' if result.exit_code == 1 else 'configuration-error'}", f"Exit code: {result.exit_code}"]
    return "\n".join(lines)

def main(argv: list[str] | None = None) -> int:
    root = Path.cwd() if not argv else Path(argv[0])
    try: result = validate_repository(root)
    except Exception as exc:
        print("Repository validation summary"); print("Validation error count: 1"); print(f"[configuration] {root.as_posix()} - Unexpected validation failure: {exc.__class__.__name__}"); print("Final status: configuration-error"); print("Exit code: 2"); return 2
    print(format_result(result)); return result.exit_code

if __name__ == "__main__": raise SystemExit(main(sys.argv[1:]))
