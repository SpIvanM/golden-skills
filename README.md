# golden-skills

A curated collection of foundational, battle-tested skills for AI coding agents (Claude Code, Google Antigravity, Cursor, Codex, OpenCode).

These skills are designed around the **Agent-First** philosophy: high leverage, minimal token overhead, strict escalation tiers, and high signal-to-noise ratio.

---

## 📦 Included Skills

### 1. `/rc` — Rule & Skill Crafting
*Location:* `rc/`

Enforces strict standards for writing compact, unambiguous instructions for AI agents. Eliminates context pollution, verbosity, and weak phrasing.

- **Audience Routing:** Places rules strictly where they belong (Global, Project, Scoped, Role, Hook, or Discard).
- **Escalation Levels (0–6):** From direct imperatives (Level 0) to categorical prohibitions (Level 2) and concrete positive/negative examples (Levels 4–5).
- **Constraint Limits:** Strict 1-line-per-directive rule, character caps, and active imperative phrasing.
- **Bilingual:** Contains both English (`SKILL.md`) and Russian (`SKILL_RU.md`) definitions and authoring guides.

### 2. `/rca` — Targeted Behavioral Root Cause Analysis
*Location:* `rca/`

Conducts systematic Root Cause Analysis (5 Whys) when an AI agent misbehaves, violates guidelines, or exhibits cognitive bias.

- **Diagnostic Layers:** Analyzes failures across Prompt, Rules, Skills, Harness, and Context saturation layers.
- **Anti-Reassurance Guarantee:** Replaces polite apologies and verbal soothing with actionable, permanent fixes committed to disk.
- **Handoff to `/rc`:** Formulates calibrated rule patches ready for deployment.
- **Bilingual:** English (`SKILL.md`) and Russian (`SKILL_RU.md`).

---

## 🚀 Installation & Usage

### Installing into Skills directory

Clone or copy individual skills into your agent's skills directory:

#### Google Antigravity
Copy skill directories to `~/.gemini/config/skills/` or `.agents/skills/`:
```bash
cp -r rc ~/.gemini/config/skills/
cp -r rca ~/.gemini/config/skills/
```

#### Claude Code
Copy skill directories to your Claude skills folder (e.g. `~/.claude/skills/`):
```bash
cp -r rc ~/.claude/skills/
cp -r rca ~/.claude/skills/
```

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
