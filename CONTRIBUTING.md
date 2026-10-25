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

Small contributions, such as typo corrections, may be submitted without an issue.

Pull requests should have:

- Exactly one `type:*` label.
- Relevant `area:*` labels.
- Exactly one `semver:*` label before merging.

Labels may be assigned by maintainers when contributors lack permission.

## 3. Semantic versioning

We use Semantic Versioning to classify release impact.

| Label | Meaning |
|---|---|
| `semver:major` | Introduces backward-incompatible changes. |
| `semver:minor` | Adds backward-compatible functionality. |
| `semver:patch` | Fixes existing functionality without breaking compatibility. |
| `semver:none` | Does not require a new release. |

During the `0.x` development series, breaking changes normally increment the minor version. Starting with `1.0.0`, breaking changes increment the major version.

Compatibility considerations include the Python API, CLI, operational metadata schema, and openBIS integration.

## 4. Review and release workflow

Development PRs are reviewed and merged into `dev`.

Releases are prepared by merging `dev` into `main`. Release impact is determined from the changes included since the previous release.

GitHub releases are created from `main`, and publication to PyPI is handled by GitHub Actions.

Release publication remains a maintainer decision.
