# Contributing to golden-skills

Thank you for your interest in improving `golden-skills`!

This project is built around the **Agent-First** paradigm: instructions for autonomous AI agents must be minimal, deterministic, and maximally dense in signal.

---

## 🎯 Contribution Principles

When proposing changes to existing skills or submitting new ones:

1. **High Signal-to-Noise Ratio (SNR):** Every word must carry operational weight. Remove conversational fluff, politeness tokens, and repetitive directives.
2. **Strict Sentence Constraints:**
   - One line = one atomic directive or one example.
   - Start with an imperative verb (e.g. `Write`, `Check`) or a condition (`If ...`).
   - Line length targets: `<10 words` and `<100 characters` ideal; `>=20 words` strictly prohibited.
3. **Escalation Calibration:**
   - Default new directives to **Level 0**.
   - Escalate to Level 1–2 only when models consistently breach base directives.
4. **Bilingual Parity:**
   - All skills must maintain identical English (`SKILL.md`) and Russian (`SKILL_RU.md`) specifications.
5. **No Context Pollution:**
   - Never inject temporary project filenames, ephemeral bug descriptions, or personal preferences into universal skills.

---

## 🛠️ How to Submit Changes

1. Fork the repository.
2. Create your feature branch (`git checkout -b feat/new-skill-or-fix`).
3. Verify that YAML frontmatter in all modified `SKILL.md` / `SKILL_RU.md` files is valid.
4. Check character and word limits according to the `/rc` guideline.
5. Commit your changes with conventional commit messages (`feat: ...`, `fix: ...`, `docs: ...`).
6. Push to your branch and open a Pull Request.

---

## 💬 Community

Questions or suggestions? Join the discussion in our Telegram community: [@prompts4llm](https://t.me/prompts4llm).
