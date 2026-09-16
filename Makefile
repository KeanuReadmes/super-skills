REPO_DIR := $(shell pwd)
SKILLS   := $(patsubst skills/%.md,%,$(wildcard skills/*.md))

CLAUDE_SKILLS_DIR := $(HOME)/.claude/skills
AGENTS_SKILLS_DIR := $(HOME)/.agents/skills
GEMINI_SKILLS_DIR := $(HOME)/.gemini/skills
CURSOR_SKILLS_DIR := $(HOME)/.cursor/skills
COPILOT_SKILLS_DIR := $(HOME)/.copilot/skills
CODEX_HOME ?= $(HOME)/.codex
CODEX_SKILLS_DIR := $(CODEX_HOME)/skills

.PHONY: help install uninstall lint validate audit

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

# Codex discovery requires a regular SKILL.md. Stage then rename to replace legacy
# file symlinks without writing through them. Re-run install after editing skills.
install: ## Install Codex skill files and symlinks for other supported tools
	@echo "Installing skills to $(CODEX_SKILLS_DIR), $(CLAUDE_SKILLS_DIR), $(AGENTS_SKILLS_DIR), $(GEMINI_SKILLS_DIR), $(CURSOR_SKILLS_DIR), and $(COPILOT_SKILLS_DIR)..."
	@$(foreach name,$(SKILLS), \
		mkdir -p "$(CODEX_SKILLS_DIR)/$(name)" && \
		cp "$(REPO_DIR)/skills/$(name).md" "$(CODEX_SKILLS_DIR)/$(name)/.SKILL.md.tmp" && \
		mv -f "$(CODEX_SKILLS_DIR)/$(name)/.SKILL.md.tmp" "$(CODEX_SKILLS_DIR)/$(name)/SKILL.md" && \
		mkdir -p "$(CLAUDE_SKILLS_DIR)/$(name)" && \
		ln -sf "$(REPO_DIR)/skills/$(name).md" "$(CLAUDE_SKILLS_DIR)/$(name)/SKILL.md" && \
		mkdir -p "$(AGENTS_SKILLS_DIR)/$(name)" && \
		cp "$(REPO_DIR)/skills/$(name).md" "$(AGENTS_SKILLS_DIR)/$(name)/.SKILL.md.tmp" && \
		mv -f "$(AGENTS_SKILLS_DIR)/$(name)/.SKILL.md.tmp" "$(AGENTS_SKILLS_DIR)/$(name)/SKILL.md" && \
		mkdir -p "$(GEMINI_SKILLS_DIR)/$(name)" && \
		ln -sf "$(REPO_DIR)/skills/$(name).md" "$(GEMINI_SKILLS_DIR)/$(name)/SKILL.md" && \
		mkdir -p "$(CURSOR_SKILLS_DIR)/$(name)" && \
		ln -sf "$(REPO_DIR)/skills/$(name).md" "$(CURSOR_SKILLS_DIR)/$(name)/SKILL.md" && \
		mkdir -p "$(COPILOT_SKILLS_DIR)/$(name)" && \
		ln -sf "$(REPO_DIR)/skills/$(name).md" "$(COPILOT_SKILLS_DIR)/$(name)/SKILL.md" && \
	) true
	@echo "Done. $(words $(SKILLS)) skill(s) installed."

uninstall: ## Remove installed skills from Codex and other supported skill dirs
	@echo "Uninstalling skills from $(CODEX_SKILLS_DIR), $(CLAUDE_SKILLS_DIR), $(AGENTS_SKILLS_DIR), $(GEMINI_SKILLS_DIR), $(CURSOR_SKILLS_DIR), and $(COPILOT_SKILLS_DIR)..."
	@$(foreach name,$(SKILLS), \
		rm -f "$(CODEX_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(CODEX_SKILLS_DIR)/$(name)" 2>/dev/null; \
		rm -f "$(CLAUDE_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(CLAUDE_SKILLS_DIR)/$(name)" 2>/dev/null; \
		rm -f "$(AGENTS_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(AGENTS_SKILLS_DIR)/$(name)" 2>/dev/null; \
		rm -f "$(GEMINI_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(GEMINI_SKILLS_DIR)/$(name)" 2>/dev/null; \
		rm -f "$(CURSOR_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(CURSOR_SKILLS_DIR)/$(name)" 2>/dev/null; \
		rm -f "$(COPILOT_SKILLS_DIR)/$(name)/SKILL.md" && \
		rmdir --ignore-fail-on-non-empty "$(COPILOT_SKILLS_DIR)/$(name)" 2>/dev/null; \
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
