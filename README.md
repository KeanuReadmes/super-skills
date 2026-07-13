# super-skills

**Super Skills** is a collection of expert-level system prompts designed to supercharge AI assistants (Claude, Gemini, Cursor, OpenAI) into specialized senior engineers. Each skill gives the AI a deep, opinionated persona with clear behavioral guidelines, so you get expert-level assistance — not generic answers.

## Available Skills

| Skill | Description |
|---|---|
| [SRE Engineer](skills/sre.md) | Site Reliability Engineer combining Infrastructure, Networking, Cybersecurity, DevOps, FinOps, and Disaster Recovery expertise with a pessimist mindset |
| [QA Engineer](skills/qa-engineer.md) | Quality Assurance Engineer covering test strategy, automation, performance, accessibility, and CI quality gates |
| [Backend Engineer](skills/backend-engineer.md) | Backend Engineer expert in API design, distributed systems, databases, messaging, security, and performance |
| [Frontend Engineer](skills/frontend-engineer.md) | Frontend Engineer specializing in React/Vue/Angular, performance (Core Web Vitals), accessibility, and design systems |
| [Cybersecurity Engineer](skills/cybersecurity-engineer.md) | Cybersecurity Engineer covering AppSec, cloud security, penetration testing, threat modeling, and incident response |
| [Project Manager Engineer](skills/project-manager.md) | Project Manager Engineer bridging technical execution and business goals via Agile, risk management, and stakeholder communication |
| [Architect / Documentator / Diagramer / Planner](skills/architect.md) | Systems architect who understands, organizes, diagrams, and improves complex systems with C4, UML, ADRs, and technical roadmaps |
| [CLI / Tools Engineer](skills/cli-tools-engineer.md) | CLI & Tools Engineer specializing in Python-first tooling with uv/poetry, clean code, proper packaging, CI/CD workflows, and pre-commit hooks |

## How to Use

Copy the **System Prompt** section from any skill file and paste it as the system prompt in your AI assistant of choice:

- **Claude** — Project instructions or system prompt in the API
- **Gemini** — System instruction field
- **Cursor** — `.cursorrules` file or Rules for AI in settings
- **OpenAI (ChatGPT / API)** — System message or Custom Instructions

You can combine multiple skills by merging their prompts, or use them individually depending on the task at hand.

## Validation & Delivery Standards

Every skill in this collection is designed to deliver **fully functioning solutions** — not just code snippets. When you use any skill, the AI will produce:

- **Makefile** — A self-documenting `Makefile` with targets to install, run, test, lint, format, and clean the project. Just run `make help` to see all available commands.
- **Pre-commit hooks** — A `.pre-commit-config.yaml` using open-source, pinned hooks appropriate for the stack (linters, formatters, secrets scanners). Run `pre-commit install` once to activate.
- **Test scripts (`tools/`)** — Standalone validation, smoke-test, and helper scripts organized as a Python `uv` project under `tools/`. Run any script with `uv run <script-name>` without manual dependency installation.
- **README.md** — Every deliverable includes a reviewed and updated `README.md` with setup, run, test, lint, and contribution instructions.

This means every output is ready to run, easy to validate, and clean of errors from the start.

## Skills Overview

### 🔧 [SRE Engineer](skills/sre.md)
A combined expert in Infrastructure, Networking, Cybersecurity, DevOps, FinOps, and Disaster Recovery — with a **pessimist mindset** that assumes failure at every layer. Ideal for reviewing infrastructure, designing resilient systems, managing incidents, and controlling cloud costs.

### 🧪 [QA Engineer](skills/qa-engineer.md)
A quality-first engineer who shifts testing left, automates the right scenarios, and integrates quality gates into CI/CD. Expert in Playwright, Cypress, k6, and risk-based test strategy.

### ⚙️ [Backend Engineer](skills/backend-engineer.md)
A battle-tested server-side engineer focused on clean API design, database performance, event-driven architecture, and secure, observable services.

### 🎨 [Frontend Engineer](skills/frontend-engineer.md)
A modern UI engineer with deep expertise in React/Next.js, TypeScript, Core Web Vitals, WCAG accessibility, and design system development.

### 🔐 [Cybersecurity Engineer](skills/cybersecurity-engineer.md)
A full-spectrum security professional covering OWASP AppSec, cloud security posture, penetration testing, threat modeling (STRIDE), and incident response — with the "assume breach" mindset.

### 📋 [Project Manager Engineer](skills/project-manager.md)
A technically literate PM who combines Agile mastery, risk management, stakeholder communication, and engineering literacy to deliver projects on time with clarity.

### 🏛️ [Architect / Documentator / Diagramer / Planner](skills/architect.md)
A strategic technical leader who excels at understanding complex systems, producing C4 diagrams and ADRs, organizing information, and proactively suggesting improvements. This skill aces at making sense of ambiguity and turning it into structured, actionable artifacts.

### 🛠️ [CLI / Tools Engineer](skills/cli-tools-engineer.md)
A Python-first CLI and developer-tooling specialist who builds clean, installable, and well-documented command-line tools. Expert in `uv`, `poetry`, `Typer`/`Click`, `pyproject.toml` packaging, `--help`/`--version` wiring, CI/CD release pipelines, pre-commit hooks, and Makefile-driven workflows.
