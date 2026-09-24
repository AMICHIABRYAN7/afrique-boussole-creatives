# Skill: Afrique Boussole Creative Intelligence

## Metadata

**Skill Name** : `afrique-boussole-creatives`

**Version** : 1.0

**Author** : Afrique Boussole Creative Team

**Last Updated** : September 2024

**Purpose** : Generate professional creative communications (flyers, posters, advertisements, social media, campaigns) for Afrique Boussole brand

**Language** : French, English (extensible)

---

## Skill Description

This Skill provides comprehensive guidance and frameworks for creating authentic, strategic, and on-brand creative communications for Afrique Boussole.

It serves as a **Creative Director AI** that can:

1. Analyze marketing briefs
2. Develop creative strategies
3. Create visual designs
4. Adapt creatives across formats and platforms
5. Perform quality control
6. Generate complete campaigns

---

## Triggering Conditions

Load this Skill when user requests:

### 🎯 **SLASH COMMANDS (Priorité Absolue)**

**QUAND L'UTILISATEUR TAPE UNE DE CES COMMANDES, CHARGE IMMÉDIATEMENT LE QUESTIONNAIRE CORRESPONDANT :**

- `/campagne` → **ÉTAPE 0: CHARGER ASSETS** → Charge `workflows/asset-integration-mandatory.md`
  - Lance le questionnaire complet (8 questions)
  - Charge `workflows/slash-commands.md` section "CAMPAGNE"
  - Créé stratégie + visuels multi-canal
  - Utilise obligatoirement les assets chargés

- `/flyer` → **ÉTAPE 0: CHARGER ASSETS** → Charge `workflows/asset-integration-mandatory.md`
  - Lance le questionnaire (7 questions)
  - Charge `workflows/slash-commands.md` section "FLYER"
  - Créé flyer one-page optimisé
  - Force utilisation des assets (flyers, typography, brand)

- `/affiche` → **ÉTAPE 0: CHARGER ASSETS** → Charge `workflows/asset-integration-mandatory.md`
  - Lance le questionnaire (7 questions)
  - Charge `workflows/slash-commands.md` section "AFFICHE"
  - Créé affiche haute attention
  - Force utilisation des assets (posters, visual-system)

- `/comm` → **ÉTAPE 0: CHARGER ASSETS** → Charge `workflows/asset-integration-mandatory.md`
  - Lance le questionnaire (7 questions)
  - Charge `workflows/slash-commands.md` section "COMM"
  - Créé contenu éducatif/storytelling
  - Force utilisation des assets (social, templates)

- `/prompt` → **ÉTAPE 0: CHARGER PROMPT SYSTEM** → Charge `references/ai-prompt-engineering.md`
  - Lance le questionnaire (6 questions)
  - Charge `workflows/prompt-generation-workflow.md`
  - Génère 3 prompts IA optimisés (conservative, creative, bold)
  - Pour Midjourney, DALL-E, Flux, Stable Diffusion
  - Produit des visuels brand-compliant (#013C87, #1D7742)

**⚠️ RÈGLE CRITIQUE** : 
1. TOUJOURS charger `asset-integration-mandatory.md` EN PREMIER (ÉTAPE 0)
2. PUIS poser les questions dans l'ordre exact défini dans `workflows/slash-commands.md`
3. NE PAS sauter d'étapes
4. OBLIGER l'utilisation des assets avant génération
5. Charger `references/typography-system-pro.md` pour specs typographiques

## 🧠 Architecture du Directeur Créatif IA

Ce skill ne se contente pas de donner des conseils théoriques. Il est architecturé comme un moteur de création complet :

1. **Brand Intelligence** : Chargement strict des couleurs (#013C87, #1D7742), typos (Inter) et ADN de marque GAB SARL.
2. **Asset Intelligence** : Sélection autonome et intelligente d'assets pertinents par rapport au pôle (IT, Sécurité, Academy).
3. **Creative Strategy** : Proposition de 3 concepts graphiques distincts avant production.
4. **Layout Engine** : Moteur de mise en page (composition géométrique, typographique, institutionnelle).
5. **Render Engine** : Production réelle du rendu (génération HTML/Tailwind, SVG, ou prompt scripté) livrant une maquette finie.
6. **Quality Assurance (QA)** : Auto-inspection (bords, contraste WCAG, lisibilité) et correction.

---

## 🛠️ Capacités d'Exécution (Les Moteurs / Slash Commands)

Ce skill remplace les longs questionnaires par de la déduction intelligente. 
Utilisez les Slash Commands suivantes (définies dans `workflows/slash-commands.md`) pour déclencher les moteurs :

- `/crea` : Moteur de création complet (de la stratégie au rendu final).
- `/variations` : Moteur d'exploration (produit 3 concepts visuels).
- `/reference` : Moteur d'analyse (extrait l'ADN d'une image pour l'appliquer à une création).
- `/adapt` : Moteur de déclinaison (adapte un visuel print vers du digital et vice-versa).
- `/campaign` : Orchestrateur (pilote les visuels d'une campagne sur plusieurs formats).
- `/audit` : Moteur QA (analyse un visuel et corrige les failles graphiques).

---

## Core Components

### 1. Profil Entreprise GAB SARL (Priorité Absolue)

**File** : `references/gab-sarl-company-profile.md`

- Coordonnées officielles (Téléphone, email, site web)
- Les 5 pôles d'expertise IT, Sécurité, Management, Marketing, Academy
- Équipe de direction et métriques clés
- Slogans et devises ("Se former pour mieux Servir")
- Règles de footer et contextes visuels autorisés

**Load when** : Au DÉBUT de toute création, pour s'assurer d'avoir les bonnes infos et contacts GAB SARL

---

### 1b. Brand System Reference

**File** : `references/brand-system.md`

- Brand colors (#013C87 Blue, #1D7742 Green)
- Typography system (Inter font)
- Logo usage guidelines
- Accessibility standards
- Design tokens

**Load when** : Any creative production task

---

### 2. Creative Strategy

**File** : `references/creative-strategy.md`

- Strategic brief analysis
- 6 creative angles (AUTHORITY, OPPORTUNITY, HUMAN IMPACT, NAVIGATION, DATA/EXPERTISE, EDUCATION)
- Positioning framework
- Multi-variation strategy

**Load when** : Developing creative concept or analyzing brief

---

### 3. Creative Framework

**File** : `references/creative-framework.md`

- 5-level hierarchy pyramid (HOOK → MESSAGE → VALUE → PROOF → CTA)
- Element mapping
- Functional variations
- Flow and progression

**Load when** : Building visual hierarchy or layout

---

### 4. Composition System

**File** : `references/composition-system.md`

- Fundamental principles (hierarchy, balance, alignment, contrast, repetition, white space)
- 7 composition systems (Rule of Thirds, Center, Split, Asymmetric, Z/F-Layout, Diagonal, Editorial)
- Focal point techniques

**Load when** : Planning layout and composition

---

### 5. Typography System

**File** : `references/typography-system.md`

- Font families and weights
- Sizing hierarchy (72px hero to 10px caption)
- Line heights, letter spacing
- Color system for text
- Platform-specific guidance

**Load when** : Setting up text or refining typography

---

### 6. Photography Direction

**File** : `references/photography-direction.md`

- Subject matter guidelines
- Photography principles (authenticity, quality, purpose, African contemporary)
- Sourcing strategies (stock, commissioned, original)
- Specifications (resolution, color, lighting)
- Direction by creative angle

**Load when** : Selecting or sourcing images

---

### 7. Image Generation

**File** : `references/image-generation.md`

- AI image generation workflows (DALL-E, Midjourney, Stable Diffusion)
- Prompt structure and examples
- Quality standards
- When to use AI vs. stock vs. commissioned

**Load when** : Generating images with AI tools

---

### 7b. AI Prompt Engineering (NEW)

**File** : `references/ai-prompt-engineering.md`

- Professional prompt architecture (8 blocs: SUBJECT, ENVIRONMENT, COMPOSITION, CAMERA, LIGHTING, COLOR, MOOD, TECHNICAL)
- 5 templates by use case (portrait, team, abstract, background, detail)
- 3 variation system (conservative 90% realistic, creative 70/30, bold 40/60)
- Brand-compliant prompting (#013C87, #1D7742, contemporary African aesthetic)
- Platform-specific parameters (Midjourney --ar, --style, DALL-E specs, Flux settings)
- Quality checklist & anti-patterns

**Workflow** : `workflows/prompt-generation-workflow.md` (12-step process)

**Load when** : 
- User types `/prompt` command
- User wants to generate AI images for flyers/posters/campaigns
- Need optimized prompts for Midjourney, DALL-E, Flux, Stable Diffusion

**Triggers** :
- "Generate a prompt for [...]"
- "Create an AI image prompt"
- "I want to use Midjourney/DALL-E for this"
- "Help me generate the visual with AI"

---

### 8. Campaign Formats

**File** : `references/campaign-formats.md`

- Social formats (1:1, 4:5, 9:16, 16:9)
- Print formats (A4, A3, A2)
- Format-specific optimization
- Responsive adaptation principles

**Load when** : Designing for specific format or adapting to new format

---

### 9. Platform Guidelines

**File** : `references/platform-guidelines.md`

- Platform-specific strategies (Instagram, LinkedIn, Facebook, TikTok, YouTube, Email, OOH)
- Content optimization per platform
- Posting strategy
- Audience targeting

**Load when** : Creating for specific social platform or channel

---

### 10. Quality Control Framework

**File** : `references/quality-control.md`

- Brand compliance checklist
- Composition checklist
- Image quality checklist
- Typography detail checklist
- Platform-specific QA
- Critical fail indicators

**Load when** : Reviewing or finalizing creative

---

### 11. Anti-Patterns

**File** : `references/anti-patterns.md`

- 30 explicit patterns to AVOID
- Color mistakes, typography mistakes, composition mistakes
- Image mistakes, message mistakes, technical mistakes
- Critical fail indicators

**Load when** : Reviewing work or avoiding common mistakes

---

### 12. Logo Usage Guidelines

**File** : `references/logo-usage.md`

- Logo versions (full, mark, monochrome)
- Sizing (minimum 40px digital, 15mm print)
- Clear space requirements
- Approved backgrounds
- Positioning rules
- Prohibitions

**Load when** : Placing or sizing logo

---

### 13. Design System

**File** : `references/design-system.md`

- Color tokens (#013C87, #1D7742, etc.)
- Typography tokens (sizes, weights)
- Spacing scale (4px, 8px, 16px, 24px, 32px, etc.)
- Border radius, shadows, opacity
- Component specifications (buttons, cards, tags, etc.)

**Load when** : Building designs or specifying components

---

### 14. Workflows

**Directory** : `workflows/`

Individual workflow files for specific creative types:

- `flyer-workflow.md` — 10-step flyer creation process
- `poster-workflow.md` — 11-step poster creation process
- `ad-workflow.md` — 11-step advertising workflow
- `social-workflow.md` — 12-step social media workflow
- `campaign-workflow.md` — 14-step campaign workflow
- `adaptation-workflow.md` — 12-step format adaptation workflow

**Load when** : Starting production for that specific format

---

### 15. Schemas

**Directory** : `schemas/`

JSON schemas for structured briefs and outputs:

- `creative-brief.schema.json` — Structured brief template
- `campaign.schema.json` — Campaign structure
- `creative-output.schema.json` — Output metadata

**Load when** : Creating or validating briefs

---

### 16. Scripts

**Directory** : `scripts/`

Python validation tools:

- `validate-brand.py` — Verify brand system completeness
- `validate-creative.py` — Quality control checklist
- `generate-brief.py` — Generate creative brief templates

**Load when** : Validating or generating briefs

---

### 17. Examples

**Directory** : `examples/`

Complete, documented examples:

- `flyer-example.md` — Webinar flyer case study
- `poster-example.md` — Tech summit poster case study
- `campaign-example.md` — Q4 growth campaign example

**Load when** : Reference examples or learning

---

## Workflow: Creating a Creative

### When user asks for a creative:

**Step 1: Understand the Brief**

Load → `references/creative-strategy.md` (Strategic Brief Analysis section)

- What's the objective?
- Who's the audience?
- What's the core message?
- What's the CTA?

**Step 2: Choose Creative Direction**

Load → `references/creative-strategy.md` (6 Creative Angles)

- Which angle best serves the objective?
- (AUTHORITY, OPPORTUNITY, HUMAN IMPACT, NAVIGATION, DATA/EXPERTISE, EDUCATION)

**Step 3: Plan Composition**

Load → `references/composition-system.md`

- Which composition system? (Rule of Thirds, Center, Split, etc.)
- Where's the focal point?
- How to achieve hierarchy?

**Step 4: Build Creative Framework**

Load → `references/creative-framework.md`

- LEVEL 1: HOOK (attention-grab)
- LEVEL 2: MESSAGE (primary)
- LEVEL 3: VALUE (why care)
- LEVEL 4: PROOF (credibility)
- LEVEL 5: CTA (action)

**Step 5: Design Typography**

Load → `references/typography-system.md`

- Headline size/weight/color
- Body text specifications
- CTA styling
- Color contrast verification

**Step 6: Plan Imagery**

Load → `references/photography-direction.md` or `references/image-generation.md`

- What image concept?
- Stock, commissioned, or AI-generated?
- Specific direction and requirements

**Step 7: Verify Brand Compliance**

Load → `references/brand-system.md`

- Colors correct?
- Typography on-brand?
- Logo present and positioned?
- Visual identity maintained?

**Step 8: Build the Creative**

Follow relevant workflow:
- Load → `workflows/flyer-workflow.md` (for flyer)
- Load → `workflows/poster-workflow.md` (for poster)
- Load → `workflows/social-workflow.md` (for social)
- etc.

**Step 9: Format Adaptation**

Load → `references/campaign-formats.md`

- Convert to additional formats (social, print, email)
- Recompose, don't shrink
- Load → `workflows/adaptation-workflow.md`

**Step 10: Quality Control**

Load → `references/quality-control.md`

- Brand compliance ✓
- Hierarchy ✓
- Readability ✓
- Professionalism ✓
- Load → `references/anti-patterns.md` (avoid common mistakes)

**Step 11: Final Review**

Load → `references/logo-usage.md`

- Logo correct?
- Clear space maintained?
- Positioned appropriately?

**Step 12: Platform Optimization**

Load → `references/platform-guidelines.md`

- If social: Optimize for specific platform
- If email: Email-specific specifications
- If web: Responsive considerations

**Step 13: Deliver**

- Export at correct resolution and color space
- Provide all required formats
- Include metadata and file specs

---

## Multi-Variation Workflow

For campaigns requiring multiple variations:

**Step 1-4** : Same as above

**Step 5** : Choose 4 creative angles

- Variation A: AUTHORITY
- Variation B: OPPORTUNITY
- Variation C: HUMAN IMPACT
- Variation D: NAVIGATION

**Step 6-13** : Repeat for each variation, maintaining brand consistency

Load → `workflows/campaign-workflow.md` for full campaign guidance

---

## Key Principles (Always Remember)

1. **Brand Integrity First** → Colors, typography, identity non-negotiable
2. **Message Clarity** → Readable in 2 seconds, hierarchy obvious
3. **Authenticity** → No clichés, no stereotypes, genuine representation
4. **Strategic Purpose** → Every element serves the message
5. **Platform Optimization** → Each format adapted intentionally
6. **Quality Obsession** → QA is mandatory, not optional
7. **Creativity with Constraints** → Work within brand system, that's the strength

---

## Common Scenarios

### Scenario 1: "Create a flyer"

1. Load: `creative-strategy.md` (analyze brief)
2. Load: `creative-framework.md` (build hierarchy)
3. Load: `composition-system.md` (plan layout)
4. Load: `typography-system.md` (set type)
5. Load: `flyer-workflow.md` (follow process)
6. Load: `quality-control.md` (verify)
7. Deliver: A4 PDF + PSD files

---

### Scenario 2: "Adapt this to social media"

1. Load: `campaign-formats.md` (understand format specs)
2. Load: `adaptation-workflow.md` (follow adaptation process)
3. Load: `platform-guidelines.md` (optimize for platform)
4. Load: `quality-control.md` (verify mobile readability)
5. Deliver: Social media files (1:1, 4:5, 9:16)

---

### Scenario 3: "Create a campaign"

1. Load: `campaign-workflow.md` (overview)
2. Load: `creative-strategy.md` (choose 4 angles)
3. Load: `creative-framework.md` (build each concept)
4. Load: `campaign-formats.md` (plan all formats)
5. Load: `platform-guidelines.md` (optimize by platform)
6. Load: `examples/campaign-example.md` (reference structure)
7. Deliver: Complete asset library, calendar, brief

---

### Scenario 4: "Generate AI image prompt for flyer" (NEW)

1. User types: `/prompt`
2. Load: `ai-prompt-engineering.md` (8-bloc architecture)
3. Load: `prompt-generation-workflow.md` (12-step process)
4. Ask 6 questions:
   - Use case (portrait/team/concept/background/detail)
   - Objective & message
   - Audience & mood
   - Format & text space
   - Visual style (realistic/creative/bold)
   - AI platform (Midjourney/DALL-E/Flux/SD)
5. Generate 3 prompts (conservative, creative, bold)
6. Deliver: Ready-to-submit prompts with platform instructions
7. User generates image → returns with `/flyer continue` for text composition

---

### Scenario 5: "Create flyer with AI-generated image"

1. User types: `/flyer`
2. ÉTAPE 0: Load assets
3. ÉTAPE 0.5: Propose AI image generation (optional)
4. If yes → mini-prompt (3 questions) → generate prompt
5. User submits to Midjourney/DALL-E → gets image
6. Continue with flyer questionnaire (7 questions)
7. Compose text over AI-generated image
8. Validate with checklist
9. Deliver: A4 PDF + digital formats

---

## Anti-Pattern: What NOT to Do

Load → `references/anti-patterns.md` AT THE START of any project to avoid:

- Brand color substitution
- Typography chaos (too many weights/fonts)
- Cramped composition
- Unreadable text
- Generic stock photos
- Multiple competing CTAs
- False claims or invented stats
- Generic templates

---

## Success Indicator

Your creative is successful if:

✓ Message readable in 2 seconds
✓ Hierarchy is obvious
✓ Colors are brand-correct
✓ Typography follows system
✓ Image is professional and on-brand
✓ CTA is clear and actionable
✓ Feels authentically Afrique Boussole (not generic template)
✓ Passes all QA checks

---

## Assets and Resources

All assets are stored in `assets/` directory and can be added progressively:

- `/assets/brand/logos/` — Official logos (all versions)
- `/assets/brand/icons/` — Icon library
- `/assets/visual-system/compass/` — Compass elements
- `/assets/visual-system/africa-map/` — Map elements
- `/assets/references/` — Example designs

**Note** : Currently placeholder-ready. Actual assets will be added as they're created.

---

## Support and Documentation

- **SKILL.md** ← You are here
- **README.md** ← Project overview and structure
- **references/\*** ← Detailed guidance documents
- **workflows/\*** ← Step-by-step processes
- **schemas/\*** ← Structured templates
- **scripts/\*** ← Validation tools
- **examples/\*** ← Complete case studies

---

## Version History

**v1.0** (September 2024) :
- Initial release
- 13 reference documents
- 6 workflows
- 3 JSON schemas
- 3 validation scripts
- 3 complete examples

---

End of SKILL.md
