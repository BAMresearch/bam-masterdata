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
