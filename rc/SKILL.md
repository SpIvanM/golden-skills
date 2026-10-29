---
name: rc
description: "Use when you need to change or write a rule, skill"
origin: IAM
version: 1.2.0
---

# /rc — Rule & Skill Crafting

Goal: create minimal, high-leverage rules or skills that effectively improve behavior with maximum signal-to-noise ratio.

## Agent Tasks (Effort Allocation)
1. Compress rules: cut every redundant word, maximize clarity and execution speed (spend 4k+ thinking tokens).
2. Route audience: assign rule strictly to its true owner, eliminate context pollution where unneeded (spend 2k+ thinking tokens).
3. Translate: maintain Russian mirror without extra effort (0k tokens).
4. Report: output exact before/after diff and additions without extra effort (0k tokens).
Principles: YAGNI, KISS.

## Audience Routing (Who Owns the Rule)
- Global (all agents, universal invariants): repo root or global AGENTS.md.
- Project (repo-specific stack and layouts): project AGENTS.md.
- Scoped (specific files or path globs): .agents/rules/*.md.
- Role (specific agent archetypes): governing role skill SKILL.md.
- Hook / Linter (mechanical checks, deterministic formats): git hook or script.
- Discard (ephemeral whims, localized bugs): zero persistent rules.

## Modular Role & Competency Architecture
- Compose each role from exactly two orthogonal competencies: interface and core.
- Build Orchestrator (/s) by pairing user-communication with subagent-orchestration.
- Build Direct Executor (/d) by pairing user-communication with hands-on-execution.
- Build Subagent worker by pairing subagent-protocol with hands-on-execution.
- Write role switchers (/d, /s) as minimal three-line blueprints.
- Limit role switcher lines to loading competencies and stating execution boundary.
- Restrict global AGENTS.md to invariants applying to all roles simultaneously.
- Route roles to their respective switchers from global AGENTS.md.
- Read required competency files in one step via parallel tool calls.
- Extract exactly one competency at a time during rule refactoring.

## Grammar & Sentence Structure
- Start every rule with an imperative verb (e.g. Write...) or conditional If (e.g. If context lacks...).
- ‼ Inline pre-headers, anchors, pseudo-titles, or label prefixes before rules are strictly prohibited.
- Formulate exactly one atomic directive per line; chaining multiple thoughts with conjunctions is prohibited.
- Maximize information payload per token; eliminate redundant tags like Rule:, Mandate:, or Anchor:.
- ‼ Repeating section names or subject roles inside rule lines is strictly prohibited.

## Escalation Levels
- 0: direct positive imperative starting with a verb (e.g. - Write concisely.).
- 1 (!): contrastive imperative or conditional (e.g. - Pass task messages: inclusion is better than omission.).
- 2 (!!): categorical prohibition starting with If or negative verb, containing strictly prohibited.
- 3 (!!!): apply CAPITALIZATION to critical operational verbs upon verified repeated violations.
- 4 (!!!!): add positive example (1 line).
- 5 (!!!!!): add negative example (1 line).
- 6 (💬): add explanation (1 line).

## Format Constraints & Length Limits
- 1 line = 1 rule or 1 example to a rule.
- 3 length tiers: <10 words and <100 chars ideal; 10-19 words warning; >=20 words or >=140 chars strictly prohibited.
- Stop words rule: conjunctions, prepositions, and particles are excluded when counting rule words.
- Description format: start with Use when/for, use action verbs and singular objects.
- ‼ Trailing periods, repeating skill name, or plural duplicates in description are strictly prohibited.
- ‼ Explicit trigger labels like Triggers: are strictly prohibited; embed triggers into prose.
- Skill authoring protocol: read [skill-authoring.md](./references/skill-authoring.md).
- Write authoring guides as step-by-step assembly checklists.
- Insert literal ready templates instead of describing them in prose.
- Split composite rules: chaining two directives with and is forbidden; split into 2 separate lines.
- No markdown bold (**), no decorative frames, no wordiness.
- New rules start at Level 0. Escalate only upon verified repeated violations.
- Edit files strictly in place via replace_file_content. Overwriting files is prohibited.
- Anchor project-level target paths with <project-root>/ prefix.

## Concrete Examples
- Good Level 0: - Write concisely.
- Good Level 1: - Pass all task-relevant messages to the subagent; prefer including more messages over fewer.
- Good Level 2: - ‼ If context lacks message numbers, launching a subagent is strictly prohibited.
- Bad rule (inline pre-header): - Blind launch ban: launching without message numbers is prohibited.
- Bad rule (bold / composite): - **Paths**: Always use relative paths, and also ask confirmation before rm.
- Positive example (Level 4): - !!!! ✅ [readme](../../folder/file.ext)
- Negative example (Level 5): - !!!!! ❌ [readme](file:///path/file.ext)
- Explanation (Level 6): - 💬 Verbal soothing is a lie; active fix requires updating rules.

## Chat Report Format
- Target file path.
- Changed: previous line -> new line.
- Added: new line.
- Level (0 to 6) and audience rationale.

