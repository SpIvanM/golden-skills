# Subskill Authoring Protocol

[Русская версия (subskill-authoring_RU.md)](./subskill-authoring_RU.md)

## Goal
Standardize modular subskill creation with zero rule duplication and clean inheritance.

## 1. Subskill Structure & Inheritance
- Follow [skill-authoring.md](./skill-authoring.md) applying only deltas below.
- Omit YAML frontmatter from subskills in references/.
- Omit the Goal section when matching base target.
- Omit the Role section when matching base persona.
- Omit Thinking and Steps unless defining procedural workflow.
- ‼ Duplicating base skill rules inside subskills is strictly prohibited.

## 2. Hierarchy, Naming & Navigation
- Name subskill files in kebab-case with paired _RU.md mirrors.
- Place child subskills in nested subfolders of references/.
- Target sibling subskills using relative paths within references/.
- Link hierarchy via "If <case>, read [<subskill>](<path>)".
- ✅ If validating company, read [inn.md](./validation/inn.md).
- 💬 Form development -> validation -> legal entity -> INN.
