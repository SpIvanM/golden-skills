<div align="center">

# 🌟 golden-skills

**The foundational, battle-tested skill suite for autonomous AI coding agents.**  
*High leverage • Zero context pollution • Strict escalation tiers • Closed-loop self-correction*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Agents](https://img.shields.io/badge/Agents-Claude%20Code%20%7C%20Antigravity%20%7C%20Cursor%20%7C%20Codex-8A2BE2)](#-platform-compatibility)
[![Telegram](https://img.shields.io/badge/Telegram-prompts4llm-2CA5E0?logo=telegram)](https://t.me/prompts4llm)

[English](README.md) • [Русский](README_RU.md)

</div>

---

## 💡 Why golden-skills?

Most AI agent failures are **not** capability issues — they are **governance and feedback issues**:
- **Instruction drift & context bloat:** LLMs lose adherence as rules grow long, verbose, and vague.
- **Sycophancy & verbal soothing:** When criticized, agents apologize repeatedly without fixing the underlying system failure.
- **Wrong audience routing:** Rules intended for one subagent pollute global prompt memory, degrading overall performance.

**`golden-skills`** provides a minimal, closed-loop operating framework to systematically govern, diagnose, and refine agent behavior across all modern AI environments.

---

## 🔄 The Closed-Loop Architecture

The repository revolves around two complementary superpowers:

```mermaid
flowchart TD
    A[Agent Failure / Behavioral Defect] --> B[/rca: Root Cause Analysis]
    B --> C{5 Diagnostic Layers}
    C -->|Layer 1: Prompt| D[Prompt Calibration]
    C -->|Layer 2: Rules| E[Rule Gap / Conflict]
    C -->|Layer 3: Skills| F[Missing / Weak Skill]
    C -->|Layer 4: Harness| G[System Harness Conflict]
    C -->|Layer 5: Context| H[Context Saturation]
    
    E & F --> I[/rc: Rule & Skill Crafter]
    I --> J[Audience Routing: Global / Project / Role]
    J --> K[Calibrated Escalation Level 0 - 6]
    K --> L[Atomic In-Place Disk Update]
    L --> M[Permanent Behavioral Immune Response]

    style A fill:#ff4d4f,stroke:#333,stroke-width:1px,color:#fff
    style B fill:#1890ff,stroke:#333,stroke-width:1px,color:#fff
    style I fill:#52c41a,stroke:#333,stroke-width:1px,color:#fff
    style M fill:#722ed1,stroke:#333,stroke-width:1px,color:#fff
```

1. **Diagnose with `/rca`:** Pinpoint the exact layer that failed (Prompt, Rules, Skills, Harness, Context) using targeted 5 Whys.
2. **Cure with `/rc`:** Formulate atomic, token-dense directives calibrated to the minimum necessary escalation tier.

---

## 📦 Included Skills

### 1. `/rc` — Rule & Skill Crafting
📁 **Path:** `rc/` • **Description:** *"Use when you need to change or write a rule, skill"*

Eliminates prompt bloat and enforces high-signal directives. Built on YAGNI and KISS principles.

#### Audience Routing (Where rules belong)
| Audience | Destination | Purpose |
| :--- | :--- | :--- |
| **Global** | Root / Global `AGENTS.md` | Universal invariants applying across all agents. |
| **Project** | `<project-root>/AGENTS.md` | Project-specific tech stack, architectural conventions. |
| **Scoped** | `.agents/rules/*.md` | Path-based globs and sub-domains. |
| **Role** | Governing `SKILL.md` | Archetype-specific workflows and competencies. |
| **Hook / Linter** | Git hooks / CLI scripts | Mechanical, deterministic validations. |
| **Discard** | *None (Do not persist)* | Ephemeral bugs or one-off developer quirks. |

#### Escalation Levels
Start new rules at **Level 0**. Escalate strictly upon verified, repeated violations:

| Level | Identifier | Syntax / Nature | Example |
| :---: | :---: | :--- | :--- |
| **0** | Base | Direct imperative verb; maximal brevity | `- Write concisely.` |
| **1** | `!` | Contrastive imperative or conditional | `- Pass all task messages: inclusion is better than omission.` |
| **2** | `!!` | Categorical prohibition (`strictly prohibited`) | `- ‼ If context lacks message numbers, launch is strictly prohibited.` |
| **3** | `!!!` | CAPITALIZED operational verbs for repeated breaches | `- ‼ RUN tests before committing changes.` |
| **4** | `!!!!` | Concrete positive example (1 line) | `- !!!! ✅ [readme](../../folder/file.ext)` |
| **5** | `!!!!!` | Concrete negative anti-pattern (1 line) | `- !!!!! ❌ [readme](file:///path/file.ext)` |
| **6** | `💬` | Mechanistic explanation (1 line) | `- 💬 Verbal soothing is a lie; active fix requires updating rules.` |

#### Good vs. Bad Directives

| ❌ Bad (Bloated, Weak, Ambiguous) | ✅ Good (Atomic, High-Density, Enforceable) |
| :--- | :--- |
| `- **Paths**: Always use relative paths, and also ask confirmation before rm.` | `- Use relative paths for all workspace references.`<br>`- ‼ Removing files without user confirmation is strictly prohibited.` |
| `- Blind launch ban: launching without message numbers is prohibited.` | `- ‼ If context lacks message numbers, launching a subagent is strictly prohibited.` |
| `- Please make sure you write tests whenever you can.` | `- Write failing tests before modifying implementation code.` |

---

### 2. `/rca` — Targeted Behavioral Root Cause Analysis
📁 **Path:** `rca/` • **Description:** *"Use when you need to find defect root cause via 5 why, rca, or /rca"*

A structured, bias-aware diagnostic framework for AI agents.

#### The 5 Diagnostic Layers
1. **Layer 1 (Prompt):** Missing boundaries, ambiguous instructions, unstated user assumptions.
2. **Layer 2 (Rules):** Contradictory rules, gaps in `AGENTS.md`, or perverse incentive structures.
3. **Layer 3 (Skills):** Ambiguous step sequences, missing verification gates in `SKILL.md`.
4. **Layer 4 (Harness):** Developer system prompts or platform constraints conflicting with user goals.
5. **Layer 5 (Context):** Context saturation (>100k tokens), attention dispersion, or instruction drift.

#### Core Diagnostic Principles
- **Strict Anti-Reassurance:** Apologetic commentary and verbal promises are strictly forbidden. Fixes must be structural and written to disk.
- **Model Priors Assessment:** Accounts for inherent LLM biases (eager agreement, sycophancy, premature execution).
- **Principle Over Instance:** Generalize episodic errors into systemic behavioral archetypes — never put temporary filenames into rules.
- **Seamless `/rc` Handoff:** Every `/rca` session terminates with an exact specification ready for execution by `/rc`.

---

## 🛠️ Platform Compatibility & Installation

`golden-skills` conforms to the open Agent Skill specification (`SKILL.md` with YAML frontmatter) and is compatible with all leading agentic platforms:

| Platform | Skill Location | Support Status |
| :--- | :--- | :---: |
| **Google Antigravity** | `~/.gemini/config/skills/` or `<project>/.agents/skills/` | ✅ Native |
| **Claude Code** | `~/.claude/skills/` or `<project>/.claude/skills/` | ✅ Native |
| **Cursor** | `.cursor/rules/` or project skills | ✅ Compatible |
| **OpenAI Codex / CLI** | `.codex/skills/` or project config | ✅ Compatible |
| **Hermes Agent** | `~/.hermes/skills/` | ✅ Compatible |

### Quick Installation

```bash
# Clone the repository
git clone https://github.com/SpIvanM/golden-skills.git

# Install globally for Google Antigravity
cp -r golden-skills/rc ~/.gemini/config/skills/
cp -r golden-skills/rca ~/.gemini/config/skills/

# Install globally for Claude Code
cp -r golden-skills/rc ~/.claude/skills/
cp -r golden-skills/rca ~/.claude/skills/
```

Or symlink into your active workspace:
```bash
ln -s /path/to/golden-skills/rc .agents/skills/rc
ln -s /path/to/golden-skills/rca .agents/skills/rca
```

---

## 📂 Repository Structure

```text
golden-skills/
├── LICENSE                       # MIT License
├── README.md                     # English documentation
├── README_RU.md                  # Полная русскоязычная документация
├── CONTRIBUTING.md               # Guidelines for contributors
├── rc/                           # Rule & Skill Crafting skill
│   ├── SKILL.md                  # English specification
│   ├── SKILL_RU.md               # Русская спецификация
│   └── references/               # Authoring guidelines & templates
│       ├── skill-authoring.md
│       └── skill-authoring_RU.md
└── rca/                          # Behavioral Root Cause Analysis skill
    ├── SKILL.md                  # English specification
    └── SKILL_RU.md               # Русская спецификация
```

---

## 🤝 Contributing

Contributions are welcome! If you have refined an escalation tier, created a specialized diagnostic layer, or want to submit another foundational skill, please see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 👤 Author & Community

- **Author:** Ivan Moiseev ([@SpIvanM](https://github.com/SpIvanM)) — Senior Product Manager & AI Agent Architect
- **Telegram Channel:** [t.me/prompts4llm](https://t.me/prompts4llm) — Prompt engineering, agent architectures, and LLM practices.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
