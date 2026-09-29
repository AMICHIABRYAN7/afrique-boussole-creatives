# Generation Protocol — Provider-Agnostic Image Generation

**Version** : 1.0  
**Date** : Septembre 2026  
**Objectif** : Gérer la génération d'images de manière agnostique — adapter à toute capacité hôte

---

## PRINCIPES FONDAMENTAUX

### 1. Zero Hard-Coding

Ne **JAMAIS** supposer une capacité spécifique :
- ❌ "Je vais générer avec Midjourney"
- ❌ "Je vais utiliser DALL-E"
- ❌ Appels directs à une API

### 2. Capability Detection

Avant de générer, déterminer quelles capacités le host expose :
- ❌ Ne pas inventer une capacité
- ✅ Utiliser **exactement** ce qui est disponible

### 3. Four Generation Modes

Le système doit supporter 4 modes différents, adaptés au contexte.

### 4. Real or Nothing

Si une image est générée → elle est **réelle**  
Si aucune capacité → retourner un **structured request**, pas prétendre

---

## DETECTION DES CAPACITÉS

### Capabilities à détecter

```text
CAP_TEXT_TO_IMAGE         → "Je peux générer depuis un texte"
CAP_IMAGE_TO_IMAGE        → "Je peux modifier une image existante"
CAP_REFERENCE_IMAGES      → "Je peux utiliser plusieurs images de référence"
CAP_BRAND_ASSET_INPUT     → "Je peux intégrer les assets brand dans la génération"
CAP_CUSTOM_DIMENSIONS     → "Je peux générer à dimensions personnalisées"
CAP_TRANSPARENT_BGND      → "Je peux générer avec fond transparent"
CAP_DETERMINISTIC_LAYOUT  → "Je peux placer exactement du texte/logo/CTA"
CAP_VECTOR_OUTPUT         → "Je peux générer en format vectoriel"
CAP_MULTIPLE_VARIANTS     → "Je peux générer plusieurs variantes à la fois"
CAP_IMAGE_INPUT           → "Je peux recevoir des images utilisateur"
```

### Detection Logic

```
IF host exposes image generation
  → Query capabilities
  → Store: [CAP_TEXT_TO_IMAGE, CAP_REFERENCE_IMAGES, ...]
  ELSE
  → Generation mode = MODE_D (structured request only)
```

---

## FOUR GENERATION MODES

### MODE A — Native Image Generation

**Quand** : Host a `CAP_TEXT_TO_IMAGE`  
**Comment** : Brief complet → Prompt → Image générée

**Flux:**
```
Brief complet
  ↓
Sélection assets pertinents
  ↓
Création prompt optimisé (voir ai-prompt-engineering.md)
  ↓
Appel à la capacité image generation du host
  ↓
Image reçue
  ↓
QA + corrections si nécessaire
  ↓
Livraison
```

**Exemple:**
```
User: "Flyer A4 cybersécurité premium"
Host capability: TEXT_TO_IMAGE ✓
→ Generate hero image from text prompt
→ Deliver final flyer with generated image
```

---

### MODE B — Image Generation + Reference Images

**Quand** : Host a `CAP_TEXT_TO_IMAGE` + `CAP_REFERENCE_IMAGES`  
**Comment** : Passer références sélectionnées + prompt au générateur

**Flux:**
```
Brief complet
  ↓
Sélection 3-5 références pertinentes
  ↓
Sélection assets brand pertinents
  ↓
Création prompt + liens références
  ↓
Appel avec références intégrées
  ↓
Image générée (inspirée par les références)
  ↓
QA + corrections
  ↓
Livraison
```

**Exemple:**
```
User: "Flyer style comme ces 3 exemples"
Host capability: TEXT_TO_IMAGE + REFERENCE_IMAGES ✓
→ Pass 3 reference images + prompt
→ Generator produces image inspired by references
→ Deliver final creative
```

---

### MODE C — Generate Then Compose Deterministically

**Quand** : Générateur d'images bon pour scènes, **mauvais pour texte exact/logo/CTA**  
**Comment** : Générer juste l'image héro, puis composer exactement le reste

**Flux:**
```
Brief complet
  ↓
Création prompt SANS texte/logo/CTA
  ↓
Appel générateur (juste l'image de fond)
  ↓
Image reçue (héro visual pur)
  ↓
Composition déterministe:
  - Ajouter texte exact (position, couleur, font)
  - Ajouter logo exact (officiel, pas redessiner)
  - Ajouter CTA exact
  - Ajouter couleurs brand exactes
  ↓
QA complet
  ↓
Livraison
```

**Exemple:**
```
User: "Flyer avec logo ABC, prix exact €99, numéro de tél"
Host: TEXT_TO_IMAGE ✓  +  DETERMINISTIC_LAYOUT ✗
→ Generate just the hero image
→ Compose text/logo/price deterministically on top
→ Deliver final (image + text perfectly placed)
```

---

### MODE D — No Image Engine = Structured Request

**Quand** : Host n'expose **AUCUNE** capacité image  
**Comment** : Retourner structured JSON, ne pas prétendre

**Flux:**
```
Brief complet
  ↓
Pas de capacité image détectée
  ↓
Créer structured generation-request.json avec:
  - prompt complet
  - dimensions
  - références sélectionnées
  - assets brand à utiliser
  - contraintes
  ↓
Retourner le JSON
  + Instructions pour l'utilisateur: "Soumettre à [outil X]"
  + Exemple de ce qu'on s'attend à recevoir
  ↓
Attendre l'image utilisateur OU FIN
```

**Exemple:**
```
User: "Crée un flyer"
Host: Aucune image capability détectée
→ Retourner:
{
  "generation_mode": "MODE_D",
  "status": "request_structured",
  "prompt": "Hero image for cybersecurity flyer...",
  "dimensions": "2480x3508px (A4 300dpi)",
  "instructions": "Soumettre ce prompt à Midjourney /imagine"
}

Do NOT pretend an image was generated.
```

---

## PROMPT STRUCTURE (All Modes)

Reference : `references/ai-prompt-engineering.md`

Prompts must include:

```
[SUBJECT] + [ENVIRONMENT] + [COMPOSITION] 
+ [LIGHTING] + [COLOR] + [MOOD] + [TECHNICAL]
```

Plus:

```
NEGATIVE_PROMPT (ce qu'on NE veut PAS)
DIMENSIONS (résolution exacte)
STYLE (si applicable)
CONSTRAINTS (ex: space for text in upper third)
```

---

## BRAND ASSET INTEGRATION

### Rule 1: Real Assets or Nothing

If a brand asset exists (logo, compass, map):
- Use the **real file** when possible
- Do NOT ask image model to redraw it
- Integrate deterministically after generation

### Rule 2: Pass Assets When Supported

If host supports `CAP_BRAND_ASSET_INPUT`:
- Pass official assets with the prompt
- Generator may integrate them contextually

If host does NOT support:
- Reference them in prompt verbally ("include ABC logo")
- Compose them deterministically afterward

### Rule 3: Exact Colors

Use official Afrique Boussole colors:
- Primary Blue: `#013C87` → In prompt AND in composed elements
- Primary Green: `#1D7742` → In prompt AND in composed elements

Never substitute arbitrary near-colors.

---

## REFERENCE IMAGE SELECTION

### Selection Criteria

When choosing 3-5 references:

1. **Relevance** : Same category (flyer vs poster, corporate vs social)
2. **Quality** : Professional production standard
3. **Diversity** : Don't repeat the same composition 3× 
4. **Inspirational** : What design principles do we extract?

### Never Copy Directly

Extract principles:
- ✅ "This flyer has strong left-right balance"
- ✅ "This reference shows 60% image, 40% text"
- ✅ "CTA positioned bottom-right, high contrast"

- ❌ Copy exact layout
- ❌ Copy text or brand from reference
- ❌ Recreate reference composition identically

---

## FALLBACK BEHAVIOR

### If Prompt Fails

If image generation fails (error, timeout, invalid):

1. **Retry once** with simplified prompt
2. **If still fails** → Fallback to MODE_D (structured request)
3. **Never pretend** the image was generated

### If Reference Images Unavailable

If host doesn't support reference images but we want to use them:

1. Analyze references manually
2. Extract principles in text prompt
3. Proceed with MODE A or MODE C

### If Brand Assets Unavailable

If we can't pass official assets to generator:

1. Describe them in prompt ("official ABC logo in corner")
2. Compose them deterministically afterward

---

## QA AFTER GENERATION

Every generated image must pass:

```
[ ] Brand colors correct (#013C87, #1D7742)
[ ] Logo present and correctly placed
[ ] Hierarchy is clear
[ ] Message readable in 2 seconds
[ ] CTA visible
[ ] No unrelated branding
[ ] Professional production quality
[ ] Contrast meets WCAG AA minimum
```

If critical fail → Regenerate or switch modes.

---

## NO FAKE EXECUTION

### NEVER Say:

❌ "Image generated" if it wasn't  
❌ "Used Midjourney" if you didn't call it  
❌ "Reference analyzed" if you didn't access it  
❌ "Asset integrated" if you didn't actually do it  

### ALWAYS Say:

✅ "No image generation capability detected → Returning structured request"  
✅ "Reference image not accessible in this environment → Proceeding with text-based analysis"  
✅ "Host doesn't support deterministic layout → Generating full image with text included"  

---

## EXAMPLE DECISION TREE

```
REQUEST RECEIVED
  ↓
BRIEF COMPLETE?
  NO → Collect more info (intake.md)
  YES → Continue
  ↓
DETECT HOST CAPABILITIES
  ↓
  HAS TEXT_TO_IMAGE?
    NO → Go to MODE_D
    YES → Continue
  ↓
  HAS REFERENCE_IMAGES?
    YES → MODE B (generate with references)
    NO → Continue
  ↓
  HAS DETERMINISTIC_LAYOUT?
    YES → MODE C (generate image only, compose text after)
    NO → MODE A (generate complete with text)
  ↓
SELECT MODE → EXECUTE → QA → DELIVER
```

---

End of Generation Protocol
