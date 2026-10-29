---
name: rca
description: "Use when you need to find defect root cause via 5 why, rca, or /rca"
origin: IAM
version: 1.0.0
---

# /rca — Targeted Behavioral Root Cause Analysis

Goal: identify fundamental causes of agent misbehavior via targeted 5 Whys and synthesize actionable rule fixes for /rc.

## Activation & Scope
- Trigger: activate on agent behavioral defects, user critiques, rule breaches, or unintended execution paths.
- Goal: collaborate with user to isolate why failure occurred and determine optimal structural correction.
- Anti-reassurance: verbal soothing or promises to improve are strictly prohibited; isolate structural defect on disk.

## Diagnostic Layers
- Layer 1 (Prompt): examine user prompt ambiguity, missing boundary constraints, or implicit assumptions.
- Layer 2 (Rules): inspect AGENTS.md for rule gaps, contradictory directives, or perverse incentives.
- Layer 3 (Skills): inspect SKILL.md for missing workflows, ambiguous steps, or weak validation gates.
- Layer 4 (Harness): evaluate developer system prompts and harness constraints conflicting with requested goals.
- Layer 5 (Context): check context saturation (>100k tokens), attention dispersion, and instruction drift.

## Model Priors & Direct Instruction
- Direct instruction check: first verify whether an explicit directive existed commanding the correct action.
- Model prior assessment: account for intrinsic LLM habits like sycophancy, eager agreement, and premature execution.
- Counter-bias calibration: start new rules at Level 0; escalate to Level 2-5 only upon verified repeated violations.
- Perverse incentives: detect rules that inadvertently encourage unwanted behavior while pursuing valid sub-goals.

## Principle Over Instance
- Abstraction requirement: extract core behavioral pattern; task specifics in rules are strictly prohibited.
- Universal framing: generalize domain episodes into operational archetypes without narrow specifics.
- Anti-clutter mandate: adding temporary topic names or episodic filenames to rules is strictly prohibited.

## Targeted 5 Whys Execution
- Targeted convergence: focus each Why query toward identifying the responsible layer and missing systemic constraint.
- Branching cycles: execute parallel 5 Whys branches when multiple layers interact (e.g. model bias plus rule ambiguity).
- Conflict resolution: detect direct contradictions where Rule A mandates action X but Rule B penalizes outcome X.
- Actionable exit: terminate analysis immediately upon isolating target rule file, anchor, and escalation level.

## Output Report & /rc Handoff
- 1. Symptom: factual description of what occurred and trigger.
- 2. Fundamental Cause: isolated layer and core mechanism discovered via 5 Whys.
- 3. Proposed Fix: generalized principle without narrow episodic specifics.
- 4. Task for /rc: explicit directive specifying target rule file, escalation level, and wording.
- !!!! ✅ Launch Rule-Crafter with: update <file> at Level 0 enforcing <X> (escalate to Level 2 upon repeated violations).
