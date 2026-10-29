# Skill Authoring Protocol

Goal: create an effective skill that improves agent efficacy. Efficacy = (efficacy with skill / efficacy without skill) * (signal / noise). Signal / noise = 1 / skill size in tokens.

## 1. Goal Section (Цель)
- State the goal of the skill: what it aims at and why it exists.

## 2. Role Section (Роль)
- Select the world's best expert in the domain.
- Describe their key experience and depth of practice.
- Describe their brief history and professional track record.
- Add directive: Execute the skill as this expert.

## 3. Thinking Section (Мышление)
- Insert the standard thinking framework:
```text
To maximize value and minimize cost, think through the solution using this template:
- Target Audience: describe who we are creating this for.
- Essence: think through the essence and hidden motives first, what is important and valuable.
- Constraints: formulate self-constraints to avoid wasting effort with zero value.
```
- Adapting this universal thinking block to the specific skill is allowed and recommended.

## 4. Steps Section (Шаги)
- Describe execution steps as a directed acyclic graph (DAG).

## 5. Rules Section (Правила)
- Formulate rules strictly according to the /rc skill standards (1 line = 1 rule).
- Focus on best practices, fastest paths, and effective solutions.
- ‼ Including 100% obvious rules performed by LLMs by default is strictly prohibited.
- Start each rule with an imperative verb or If; frames and conjunctions are prohibited.

## 6. Progressive Disclosure (Frequency)
- Create a section table and estimate usage frequency for each section.
- Keep in root SKILL.md only sections with usage frequency >=65% of cases.
- Extract sections with frequency <65% of cases into separate sub-skills or references/.
- Add an atomic navigating rule in SKILL.md linking to the extracted block.

## 7. Scripts & Automation
- Automate all deterministic mechanical skill operations with scripts.
- Create scripts whenever they save tokens, speed up execution, or boost quality.
- Store scripts in the scripts/ folder and add execution rules into SKILL.md.

## 8. Description Formulation Rules
- Start with Use when you need to... / Применяй когда нужно... (or Use for... / Применяй для...).
- List all triggers in a comma-separated sequence directly after to or for.
- Formulate using infinitive action verbs and singular target objects.
- ‼ Trailing period, repeating skill name, plural duplicates, and Triggers: labels are strictly prohibited.
