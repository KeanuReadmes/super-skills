# super-skills

**Super Skills** is a collection of expert-level system prompts designed to supercharge AI assistants (Claude, Gemini, Cursor, OpenAI) into specialized senior engineers. Each skill gives the AI a deep, opinionated persona with clear behavioral guidelines, so you get expert-level assistance — not generic answers.

## Available Skills

| Skill | Description |
|---|---|
| [SRE Engineer](skills/sre.md) | Site Reliability Engineer combining Infrastructure, Networking, Cybersecurity, DevOps, FinOps, and Disaster Recovery expertise with a pessimist mindset |
| [QA Engineer](skills/qa-engineer.md) | Quality Assurance Engineer covering test strategy, automation, performance, accessibility, and CI quality gates |
| [Backend Engineer](skills/backend-engineer.md) | Backend Engineer expert in API design, distributed systems, databases, messaging, security, and performance |
| [Frontend Engineer](skills/frontend-engineer.md) | Frontend Engineer specializing in React/Vue/Angular/Nuxt.js 4, performance (Core Web Vitals), accessibility, and design systems |
| [Cybersecurity Engineer](skills/cybersecurity-engineer.md) | Cybersecurity Engineer covering AppSec, cloud security, penetration testing, threat modeling, and incident response |
| [Project Manager Engineer](skills/project-manager.md) | Project Manager Engineer bridging technical execution and business goals via Agile, risk management, and stakeholder communication |
| [Architect / Documentator / Diagramer / Planner](skills/architect.md) | Systems architect who understands, organizes, diagrams, and improves complex systems with C4, UML, ADRs, and technical roadmaps |
| [CLI / Tools Engineer](skills/cli-tools-engineer.md) | CLI & Tools Engineer specializing in Python-first tooling with uv/poetry, clean code, proper packaging, CI/CD workflows, and pre-commit hooks |
| [SEO Specialist](skills/seo-specialist.md) | World-class SEO specialist covering technical SEO, E-E-A-T, Core Web Vitals, schema/structured data, GEO, AEO, hreflang, GitHub repository SEO, and AI search optimization |
| [Troubleshooter](skills/troubleshooter.md) | Root-cause analyst and protocol debugger covering system state collection, process anomaly detection, HTTP/REST/gRPC/GraphQL debugging, network diagnostics, VPN, and SSH — read-first, never damages a running system |

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
A modern UI engineer with deep expertise in React/Next.js/Nuxt.js 4, TypeScript, Core Web Vitals, WCAG accessibility, and design system development.

### 🔐 [Cybersecurity Engineer](skills/cybersecurity-engineer.md)
A full-spectrum security professional covering OWASP AppSec, cloud security posture, penetration testing, threat modeling (STRIDE), and incident response — with the "assume breach" mindset.

### 📋 [Project Manager Engineer](skills/project-manager.md)
A technically literate PM who combines Agile mastery, risk management, stakeholder communication, and engineering literacy to deliver projects on time with clarity.

### 🏛️ [Architect / Documentator / Diagramer / Planner](skills/architect.md)
A strategic technical leader who excels at understanding complex systems, producing C4 diagrams and ADRs, organizing information, and proactively suggesting improvements. This skill aces at making sense of ambiguity and turning it into structured, actionable artifacts.

### 🛠️ [CLI / Tools Engineer](skills/cli-tools-engineer.md)
A Python-first CLI and developer-tooling specialist who builds clean, installable, and well-documented command-line tools. Expert in `uv`, `poetry`, `Typer`/`Click`, `pyproject.toml` packaging, `--help`/`--version` wiring, CI/CD release pipelines, pre-commit hooks, and Makefile-driven workflows.

### 🔍 [SEO Specialist](skills/seo-specialist.md)
A world-class SEO specialist combining LLM-first reasoning with deterministic script-backed evidence. Covers technical SEO, E-E-A-T content scoring, Core Web Vitals (LCP, INP, CLS), schema/structured data (JSON-LD), hreflang, GEO (AI search optimization), AEO (featured snippets, PAA, Knowledge Panels), GitHub repository SEO, and strategic planning across SaaS, e-commerce, local, publisher, and agency verticals. Every audit delivers confidence-labeled findings, a scored report, and a prioritized `ACTION-PLAN.md`.

### 🔎 [Troubleshooter](skills/troubleshooter.md)
A root-cause analyst and protocol debugger who investigates server, OS, and application issues **without damaging running systems**. Collects a full read-only snapshot (logs, config files, open ports, processes, crontabs, users, shell histories, iptables/nftables, systemd services, init scripts, installed packages, changed files, Ansible drift, and abnormal processes) and correlates evidence to reach a confident root cause. Extends to debugging HTTP/REST APIs, gRPC, GraphQL, and networking (VPNs, SSH, DNS, firewall, MTU, packet captures). Every investigation follows a structured 10-step methodology with confidence-labeled hypotheses and explicit safety guardrails.

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
| [Rust](https://www.rust-lang.org/tools/install) | Systems-language backend runtime for high-performance services | `rustup toolchain install stable && rustup override set stable` |
| [clippy](https://github.com/rust-lang/rust-clippy) | Rust lints and correctness checks | `rustup component add clippy` |
| [rustfmt](https://github.com/rust-lang/rustfmt) | Rust formatter | `rustup component add rustfmt` |
| [cargo-nextest](https://nexte.st/) | Fast Rust test runner | `cargo install cargo-nextest` |
| [cargo-audit](https://github.com/rustsec/rustsec/tree/main/cargo-audit) | Scan Rust dependencies for known vulnerabilities | `cargo install cargo-audit` |
| [cargo-deny](https://github.com/EmbarkStudios/cargo-deny) | Dependency license/advisory policy checks for Rust | `cargo install cargo-deny` |
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
| [Rust](https://www.rust-lang.org/tools/install) | Build high-performance static CLI binaries | `rustup toolchain install stable && rustup override set stable` |
| [clap](https://github.com/clap-rs/clap) | Rust CLI argument parser and command framework | `cargo add clap` |
| [cross](https://github.com/cross-rs/cross) | Cross-compilation for Rust CLI releases | `cargo install cross` |
| [cargo-dist](https://github.com/axodotdev/cargo-dist) | Build and package Rust CLI release artifacts | `cargo install cargo-dist` |
| [cargo-nextest](https://nexte.st/) | Fast Rust test runner | `cargo install cargo-nextest` |
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
| [Nuxt.js 4 (`nuxi`)](https://nuxt.com/docs/getting-started/installation) | Nuxt 4 scaffolding, dev server, and build tooling | `npx nuxi@latest init <app-name>` |
| [@nuxt/devtools](https://github.com/nuxt/devtools) | Nuxt application inspection and debugging tools | `npx nuxi@latest module add @nuxt/devtools` |
| [@nuxt/image](https://image.nuxt.com/) | Nuxt-native image optimization module | `npx nuxi@latest module add @nuxt/image` |
| [@nuxtjs/i18n](https://i18n.nuxtjs.org/) | Internationalization module for Nuxt apps | `npx nuxi@latest module add @nuxtjs/i18n` |
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
| [Rust](https://www.rust-lang.org/tools/install) | Build memory-safe SRE automation and ops daemons | `rustup toolchain install stable && rustup override set stable` |
| [clippy](https://github.com/rust-lang/rust-clippy) | Rust static analysis for SRE tooling code | `rustup component add clippy` |
| [rustfmt](https://github.com/rust-lang/rustfmt) | Rust formatter for ops tooling repositories | `rustup component add rustfmt` |
| [cargo-audit](https://github.com/rustsec/rustsec/tree/main/cargo-audit) | Rust dependency vulnerability scanning | `cargo install cargo-audit` |
| [cargo-deny](https://github.com/EmbarkStudios/cargo-deny) | Rust license and advisory policy checks | `cargo install cargo-deny` |
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

---

### 🔍 SEO Specialist

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started) | Core Web Vitals (LCP, INP, CLS) — free, no key required for basic usage | `uv venv .venv && uv pip install requests` |
| [Lighthouse](https://github.com/GoogleChrome/lighthouse) | Lab-based performance and SEO audit | `docker run --rm -v $(pwd):/reports --cap-add=SYS_ADMIN ghcr.io/puppeteer/puppeteer lighthouse <url>` |
| [Playwright](https://playwright.dev/) | Headless browser for screenshots and JS-rendered SEO analysis | `uv venv .venv && uv pip install playwright && playwright install chromium` |
| [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) | HTML parsing and on-page element extraction | `uv venv .venv && uv pip install beautifulsoup4 lxml` |
| [html-validate](https://html-validate.org/) | HTML structural validation (semantic SEO) | `npm install --save-dev html-validate` |
| [axe-cli](https://github.com/dequelabs/axe-core) | Accessibility audit (overlaps with SEO quality signals) | `npm install --save-dev @axe-core/cli` |
| [Schema.org validator (Python)](https://pypi.org/project/extruct/) | Extract and validate structured data (JSON-LD, Microdata, RDFa) | `uv venv .venv && uv pip install extruct` |
| [rich](https://github.com/Textualize/rich) | Terminal-formatted SEO audit reports | `uv venv .venv && uv pip install rich` |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Load API credentials from `.env` without hardcoding secrets | `uv venv .venv && uv pip install python-dotenv` |
| [Pillow](https://python-pillow.org/) | Image format detection, dimensions, and optimization analysis | `uv venv .venv && uv pip install Pillow` |
| [GitHub CLI (`gh`)](https://cli.github.com/) | GitHub repository SEO audits (topics, traffic, community health) | `docker run --rm -v $(pwd):/work ghcr.io/cli/cli gh` |
| [pre-commit](https://pre-commit.com/) | Pre-commit hooks for schema validation and SEO quality gates | `uv tool install pre-commit` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Prevent API keys from being committed in SEO config files | `uv tool install detect-secrets` |
| [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) | Lint SEO reports and README files | `npx markdownlint-cli` |

---

### 🔎 Troubleshooter

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [ss / iproute2](https://man7.org/linux/man-pages/man8/ss.8.html) | Socket and port inspection (`ss -tulnpe`) | pre-installed on Linux |
| [lsof](https://github.com/nicowillis/lsof) | List open files and network connections per process | pre-installed on Linux/macOS |
| [tcpdump](https://www.tcpdump.org/) | Packet capture with BPF filter | pre-installed on Linux; `brew install tcpdump` on macOS |
| [tshark / Wireshark](https://www.wireshark.org/) | Protocol dissection and pcap analysis | `docker run --rm -v $(pwd):/cap ghcr.io/linuxserver/wireshark` |
| [mtr](https://github.com/traviscross/mtr) | Combined traceroute + ping network path diagnostic | `apt install mtr` / `brew install mtr` |
| [nmap](https://nmap.org/) | Network discovery and port scanning | `docker run --rm instrumentisto/nmap` |
| [grpcurl](https://github.com/fullstorydev/grpcurl) | gRPC service reflection, listing, and ad-hoc requests | `docker run --rm fullstorydev/grpcurl` |
| [HTTPie](https://httpie.io/) | Human-friendly HTTP/REST request tester | `uv tool install httpie` |
| [mitmproxy](https://mitmproxy.org/) | Interactive HTTP/HTTPS proxy for protocol inspection | `docker run --rm -it -p 8080:8080 mitmproxy/mitmproxy` |
| [curl](https://curl.se/) | HTTP/gRPC/protocol testing with verbose and trace output | pre-installed on Linux/macOS |
| [openssl](https://www.openssl.org/) | TLS/certificate inspection and validation | pre-installed on Linux/macOS |
| [wg / wireguard-tools](https://www.wireguard.com/) | WireGuard VPN status, peer, and handshake inspection | `apt install wireguard-tools` |
| [iperf3](https://github.com/esnet/iperf) | Network throughput and bandwidth measurement | `docker run --rm -it networkstatic/iperf3` |
| [ansible](https://www.ansible.com/) | Configuration drift detection via `--check --diff` | `uv venv .venv && uv pip install ansible` |
| [ansible-lint](https://ansible.readthedocs.io/projects/lint/) | Lint playbooks before dry-run checks | `uv venv .venv && uv pip install ansible-lint` |
| [AIDE](https://aide.github.io/) | File integrity monitoring (detect changed/unexpected files) | `apt install aide` |
| [debsums](https://packages.debian.org/debsums) | Verify Debian package file checksums | `apt install debsums` |
| [auditd / ausearch / aureport](https://github.com/linux-audit/audit-userspace) | Linux kernel audit log collection and query | `apt install auditd` |
| [scapy](https://scapy.net/) | Python-based packet crafting and analysis | `uv venv .venv && uv pip install scapy` |
| [pyshark](https://github.com/KimiNewt/pyshark) | Python wrapper for tshark packet analysis | `uv venv .venv && uv pip install pyshark` |
| [graphql-inspector](https://the-guild.dev/graphql/inspector) | GraphQL schema validation and introspection | `npx @graphql-inspector/cli` |
| [rover (Apollo)](https://www.apollographql.com/docs/rover/) | Apollo Federation schema composition checks | `docker run --rm apollographql/rover` |
| [Spectral](https://github.com/stoplightio/spectral) | OpenAPI / REST contract linting | `npx @stoplight/spectral-cli lint` |
| [shellcheck](https://www.shellcheck.net/) | Shell script static analysis for collection scripts | `docker run --rm -v $(pwd):/mnt koalaman/shellcheck` |
| [yamllint](https://github.com/adrienverge/yamllint) | Lint YAML config files being inspected | `uv tool install yamllint` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Prevent secrets from leaking into investigation artifacts | `uv tool install detect-secrets` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Scan config and history for credential leaks | `docker run --rm -v $(pwd):/path zricethezav/gitleaks` |
| [pre-commit](https://pre-commit.com/) | Enforce hook quality gates on investigation scripts | `uv tool install pre-commit` |
