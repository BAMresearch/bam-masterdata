# Contributing to bam-masterdata

Thank you for contributing to `bam-masterdata`!

This document describes our issue management, labeling conventions, and development workflow.

## 1. Reporting issues

Before opening a new issue, check whether a similar issue already exists.

Issues should have the following labels:

| Category | Labels | Purpose |
|---|---|---|
| Type | `type:bug`, `type:feature`, `type:enhancement`, `type:documentation`, `type:maintenance`, `type:question` | What kind of work is involved? |
| Priority | `priority:urgent`, `priority:high`, `priority:medium`, `priority:low` | How urgently should it be addressed? |
| Area | `area:datamodel`, `area:cli`, `area:openbis`, `area:export`, `area:testing`, `area:ci`, `area:docs`, `area:dependencies` | Which components are affected? |

**Note**: The list of labels might be outdated. This is because we might change or modify them through time. Please, check the list of current type/priority/area labels.

Each issue should have **exactly**: 1 `type:*` label, at most 1 `priority:*` label, and any relevant `area:*` labels.

Contributors who cannot assign labels may leave classification to the maintainers.

## 2. Creating pull requests

The repository follows a two-branch development workflow:

- **`dev`** is the default branch for development.
- **`main`** contains stable releases.

To contribute:

1. Create an issue or identify an existing one.
2. Create a branch from `dev`, preferably using the issue's **Development → Create a branch** option.
3. Implement your changes and add appropriate tests.
4. Open a pull request targeting `dev`.
5. Reference the associated issue using `Refs #123` or `Closes #123`.

### Pull requests without an associated issue

Development PRs targeting `dev` normally require an associated issue.

Issue associations can be established through:
- An explicit reference in the PR description, such as `Refs #123` or `Closes #123`.
- A branch name beginning with the issue number, such as `123-fix-export`.

**Exceptions**

Some contributions do not require a separate issue:

- Minor administrative changes, such as typo corrections.
- Urgent fixes where creating an issue would add unnecessary overhead.
- Other exceptional cases explicitly approved by a maintainer.

For these cases, a maintainer may apply the `no-issue-required` label.

This label exempts the PR **only from the issue-reference requirement**. All other validation requirements remain applicable, including valid `type:*`, `area:*`, and `semver:*` labels.

Contributors should briefly explain why an issue is unnecessary in the PR description.

### Release pull requests

Release PRs must originate from `dev` and target `main` in the same repository.

These PRs:

- Do not require an associated issue.
- May contain multiple `type:*` and `area:*` labels aggregated from development PRs.
- Must contain exactly one `semver:*` label representing the highest release impact.
- Are subject to maintainer review before merging.

Other PRs targeting `main` are not accepted by the automated validation workflow.


## 3. Semantic versioning

`bam-masterdata` follows Semantic Versioning (SemVer) to classify changes
to its Python package, CLI, metadata schema, and openBIS integration.

Every development PR targeting `dev` must have exactly one `semver:*`
label describing its impact on users.

### SemVer labels

| Label | Meaning | Examples |
|---|---|---|
| `semver:major` | Backward-incompatible change | Removing a public Python API, renaming an existing metadata property, changing required schema fields incompatibly |
| `semver:minor` | Backward-compatible functionality | Adding a new entity type, introducing an optional metadata property, adding a CLI command |
| `semver:patch` | Backward-compatible fix | Fixing incorrect exports, correcting validation behavior, fixing an openBIS synchronization bug |
| `semver:none` | No user-facing release impact | Documentation-only changes, tests, CI configuration, CODEOWNERS updates |

The label describes the **compatibility impact**, not the size or complexity
of the implementation.

A small change can be breaking, while a substantial internal refactoring
may have no user-facing impact.

### What constitutes a breaking change?

A change should generally receive `semver:major` if existing users
must modify their code, metadata, configuration, or workflows to continue
using the package.

Examples include:

**Python API**
- Removing or renaming public classes, functions, or attributes.
- Changing public function signatures incompatibly.
- Changing documented behavior or return types incompatibly.

**Metadata schema**
- Removing or renaming existing entity types or properties.
- Making a previously optional property mandatory.
- Changing field types, constraints, or accepted values incompatibly.
- Changing inheritance or validation behavior in ways that invalidate
  previously valid metadata.

**CLI**
- Removing or renaming existing commands or options.
- Changing command arguments or output formats incompatibly.

**openBIS integration**
- Introducing incompatible changes to synchronized type or property codes.
- Changing property assignments or requirements in ways that break
  existing integrations.
- Requiring migrations of existing openBIS metadata or records.

Changes are not automatically breaking merely because they modify
the schema or synchronization logic. Classification depends on their
actual compatibility impact.

For example, adding an optional property is normally backward-compatible,
whereas making an existing property mandatory may require migration
and should be classified as breaking.

### Version numbering during 0.x development

While the project remains in the `0.x` series, breaking changes increase
the minor version rather than the major version.

| Highest release impact | Current version | Suggested version |
|---|---|---|
| `semver:none` | `0.15.0` | No release required |
| `semver:patch` | `0.15.0` | `0.15.1` |
| `semver:minor` | `0.15.0` | `0.16.0` |
| `semver:major` | `0.15.0` | `0.16.0` |

The `semver:major` label must still be used for breaking changes during
the `0.x` series so they remain identifiable in release notes.

Starting with version `1.0.0`, standard SemVer version increments apply:

- `semver:major`: increase the major version.
- `semver:minor`: increase the minor version.
- `semver:patch`: increase the patch version.

The transition to `1.0.0` is a deliberate maintainer decision and is
not triggered automatically by the release preparation script.

### Release classification

Release preparation aggregates the SemVer labels of the development
PRs included in the release.

The highest impact determines the suggested version increment:

`major > minor > patch > none`

For example, a release containing three `semver:minor` PRs and one
`semver:patch` PR receives an aggregated `semver:minor` classification.

The release preparation workflow suggests a version and generates
release notes, but maintainers remain responsible for reviewing
compatibility implications and approving publication.

## 4. Review and release workflow

The repository follows a controlled release process:

1. Development PRs are reviewed and merged into `dev`.
2. A maintainer opens a release PR from `dev` into `main`.
3. GitHub Actions automatically:
   - Collects the development PRs included in the release.
   - Aggregates their labels and determines the highest SemVer impact.
   - Suggests the next version based on the latest published release.
   - Generates categorized release notes.
   - Posts or updates the release preparation comment on the release PR.
4. A maintainer reviews the proposed version, release notes, and any
   compatibility concerns.
5. After approval, the release PR is manually merged into `main`.
6. A maintainer creates and publishes a GitHub Release using a version
   tag pointing to a commit on `main` and the prepared release notes.
7. Publishing the GitHub Release triggers the existing GitHub Actions
   workflow to build and publish the package to PyPI.

### Release approval

Release preparation is automated, but **release approval and publication
remain manual**.

The automation does not:
- Merge release PRs.
- Create version tags.
- Create or publish GitHub Releases.
- Initiate PyPI publication before a GitHub Release is published.

The proposed version and generated release notes must be reviewed by a
maintainer before publication.

The final release version may be adjusted by a maintainer when necessary,
for example to address compatibility concerns or to prepare the transition
to version `1.0.0`.
