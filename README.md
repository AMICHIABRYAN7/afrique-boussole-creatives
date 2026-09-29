# Afrique Boussole Creative Intelligence Skill

**Version** : 2.0 (Provider-Agnostic)  
**Status** : Production-Ready  
**Last Updated** : Septembre 2026

---

## Overview

This Skill provides comprehensive frameworks and workflows for creating professional, strategic, and on-brand creative communications for Afrique Boussole.

**Key Principle**: Provider-agnostic — works with any host environment.

---

## What This Skill Does

✅ **Collects briefs adaptively** — Asks only critical missing questions, never repeats  
✅ **Discovers assets intelligently** — Selects relevant brand assets and references  
✅ **Develops creative strategy** — Defines angles, positioning, messaging  
✅ **Generates visuals** — Uses available image capabilities (or provides structured request)  
✅ **Enforces quality** — Runs mandatory QA before delivery  
✅ **Adapts formats** — Recomposes for multiple platforms/sizes  

---

## Starting a Creative Project

### Method 1: Natural Language (Works Everywhere)

```
"Create a flyer for Afrique Boussole about our 
cybersecurity training for SMEs"
```

→ Skill asks adaptive questions → Creates professional flyer

### Method 2: Slash Commands (Kiro Only — Optional)

```
/flyer
```

→ Routes to flyer workflow → Same result

Both produce identical results. Method 1 works in any environment.

---

## Asset-Driven Design Guarantee

Every creative uses:
- ✅ Official brand assets (logo, compass, patterns)
- ✅ Professional references analyzed for principles
- ✅ Exact brand colors (#013C87 Blue, #1D7742 Green)
- ✅ Mandatory quality control before delivery

**Zero generic templates. 100% authentic Afrique Boussole.**

---

## Quick Start Guide

### Step 1: Request a Creative

```
"I need a social media post for our leadership program"
```

### Step 2: Answer Questions

The Skill asks adaptive questions to complete the brief.

### Step 3: Get Your Creative

The Skill automatically:
- Loads relevant assets
- Develops creative strategy
- Generates or composes the visual
- Runs quality control
- Delivers final files

---

## For Different Users

### Designer/Marketer

1. Read `SKILL.md` (overview)
2. Read appropriate workflow (`workflows/flyer.md`, `workflows/poster.md`, etc.)
3. Request a creative
4. Iterate on feedback
5. Deliver final assets

### Developer/Integrator

1. Read `SKILL.md` (frontmatter and core workflow)
2. Read `references/generation-protocol.md` (capability detection)
3. Integrate generation mode appropriate to your platform
4. Validate briefs against `schemas/creative-brief.json`
5. Test with `tests/README.md`

### Kiro User

1. Optional: Use slash commands (`/flyer`, `/poster`, etc.)
2. Or: Use natural language (same result)
3. Everything else is identical

---

## Directory Structure

```
afrique-boussole-creatives/
│
├── SKILL.md ← START HERE
├── README.md (this file)
│
├── references/
│   ├── brand-system.md (colors, fonts, identity)
│   ├── creative-strategy.md (briefs, angles, positioning)
│   ├── creative-framework.md (hierarchy pyramid, element mapping)
│   ├── composition-system.md (layout principles and systems)
│   ├── typography-system.md (fonts, sizes, hierarchy)
│   ├── photography-direction.md (image guidance)
│   ├── image-generation.md (AI image creation)
│   ├── campaign-formats.md (dimensions, platforms)
│   ├── platform-guidelines.md (Instagram, LinkedIn, TikTok, etc.)
│   ├── quality-control.md (QA checklists)
│   ├── anti-patterns.md (what NOT to do)
│   ├── logo-usage.md (logo specs and rules)
│   └── design-system.md (tokens, components)
│
├── workflows/
│   ├── flyer-workflow.md (10-step flyer process)
│   ├── poster-workflow.md (11-step poster process)
│   ├── ad-workflow.md (11-step advertising process)
│   ├── social-workflow.md (12-step social process)
│   ├── campaign-workflow.md (14-step campaign process)
│   └── adaptation-workflow.md (12-step format adaptation)
│
├── assets/
│   ├── brand/
│   │   ├── logos/
│   │   ├── icons/
│   │   └── symbols/
│   ├── visual-system/
│   │   ├── compass/
│   │   ├── africa-map/
│   │   ├── grids/
│   │   ├── routes/
│   │   ├── coordinates/
│   │   └── patterns/
│   ├── references/
│   │   ├── posters/
│   │   ├── flyers/
│   │   ├── social/
│   │   ├── advertisements/
│   │   └── corporate/
│   └── templates/
│
├── schemas/
│   ├── creative-brief.schema.json (brief template)
│   ├── campaign.schema.json (campaign structure)
│   └── creative-output.schema.json (output metadata)
│
├── scripts/
│   ├── validate-brand.py (verify brand system)
│   ├── validate-creative.py (QA checklist)
│   └── generate-brief.py (generate brief template)
│
└── examples/
    ├── flyer-example.md (webinar flyer case study)
    ├── poster-example.md (tech summit poster case study)
    └── campaign-example.md (Q4 growth campaign case study)
```

---

## Component Guide

### 1. References (Detailed Guidance)

Each document in `references/` provides specific guidance:

| File | Purpose | When to Load |
|------|---------|-------------|
| brand-system.md | Brand colors, fonts, identity | Every project |
| creative-strategy.md | Brief analysis, creative angles | Strategy/concept phase |
| creative-framework.md | Hierarchy pyramid, element structure | Layout phase |
| composition-system.md | Layout principles and systems | Composition planning |
| typography-system.md | Font specifications, sizing | Typography phase |
| photography-direction.md | Image sourcing and direction | Image selection |
| image-generation.md | AI image prompts and workflows | AI image generation |
| campaign-formats.md | Format specifications, adaptation | Format planning |
| platform-guidelines.md | Platform-specific optimization | Platform creation |
| quality-control.md | QA checklists | Verification |
| anti-patterns.md | What NOT to do | Avoidance reference |
| logo-usage.md | Logo specifications | Logo placement |
| design-system.md | Tokens, components, reusables | Component building |

---

### 2. Workflows (Step-by-Step Processes)

Each workflow in `workflows/` provides a structured process:

- **Flyer Workflow** : 10 steps from brief to delivery
- **Poster Workflow** : 11 steps, distance-readable focus
- **Advertising Workflow** : 11 steps, conversion-focused
- **Social Workflow** : 12 steps, platform-optimized
- **Campaign Workflow** : 14 steps, multi-format coordination
- **Adaptation Workflow** : 12 steps, format conversion

Choose the workflow matching your output type. Each guides you through the complete process.

---

### 3. Assets (Brand Resources)

The `assets/` directory is structure-ready for:

- Brand logos, icons, symbols
- Compass, map, and geometric elements
- Pattern and visual system files
- Reference photography and designs
- Design templates

**Current Status** : Placeholder structure. Actual assets will be populated as created.

**Adding Assets** :

1. Create high-resolution files
2. Place in appropriate subdirectory
3. Document in asset library
4. Reference in design guidelines

---

### 4. Schemas (Structured Data)

JSON schemas for structured data:

- **creative-brief.schema.json** : Validate creative briefs
- **campaign.schema.json** : Structure campaign data
- **creative-output.schema.json** : Document deliverables

Use these to:
- Structure briefs in code/data systems
- Validate completeness before production
- Generate reports and metadata

---

### 5. Scripts (Automation Tools)

Python scripts for validation and generation:

- **validate-brand.py** : Check skill completeness, file structure
- **validate-creative.py** : QA checklist and report generation
- **generate-brief.py** : Create brief templates with instructions

Usage:
```bash
python scripts/validate-brand.py          # Validate skill
python scripts/validate-creative.py --checklist  # Show QA checklist
python scripts/generate-brief.py --create brief.json  # Generate template
```

---

### 6. Examples (Complete Case Studies)

Three complete documented examples showing real-world application:

- **flyer-example.md** : Webinar promotion flyer (A4)
  - Shows brief analysis, strategy, layout, typography
  - Format specifications, file delivery
  
- **poster-example.md** : Tech summit announcement (A3)
  - Shows distance-readable design
  - Event-specific requirements, printing specs
  
- **campaign-example.md** : Q4 multi-channel campaign
  - Shows 4 creative variations (different angles)
  - Multi-format adaptation (7 formats)
  - Timeline, budget, metrics, optimization

---

## Key Principles

### 1. Brand Integrity

- Brand Blue (#013C87) and Brand Green (#1D7742) exact, never substituted
- Typography: Inter font family as standard
- Visual identity: Compass, maps, contemporary African aesthetic
- Never compromise brand guidelines for "creative freedom"

### 2. Clarity & Impact

- Primary message readable in 2 seconds
- Clear visual hierarchy (primary, secondary, supporting elements)
- CTA unmistakable and action-specific
- Design serves content, not vice versa

### 3. Authenticity

- Authentic imagery (not clichéd stock photos)
- Authentic representation (diverse, not tokenized)
- Authentic African perspective (contemporary, not stereotypes)
- Honest messaging (never invented stats or false claims)

### 4. Strategic Purpose

- Every element serves the objective
- Visual direction supports the creative angle
- Composition enables the message hierarchy
- Format adaptation maintains integrity

### 5. Platform Excellence

- Each platform receives optimized treatment
- Format-specific requirements respected
- Audience behavior on platform considered
- Distribution strategy integrated

---

## Using This Skill

### Scenario 1: Create a Single Flyer

```
1. Read SKILL.md (overview)
2. Load creative-strategy.md (analyze brief)
3. Load creative-framework.md (build hierarchy)
4. Load composition-system.md (plan layout)
5. Load typography-system.md (design type)
6. Load flyer-workflow.md (follow process)
7. Load quality-control.md (verify)
8. Load brand-system.md (compliance check)
9. Deliver: Print-ready PDF + editable files
```

### Scenario 2: Create a Campaign (4 Variations, 7 Formats)

```
1. Read SKILL.md (overview)
2. Load campaign-workflow.md (plan campaign)
3. Load creative-strategy.md (develop 4 angles)
4. Load campaign-formats.md (plan formats)
5. For each variation & format:
   - Load relevant workflow
   - Load platform-guidelines.md (if social)
6. Load quality-control.md (QA all variants)
7. Deliver: 28+ files organized by variation
```

### Scenario 3: Adapt Existing Flyer to Social Media

```
1. Load campaign-formats.md (understand formats)
2. Load adaptation-workflow.md (follow process)
3. Load platform-guidelines.md (optimize for platform)
4. Load quality-control.md (verify mobile readability)
5. Deliver: Social files (1:1, 4:5, 9:16)
```

---

## Quality Standards

Every creative must meet these standards:

**Brand Compliance**
- [ ] Logo correct, well-placed
- [ ] Colors exact (#013C87, #1D7742)
- [ ] Typography is Inter font family
- [ ] Visual identity consistent

**Message Clarity**
- [ ] Readable in 2 seconds
- [ ] Focal point obvious
- [ ] Hierarchy is clear (primary > secondary > supporting)
- [ ] CTA is action-specific

**Professional Execution**
- [ ] Image high-quality, professional
- [ ] No typos or errors
- [ ] Spacing and alignment precise
- [ ] Contrast meets WCAG AA (4.5:1 minimum)

**Strategic Alignment**
- [ ] Supports stated objective
- [ ] Resonates with audience
- [ ] Uses appropriate creative angle
- [ ] Maintains authentic voice

**→ For complete validation checklist, see [`references/validation-checklist.md`](references/validation-checklist.md)** (10 comprehensive checks before delivery)

---

## Avoiding Common Mistakes

Reference `anti-patterns.md` for 30 explicit patterns to avoid:

**Critical Fails** (reject and revise if present):

1. Brand color substituted with non-brand color
2. Text unreadable at intended viewing size
3. Multiple competing focal points
4. Factually false or invented claims
5. Generic template feel (not authentically Afrique Boussole)

---

## Getting Started

### New to the Skill?

1. **Read** : This README
2. **Read** : `SKILL.md` (the orchestrator)
3. **Browse** : `examples/` to see complete projects
4. **Review** : `references/brand-system.md` (essential foundation)

### Creating Your First Creative?

1. **Prepare** : Your creative brief
2. **Read** : Appropriate workflow (`workflows/flyer-workflow.md` or similar)
3. **Load** : Reference documents as you progress
4. **Verify** : Use `quality-control.md` before final delivery

### Managing a Design Team?

1. **Share** : This entire skill with your team
2. **Ensure** : All understand `brand-system.md`
3. **Use** : Scripts for validation (`validate-creative.py`)
4. **Reference** : Examples for training

---

## File Formats & Deliverables

### Recommended Formats by Purpose

| Purpose | Format | Specs |
|---------|--------|-------|
| Digital/Screen | JPEG | RGB, 96dpi, <2MB |
| Print | PDF | CMYK, 300dpi, fonts embedded |
| Web | PNG | RGB, 96dpi, optimized |
| Editable | PSD/AI | RGB or CMYK, all layers |
| Archive | TIFF | CMYK, 300dpi, lossless |

### File Naming Convention

```
Project-Name_Format_Version_Date.extension

Examples:
Webinar-Campaign_A4-Flyer_v1_2024-09-24.pdf
Webinar-Campaign_Social-1x1_v2_2024-09-24.jpg
Webinar-Campaign_Story-9x16_final_2024-09-24.jpg
```

---

## Support Resources

- **Questions about brand**: See `references/brand-system.md`
- **Questions about composition**: See `references/composition-system.md`
- **Questions about a specific format**: See `references/campaign-formats.md`
- **QA help**: See `references/quality-control.md`
- **What NOT to do**: See `references/anti-patterns.md`
- **Step-by-step help**: See `workflows/`
- **Real examples**: See `examples/`

---

## Contributing & Improvements

This Skill is designed to evolve:

- **Add new workflows** : For new creative types not covered
- **Add new references** : For emerging platforms or techniques
- **Update brand system** : As brand identity evolves
- **Add assets** : As official brand assets are created
- **Expand examples** : Add new case studies as projects complete

---

## Version Information

- **Skill Version** : 1.0 (September 2024)
- **Last Updated** : September 2024
- **Maintenance** : Regular updates as needs evolve
- **Status** : Production-ready

---

## License & Usage

This Skill is proprietary to Afrique Boussole.

**Permitted Uses** :
- Internal creative production
- Team training and reference
- Brand guidance and compliance
- Quality assurance

**Prohibited Uses** :
- External sharing without permission
- Commercial use outside Afrique Boussole
- Modification without approval
- Resale or redistribution

---

## Next Steps

1. **Read** : `SKILL.md` (orchestrator)
2. **Prepare** : Your creative brief
3. **Choose** : Appropriate workflow
4. **Execute** : Follow process, load references as needed
5. **Validate** : Use `quality-control.md`
6. **Deliver** : Professional creative

---

**Questions?** Reference the appropriate document or workflow. This Skill is designed to be self-guided and comprehensive.

---

End of README
