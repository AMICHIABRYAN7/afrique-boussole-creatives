# Compatibility & Host-Specific Notes

This directory contains guidance for running the Afrique Boussole Creative Skill in different host environments.

## Files

- **kiro.md** — Running in Kiro IDE
- **host-notes.md** — General host compatibility notes

---

## Core Principle

The Skill is **provider-agnostic**. The workflow is the same regardless of host:

1. Collect brief
2. Discover assets
3. Develop strategy
4. Detect capabilities
5. Generate or compose
6. QA and deliver

Only the **capability detection** (step 4) and **generation method** (step 5) change per host.

---

## Minimal Host Requirements

A minimal host needs:
- ✅ LLM (to run the Skill instructions)
- ✅ Ability to read files from `references/`, `workflows/`, `assets/`
- ✅ Ability to discuss and iterate with user

Image generation is **optional**:
- If available → Use it (Modes A, B, C)
- If unavailable → Return structured request (Mode D)

---

End of README
