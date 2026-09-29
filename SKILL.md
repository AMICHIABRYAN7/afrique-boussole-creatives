---
name: afrique-boussole-creatives
description: >
  Create premium flyers, posters, advertisements, social media creatives,
  campaign visuals and branded communication assets for Afrique Boussole.
  Use this skill when the user asks to create, generate, design, adapt,
  refine or analyze a visual creative for Afrique Boussole.
tags:
  - creative
  - design
  - brand
  - marketing
  - visual
  - afrique
version: 2.0
---

# Skill: Afrique Boussole Creative Intelligence

**Version** : 2.0 (Provider-Agnostic)  
**Date** : Septembre 2026  
**Purpose** : Generate professional creative communications for Afrique Boussole, adapting to any host environment's capabilities

---

## Quick Reference

**When to use this Skill:**
- User requests a flyer, poster, advertisement, or social creative
- User wants to adapt an existing creative to multiple formats
- User needs creative strategy or art direction for Afrique Boussole
- User requests campaign visual assets

**What this Skill does:**
- Collects incomplete briefs via adaptive questions
- Selects relevant brand assets and creative references
- Develops creative strategy and art direction
- Detects available image-generation capabilities
- Generates or composes final creatives
- Performs quality control

**What this Skill does NOT do:**
- Pretend image generation happened when it didn't
- Hard-code a specific LLM, image service, or API
- Copy reference designs directly
- Redraw official brand assets (use the real files)
- Generate under Kiro-specific constraints only

---

## Skill Activation

This Skill activates when a user requests:

### Direct Requests
- "Create a flyer for Afrique Boussole"
- "Design a poster about [topic]"
- "Make a social media post for our event"
- "Generate an advertisement for our service"
- "Adapt this flyer to Instagram Stories format"
- "Refine this visual against brand guidelines"

### Creative Requests
- "I need visuals for a campaign"
- "Help me communicate [message] visually"
- "What should the design look like for [project]?"
- "Improve this creative to be more on-brand"

### Strategic Requests
- "What creative angle should we use?"
- "Review this against Afrique Boussole brand guidelines"
- "Generate multiple variations of this concept"

---

## Core Workflow

### Step 1: Intake (Adaptive Questions)

→ Load: `workflows/intake.md`

- Detect what information is **missing**
- Ask **only critical** missing questions
- Never re-ask information already provided
- Build a complete brief

### Step 2: Brief Validation

Once brief information is sufficient:
- Summarize the brief
- Confirm understanding with user
- Proceed when confirmed

### Step 3: Asset Discovery

→ Load: `references/brand-system.md`  
→ Load: `assets/manifest.json` (when available)

- Identify relevant brand assets (logo, compass, patterns, etc.)
- Select 3–5 appropriate creative references
- Inspect references for design principles
- Determine how each asset will be used

### Step 4: Creative Strategy

→ Load: `references/creative-strategy.md`

- Define the objective
- Identify the audience
- Select a creative angle (Authority, Opportunity, Human Impact, Navigation, Data/Expertise, Education)
- Define the emotional territory

### Step 5: Art Direction

→ Load: `references/composition-system.md`  
→ Load: `references/typography-system.md`

- Plan composition (rule of thirds, balance, hierarchy)
- Define type hierarchy (sizes, weights, colors)
- Plan visual flow and focal points
- Specify image direction (style, mood, subject)

### Step 6: Capability Detection

→ Load: `references/generation-protocol.md`

Detect what image-generation capabilities the host exposes:
- `CAP_TEXT_TO_IMAGE` — Can generate from text
- `CAP_REFERENCE_IMAGES` — Can use reference images
- `CAP_DETERMINISTIC_LAYOUT` — Can place text/logo exactly
- `CAP_BRAND_ASSET_INPUT` — Can integrate official assets
- (or none of the above)

### Step 7: Generation

Route to appropriate mode based on Step 6:

- **Mode A** : Native image generation (host has text-to-image)
- **Mode B** : Image generation + references (host supports reference images)
- **Mode C** : Generate image, compose text/logo deterministically
- **Mode D** : No image capability → Return structured request

→ Load: `references/generation-protocol.md` for full details

### Step 8: Quality Control

→ Load: `references/quality-control.md`

Every final creative must pass:
- ✅ Brand colors exact (#013C87, #1D7742)
- ✅ Logo correct and well-placed
- ✅ Message readable in 2 seconds
- ✅ Hierarchy clear
- ✅ CTA visible
- ✅ No broken text or overlap
- ✅ Professional production quality

If critical checks fail → Regenerate or refine.

### Step 9: Delivery

- Export to requested format(s)
- Provide all necessary file types
- Include metadata and specifications

---

## Critical Files (Always Load First)

| File | When | Why |
|------|------|-----|
| `references/brand-system.md` | Every project | Official colors, fonts, identity |
| `references/brand-dna.md` | Strategy phase | Who is Afrique Boussole, values, positioning |
| `references/generation-protocol.md` | Before image work | Determine capabilities, choose generation mode |
| `workflows/intake.md` | If brief incomplete | Ask adaptive questions |
| `references/quality-control.md` | Before delivery | Verify all standards met |

---

## Workflow Files

Each creative type has a detailed workflow:

- `workflows/intake.md` — Collect brief information adaptively
- `workflows/flyer.md` — Flyer-specific workflow (10 steps)
- `workflows/poster.md` — Poster-specific workflow (11 steps)
- `workflows/ad-workflow.md` — Advertisement workflow (11 steps)
- `workflows/social-workflow.md` — Social media workflow (12 steps)
- `workflows/campaign-workflow.md` — Campaign workflow (14 steps)
- `workflows/adaptation-workflow.md` — Format adaptation (12 steps)

Follow the appropriate workflow based on output type.

---

## Reference Files (Detailed Guidance)

Load as needed during creative development:

| File | Purpose |
|------|---------|
| `references/brand-system.md` | Colors, fonts, identity rules |
| `references/brand-dna.md` | Company mission, values, personas, ADN |
| `references/creative-strategy.md` | Strategic angles and positioning |
| `references/creative-framework.md` | Hierarchy pyramid, element mapping |
| `references/composition-system.md` | Layout systems and principles |
| `references/typography-system.md` | Font specifications and hierarchy |
| `references/photography-direction.md` | Image sourcing and style |
| `references/image-generation.md` | Prompt structure for image models |
| `references/generation-protocol.md` | Provider-agnostic generation routing |
| `references/campaign-formats.md` | Dimensions, platforms, adaptation |
| `references/platform-guidelines.md` | Social media, email, web specifics |
| `references/quality-control.md` | QA checklists before delivery |
| `references/anti-patterns.md` | 30 patterns to explicitly avoid |

---

## Asset System

### Brand Assets

Official Afrique Boussole assets:
- Logos (full, mark, monochrome)
- Compass symbol
- Africa map
- Icons and symbols
- Official patterns and grids

**Rule**: Use the real asset file. Never ask an image model to redraw the official logo.

### Creative References

Professional examples organized by type:
- `assets/references/flyers/` — Flyer examples
- `assets/references/posters/` — Poster examples
- `assets/references/advertisements/` — Ad examples
- `assets/references/social/` — Social media examples

**Rule**: Extract design principles, never copy directly.

### Visual System

Geometric elements and patterns:
- `assets/visual-system/compass/` — Compass variations
- `assets/visual-system/africa-map/` — Map elements
- `assets/visual-system/routes/` — Route and pathway elements
- `assets/visual-system/grids/` — Grid and structure systems
- `assets/visual-system/coordinates/` — Location markers and coordinates
- `assets/visual-system/patterns/` — Repeating patterns

---

## Generation Modes

### Mode A — Native Image Generation

**When**: Host has text-to-image capability  
**How**: Brief + prompt → Generated image

→ See `references/generation-protocol.md` for full flow

### Mode B — Image Generation + References

**When**: Host has text-to-image + reference image support  
**How**: Brief + references + prompt → Generated image (inspired by references)

### Mode C — Generate Then Compose

**When**: Image generator is good at scenes, poor at exact text/logo  
**How**: Generate hero image → Compose text, logo, CTA deterministically on top

### Mode D — Structured Request

**When**: No image generation capability available  
**How**: Return structured JSON with prompt, dimensions, references, constraints

**Important**: Do NOT pretend an image was generated when it wasn't.

---

## Provider-Agnostic Principles

### 1. No Hard-Coding

❌ Never hard-code ChatGPT, Claude, Gemini, Kiro, DALL-E, Midjourney, Flux, etc.  
✅ Always query host for available capabilities

### 2. Real Capabilities or Nothing

❌ Never pretend a capability exists  
✅ Use exactly what the host exposes, fallback when unavailable

### 3. Real Assets or Descriptions

❌ Never claim an asset was used if it wasn't accessible  
✅ Either actually pass the asset, or describe it in the prompt

### 4. Honest Execution

❌ Never say "generated" if no generation happened  
✅ Say "No image capability → Returning structured request"

---

## Multi-Format Workflow

When creating a campaign across formats:

1. Create master creative (primary format)
2. Adapt to each secondary format
3. Recompose, never just crop
4. Maintain hierarchy and message
5. Optimize for each platform

→ See `workflows/campaign-workflow.md` and `workflows/adaptation-workflow.md`

---

## Quality Standards

Every final creative must:

✅ Use exact brand colors (#013C87 Blue, #1D7742 Green)  
✅ Include logo correctly placed and sized  
✅ Have clear visual hierarchy  
✅ Communicate main message in 2 seconds  
✅ Include clear, actionable CTA  
✅ Meet professional production standards  
✅ Pass WCAG AA contrast requirements (4.5:1 minimum)  
✅ Have no spelling errors or overlapping text  
✅ Feel authentically Afrique Boussole (not generic template)  

If ANY critical standard fails → Regenerate before delivery.

---

## Common Scenarios

### Scenario 1: "Create a flyer"

1. Load `workflows/intake.md` → Ask adaptive questions
2. Build brief
3. Load `assets/manifest.json` → Select brand assets
4. Load `references/creative-strategy.md` → Choose angle
5. Load `references/generation-protocol.md` → Detect capabilities
6. Generate or compose based on available capabilities
7. Load `references/quality-control.md` → QA
8. Deliver final files

---

### Scenario 2: "Adapt this to social media"

1. Load `references/campaign-formats.md` → Understand format specs
2. Load `workflows/adaptation-workflow.md` → Follow adaptation process
3. Recompose for each format (1:1, 4:5, 9:16)
4. Load `references/platform-guidelines.md` → Optimize for platform
5. QA and deliver

---

### Scenario 3: "Create a campaign with 4 angles"

1. Load `workflows/campaign-workflow.md`
2. Load `references/creative-strategy.md` → Choose 4 angles
3. For each angle:
   - Develop concept
   - Plan composition
   - Adapt to all required formats
4. Load `references/quality-control.md` → QA all variants
5. Deliver complete asset library

---

## Avoiding Common Mistakes

→ Load `references/anti-patterns.md` at the start of any project

Explicitly prohibit:
- Clutter and overload
- Brand color substitution
- Too many fonts or colors
- Generic clichés
- Multiple competing CTAs
- Bad contrast
- Unreadable text
- Invented contact details

---

## Limitations & Fallbacks

### If Brief is Incomplete

Ask adaptive questions. Never proceed without critical information.

### If Host Has No Image Capability

Return structured `generation-request.json` with all details for external use.  
Do NOT pretend an image was generated.

### If Image Generation Fails

Retry once with simplified prompt. If still fails → Fallback to MODE_D.

### If References Are Inaccessible

Analyze what information is available. Proceed with text-based principles extraction.

### If Brand Assets Unavailable

Describe in prompt ("official ABC logo in corner").  
Compose deterministically afterward if possible.

---

## Compatibility Notes

This Skill is **host-agnostic** but may run in specific environments:

- **Kiro** : Slash commands like `/flyer` are optional shortcuts, not required
- **Other LLM hosts** : Natural-language requests work the same way
- **CLI/APIs** : Structured input formats supported via schemas

See `compatibility/` directory for host-specific notes.

---

## File Structure

```
afrique-boussole-creatives/
├── SKILL.md (this file)
├── README.md
├── references/ (detailed guidance)
├── workflows/ (step-by-step processes)
├── assets/ (brand and reference assets)
├── schemas/ (structured data templates)
├── scripts/ (validation and utility tools)
├── tests/ (test cases and compatibility)
└── compatibility/ (host-specific notes)
```

---

## Support

For questions about:
- **Brand**: See `references/brand-system.md`
- **Strategy**: See `references/creative-strategy.md`
- **Generation**: See `references/generation-protocol.md`
- **Quality**: See `references/quality-control.md`
- **Specific format**: See appropriate `workflows/` file
- **Images**: See `references/image-generation.md`

---

**Version**: 2.0 (Provider-Agnostic)  
**Last Updated**: Septembre 2026  
**Status**: Production-Ready

---

End of SKILL.md
