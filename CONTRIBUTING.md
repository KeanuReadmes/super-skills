# Contributing

Thanks for improving **super-skills**.

## Prerequisites

- GNU Make
- Node.js (for markdownlint via npx)
- yamllint
- pre-commit (recommended)

## Setup

1. Fork and clone the repository.
2. Run `make install` to install skills locally into `$CODEX_HOME/skills` (or `~/.codex/skills` when unset), `~/.claude/skills`, `~/.agents/skills`, `~/.gemini/skills`, `~/.cursor/skills`, and `~/.copilot/skills`.
3. (Optional) Run `pre-commit install --hook-type pre-commit --hook-type commit-msg`.

## Validation

Run these checks before opening a pull request:

- `make lint`
- `make validate`
- `make audit`

## Skill authoring rules

`make audit` enforces these for every `skills/*.md`, following Anthropic's [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices):

- At most 100 lines, frontmatter included. Cut what Claude already knows; keep commands, thresholds, output formats, handoffs, and approval gates.
- `name` equals the file name: lowercase letters, digits, and hyphens, at most 64 characters.
- `description` is third person, at most 1024 characters, states what the skill does, and includes `Use when ...` triggers that distinguish it from neighbouring skills.
- Keep the `## System Prompt`, `### Repository Context & License Compatibility (Mandatory)`, and `### Guardrails` sections.

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
