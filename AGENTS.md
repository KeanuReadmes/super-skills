# Agent Governance

This repository requires all automation agents to follow these rules.

## Issue and pull request creation

- Open a new GitHub Issue for each confirmed audit gap unless an equivalent open issue already exists.
- Open a pull request for mechanical fixes and link it to the tracking issue with `Closes #<number>`.

## Template usage (mandatory)

- All new issues must use templates from `.github/ISSUE_TEMPLATE/`.
- All new pull requests must use `.github/pull_request_template.md`.
- If a required template is missing or outdated, update the template before creating new items.

## Template maintenance on push

Whenever code is pushed and it changes contribution workflow, CI quality gates, security process, or release process:

1. Review `.github/ISSUE_TEMPLATE/*` and `.github/pull_request_template.md`.
2. Update template fields/checklists so they match the new process.
3. Include those template updates in the same change set.
