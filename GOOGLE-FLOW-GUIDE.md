# 🎨 Guide Complet: Google Flow + Afrique Boussole Skill

## C'est quoi Google Flow?

**Google Flow** est le studio créatif IA de Google qui permet de:
- ✅ Générer des images (avec Gemini Image / "Nano Banana")
- ✅ Générer des vidéos (avec Veo models)
- ✅ Éditer des images
- ✅ Utiliser des références visuelles
- ✅ Créer des personnages consistants
- ✅ Travailler avec un Agent conversationnel

**Accès:** https://labs.google/fx/tools/flow

**Modèles d'image disponibles:**
- **Nano Banana Pro** (anciennement Imagen 3) — Le meilleur pour images
- **Gemini Omni Flash** — Pour consistance de personnages et multi-modal

---

## 🎯 Avantages pour Afrique Boussole

### ✅ Ce que Flow PEUT Faire

1. **Générer des images à partir de texte**
   - Prompts détaillés
   - Haute qualité (jusqu'à 1024x1024)
   - Rendu de texte précis

2. **Utiliser des références visuelles ("ingredients")**
   - Upload tes flyers de référence
   - Flow les analyse et applique le style
   - Jusqu'à 14 objets avec consistance

3. **Éditer des images**
   - Modifications conversationnelles
   - Historique des versions
   - Crop, ajustements

4. **Agent conversationnel**
   - Dialogue naturel
   - Itérations rapides
   - Sélection automatique du meilleur modèle

5. **Personnages consistants**
   - Créer des avatars
   - Les réutiliser avec `@nom`
   - Consistance cross-images

---

## 🚀 Comment Utiliser Flow avec le Skill

### Méthode 1 — Agent Conversationnel (Recommandé)

**Étape 1:** Va sur https://labs.google/fx/tools/flow

**Étape 2:** Crée un nouveau projet

**Étape 3:** Active l'Agent (toggle en haut)

**Étape 4:** Copie-colle cette instruction:

```
Tu es le Directeur Créatif d'Afrique Boussole.

RÈGLES DE MARQUE:
- Couleurs principales: #013C87 (bleu) et #1D7742 (vert)
- Logo: Boussole stylisée + texte "AFRIQUE BOUSSOLE"
- Style: Corporate, moderne, premium, africain
- Tagline: "STRATÉGIE • INNOVATION • DATA"

QUAND JE DEMANDE UN VISUEL:
1. Demande les infos manquantes
2. Propose une composition
3. Génère l'image avec les couleurs exactes
4. Inclus le logo Afrique Boussole
5. Assure-toi que le texte est lisible

Prêt?
```

**Étape 5:** Demande ton flyer:

```
Crée un flyer A4 pour notre formation en cybersécurité.
Audience: Jeunes entrepreneurs africains.
Message: Protégez votre business.
CTA: Inscrivez-vous.
Dates: 20 oct - 10 nov.
```

---

### Méthode 2 — Avec Références Visuelles (Meilleure Qualité)

**Étape 1:** Upload tes références

1. Va dans ton projet Flow
2. Upload 3-4 flyers de `assets/references/flyers/`
3. Les images sont maintenant dans ton projet

**Étape 2:** Utilise-les comme "ingredients"

```
@[nom-du-flyer-reference] 

Crée un flyer pour Afrique Boussole en utilisant 
la composition de cette référence mais avec:
- Couleurs: #013C87 bleu et #1D7742 vert
- Sujet: Formation cybersécurité
- Logo: Boussole stylisée + "AFRIQUE BOUSSOLE"
- Message: Protégez votre business
- CTA: Inscrivez-vous
```

**Flow va:**
- Analyser la composition de la référence
- Appliquer le style
- Utiliser tes couleurs
- Générer ton flyer

---

### Méthode 3 — Prompt Direct (Plus Rapide)

**Dans Flow, mode Image:**

```
Professional A4 business flyer for "AFRIQUE BOUSSOLE" cybersecurity training.

LAYOUT:
- Left 60%: Young African entrepreneur on laptop with cybersecurity graphics overlay
- Right 40%: Content area with blue gradient background
- Top: "AFRIQUE BOUSSOLE" logo (compass icon + text)

COLORS:
- Primary: #013C87 (deep blue)
- Secondary: #1D7742 (green)
- Accent: white text on blue overlay

CONTENT:
- Main headline: "FORMATION EN CYBERSÉCURITÉ" (white, bold, large)
- Subheadline: "Protégez votre business" (white)
- 4 program modules with lock/shield icons
- Dates: "20 OCT - 10 NOV" 
- CTA button: "INSCRIVEZ-VOUS" (green button, white text, prominent)
- Footer: Contact info

STYLE:
- Corporate
- Modern
- Premium
- African professional aesthetic
- Clean geometric elements
- Diagonal green accent lines
```

---

## 📋 Template de Prompt pour Flow

Utilise ce template pour tous tes visuels:

```
Professional [FORMAT] for "AFRIQUE BOUSSOLE" [SUJET].

BRAND IDENTITY:
- Logo: Compass icon + "AFRIQUE BOUSSOLE" text
- Colors: #013C87 blue (primary), #1D7742 green (secondary)
- Tagline: "STRATÉGIE • INNOVATION • DATA"
- Style: Corporate, modern, premium, African

LAYOUT:
[Décris la composition voulue]

VISUAL ELEMENTS:
[Décris les images/graphiques]

CONTENT:
- Main headline: [TON TITRE]
- Message: [TON MESSAGE]
- CTA: [TON APPEL À L'ACTION]
- Additional info: [DATES, PRIX, ETC.]

DESIGN STYLE:
- Corporate professional
- Modern geometric elements
- Clean spacious layout
- African business aesthetic
- Premium finish
```

---

## 🎨 Conseils Spécifiques Flow

### Pour Obtenir les Bonnes Couleurs

Flow comprend les codes HEX. Utilise:
```
Primary color: #013C87 (deep corporate blue)
Secondary color: #1D7742 (professional green)
```

Pas juste "bleu" ou "vert".

### Pour le Texte Lisible

Flow a un **excellent rendu de texte**. Spécifie:
```
Text elements (all must be clearly readable):
- "FORMATION EN CYBERSÉCURITÉ" - white, bold, 48pt
- "Protégez votre business" - white, 24pt
- "INSCRIVEZ-VOUS" - button text, white on green
```

### Pour les Éléments de Marque

```
AFRIQUE BOUSSOLE branding:
- Compass icon: geometric, modern, directional
- Typography: sans-serif, bold, professional
- Visual language: navigation, direction, strategy, data, Africa
```

### Pour la Composition

Flow comprend les termes de design:
```
COMPOSITION:
- Z-layout reading pattern
- 60/40 split (image/content)
- Rule of thirds for focal points
- Generous white space
- Diagonal accent elements
```

---

## 🔄 Workflow Complet dans Flow

### 1. Setup Initial

**Créer un Character pour le Logo:**

Dans Flow:
```
Create a character named "AfriqueBoussole":
- Geometric compass icon in #013C87 blue and #1D7742 green
- Modern sans-serif text "AFRIQUE BOUSSOLE" below
- Tagline "STRATÉGIE • INNOVATION • DATA"
- Corporate professional style
```

Sauvegarde comme `@AfriqueBoussole`.

### 2. Upload Références

- Upload 5-6 flyers de `assets/references/flyers/`
- Nomme-les: `ref-corporate`, `ref-tech`, `ref-creative`, etc.

### 3. Création

**Pour chaque projet:**

```
Agent activé:

"En utilisant @AfriqueBoussole comme logo et en t'inspirant 
de @ref-corporate pour la composition, crée un flyer A4 pour:

[TON BRIEF ICI]

Utilise exactement les couleurs #013C87 et #1D7742.
Assure-toi que tous les textes sont lisibles."
```

### 4. Itération

Si le résultat n'est pas parfait:
```
"Ajuste ce flyer:
- Rends le titre plus bold
- Place le CTA plus en évidence
- Ajuste les couleurs pour être exactement #013C87 et #1D7742"
```

### 5. Export

Flow sauvegarde automatiquement. Tu peux:
- Télécharger en haute résolution
- Voir l'historique des versions
- Retravailler plus tard

---

## 📊 Comparaison: ChatGPT vs Flow

| Aspect | ChatGPT + DALL-E | Google Flow |
|--------|------------------|-------------|
| Qualité image | ⭐⭐⭐ Bonne | ⭐⭐⭐⭐ Excellente |
| Rendu texte | ⭐⭐ Moyen | ⭐⭐⭐⭐⭐ Excellent |
| Références visuelles | ❌ Indirect | ✅ Direct (upload) |
| Couleurs exactes | ⭐⭐⭐ Approximatif | ⭐⭐⭐⭐ Précis |
| Itérations | ✅ Conversationnel | ✅ Conversationnel |
| Consistance | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Prix | $ Crédits | Gratuit (Labs) |
| Accès assets | ❌ Non | ✅ Upload direct |

**Verdict:** Flow est **MIEUX** pour Afrique Boussole car:
1. Rendu de texte excellent
2. Upload direct des références
3. Couleurs précises
4. Gratuit pendant phase Labs

---

## 🎯 Exemples Concrets

### Exemple 1 — Flyer Formation

**Dans Flow Agent:**
```
Using @AfriqueBoussole logo and inspired by @ref-corporate layout, 
create an A4 flyer for cybersecurity training.

TARGET: Young African digital entrepreneurs
MESSAGE: "Protégez votre business"
DATES: Oct 20 - Nov 10
PROGRAM: 6 weeks, 4 modules
CTA: "INSCRIVEZ-VOUS"

COMPOSITION:
- Right: Professional African on laptop with blue overlay
- Left: Content with program details
- Header: Logo + "FORMATION EN CYBERSÉCURITÉ"
- Footer: Contact + dates

COLORS: #013C87 (blue primary), #1D7742 (green accents)
STYLE: Corporate, modern, premium
```

### Exemple 2 — Post LinkedIn

**Dans Flow Agent:**
```
Using @AfriqueBoussole branding, create a LinkedIn post image (1200x627).

CONTENT: "New consulting service launch"
VISUAL: African business professionals in modern office
OVERLAY: Semi-transparent #013C87 blue with text
TEXT: "Naviguer l'Afrique avec Expertise" - white, bold
LOGO: @AfriqueBoussole top-left corner
CTA: "Découvrir nos services"

STYLE: Professional, aspirational, African excellence
```

### Exemple 3 — Instagram Story

**Dans Flow Agent:**
```
Using @AfriqueBoussole, create Instagram Story (1080x1920).

LAYOUT: Vertical mobile-first
TOP: @AfriqueBoussole logo small
MIDDLE: Bold statistic "87% des PME africaines..." 
VISUAL: Abstract tech/data visualization in #013C87 and #1D7742
BOTTOM: Swipe up CTA "En savoir plus"

COLORS: Gradient from #013C87 to #1D7742
STYLE: Modern, data-driven, mobile-optimized
```

---

## 🚨 Troubleshooting Flow

### Problème: Couleurs Pas Exactes

**Solution:**
```
Adjust colors to match EXACTLY these hex codes:
- #013C87 for blue (not similar, exact)
- #1D7742 for green (not similar, exact)
```

### Problème: Texte Illisible

**Solution:**
```
Make all text clearly readable:
- Increase font size for headline
- Use white text on dark background
- Add contrast with overlay or shadow
```

### Problème: Logo Incorrect

**Solution:** Utilise un character créé:
```
First, let me create @AfriqueBoussole character properly.

Then: "Place @AfriqueBoussole logo prominently in top-left"
```

### Problème: Composition Mauvaise

**Solution:** Utilise une référence:
```
Follow the layout from @ref-corporate:
- 60/40 split
- Image on left
- Content on right
- Clear hierarchy
```

---

## 📥 Prochaines Étapes

### 1. Setup Flow (5 min)
- [ ] Créer compte Google Labs
- [ ] Accéder à Flow: https://labs.google/fx/tools/flow
- [ ] Créer premier projet "Afrique Boussole"

### 2. Préparer Assets (10 min)
- [ ] Créer character `@AfriqueBoussole` avec description du logo
- [ ] Upload 5 flyers de référence depuis `assets/references/flyers/`
- [ ] Nommer les références clairement

### 3. Premier Test (5 min)
- [ ] Activer Agent
- [ ] Copier l'instruction de marque
- [ ] Demander un flyer simple
- [ ] Vérifier couleurs + logo + texte

### 4. Itérer (répéter)
- [ ] Ajuster selon résultats
- [ ] Sauvegarder les bons prompts
- [ ] Construire bibliothèque de visuels

---

## 🔗 Ressources

**Accès Flow:**
https://labs.google/fx/tools/flow

**Documentation officielle:**
https://support.google.com/flow/answer/16729550

**Skill Afrique Boussole:**
https://github.com/AMICHIABRYAN7/afrique-boussole-creatives

**Instruction ChatGPT (référence):**
`CHATGPT-COMPLETE-INSTRUCTION.md` dans le repo

---

## 💡 Conseils Pro

1. **Créer des variations:**
   ```
   "Generate 5 variations with different:
   - Layouts
   - Photo subjects
   - Text hierarchies"
   ```

2. **Sauvegarder les bons prompts:**
   Flow garde l'historique. Note les prompts qui marchent.

3. **Utiliser l'historique:**
   Chaque image a un historique de versions. Tu peux revenir en arrière.

4. **Combiner avec editing:**
   Génère → Édite → Re-génère → Affine

5. **Batch generation:**
   ```
   "Create 3 versions of this flyer:
   - Version A: Bold and modern
   - Version B: Elegant and minimalist  
   - Version C: Dynamic and tech-focused"
   ```

---

## ✅ Checklist Qualité Flow

Avant de valider un visuel:

- [ ] Logo Afrique Boussole présent et correct?
- [ ] Couleurs exactes #013C87 #1D7742?
- [ ] Texte TOUS lisible (headline, message, CTA)?
- [ ] Composition équilibrée et professionnelle?
- [ ] Style correspond à la marque (corporate, premium)?
- [ ] CTA visible et prominent?
- [ ] Informations correctes (dates, prix, contact)?
- [ ] Résolution suffisante pour impression/digital?

Si 8/8 → ✅ Valide
Si <8/8 → Itère avec Agent

---

**BON TRAVAIL AVEC FLOW! 🚀**

Questions? Problèmes? Reviens vers moi.
