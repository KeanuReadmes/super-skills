REPO_DIR := $(shell pwd)
SKILLS   := $(patsubst skills/%.md,%,$(wildcard skills/*.md))

GEMINI_SKILLS_DIR := $(HOME)/.gemini/skills
CURSOR_SKILLS_DIR := $(HOME)/.cursor/skills

.PHONY: help install uninstall lint validate audit

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Install skill symlinks into ~/.gemini/skills and ~/.cursor/skills
	@echo "Installing skills to $(GEMINI_SKILLS_DIR) and $(CURSOR_SKILLS_DIR)..."
	@$(foreach name,$(SKILLS), \
		mkdir -p "$(GEMINI_SKILLS_DIR)/$(name)" && \
		ln -sf "$(REPO_DIR)/skills/$(name).md" "$(GEMINI_SKILLS_DIR)/$(name)/SKILL.md" && \
		mkdir -p "$(CURSOR_SKILLS_DIR)/$(name)" && \
		ln -sf "$(REPO_DIR)/skills/$(name).md" "$(CURSOR_SKILLS_DIR)/$(name)/SKILL.md" && \
	) true
	@echo "Done. $(words $(SKILLS)) skill(s) installed."

uninstall: ## Remove installed skill symlinks from ~/.gemini/skills and ~/.cursor/skills
	@echo "Uninstalling skills from $(GEMINI_SKILLS_DIR) and $(CURSOR_SKILLS_DIR)..."
	@$(foreach name,$(SKILLS), \
		rm -f "$(GEMINI_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(GEMINI_SKILLS_DIR)/$(name)" 2>/dev/null; \
		rm -f "$(CURSOR_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(CURSOR_SKILLS_DIR)/$(name)" 2>/dev/null; \
	) true
	@echo "Done."

lint: ## Lint all Markdown skill files and README (requires markdownlint-cli via npx)
	npx --yes markdownlint-cli skills/*.md README.md

validate: ## Validate YAML workflow files (requires yamllint via uv tool install yamllint)
	yamllint .github/workflows/

audit: ## Run baseline repository audit checks
	@if command -v uv >/dev/null 2>&1; then \
		uv run --directory tools --package audit-runner audit-runner; \
	else \
		python3 tools/apps/audit_runner/src/audit_runner/cli.py; \
	fi
