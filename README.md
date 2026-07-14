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

---

## Open Source Tools Reference

Each skill relies on a set of open source tools to do its job well. The tables below map every skill to its recommended tools, along with the preferred **sandbox installation method** to keep your host system clean and avoid version conflicts.

> **Sandbox-first rule:** Never install tools globally with `sudo pip install`, `sudo npm install -g`, or `brew install` unless you are working inside a dedicated container or VM. Always prefer the isolated install commands shown below.

---

### 🏛️ Architect / Documentator / Diagramer / Planner

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) | Render Mermaid diagrams to PNG/SVG from the CLI | `npx @mermaid-js/mermaid-cli` |
| [PlantUML](https://plantuml.com/) | Generate UML diagrams from text | `docker run --rm -v $(pwd):/data plantuml/plantuml` |
| [Structurizr CLI](https://github.com/structurizr/cli) | Work with Structurizr DSL / C4 models | `docker run --rm -v $(pwd):/usr/local/structurizr structurizr/cli` |
| [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) | Lint Markdown documentation | `npx markdownlint-cli` |
| [yamllint](https://github.com/adrienverge/yamllint) | Lint YAML configuration files | `uv tool install yamllint` |
| [pre-commit](https://pre-commit.com/) | Run multi-language pre-commit hooks | `uv tool install pre-commit` |
| [mkdocs](https://www.mkdocs.org/) | Build project documentation sites | `uv venv .venv && uv pip install mkdocs` |
| [Sphinx](https://www.sphinx-doc.org/) | Generate documentation from source | `uv venv .venv && uv pip install sphinx` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Scan for accidentally committed secrets | `uv tool install detect-secrets` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Detect hardcoded secrets in git history | `docker run --rm -v $(pwd):/path zricethezav/gitleaks` |

---

### ⚙️ Backend Engineer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [ruff](https://github.com/astral-sh/ruff) | Python linter and formatter | `uv tool install ruff` |
| [golangci-lint](https://golangci-lint.run/) | Go linter aggregator | `docker run --rm -v $(pwd):/app golangci/golangci-lint golangci-lint run` |
| [ESLint](https://eslint.org/) | JavaScript/TypeScript linter | `npm install --save-dev eslint` |
| [Prettier](https://prettier.io/) | Code formatter (JS/TS/JSON/YAML) | `npm install --save-dev prettier` |
| [hadolint](https://github.com/hadolint/hadolint) | Dockerfile linter | `docker run --rm -i hadolint/hadolint` |
| [Spectral](https://github.com/stoplightio/spectral) | OpenAPI / AsyncAPI linter | `npx @stoplight/spectral-cli lint` |
| [sqlfluff](https://sqlfluff.com/) | SQL linter and formatter | `uv venv .venv && uv pip install sqlfluff` |
| [Trivy](https://github.com/aquasecurity/trivy) | Vulnerability and dependency scanner | `docker run --rm -v $(pwd):/work aquasec/trivy fs /work` |
| [Semgrep](https://semgrep.dev/) | SAST — static code analysis | `docker run --rm -v $(pwd):/src semgrep/semgrep semgrep scan` |
| [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) | Receive, process and export telemetry | `docker run --rm otel/opentelemetry-collector` |
| [OpenAPI Generator](https://openapi-generator.tech/) | Generate client/server code from OpenAPI specs | `docker run --rm -v $(pwd):/local openapitools/openapi-generator-cli` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets scanning | `uv tool install detect-secrets` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Git secrets detection | `docker run --rm -v $(pwd):/path zricethezav/gitleaks` |

---

### 🛠️ CLI / Tools Engineer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [uv](https://github.com/astral-sh/uv) | Python project and dependency manager | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| [ruff](https://github.com/astral-sh/ruff) | Python linter and formatter | `uv tool install ruff` |
| [mypy](https://mypy-lang.org/) | Python static type checker | `uv venv .venv && uv pip install mypy` |
| [pytest](https://pytest.org/) | Python test framework | `uv pip install pytest pytest-cov` (inside venv) |
| [Typer](https://typer.tiangolo.com/) | CLI framework built on Click | `uv pip install typer` (inside venv) |
| [Click](https://click.palletsprojects.com/) | CLI framework | `uv pip install click` (inside venv) |
| [pre-commit](https://pre-commit.com/) | Pre-commit hook runner | `uv tool install pre-commit` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets scanning hook | `uv tool install detect-secrets` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Git secrets detection | `docker run --rm -v $(pwd):/path zricethezav/gitleaks` |
| [pipx](https://pipx.pypa.io/) | Install and run Python CLI tools in isolation | `uv tool install pipx` |

---

### 🔐 Cybersecurity Engineer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [Semgrep](https://semgrep.dev/) | SAST — static application security testing | `docker run --rm -v $(pwd):/src semgrep/semgrep semgrep scan` |
| [Bandit](https://github.com/PyCQA/bandit) | Python SAST scanner | `uv venv .venv && uv pip install bandit` |
| [Trivy](https://github.com/aquasecurity/trivy) | Container and dependency vulnerability scanner | `docker run --rm -v $(pwd):/work aquasec/trivy fs /work` |
| [OWASP ZAP](https://www.zaproxy.org/) | DAST — dynamic application security testing | `docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable zap-baseline.py` |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | Fast vulnerability scanner with templates | `docker run --rm projectdiscovery/nuclei` |
| [Prowler](https://github.com/prowler-cloud/prowler) | AWS / GCP / Azure security posture assessment | `docker run --rm -v ~/.aws:/home/prowler/.aws toniblyx/prowler` |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | Multi-cloud security auditing tool | `uv venv .venv && uv pip install scoutsuite` |
| [Checkov](https://www.checkov.io/) | IaC security and misconfiguration scanner | `docker run --rm -v $(pwd):/tf bridgecrew/checkov` |
| [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) | Identify vulnerable dependencies | `docker run --rm -v $(pwd):/src owasp/dependency-check --scan /src` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Detect secrets in git history | `docker run --rm -v $(pwd):/path zricethezav/gitleaks` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets baseline and scanning | `uv tool install detect-secrets` |
| [nmap](https://nmap.org/) | Network discovery and port scanning | `docker run --rm instrumentisto/nmap` |
| [sqlmap](https://sqlmap.org/) | Automated SQL injection detection | `docker run --rm -it cytopia/sqlmap` |
| [CycloneDX CLI](https://github.com/CycloneDX/cyclonedx-cli) | Generate and validate SBOMs | `docker run --rm cyclonedx/cyclonedx-cli` |
| [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) | Threat modeling tool | `docker run --rm -p 3000:3000 owasp/threat-dragon` |

---

### 🎨 Frontend Engineer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [ESLint](https://eslint.org/) | JavaScript/TypeScript linter | `npm install --save-dev eslint` |
| [Prettier](https://prettier.io/) | Code formatter | `npm install --save-dev prettier` |
| [Stylelint](https://stylelint.io/) | CSS/SCSS/Less linter | `npm install --save-dev stylelint` |
| [HTMLHint](https://htmlhint.com/) | HTML static analysis | `npm install --save-dev htmlhint` |
| [Playwright](https://playwright.dev/) | End-to-end browser testing | `npm install --save-dev @playwright/test && npx playwright install --with-deps` |
| [Cypress](https://www.cypress.io/) | End-to-end and component testing | `npm install --save-dev cypress` |
| [Vitest](https://vitest.dev/) | Unit test framework (Vite-native) | `npm install --save-dev vitest` |
| [axe-core / axe-cli](https://github.com/dequelabs/axe-core) | Accessibility automated testing | `npm install --save-dev axe-core @axe-core/cli` |
| [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) | Automated Lighthouse performance audits in CI | `npm install --save-dev @lhci/cli` |
| [Storybook](https://storybook.js.org/) | Component development and documentation | `npx storybook@latest init` |
| [Chromatic](https://www.chromatic.com/) | Visual regression testing (OSS tier) | `npm install --save-dev chromatic` |
| [TypeScript](https://www.typescriptlang.org/) | Static typing for JavaScript | `npm install --save-dev typescript` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets scanning | `uv tool install detect-secrets` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Git secrets detection | `docker run --rm -v $(pwd):/path zricethezav/gitleaks` |

---

### 📋 Project Manager Engineer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [GitHub CLI (`gh`)](https://cli.github.com/) | Manage issues, PRs, and projects from the CLI | `docker run --rm -v $(pwd):/work ghcr.io/cli/cli gh` |
| [go-jira](https://github.com/ankitpokhrel/jira-cli) | JIRA CLI for issue and sprint management | `docker run --rm ankitpokhrel/jira-cli` |
| [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) | Lint project documentation and reports | `npx markdownlint-cli` |
| [yamllint](https://github.com/adrienverge/yamllint) | Lint YAML configuration files | `uv tool install yamllint` |
| [pre-commit](https://pre-commit.com/) | Enforce code quality gates on commit | `uv tool install pre-commit` |
| [ruff](https://github.com/astral-sh/ruff) | Python linter/formatter for automation scripts | `uv tool install ruff` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Prevent secrets from entering the repo | `uv tool install detect-secrets` |
| [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) | Render roadmap and dependency diagrams | `npx @mermaid-js/mermaid-cli` |

---

### 🧪 QA Engineer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [Playwright](https://playwright.dev/) | End-to-end browser and API testing | `npm install --save-dev @playwright/test && npx playwright install --with-deps` |
| [Cypress](https://www.cypress.io/) | End-to-end and component testing | `npm install --save-dev cypress` |
| [pytest](https://pytest.org/) | Python test framework | `uv venv .venv && uv pip install pytest pytest-cov` |
| [Jest](https://jestjs.io/) | JavaScript unit testing | `npm install --save-dev jest` |
| [Vitest](https://vitest.dev/) | Vite-native unit testing | `npm install --save-dev vitest` |
| [k6](https://k6.io/) | Performance and load testing | `docker run --rm -v $(pwd):/scripts grafana/k6 run /scripts/test.js` |
| [Locust](https://locust.io/) | Python-based load testing | `uv venv .venv && uv pip install locust` |
| [Gatling](https://gatling.io/) | Scala-based load and performance testing | `docker run --rm -v $(pwd):/gatling denvazh/gatling` |
| [Newman](https://github.com/postmanlabs/newman) | Run Postman collections from the CLI | `npx newman run` |
| [Allure](https://allurereport.org/) | Test report generation | `docker run --rm -v $(pwd):/app frankescobar/allure-docker-service` |
| [axe-core](https://github.com/dequelabs/axe-core) | Accessibility automated testing | `npm install --save-dev axe-core` |
| [OWASP ZAP](https://www.zaproxy.org/) | DAST for security-in-QA workflows | `docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable zap-baseline.py` |
| [Pact](https://docs.pact.io/) | Consumer-driven contract testing | `npm install --save-dev @pact-foundation/pact` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets scanning in test data | `uv tool install detect-secrets` |

---

### 🔧 SRE Engineer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [Terraform](https://www.terraform.io/) | Infrastructure as Code | `docker run --rm -v $(pwd):/workspace hashicorp/terraform` |
| [tflint](https://github.com/terraform-linters/tflint) | Terraform linter | `docker run --rm -v $(pwd):/data ghcr.io/terraform-linters/tflint` |
| [terraform-docs](https://terraform-docs.io/) | Generate docs from Terraform modules | `docker run --rm -v $(pwd):/terraform-docs quay.io/terraform-docs/terraform-docs` |
| [Checkov](https://www.checkov.io/) | IaC security and misconfiguration scanner | `docker run --rm -v $(pwd):/tf bridgecrew/checkov` |
| [Pulumi](https://www.pulumi.com/) | Cloud infrastructure as code (multi-language) | `docker run --rm -v $(pwd):/pulumi/projects pulumi/pulumi` |
| [hadolint](https://github.com/hadolint/hadolint) | Dockerfile linter | `docker run --rm -i hadolint/hadolint` |
| [yamllint](https://github.com/adrienverge/yamllint) | YAML linter | `uv tool install yamllint` |
| [shellcheck](https://www.shellcheck.net/) | Shell script static analysis | `docker run --rm -v $(pwd):/mnt koalaman/shellcheck` |
| [ansible-lint](https://ansible.readthedocs.io/projects/lint/) | Ansible playbook linter | `uv venv .venv && uv pip install ansible-lint` |
| [Trivy](https://github.com/aquasecurity/trivy) | Container image and IaC vulnerability scanner | `docker run --rm -v $(pwd):/work aquasec/trivy fs /work` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Detect secrets in git history | `docker run --rm -v $(pwd):/path zricethezav/gitleaks` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets baseline | `uv tool install detect-secrets` |
| [k6](https://k6.io/) | Load and performance testing | `docker run --rm -v $(pwd):/scripts grafana/k6 run /scripts/test.js` |
| [Prometheus](https://prometheus.io/) | Metrics collection and alerting | `docker run --rm -p 9090:9090 prom/prometheus` |
| [Grafana](https://grafana.com/) | Metrics visualization and dashboards | `docker run --rm -p 3000:3000 grafana/grafana` |
| [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) | Telemetry pipeline (traces, metrics, logs) | `docker run --rm otel/opentelemetry-collector` |
| [Helm](https://helm.sh/) | Kubernetes package manager | `docker run --rm -v $(pwd):/apps alpine/helm` |
| [kube-score](https://kube-score.com/) | Kubernetes manifest static analysis | `docker run --rm -v $(pwd):/manifests zegl/kube-score` |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | CIS Kubernetes benchmark checks | `docker run --rm --pid=host -v /etc:/node/etc:ro aquasec/kube-bench` |
| [Chaos Mesh](https://chaos-mesh.org/) | Cloud-native chaos engineering platform | Deploy via Helm: `helm install chaos-mesh chaos-mesh/chaos-mesh -n chaos-mesh` |
| [Litmus](https://litmuschaos.io/) | Kubernetes chaos engineering framework | Deploy via Helm: `helm install litmuschaos litmuschaos/litmus -n litmus` |
| [dive](https://github.com/wagoodman/dive) | Docker image layer analysis | `docker run --rm -v /var/run/docker.sock:/var/run/docker.sock wagoodman/dive` |
| [cosign](https://github.com/sigstore/cosign) | Container image signing and verification | `docker run --rm -v $(pwd):/workspace gcr.io/projectsigstore/cosign` |
