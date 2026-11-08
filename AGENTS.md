
# BAM Masterdata Agent Instructions

## Goal

Maintain correct, minimal, ontology-informed
operational schemas for BAM Data Store.

## Development workflow

For user-requested datamodel changes:

1. Analyze the GitHub issue and existing definitions.
2. Propose the smallest appropriate schema design.
3. Stop for human approval.
4. Implement the approved design.
5. Run relevant tests and linting checks.
6. Request independent test and architecture reviews.
7. Correct critical issues, with at most one
   automatic correction cycle.
8. Present the final diff and verification report.

## Architectural constraints

- Read `docs/explanations/schema_defs.md` before designing datamodel changes.
- Prefer reuse over new definitions.
- Keep v0 and v1 conventions separate.
- Never change v0 merely to implement a v1 feature.
- Preserve existing public APIs unless approved.
- Reuse existing property and vocabulary definitions.
- Do not invent ontology mappings or semantic claims.
- Do not confuse Python inheritance with native
  openBIS object-type inheritance.
- Never remove or loosen an OBJECT `object_code` (to `None` or `"(ALL)"`) without approval.

## Quality

- Follow the repository's pytest patterns.
- Use Ruff for formatting and linting checks.
- Avoid duplicated and implementation-coupled tests.
- Distinguish local validation from openBIS integration.
- Never claim external integration was tested
  without actual execution evidence.

## Safety and scope

- Do not execute destructive migrations.
- Do not modify production openBIS data.
- Do not expose secrets or credentials.
- Do not install dependencies without approval.
- Do not modify unrelated files.
- Do not commit, push, or merge automatically.

## Final report

Provide:
- Issue and approved requirements
- Proposed and implemented definitions
- Files changed
- Tests executed with results
- Review findings and outstanding concerns
- Git diff summary
- Recommendation for human review

## Multi-agent progress reporting

When orchestrating multiple agents:

- Announce each delegated task and assigned agent.
- Report when a subagent completes or encounters a blocker.
- Maintain a concise task-status summary.
- Identify which tasks can execute concurrently.
- Report which tasks depend on previous results.
- Never mark a task complete before receiving its result.
- Present the consolidated status before requesting approval.
