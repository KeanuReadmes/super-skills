# super-skills

**Super Skills** is a collection of expert-level system prompts designed to supercharge AI assistants (Claude, Gemini, Cursor, OpenAI) into specialized senior engineers. Each skill gives the AI a deep, opinionated persona with clear behavioral guidelines, so you get expert-level assistance — not generic answers.

## Available Skills

| Skill | Description |
|---|---|
| [SRE Engineer](skills/sre.md) | Site Reliability Engineer combining Infrastructure, Networking, Cybersecurity, DevOps, FinOps, and Disaster Recovery expertise with a pessimist mindset |
| [QA Engineer](skills/qa-engineer.md) | Quality Assurance Engineer covering test strategy, automation, performance, accessibility, and CI quality gates |
| [Backend Engineer](skills/backend-engineer.md) | Backend Engineer expert in API design, distributed systems, databases, messaging, security, and performance |
| [PostgreSQL Engineer](skills/postgres-engineer.md) | PostgreSQL performance engineer focused on read-only diagnostics, slow query analysis, lock contention reduction, and high-impact runtime tuning |
| [Frontend Engineer](skills/frontend-engineer.md) | Frontend Engineer specializing in React/Vue/Angular/Nuxt.js 4, performance (Core Web Vitals), accessibility, and design systems |
| [Cybersecurity Engineer](skills/cybersecurity-engineer.md) | Cybersecurity Engineer covering AppSec, cloud security, penetration testing, threat modeling, and incident response |
| [Project Manager Engineer](skills/project-manager.md) | Project Manager Engineer bridging technical execution and business goals via Agile, risk management, and stakeholder communication |
| [Architect / Documentator / Diagramer / Planner](skills/architect.md) | Systems architect who understands, organizes, diagrams, and improves complex systems with C4, UML, ADRs, and technical roadmaps |
| [CLI / Tools Engineer](skills/cli-tools-engineer.md) | CLI & Tools Engineer specializing in Python-first tooling with uv/poetry, clean code, proper packaging, CI/CD workflows, and pre-commit hooks |
| [SEO Specialist](skills/seo-specialist.md) | World-class SEO specialist covering technical SEO, E-E-A-T, Core Web Vitals, schema/structured data, GEO, AEO, hreflang, GitHub repository SEO, and AI search optimization |
| [Troubleshooter](skills/troubleshooter.md) | Root-cause analyst and protocol debugger covering system state collection, process anomaly detection, HTTP/REST/gRPC/GraphQL debugging, network diagnostics, VPN, and SSH — read-first, never damages a running system |
| [Code Reviewer](skills/code-reviewer.md) | Senior code reviewer covering full branch-diff analysis, blast radius assessment, lint enforcement, documentation verification against exact library versions, test coverage audit, naming and scope review, architecture alignment, and Conventional Commits validation |
| [Auditor](skills/auditor.md) | Repository auditor covering branch protection, security & supply chain guardrails, CI automation gaps, pre-commit setup, and community health standards — opens GitHub Issues and PRs to track and remediate every finding |
| [Weekly Activities Generator](skills/weekly-activities-generator.md) | Generates simple, high-level, concise weekly activity summaries from a user's open PRs and code changes |
| [Rust MCP Coder](skills/rust-mcp-coder.md) | Expert Rust engineer who builds production-grade, token-authenticated MCP servers with Axum using TDD, cargo audit, clippy, full CI/CD, and dual HTTP/SSE transport for maximum client compatibility |

## How to Use

Copy the **System Prompt** from any skill file and paste it as the system prompt in your AI assistant:

- **Claude** — Project instructions or system prompt in the API
- **Gemini** — System instruction field
- **Cursor** — `.cursorrules` or Rules for AI in settings
- **OpenAI** — System message or Custom Instructions

Combine multiple skills by merging their prompts, or use them individually.

## Delivery Standards

Every skill produces **fully functioning solutions**, not just code snippets:

- **Makefile** — Self-documenting targets for install, run, test, lint, format, and clean. Run `make help` to list them.
- **Pre-commit hooks** — `.pre-commit-config.yaml` with pinned, stack-appropriate hooks. Run `pre-commit install` once.
- **Test scripts (`tools/`)** — Validation and smoke-test scripts as a `uv` project. Run any with `uv run <script>`.
- **README.md** — Setup, run, test, lint, and contribution instructions included with every deliverable.

## Open Source Tools Reference

<details>
<summary>Per-skill tool tables with sandbox install commands</summary>

> **Sandbox-first:** Avoid `sudo pip install`, `sudo npm install -g`, or bare `brew install`. Use the isolated commands below.

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

---

### 🔬 Code Reviewer

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [ruff](https://github.com/astral-sh/ruff) | Python linting and formatting | `uv tool install ruff` |
| [mypy](https://mypy.readthedocs.io/) | Python static type checking | `uv venv .venv && uv pip install mypy` |
| [bandit](https://github.com/PyCQA/bandit) | Python security linting (OWASP) | `uv venv .venv && uv pip install bandit` |
| [pylint](https://pylint.readthedocs.io/) | Python code analysis and convention checks | `uv venv .venv && uv pip install pylint` |
| [coverage.py / pytest-cov](https://coverage.readthedocs.io/) | Python test coverage measurement | `uv venv .venv && uv pip install pytest-cov` |
| [ESLint](https://eslint.org/) | JavaScript/TypeScript linting | `npm install --save-dev eslint` |
| [TypeScript (`tsc`)](https://www.typescriptlang.org/) | TypeScript type checking | `npm install --save-dev typescript` |
| [Prettier](https://prettier.io/) | Code formatter for JS/TS/JSON/YAML | `npm install --save-dev prettier` |
| [nyc / c8](https://github.com/istanbuljs/nyc) | JavaScript/TypeScript test coverage | `npm install --save-dev c8` |
| [golangci-lint](https://golangci-lint.run/) | Go meta-linter (vet, staticcheck, errcheck, …) | `docker run --rm -v $(pwd):/app golangci/golangci-lint golangci-lint run` |
| [staticcheck](https://staticcheck.dev/) | Go static analysis and bug detection | `docker run --rm -v $(pwd):/app golangci/golangci-lint golangci-lint run` |
| [clippy](https://github.com/rust-lang/rust-clippy) | Rust linter | `rustup component add clippy && cargo clippy -- -D warnings` |
| [rustfmt](https://github.com/rust-lang/rustfmt) | Rust code formatter | `rustup component add rustfmt && cargo fmt --check` |
| [cargo-audit](https://rustsec.org/) | Rust dependency vulnerability scanner | `cargo install cargo-audit && cargo audit` |
| [cargo-tarpaulin](https://github.com/xd009642/tarpaulin) | Rust test coverage | `cargo install cargo-tarpaulin && cargo tarpaulin` |
| [semgrep](https://semgrep.dev/) | Multi-language static analysis and security patterns | `docker run --rm -v $(pwd):/src semgrep/semgrep semgrep scan --config=auto` |
| [trivy](https://aquasecurity.github.io/trivy/) | Dependency and container vulnerability scanning | `docker run --rm -v $(pwd):/work aquasec/trivy fs /work` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Git history and staged-change secret scanning | `docker run --rm -v $(pwd):/path zricethezav/gitleaks detect` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Pre-commit secret baseline scanning | `uv tool install detect-secrets` |
| [pip-audit](https://pypi.org/project/pip-audit/) | Python dependency vulnerability audit | `uv tool install pip-audit` |
| [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) | Node.js dependency vulnerability audit | `npm audit` |
| [pre-commit](https://pre-commit.com/) | Run multi-language pre-commit hooks | `uv tool install pre-commit` |
| [shellcheck](https://www.shellcheck.net/) | Shell script static analysis | `docker run --rm -v $(pwd):/mnt koalaman/shellcheck` |
| [hadolint](https://github.com/hadolint/hadolint) | Dockerfile linting | `docker run --rm -i hadolint/hadolint < Dockerfile` |
| [yamllint](https://github.com/adrienverge/yamllint) | YAML configuration file linting | `uv tool install yamllint` |
| [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) | Markdown documentation linting | `npx markdownlint-cli` |

---

### 🔎 Auditor

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [GitHub CLI (`gh`)](https://cli.github.com/) | Query branch protection, open issues and PRs, manage repository settings | `docker run --rm -v $(pwd):/work ghcr.io/cli/cli gh` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Detect secrets in git history and staged changes | `docker run --rm -v $(pwd):/path zricethezav/gitleaks detect --source /path` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets baseline scanning and pre-commit hook | `uv tool install detect-secrets` |
| [Semgrep](https://semgrep.dev/) | SAST — static application security testing | `docker run --rm -v $(pwd):/src semgrep/semgrep semgrep scan --config=auto` |
| [Trivy](https://github.com/aquasecurity/trivy) | Dependency and container vulnerability scanning | `docker run --rm -v $(pwd):/work aquasec/trivy fs /work` |
| [pip-audit](https://pypi.org/project/pip-audit/) | Python dependency vulnerability audit | `uv tool install pip-audit` |
| [pre-commit](https://pre-commit.com/) | Pre-commit hook runner and configuration validator | `uv tool install pre-commit` |
| [yamllint](https://github.com/adrienverge/yamllint) | Lint workflow YAML and `.pre-commit-config.yaml` | `uv tool install yamllint` |
| [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) | Lint `README.md`, `CONTRIBUTING.md`, and community files | `npx markdownlint-cli` |

---

### 🦀 Rust MCP Coder

| Tool | Purpose | Sandbox Install |
|------|---------|----------------|
| [Rust](https://www.rust-lang.org/tools/install) | Systems language for building memory-safe, high-performance MCP servers | `rustup toolchain install stable && rustup override set stable` |
| [clippy](https://github.com/rust-lang/rust-clippy) | Rust linter — always run with `-- -D warnings` | `rustup component add clippy` |
| [rustfmt](https://github.com/rust-lang/rustfmt) | Rust code formatter | `rustup component add rustfmt` |
| [cargo-nextest](https://nexte.st/) | Fast Rust test runner with better output and parallelism | `cargo install cargo-nextest --locked` |
| [cargo-audit](https://rustsec.org/) | Scan Rust dependencies for known CVEs via the RustSec advisory DB | `cargo install cargo-audit --locked` |
| [cargo-deny](https://github.com/EmbarkStudios/cargo-deny) | Dependency license, advisory, and duplicate-crate policy checks | `cargo install cargo-deny --locked` |
| [cargo-tarpaulin](https://github.com/xd009642/tarpaulin) | Rust code coverage (HTML, XML/Cobertura, LCOV output) | `cargo install cargo-tarpaulin --locked` |
| [axum](https://github.com/tokio-rs/axum) | Ergonomic and modular Axum HTTP framework for MCP server transport | `cargo add axum --features macros,json` |
| [tokio](https://tokio.rs/) | Async runtime powering all I/O in the MCP server | `cargo add tokio --features full` |
| [tower-http](https://github.com/tower-rs/tower-http) | Tower middleware: CORS, tracing, compression, request-id | `cargo add tower-http --features cors,trace,compression-gzip,request-id` |
| [subtle](https://github.com/dalek-cryptography/subtle) | Constant-time comparison for ****** auth (prevents timing oracles) | `cargo add subtle` |
| [tower_governor](https://github.com/benwis/tower-governor) | Rate limiting middleware for Axum/Tower | `cargo add tower_governor` |
| [thiserror](https://github.com/dtolnay/thiserror) | Derive macro for ergonomic typed error enums | `cargo add thiserror` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Detect secrets in git history and staged changes | `docker run --rm -v $(pwd):/path zricethezav/gitleaks detect --source /path` |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Secrets baseline scanning and pre-commit hook | `uv tool install detect-secrets` |
| [pre-commit](https://pre-commit.com/) | Pre-commit hook runner for fmt, clippy, audit, and secrets | `uv tool install pre-commit` |

</details>

## Contribution Guidelines

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
- Use Conventional Commits for all commit messages.
- Run `make lint` and `make validate` before submitting changes.

## Security

- Read [SECURITY.md](SECURITY.md) for vulnerability reporting instructions.
- Do not disclose unpatched vulnerabilities in public issues.

## Code of Conduct

All contributors are expected to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
