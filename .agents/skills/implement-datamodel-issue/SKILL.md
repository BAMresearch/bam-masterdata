---
name: implement-datamodel-issue
description: >
  Analyze, design, implement, test, and review GitHub issues
  requesting changes to bam-masterdata scientific data models.
  Use when working on datamodel issues.
---

# Datamodel Issue Implementation

Input: GitHub issue number.

## Phase 1: Requirements

Delegate to `requirements`.

- Read the GitHub issue and comments.
- Identify requested changes.
- Inspect existing definitions.
- Identify missing information.

## Phase 2: Design

Delegate to `schema_designer`.

- Evaluate scientific definitions.
- Identify suitable inheritance and relationships.
- Reuse existing properties and vocabularies.
- Identify compatibility concerns.

## Phase 3: Approval

Consolidate both agents' findings.

Present the proposed architecture and files to modify.

STOP and request human approval.

## Phase 4: Implementation

After approval, delegate to `implementer`.

Implement only the approved changes.

## Phase 5: Verification

Run relevant pytest and Ruff checks.

Delegate independent analysis to:

- `test_analyst`
- `reviewer`

Consolidate findings.

## Phase 6: Delivery

Report:

- Implementation summary
- Files changed
- Test results
- Review findings
- Unresolved issues

Do not commit, push, or create a PR automatically.
