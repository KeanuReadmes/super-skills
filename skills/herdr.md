---
name: herdr
description: >-
  Controls the Herdr terminal workspace from inside a Herdr-managed pane with the herdr CLI: inspects workspaces, tabs, and panes, splits panes, starts and prompts coding agents, runs commands in sibling panes, reads their output, and waits for state changes. Use when running inside Herdr (HERDR_ENV=1) and the work needs parallel agents or commands in other panes; refuses to act outside Herdr.
---

# Herdr

## System Prompt

### Repository Context & License Compatibility (Mandatory)

Before changing a repository through Herdr panes, read `AGENTS.md`, `CONTRIBUTING.md`, every file under `/docs`, and `CONVENTIONS.md` / `CONTEXT.md` if present, and pass the relevant rules to every agent you start. Before any pane or agent adds or upgrades a third-party component, read `/LICENSE`, confirm the component's license is compatible, and report license-check tooling output (`npx --yes license-checker --summary`, `uvx pip-licenses`, `cargo deny check licenses`, `go-licenses check ./...`). Never recommend an incompatible component.

### Preconditions

Herdr organizes terminals into workspaces, tabs, and panes and recognizes coding agents running inside panes. Act only from inside a Herdr-managed pane:

```bash
test "${HERDR_ENV:-}" = 1
```

If the check fails, say you are not running inside Herdr and stop. Never inspect or control a Herdr session from outside it.

### Learn the CLI

The installed binary is the authority on syntax. Run `herdr --help`, then a command group without a subcommand to print its usage: `herdr agent`, `pane`, `workspace`, `tab`, `worktree`, `terminal`, `notification`, `integration`, `session`. Never run bare `herdr` (it opens the TUI), and never probe a mutating subcommand by omitting arguments — `herdr workspace create` runs with defaults. Most commands return JSON; read IDs and state from it instead of predicting them.

### Model

- **Pane vs agent**: pane commands control raw terminals (shells, tests, servers, input, output); agent commands control the recognized coding agent in a pane and interpret its lifecycle. `agent start` needs an existing shell pane and never creates, splits, or moves layout.
- **Agent targets**: a unique live agent name (`[a-z][a-z0-9_-]{0,31}`) or the pane ID hosting it — never terminal IDs or agent kinds. A name follows the pane occupant and clears when the agent exits, is released, or is replaced.
- **States**: `idle` = ready and its tab seen; `done` = idle after unseen background work (focusing marks it seen; CLI reads do not); `working`; `blocked` = approval or question UI; `unknown` = present but unclassified, which does not prove completion.
- **IDs** are opaque and never reused: workspace `w1`, tab `w1:t1`, pane `w1:p1`. After `pane move`, use `.result.move_result.pane.pane_id` or the agent name, never `.result.move_result.previous_pane_id`.
- **Caller context**: `$HERDR_WORKSPACE_ID`, `$HERDR_TAB_ID`, `$HERDR_PANE_ID`. Use `--current` to target the calling pane; omitting a target may hit the pane the user or another client has focused.
- **Discover**: `herdr workspace list`, `herdr tab list --workspace "$HERDR_WORKSPACE_ID"`, `herdr pane current --current`, `herdr pane list --workspace "$HERDR_WORKSPACE_ID"`, `herdr agent list`.
- **Creation results**: `workspace create` → `.result.workspace`, `.result.tab`, `.result.root_pane`; `tab create` → `.result.tab`, `.result.root_pane`; `pane split` → `.result.pane`.

### Workflow: start and prompt an agent

1. Default to a sibling pane in the current tab and cwd; create workspaces, tabs, worktrees, or other cwds only when the user asks. Honor a requested direction; otherwise check `herdr pane layout --pane "$HERDR_PANE_ID"` and split wide panes `right`, narrow or tall panes `down`, avoiding repeated same-direction splits.
2. `herdr pane split --current --direction right --cwd "$PWD" --no-focus`, then read `.result.pane.pane_id`.
3. With the shell at its prompt and nothing in the foreground, run `herdr agent start reviewer --kind codex --pane <pane-id>`, adding native agent args only after `--`. Use the kind the user asked for (`herdr agent` lists kinds). It returns once the agent is ready (30 s default timeout); `agent_not_ready` means it is blocked at startup, so wait for `idle` before prompting.
4. `herdr agent prompt reviewer "<task>" --wait --timeout 120000`. `--wait` returns at the first settled `idle`, `done`, or `blocked`; do not repeat those with `--until`. `agent_blocked` means a dialog is open — inspect it and ask the user before answering. `agent_prompt_stalled` means no lifecycle change within 5 s. `--wait` tracks lifecycle state, not your turn: if the agent was already working, it may return when that turn ends, so check the output answers your prompt.
5. Use `herdr agent wait reviewer --until blocked --timeout 120000` only for state-specific waits. Send UI keys as logical names: `herdr agent send-keys reviewer esc` or `ctrl+c`.
6. Read results with `herdr agent get reviewer` and `herdr agent read reviewer --source recent-unwrapped --lines 120`. After a failed wait or `blocked`, inspect both before sending any input; use pane commands only when raw terminal control is intended.

### Workflow: run a command in another pane

Split a sibling pane as above, then:

```bash
herdr pane run <pane-id> "just test"
herdr pane wait-output <pane-id> --match "test result" --timeout 120000
herdr pane read <pane-id> --source recent-unwrapped --lines 120
```

- `pane run` sends the text and Enter atomically. `wait-output` also matches output that already exists; use `--match` for literals or `--regex` for Rust regexes, and always pass `--timeout` (omitting it waits forever).
- Read sources: `visible` (viewport), `recent` (with soft wraps), `recent-unwrapped` (wraps joined; best for logs), `detection` (agent-detection buffer). Add `--format ansi` only when styling is evidence.
- If raising `--lines` reveals nothing more, the agent is on the alternate screen. Only then, ask it to write its full answer to a temporary Markdown file, reply with the path, and read the file.

### Guardrails

1. Use `--no-focus` for background work unless the user asked to switch context.
2. Target with `--current`, an explicit pane ID, or a unique agent name; never rely on another client's focused pane.
3. Parse IDs from JSON responses, never from sidebar order or examples.
4. Close only the workspaces, tabs, panes, or sessions you created, unless the user explicitly asks.
5. Never run `herdr server stop` from an active session unless the user means to stop the server and its pane processes; never kill the main Herdr process; use named test sessions for isolated experiments.
6. Errors: server errors are JSON on stderr with exit status 1; CLI syntax errors exit with status 2.
