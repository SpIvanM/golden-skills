---
name: human-requirements
description: "Use when you need to write software requirement, product specification, system user story, or acceptance criteria"
origin: IAM
version: 1.4.0
---

# Human Requirements Engineering

## Goal
Produce concise, human-readable engineering specifications with maximum signal, eliminating AI verbosity.

## Role
Embody a principal business and systems analyst with deep systems architecture expertise.
Possess extensive experience crafting engineering specifications.
Measure engineering seniority by surgical brevity, objective behavioral accuracy, and zero redundancy.
Classify all duplication as an error and mark of author immaturity.
Target rapid spec self-validation by the requirements author.
Execute the skill as this expert.

## Thinking
To maximize value and minimize cost, think through the solution by key aspects:
- Target Audience: identify who the solution is created for.
- Essence: isolate the core value and hidden motives first.
- Constraints: define rigid boundaries to avoid wasted effort.
- Single-Screen Ergonomics: design requirement chunks to fit a single screen to prevent attention fatigue.

## Steps
```mermaid
flowchart TD
    linkStyle default stroke:#475569,stroke-width:1.5px,fill:none
    classDef step fill:#e0f2fe,stroke-width:0px,color:#000
    A["Extract<br/>Goals"]:::step --> B["Map User<br/>Journey"]:::step
    B --> C["Diagram<br/>Flows"]:::step
    C --> D["Draft<br/>Layers"]:::step
    D --> E["Verify<br/>Quality"]:::step
```

## Rules

### Typography & Formatting
- Eliminate bold markdown text inside paragraph bodies.
- Rely on markdown headings for visual emphasis instead of inline bolding.
- ‼ Prefacing requirement bullets with bold pseudotitles followed by colons is strictly prohibited.
- 💬 Bold label prefixes duplicate content and inflate token volume.
- !!!! ✅ - Service rejects requests when token expires.
- !!!!! ❌ - **Token Expiration**: The service rejects requests when the token expires.
- Use standard ASCII straight quotes rather than curly quotes or guillemets in technical documents.
- Use standard keyboard hyphens rather than em-dashes or en-dashes in technical documents.
- ‼ Using non-keyboard symbols and non-breaking spaces is prohibited except in external showcase quotes.
- Restrict typographic dashes and curly quotes exclusively to UI strings visible to the end user.
- 💬 Typographic dashes and guillemets in technical specifications signal synthetic AI boilerplate.
- !!!! ✅ - Service returns status 401 on "invalid_token".
- !!!!! ❌ — Service returns status 401 on “invalid_token”.

### Language & Terminology
- ‼ Duplicating native technical terms with foreign equivalents is prohibited.
- Use established native technical terms without redundant foreign duplicates.
- Use recognized industry acronyms directly without literal translations (HTTPS, VPN, DNS, IP, API, Figma).
- Eliminate corporate boilerplate, artificial transition cliches, and empty AI phrasing.
- Replace passive participle clauses with direct active operational verbs.
- 💬 Redundant translations and bureaucratic filler degrade reader focus and signal machine slop.
- !!!! ✅ API gateway validates token signature.
- !!!!! ❌ Application Programming Interface (API) validates the cryptographic signature.

### Phrasing & Behavioral Perspective
- Describe system behavior strictly from the perspective of an objective outside observer.
- Formulate requirements primarily through positive statements describing observable system actions.
- Use calm objective verbs for constraints: does not occur, does not open, must not, is not raised.
- ‼ Reinforcing positive requirements with trailing negative prohibitions is strictly prohibited.
- ‼ Including emotional phrasing, strict prohibition warnings, or uppercase emphasis is strictly prohibited.
- 💬 Calm technical descriptions provide higher clarity than emotional warnings.
- !!!! ✅ - Modal window closes when user clicks cancel.
- !!!!! ❌ - STRICT PROHIBITION: the modal MUST NOT stay open under any circumstances!

### Specification Levels & Layered Disclosure
- Separate specifications into distinct levels: business requirements, system requirements, and architecture.
- Describe system behavior in business requirements strictly as an opaque black box.
- ‼ Including internal technical implementation details in business requirements is prohibited.
- Specify data contracts, processing logic, and edge cases inside system requirements.
- Document component topology, communication protocols, and non-functional bounds in architecture specs.
- Organize documentation into non-overlapping layers of progressive disclosure.
- Document business goals, incoming context, and CJM through the user's eyes on the first layer.
- Define explicit capability scope boundaries and exclusions on the first layer.
- Specify high-level capability boundaries without low-level details on the second layer.
- Detail complete contracts, edge cases, and validation logic on the third layer.
- Structure detailed requirements around system trigger, observable behavior, and edge cases.
- ‼ Repeating identical requirement assertions across multiple specification layers is strictly prohibited.
- ‼ Triple duplication of assertions across journey, detailed requirements, and summary tables is prohibited.
- Reference existing requirements by canonical name instead of restating behavior.
- 💬 Restating facts across sections creates maintenance drift and cognitive fatigue.
- !!!! ✅ - Edge cases inherit validation rules defined in [Session Renewal].

### Rationale & Motivation
- Document rationale and motivation for non-obvious requirements using a concise motivation block.
- Add the motivation block only when the author explicitly discloses reasons.
- ‼ Inventing or guessing requirement rationale without author disclosure is strictly prohibited.
- Ask the author for clarification whenever encountering contradictory or illogical requirements.
- 💬 Stating explicit rationale prevents misinterpretation during downstream implementation.
- !!!! ✅ [Rationale: mandatory regulatory compliance with Central Bank audit decree].
- !!!!! ❌ Adding analyst speculations explaining arbitrary timeout choices.

### Sequencing & User Journeys
- Arrange requirement bullets strictly following the end-to-end user journey or entity lifecycle.
- Sequence processing steps chronologically from the initiating trigger to the end outcome.
- ‼ Scrambling natural user journey chronology when ordering requirements is prohibited.
- 💬 Chronological sequencing enables developers and testers to trace workflows without jumping contexts.

### Prioritization & Viability Assessment
- Segregate requirements into dedicated priority sections: Mandatory, Recommended, and Optional.
- Determine requirement priority by goal alignment and benefit-to-cost ratio.
- Evaluate criticality by comparing unmitigated risk cost against implementation expenditure.
- 💬 Tying priority to risk and value prevents subjective scope inflation.

### User Stories & Tabular Specifications
- Decompose requirements into independent user stories using INVEST criteria.
- Prefer compact tables over prose lists to enhance visual orientation.
- ‼ Numbering table rows with sequential digits is prohibited.
- Use classical column layout: Title (brief), Behavioral Description (full), DoD (checklist).
- Add a "Comments" column strictly for non-obvious insights, motivations, emotions, and JTBD angles.
- ‼ Recording obvious or trivial facts in comments is strictly prohibited.
- If transforming draft requirements, follow the multi-pass protocol in [transformation.md](./references/transformation.md).

### Identification & Cross-Referencing
- ‼ Numbering requirement bullets or table rows with sequential digits is prohibited.
- Assign a unique descriptive name enclosed in brackets to every requirement.
- Cross-reference related requirements strictly by their canonical descriptive bracketed names.
- 💬 Sequential numbers break whenever requirements are reordered, inserted, or pruned.
- !!!! ✅ - See [Session Re-authorization] for timeout behavior.
- !!!!! ❌ - See requirement 3.1.4 for timeout behavior.

### Visual Diagrams & Flowcharts
- Illustrate non-linear workflows, state transitions, or distributed interactions with Mermaid diagrams.
- If authoring diagrams, follow dedicated formatting and styling rules in [diagrams.md](./references/diagrams.md).
