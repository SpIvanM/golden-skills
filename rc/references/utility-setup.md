# Utility Setup Protocol

[Русская версия (utility-setup_RU.md)](./utility-setup_RU.md)

## Goal
Automate utility provisioning and direct execution without checking availability.

## 1. Execution & Invocation Directives
- Automate deterministic operations with scripts in `scripts/`.
- Direct skills to invoke CLI utilities immediately assuming availability.
- ‼ Checking tool availability or --version prior to invocation is strictly prohibited.
- Add fallback rule "If utility execution fails, read [setup.md](./setup.md)".
- Place cross-platform installation tasks in setup_task.md.

## 2. Utility Setup Templates

### Ready Template: setup.md
```text
# Setup Protocol
- Delegate installation to devops subagent via invoke_subagent.
- Provide prompt: execute environment setup according to setup_task.md.
- Resume skill execution once devops subagent finishes provisioning.
```

### Ready Template: setup_task.md
```text
# Setup Task: <utility>
- Install on Windows via mise or package manager into PATH.
- Install on WSL or Linux via distro package into PATH.
- Install on macOS via brew into system PATH.
- Ensure executable is reachable in PATH without errors.
```
