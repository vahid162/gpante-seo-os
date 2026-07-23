# Decisions Directory Contract

## Purpose

`decisions/` owns repository-wide Decision records for `gpante-seo-os`.

## What belongs here

- `index.md`, the current Decision registry and planned future derived/generated Decision index.
- `decision-template.md`, the Markdown contract for individual Decision files.
- Individual Decision files when a Decision needs rationale, alternatives, consequences, supersession history, or relationships that do not fit cleanly in the index.

## What does not belong here

- Run-local Findings or Evidence.
- Task implementation history.
- Audit templates.
- Raw, reference-only, prohibited, or unsanitized material.

## Canonical ownership

The individual Decision record is planned to be the record-first source of truth for that Decision. `index.md` remains maintained for current registry discoverability until a future generator exists; once generated, it must not become a competing source of truth.

Decision IDs are repository-wide and use `DEC-YYYY-NNN`, where `YYYY` is a four-digit year and `NNN` is a three-digit sequence. `DEC-2026-999` is an example format only, not an assigned identifier.

Decision statuses and lifecycle rules are defined in `../workflows/status-definitions.md` and `../workflows/decision-process.md`.

## Relationships

A Decision may reference Evidence IDs and Finding IDs from a Run, the related Run ID, and related repository-wide Task IDs. Evidence and Findings remain owned by the Run. Task status remains owned by `../tasks/backlog.md`.

## Supersession

Superseded Decisions remain historical records. Mark supersession relationships instead of deleting or rewriting historical Decisions.

## Applicable policies

Follow repository governance and data policies before adding Decision content.

## Production access

This directory does not authorize WordPress, WooCommerce, Yoast, aaPanel, server, database, analytics, Search Console, or Production access.
