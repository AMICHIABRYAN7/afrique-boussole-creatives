# Kiro Compatibility Notes

This Skill runs perfectly in Kiro but does **NOT require** Kiro-specific features.

---

## Optional Enhancements in Kiro

### Slash Commands (Optional Shortcuts)

In Kiro, users can type slash commands for convenience:

```
/flyer    → Routes to workflows/flyer.md
/poster   → Routes to workflows/poster.md
/campaign → Routes to workflows/campaign.md
/ad       → Routes to workflows/ad-workflow.md
/social   → Routes to workflows/social-workflow.md
```

**Important**: These are **optional shortcuts only**. The Skill works exactly the same with natural language:

```
"Create a flyer for Afrique Boussole"
→ Same result as `/flyer` in Kiro

"Design a poster about our event"
→ Same result as `/poster` in Kiro
```

### File Attachment

In Kiro, users can drag reference images or briefs into chat:

```
#[[file: ~/path/to/image.jpg]]  → Reference image for the creative
#[[file: ~/brief.md]]            → Pre-written brief
```

The Skill can receive and reference these attachments.

### Steering & Context

In Kiro, steering files (`~/.kiro/steering/`) can be used to load Afrique Boussole brand guidelines automatically at session start. This is optional but recommended:

```
# ~/.kiro/steering/afrique-boussole.md
---
inclusion: auto
name: afrique-boussole-brand
---

Load automatically when creating Afrique Boussole visuals.

See: ../afrique-boussole-creatives/references/brand-system.md
```

### Hooks (Optional Automation)

Kiro hooks can automate workflows. Example:

```json
{
  "version": "v1",
  "hooks": [
    {
      "name": "Load ABC Brand on Skill Start",
      "trigger": "SessionStart",
      "action": {
        "type": "agent",
        "prompt": "Load the Afrique Boussole brand system and brief intake workflow"
      }
    }
  ]
}
```

---

## Without Kiro Features (Standard LLM)

If running in Kiro WITHOUT these enhancements, or in a different host:

✅ All core workflows still work  
✅ Natural language requests still trigger the Skill  
✅ File references can be provided textually  
✅ Output is identical  

The Skill adapts to the host's capabilities.

---

## Capability Detection in Kiro

Kiro may expose image generation via MCPs (Model Context Protocol):

- ✅ If Midjourney MCP available → Use it (Mode B likely)
- ✅ If DALL-E MCP available → Use it (Mode A likely)
- ✅ If deterministic layout tool available → Use Mode C
- ⚠️ If no image tool available → Fall back to Mode D

The Skill automatically detects and uses what's available.

---

## Recommended Kiro Setup

For best experience with this Skill in Kiro:

1. **Clone the repository** into your workspace:
   ```
   git clone https://github.com/AMICHIABRYAN7/afrique-boussole-creatives.git
   ```

2. **Add to Kiro context** via steering or manually loading at session start

3. **Set up image generation** if available:
   - Midjourney MCP
   - DALL-E MCP
   - Or other image service MCP

4. **Test the intake workflow**:
   ```
   "Create a flyer for Afrique Boussole"
   ```
   
   You should be asked adaptive questions, not a fixed 7-8 question form.

---

## Troubleshooting in Kiro

### "I'm being asked the same question twice"

This shouldn't happen if intake.md is correctly loaded. The Skill should maintain context between turns.

**Solution**: Ensure `workflows/intake.md` is loaded and the context is retained between responses.

### "The brand colors are wrong"

The Skill uses exact hex codes: `#013C87` (Blue), `#1D7742` (Green).

**Solution**: Verify `references/brand-system.md` is loaded. Check that color substitution didn't occur.

### "No image was generated"

This is expected if:
- Kiro doesn't have image generation capability exposed, OR
- No MCP for image generation is configured

**Solution**: The Skill returns a structured `generation-request.json` instead. This is normal (Mode D).

### "Assets not found"

If the skill can't find `assets/` or reference files:

**Solution**: Ensure the repository is cloned into your workspace and paths are relative to the skill root.

---

## Session Management

For long creative sessions in Kiro:

1. Start fresh session for each major project
2. Use `/context` or steering to reload brand guidelines mid-session if needed
3. Export intermediate work frequently
4. Use Kiro's "Save Session" if available

---

## Kiro-Specific Limitations

None. The Skill is fully provider-agnostic.

The only Kiro-specific features are **enhancements** (slash commands, steering, hooks), not dependencies.

---

End of Kiro Compatibility Notes
