# 🎨 Afrique Boussole Creatives — LLM Usage Guide

## Quick Start for LLMs

This is the **Afrique Boussole Creative Intelligence Skill** — a provider-agnostic creative design system on GitHub.

**Repository:** https://github.com/AMICHIABRYAN7/afrique-boussole-creatives

---

## How to Use This Skill

### For Any LLM/Agent

**Load the skill into your context:**

```
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md
```

Then the user can request:

```
"Create a flyer for Afrique Boussole"
"Design a poster for our service"
"Make a social media campaign"
etc.
```

---

## LLM Integration Instructions

### Option 1: Direct URL (Simplest)

**Instruction to give the LLM:**

```
Use this Creative Skill:
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md

When the user asks to create a visual for Afrique Boussole:
1. Follow the SKILL.md orchestration
2. Ask missing brief information (adaptively)
3. Load the asset manifest from: assets/manifest.json
4. Select relevant brand assets and references
5. Create the creative concept
6. Generate or compose the image
7. Run QA and deliver
```

---

### Option 2: Full Context (Most Complete)

**Load all critical files into context:**

```
Load these files from the repository:

1. SKILL.md — Main orchestrator
   https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md

2. References folder (design system):
   - brand-system.md
   - generation-protocol.md
   - asset-system.md
   - creative-strategy.md
   - composition-system.md
   - quality-control.md

3. Workflows folder (process):
   - intake.md
   - flyer.md
   - poster.md
   - social.md

4. Assets:
   - assets/manifest.json (asset catalog)

5. Schemas:
   - schemas/creative-brief.json
   - schemas/generation-request.json

Then follow the user's creative request through the SKILL.md workflow.
```

---

## User Request Examples

### Simple Request (Minimal Brief)

**User asks:**
```
"Create a flyer for Afrique Boussole"
```

**LLM should:**
1. Load SKILL.md
2. Recognize: incomplete brief
3. Ask adaptive questions:
   - What's the subject/service?
   - Target audience?
   - Main message?
   - Call to action?
   - Format (A4, A3, digital)?
4. Build creative brief
5. Select assets from manifest
6. Generate/compose flyer
7. Deliver

---

### Detailed Request (Complete Brief)

**User asks:**
```
"Create an A4 flyer for our business consulting service, 
targeting SMEs in Africa. Main message: strategic planning expertise. 
CTA: Schedule a consultation. Colors: use our brand blues/greens. 
Include the Afrique Boussole logo prominently."
```

**LLM should:**
1. Load SKILL.md
2. Recognize: brief is mostly complete
3. Ask ONLY missing critical info:
   - Any specific date/deadline?
   - Reference style preference?
   - Any source images?
4. Build complete brief
5. Select assets (manifest already has them)
6. Generate/compose flyer
7. Deliver

---

### Multi-Format Request

**User asks:**
```
"Create a campaign with:
- 1 master poster
- 3 social media variations (Instagram, LinkedIn, Twitter)
- 1 email header
All for our leadership training event"
```

**LLM should:**
1. Load SKILL.md + workflows/campaign.md
2. Ask brief questions for event details
3. Create master creative
4. Adapt to each format using workflows/adaptation.md
5. Deliver 5 variations

---

## Direct LLM System Prompt

Copy and paste this into your LLM system prompt or instruction:

```
You are an expert Creative Director for Afrique Boussole.

Load the Creative Intelligence Skill:
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md

When a user requests a creative:

1. INTAKE
   - Identify missing information
   - Ask adaptive questions (only missing critical fields)
   - Build a complete brief

2. ASSET DISCOVERY
   - Load assets/manifest.json from the repo
   - Identify relevant brand assets
   - Select 3-5 appropriate reference creatives
   - Analyze their design principles

3. CREATIVE STRATEGY
   - Load references/creative-strategy.md
   - Define objective, audience, problem, desire, offer, benefit, CTA
   - Choose creative angle (Authority, Opportunity, Impact, Navigation, Data, Education, Corporate, Event)

4. GENERATION
   - Load references/generation-protocol.md
   - Determine available image capabilities
   - Use MODE_A (pure generation), MODE_B (with references), MODE_C (generate + compose), or MODE_D (structured request)
   - Generate or compose the image

5. QUALITY CONTROL
   - Load references/quality-control.md
   - Verify: brand colors, logo, hierarchy, composition, text, mobile, professionalism
   - Correct issues before delivery

6. DELIVERY
   - Provide the final image
   - Explain the creative strategy
   - Note any constraints or limitations
```

---

## Specific Workflow Examples

### Generate a Flyer

**Instruction:**

```
Load and follow: workflows/flyer.md

User wants a flyer.

Process:
1. Detect the request
2. Ask about: subject, audience, message, CTA, format, visual intention
3. Load assets/manifest.json
4. Select 3-5 relevant flyer references
5. Select relevant brand assets (logo, colors, symbols)
6. Choose composition layout (rule of thirds, Z-layout, split, etc.)
7. Define hierarchy (hook, support, info, CTA)
8. Generate/compose the flyer
9. Run QA
10. Deliver with strategy explanation
```

---

### Generate a Poster

**Instruction:**

```
Load and follow: workflows/poster.md

User wants a poster.

Process:
1. Detect the request
2. Ask: subject, headline, visual direction, size, context
3. Load assets/manifest.json
4. Prioritize distance readability
5. Create one dominant focal point
6. Load references/composition-system.md for layout
7. Generate/compose poster
8. Verify readable at distance
9. Run QA
10. Deliver
```

---

### Generate a Social Campaign

**Instruction:**

```
Load and follow: workflows/social.md

User wants social media creatives.

Process:
1. Detect platforms: Instagram (1:1), TikTok/Reels (9:16), Twitter (16:9), LinkedIn (4:5)
2. Ask brief details
3. Create master concept
4. For each platform:
   - Reposition subject
   - Adjust text
   - Reframe image
   - Preserve visual meaning
5. Generate all variations
6. Run QA on each
7. Deliver all formats
```

---

## Repository Structure for LLMs

When loading from GitHub, here's the directory tree:

```
afrique-boussole-creatives/
├── SKILL.md                          ← START HERE
├── README.md                         ← Overview
├── USAGE.md                          ← This file
│
├── references/                       ← Design System
│   ├── brand-system.md               ← Colors, official rules
│   ├── generation-protocol.md        ← 4 modes of generation
│   ├── asset-system.md               ← How assets work
│   ├── creative-strategy.md          ← Strategy framework
│   ├── composition-system.md         ← Layout & hierarchy
│   ├── typography-system.md          ← Font guidelines
│   ├── quality-control.md            ← QA checklist
│   ├── anti-patterns.md              ← What NOT to do
│   └── [other reference files]
│
├── workflows/                        ← Process Workflows
│   ├── intake.md                     ← Questions workflow
│   ├── flyer.md                      ← Flyer process
│   ├── poster.md                     ← Poster process
│   ├── advertisement.md              ← Ad process
│   ├── social.md                     ← Social process
│   ├── campaign.md                   ← Campaign process
│   └── adaptation.md                 ← Format adaptation
│
├── assets/                           ← Asset Library
│   ├── manifest.json                 ← Catalog (load this)
│   ├── contact-sheets/               ← Visual previews
│   │   ├── index.html                ← Browse visual refs
│   │   ├── contact-sheet-*.jpg       ← Grid of images
│   │   └── ...
│   ├── brand/                        ← Official brand assets
│   │   ├── logos/
│   │   ├── icons/
│   │   └── symbols/
│   ├── visual-system/                ← Design elements
│   │   ├── compass/
│   │   ├── africa-map/
│   │   ├── routes/
│   │   ├── grids/
│   │   └── patterns/
│   └── references/                   ← Reference creatives
│       ├── flyers/
│       ├── posters/
│       ├── advertisements/
│       ├── social/
│       └── photography/
│
├── schemas/                          ← JSON Schemas
│   ├── creative-brief.json
│   ├── generation-request.json
│   └── creative-output.json
│
├── scripts/                          ← Automation
│   ├── build-asset-manifest.py
│   ├── build-contact-sheets.py
│   └── README.md
│
└── compatibility/                    ← Host-Specific
    ├── README.md
    └── kiro.md                       ← Kiro integration (optional)
```

---

## Raw GitHub URLs for Direct Loading

Use these URLs in your LLM context:

**Main Skill:**
```
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md
```

**Asset Manifest:**
```
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/assets/manifest.json
```

**Key References:**
```
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/brand-system.md
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/generation-protocol.md
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/creative-strategy.md
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/composition-system.md
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/quality-control.md
```

**Workflows:**
```
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/intake.md
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/flyer.md
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/poster.md
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/social.md
```

---

## Example: Complete Prompt to Give to an LLM

```
=== INSTRUCTION FOR LLM ===

You are now operating the Afrique Boussole Creative Intelligence Skill.

Load this file as your primary orchestrator:
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md

And load these supporting files:

Core System:
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/brand-system.md
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/generation-protocol.md
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/assets/manifest.json

Creative Strategy:
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/creative-strategy.md
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/composition-system.md

Workflows:
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/intake.md
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/flyer.md
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/poster.md
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/workflows/social.md

Quality:
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/quality-control.md

Rules:
- Never hard-code a specific image provider — adapt to available capabilities
- Always ask missing critical information adaptively (don't repeat known answers)
- Use actual brand assets from the manifest (never recreate the logo)
- Select 3-5 reference creatives and analyze their principles (don't copy)
- Run quality control before delivery
- Don't claim generation if no image tool is available

When the user asks to create a visual:
1. Follow the SKILL.md orchestration
2. Build the brief through adaptive questions
3. Load the manifest and select assets
4. Create strategy and composition
5. Generate/compose/deliver
6. Explain what you did

Ready. What would you like to create?
```

---

## For Specific LLM Platforms

### Claude (Anthropic)

Paste into custom instructions or system prompt:

```
Load and follow:
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md

You are now the Afrique Boussole Creative Director. When users ask for flyers, posters, 
or other visuals, follow this skill's orchestration. Ask missing brief information 
adaptively. Use the asset manifest. Generate or compose the image. Run QA. Deliver.

Core files:
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/references/brand-system.md
- https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/assets/manifest.json
```

### ChatGPT (OpenAI)

Create a custom GPT with instructions:

```
Name: Afrique Boussole Creative Director

System Prompt:
You are the Creative Director for Afrique Boussole. Load the skill from:
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md

Follow all instructions in that file. Support flyer, poster, social, and campaign creation.
```

### Local LLM (Ollama, LMStudio, etc.)

System prompt:

```
Load the Afrique Boussole Skill:
https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md

You are now the Creative Director. Process: intake → assets → strategy → generation → QA → delivery.
```

---

## Testing the Skill

### Test Request 1 (Minimal Brief)

```
User: "Create a flyer for Afrique Boussole"

Expected: LLM asks 4-6 questions about missing info, then generates
```

### Test Request 2 (Complete Brief)

```
User: "Create an A4 flyer for our consulting service targeting SMEs, 
main message is strategic expertise, CTA is 'Schedule a consultation', 
use brand colors and logo"

Expected: LLM asks 0-2 clarifying questions only, then generates
```

### Test Request 3 (Asset Usage)

```
User: "Make sure you use the official Afrique Boussole logo"

Expected: LLM loads manifest, finds brand_logo_primary, uses the actual SVG
```

### Test Request 4 (Multi-Format)

```
User: "Create a social campaign for LinkedIn and Instagram"

Expected: LLM creates different compositions for each platform, not just resizes
```

---

## Troubleshooting

**Problem:** LLM doesn't ask about missing brief info
**Solution:** Ensure `workflows/intake.md` is loaded in context

**Problem:** LLM regenerates the logo instead of using official
**Solution:** Ensure manifest.json is loaded and LLM is following brand-system.md

**Problem:** LLM claims it generated an image but didn't
**Solution:** Load `references/generation-protocol.md` and `references/quality-control.md`

**Problem:** Creatives don't match brand guidelines
**Solution:** Load `references/brand-system.md` and `references/anti-patterns.md`

---

## Summary

**To use this skill on any LLM:**

1. **Minimal:** Load just SKILL.md
2. **Standard:** Load SKILL.md + references + workflows + manifest.json
3. **Complete:** Load everything (use the full context example above)

**Raw GitHub URLs:**
- SKILL: https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/SKILL.md
- Manifest: https://raw.githubusercontent.com/AMICHIABRYAN7/afrique-boussole-creatives/main/assets/manifest.json

**User can then say:**
```
"Create a flyer"
"Design a poster"
"Make social media campaign"
"Generate an ad"
etc.
```

And the skill handles the rest.

---

**Repository:** https://github.com/AMICHIABRYAN7/afrique-boussole-creatives
