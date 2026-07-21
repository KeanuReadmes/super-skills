# Contributing

Thanks for improving **super-skills**.

## Prerequisites

- GNU Make
- Node.js (for markdownlint via npx)
- yamllint
- pre-commit (recommended)

## Setup

1. Fork and clone the repository.
2. Run `make install` to install skills locally.
3. (Optional) Run `pre-commit install --hook-type pre-commit --hook-type commit-msg`.

## Validation

Run these checks before opening a pull request:

- `make lint`
- `make validate`

## Commit messages

Use Conventional Commits:

- `feat(scope): ...`
- `fix(scope): ...`
- `docs(scope): ...`
- `chore(scope): ...`

## Pull requests

- Keep PRs focused and small.
- Explain user impact and risk.
- Link related issues using `Closes #<number>` when applicable.
