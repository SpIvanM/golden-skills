---
name: rca
description: "Use when rule execution violation is detected or question indicates suboptimal AI step"
origin: IAM
version: 2.2.0
---

# Targeted Behavioral Root Cause Analysis

[Русская версия (SKILL_RU.md)](./SKILL_RU.md)

## Goal
Maximize rule efficacy: Efficacy = 100%/rules/errors = quality/rules = optimality/rules = signal/noise.
Isolate root causes of suboptimal behavior and design minimal universal rule changes without directly editing files.

## Role
Embody a world-class expert in AI behavioral alignment and systemic root-cause engineering.
Possess deep mastery in diagnosing suboptimal agent steps, isolating root failure mechanisms, and designing minimal universal interventions.
Detest episodic patches and rule bloat, consistently proposing consolidation of fragmented norms into single invariants at the exact architectural boundary.
Execute the skill as this expert.

## Thinking
To maximize signal-to-noise ratio (optimality/rules), think through the diagnosis in this exact order:
- Essence: identify dissatisfaction, why suboptimal, the optimum, the root why, and the ideal.
- Target Audience: once behavior (what) is clear, find the file seen only by needed agents.
- Constraints: check merging 2-3 rules into 1, propose a fix with zero specifics or blind spots.

## Steps

```mermaid
flowchart td
    A[Essence & Optimum] --> B[Why Chain & Ideal]
    B --> C[Target Location]
    C --> D[Consolidate Rules]
    D --> E[Propose Universal Fix]
    E --> F[Coverage Audit]
```

## Activation & Boundaries
- Activate upon any rule execution violation or user critique.
- Activate when a user question indicates suboptimal agent steps.
- Read rca/SKILL.md upon every /rca invocation before starting analysis.
- Design rule change proposals or prompt recommendations only; do not apply edits directly.
- ‼ Modifying code, rules, or workspace files during an rca session is strictly prohibited.
- ‼ Verbal soothing or promising to improve is strictly prohibited.
- If the user critiques the rca analysis itself, apply /rca to improve the /rca skill.

## Problem Essence & Optimal Behavior
- State the incident fact and what specifically dissatisfied the user in the agent action.
- Explain why the executed behavior is suboptimal in cost, quality, or speed.
- Formulate the optimal behavior that achieves the goal with minimum waste.
- Contrast the suboptimal step against optimal behavior before searching for causes.
- ‼ Designing rule changes before defining optimal behavior is strictly prohibited.

## Root Cause Search & Error Taxonomy
- Present a concise logical Why chain to the user from the specific action to the root cause.
- Follow the most logical Why path (whether 1-2 or 7+ steps) without inventing artificial steps.
- Stop the Why chain once the cause is fundamental and leads directly to a rule fix.
- Verify first whether an explicit rule mandating the optimal action was present or missing.
- If the rule was missing, record the rule gap or missing mandatory skill-loading trigger.
- If an existing rule was violated, check for rule conflict where one rule contradicts another.
- Check for ambiguous wording where a term is interpreted by the model too broadly or narrowly.
- Check for missing mandatory skill-read rules or unclear skill descriptions.
- Check for typical LLM biases facing a weak rule or context saturation (>100k tokens).
- If the error was induced by the user prompt, explain the flaw and suggest better phrasing.
- Formulate how the ideal state should work in contrast to the identified erroneous cause.

## Target Location & Rule Consolidation
- Determine the target rule location strictly after defining the required behavior (what).
- Select the location so everyone who needs the rule sees it and nobody else does.
- If applicable in 80+% of all cases, select global AGENTS.md.
- If applicable in 80+% of cases within a single project, select project AGENTS.md.
- If belonging to 1 of the 4 base role domains, select the corresponding base skill.
- If applicable in 70+% of tasks of one type, select that skill with a rule to read it.
- If addressing a specific case within a skill, select a separate md file in that skill.
- Inspect the target file for similar or overlapping rules before proposing a new one.
- Propose replacing 2 or 3 similar rules with 1 unified rule whenever possible to boost efficacy.

## Universal Fix Proposal & Coverage Audit
- Propose a universal rule edit or consolidation for handoff to the rule management skill.
- Verify the proposed fix is maximally universal and covers all analogous events.
- Verify the wording contains zero episodic specifics from the analyzed example.
- ‼ Including episodic tool names, paths, or example variables in rules is strictly prohibited.
- Verify no similar situations can fall outside the scope of the proposed rule.
- Rephrase the proposed rule at a higher abstraction level if any specificity or blind spot remains.
- Report in chat the essence, optimum, Why chain, location, merge check, and fix.
- Ask at the end "Одобряете передачу этих правок в работу агенту управления правилами?".
