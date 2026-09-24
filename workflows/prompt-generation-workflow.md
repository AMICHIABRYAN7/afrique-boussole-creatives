# Workflow : AI Prompt Generation — Afrique Boussole

**Version** : 1.0  
**Date** : Septembre 2026  
**Durée estimée** : 10-15 minutes par prompt  
**Prérequis** : Avoir lu `references/ai-prompt-engineering.md`

---

## 🎯 OBJECTIF

Construire un prompt IA professionnel qui génère un visuel brand-compliant Afrique Boussole.

**Entrée** : Brief créatif (objectif, audience, message, format)  
**Sortie** : 3 prompts optimisés (conservative, creative, bold) prêts à soumettre à Midjourney/DALL-E/Flux

---

## 📋 WORKFLOW EN 12 ÉTAPES

### **ÉTAPE 1 : ANALYSER LE BRIEF** (2 min)

Extraire du brief :
- **Objectif** : Que veut-on accomplir ? (génération leads, notoriété, inscription événement)
- **Audience** : Qui est la cible ? (entrepreneurs, étudiants, C-suite)
- **Message principal** : Quel est le hook ? (la phrase clé)
- **Format** : Quel livrable ? (flyer A4, affiche A3, social 1:1, story 9:16)
- **Mood** : Quelle émotion ? (confiant, inspirant, dynamique, professionnel)

**Exemple :**
```
Brief : Flyer pour webinaire "Lever des fonds en Afrique"
→ Objectif : Générer inscriptions
→ Audience : Entrepreneurs africains 25-45 ans
→ Message : "Maîtrisez les stratégies de fundraising"
→ Format : A4 print + Instagram 4:5
→ Mood : Confiant, aspirationnel, professionnel
```

---

### **ÉTAPE 2 : IDENTIFIER LE CAS D'USAGE** (1 min)

Charger le template approprié de `ai-prompt-engineering.md` :

| Si le visuel nécessite... | Utiliser template... |
|---------------------------|---------------------|
| Personne(s) identifiable(s) | **CAS 1: Portrait entrepreneur** |
| Groupe collaborant | **CAS 2: Équipe collaborative** |
| Illustration conceptuelle | **CAS 3: Concept abstrait** |
| Background pour composition | **CAS 4: Background subtil** |
| Gros plan sur détail | **CAS 5: Close-up mains + tech** |

**Exemple** : Flyer fundraising → besoin d'un entrepreneur confiant → **CAS 1**

---

### **ÉTAPE 3 : DÉFINIR LE SUBJECT** (2 min)

**Questions :**
- Qui/quoi dans l'image ?
- Âge, genre, profil ?
- Action/posture ?
- Éléments secondaires ?

**Règles Afrique Boussole :**
- ✅ Africain contemporain, contexte professionnel
- ✅ Diversité ethnique naturelle
- ✅ Vêtements corporate modernes
- ❌ PAS de clichés (costumes traditionnels sans contexte business)
- ❌ PAS de poses exagérées

**Template :**
```
African [male/female] entrepreneur age [X-Y] [action] in [context]
```

**Exemple :**
```
African male entrepreneur age 35-40 presenting confidently with hand gestures in modern office
```

---

### **ÉTAPE 4 : DÉFINIR L'ENVIRONMENT** (1 min)

**Questions :**
- Où se passe la scène ?
- Intérieur ou extérieur ?
- Contexte urbain africain spécifique ?
- Neutre ou branded ?

**Options Afrique Boussole :**
- Bureau moderne Lagos/Nairobi/Accra/Kigali
- Co-working space contemporain
- Salle de conférence professionnelle
- Studio neutre (focus sur sujet)

**Exemple :**
```
in contemporary co-working space with glass walls and modern African architectural details
```

---

### **ÉTAPE 5 : DÉFINIR LA COMPOSITION** (2 min)

**Référence** : `references/composition-system.md`

**Questions :**
- Où sera placé le texte du flyer/affiche ?
- Quelle hiérarchie visuelle ? (sujet centré, décentré, diagonal)
- Combien d'espace nécessaire pour typo ?

**Mapping composition :**
- Flyer avec headline haut → `"clean negative space in upper third"`
- Affiche avec headline centré → `"centered composition, symmetrical"`
- Social avec texte overlay → `"subject positioned left, right third empty for text"`
- Poster dynamique → `"diagonal composition from bottom-left to top-right"`

**Exemple :**
```
rule of thirds composition with subject positioned at right intersection point, clean negative space in left 40% for headline text overlay
```

---

### **ÉTAPE 6 : DÉFINIR LE CAMERA** (1 min)

**Questions :**
- Quelle distance ? (gros plan, plan moyen, plan large)
- Quel angle ? (eye level, low angle, overhead)
- Quelle focal ? (24mm wide, 50mm standard, 85mm portrait)
- Quelle profondeur de champ ?

**Mapping par format :**
- Portrait entrepreneur → `"medium shot, eye level, 50mm lens"`
- Héroïque/aspirationnel → `"slight low angle, 35mm lens"`
- Équipe collaborative → `"wide angle shot, 24mm lens"`
- Détail technique → `"close-up, 85mm lens, f/1.8 shallow depth of field"`

**Exemple :**
```
medium shot at eye level, 50mm lens, f/2.8 with blurred background for focus on subject
```

---

### **ÉTAPE 7 : DÉFINIR LE LIGHTING** (1 min)

**Questions :**
- Source lumière ? (naturelle, studio, mixte)
- Intensité ? (douce, dramatique)
- Direction ? (window light, overhead, rim light)
- Color temperature ? (warm, neutral, cool)

**Règles Afrique Boussole :**
- ✅ Lumière douce naturelle (golden hour, window light)
- ✅ Studio professionnel (softbox, rim light)
- ✅ Warm color temperature (2800-4000K)
- ❌ PAS de lumière dure/ombres agressives

**Exemple :**
```
soft natural light from large window on left side, warm color temperature 3200K, gentle rim light from back-right
```

---

### **ÉTAPE 8 : DÉFINIR LE COLOR** (2 min)

**Référence** : `references/brand-system.md`

**Palette Afrique Boussole :**
```
Primary Blue: #013C87
Primary Green: #1D7742
Neutrals: #FFFFFF, #F7F4EC
```

**Questions :**
- Couleur dominante ? (blue, green, neutral)
- Où injecter les couleurs brand ? (vêtements, objets, fond)
- Saturation ? (muted professional, vibrant)

**Templates :**
```
"color palette dominated by navy blue #013C87 with forest green #1D7742 accents"
"professional muted tones, navy blue #013C87 suit, warm ivory #F7F4EC background"
"vibrant but professional, rich navy blue #013C87 and green #1D7742 brand colors"
```

**Exemple :**
```
color palette: navy blue #013C87 suit jacket, white shirt, forest green #1D7742 notebook in hand, warm ivory #F7F4EC office background
```

---

### **ÉTAPE 9 : DÉFINIR LE MOOD** (1 min)

**Référence** : `references/creative-strategy.md`

**Mapping angle créatif → mood :**
- AUTHORITY → `"professional confident atmosphere, trustworthy"`
- OPPORTUNITY → `"dynamic aspirational mood, sense of possibility"`
- HUMAN IMPACT → `"warm inspiring atmosphere, transformative energy"`
- NAVIGATION → `"clear purposeful mood, strategic direction"`
- DATA/EXPERTISE → `"analytical professional atmosphere, precision"`
- EDUCATION → `"approachable empowering mood, learning energy"`

**Exemple :**
```
confident aspirational atmosphere, sense of expertise and forward momentum, professional yet approachable
```

---

### **ÉTAPE 10 : DÉFINIR LE TECHNICAL** (1 min)

**Choisir plateforme IA :**

#### **Si Midjourney v6.1 :**
```
--ar [ratio]      → 4:5 (Instagram), 9:16 (Story), 16:9 (landscape), 3:2 (print)
--style raw       → photo réaliste
--stylize 300     → balance esthétique
--v 6.1           → dernière version
```

#### **Si DALL-E 3 :**
```
"photorealistic style, high resolution, professional commercial photography, 4K quality, sharp focus, natural lighting"
```

#### **Si Flux Pro :**
```
"ultra detailed, 8K resolution, professional photography, DSLR camera, natural lighting, realistic textures, high dynamic range, color graded"
```

**Exemple (Midjourney) :**
```
photorealistic commercial photography, natural skin tones, sharp focus on subject, 4K quality --ar 4:5 --style raw --v 6.1
```

---

### **ÉTAPE 11 : ASSEMBLER LE PROMPT** (2 min)

**Structure finale :**
```
[SUBJECT], [ENVIRONMENT], [COMPOSITION], [CAMERA], [LIGHTING], [COLOR], [MOOD], [TECHNICAL]
```

**Exemple complet :**
```
African male entrepreneur age 35-40 presenting confidently with hand gestures in contemporary co-working space with glass walls and modern African architectural details, rule of thirds composition with subject positioned at right intersection point and clean negative space in left 40% for headline text overlay, medium shot at eye level 50mm lens f/2.8 with blurred background, soft natural light from large window on left side with warm color temperature 3200K and gentle rim light from back-right, color palette dominated by navy blue #013C87 suit jacket with white shirt and forest green #1D7742 notebook in hand against warm ivory #F7F4EC office background, confident aspirational atmosphere with sense of expertise and forward momentum, photorealistic commercial photography, natural skin tones, sharp focus on subject, 4K quality --ar 4:5 --style raw --v 6.1
```

---

### **ÉTAPE 12 : CRÉER LES 3 VARIATIONS** (3 min)

**Partir du prompt de base, créer :**

#### **VERSION CONSERVATIVE** (90% réaliste)
- Composition classique (rule of thirds, centered)
- Lumière naturelle douce
- Couleurs naturelles + accents brand subtils
- Photo pure, pas d'effets

**Modifications :**
```
Garder base + ajouter: "natural unposed candid photography, authentic moment, minimal styling, subtle brand colors"
```

---

#### **VERSION CREATIVE** (70% réaliste, 30% stylisé)
- Composition dynamique (diagonal, split)
- Lumière professionnelle + effets
- Couleurs brand plus marquées
- Photo + éléments graphiques subtils

**Modifications :**
```
Remplacer composition: "dynamic diagonal composition from lower-left to upper-right"
Ajouter: "dramatic professional lighting with subtle geometric overlay elements, saturated navy blue #013C87 and green #1D7742 brand colors, modern corporate aesthetic with light visual effects"
```

---

#### **VERSION BOLD** (40% réaliste, 60% stylisé)
- Composition avant-gardiste
- Lumière stylisée + effets visuels
- Palette brand dominante et saturée
- Mélange photo + illustration + 3D

**Modifications :**
```
Remplacer environment: "in abstract modern space with floating navy blue #013C87 geometric shapes and green #1D7742 trajectory lines in background"
Ajouter: "stylized professional photography mixed with 3D elements and graphic overlays, bold saturated brand colors, contemporary corporate art direction, cinematic visual effects, dramatic lighting with colored gels"
Changer technical: "--stylize 600" (au lieu de 300)
```

---

## ✅ CHECKLIST FINALE

Avant de soumettre, vérifier :

**Structure :**
- [ ] Les 8 blocs sont présents (SUBJECT/ENV/COMP/CAM/LIGHT/COLOR/MOOD/TECH)
- [ ] Le prompt fait 150-300 mots (ni trop court, ni trop long)
- [ ] Les virgules séparent bien chaque bloc

**Brand Compliance :**
- [ ] Couleurs brand avec hex codes (#013C87, #1D7742, #F7F4EC)
- [ ] Contexte africain contemporain (pas cliché)
- [ ] Mood aligné avec objectif marketing

**Technique :**
- [ ] Espace pour texte spécifié ("negative space in [zone]")
- [ ] Paramètres IA corrects (--ar, --style, --v pour Midjourney)
- [ ] Pas de demande de texte généré ("headline", "title", "words")
- [ ] Composition référencée (rule of thirds, diagonal, etc.)

**Qualité :**
- [ ] Photo réaliste demandée ("photorealistic", "commercial photography")
- [ ] Résolution spécifiée ("4K", "8K", "high quality")
- [ ] Profondeur de champ adaptée (f/1.8 portrait, f/8 groupe)

---

## 📤 SOUMISSION À L'IA

### **Midjourney v6.1**

1. Ouvrir Discord Midjourney
2. Taper `/imagine`
3. Coller prompt dans `prompt` field
4. Vérifier paramètres `--ar`, `--style`, `--v`
5. Envoyer
6. Attendre génération (60-90 sec)
7. Upscale image préférée (U1, U2, U3, U4)
8. Télécharger haute résolution

---

### **DALL-E 3 (ChatGPT ou API)**

1. Ouvrir ChatGPT Plus ou API playground
2. Coller prompt (sans paramètres Midjourney)
3. Préciser format : "Generate in [1024x1024 / 1024x1792 / 1792x1024]"
4. Envoyer
5. Attendre génération (20-40 sec)
6. Télécharger image

---

### **Flux Pro (Replicate, Fal.ai)**

1. Ouvrir plateforme (replicate.com ou fal.ai)
2. Sélectionner modèle "Flux Pro" ou "Flux Schnell"
3. Coller prompt
4. Définir dimensions : 1024x1024, 1024x1536, etc.
5. Steps : 25-50 (plus = meilleure qualité)
6. Guidance scale : 7-8 (balance créativité/fidélité)
7. Générer
8. Télécharger résultat

---

## 🔄 ITÉRATION SI NÉCESSAIRE

**Si le résultat n'est pas satisfaisant :**

### Problème : **Composition incorrecte**
→ Renforcer description spatiale : `"subject MUST be positioned at right third, with large empty space on left side"`

### Problème : **Couleurs brand pas respectées**
→ Répéter 2-3 fois : `"navy blue #013C87, SPECIFICALLY hex code #013C87 navy blue"`
→ Post-production : ajuster couleurs dans Photoshop/Figma

### Problème : **Mood incorrect**
→ Ajouter plus d'adjectifs : `"confident, professional, aspirational, trustworthy, modern"`

### Problème : **Trop stylisé (quand conservative souhaité)**
→ Ajouter : `"natural candid photography, authentic unposed moment, documentary style"`
→ Midjourney : baisser `--stylize` de 300 → 100

### Problème : **Pas assez stylisé (quand bold souhaité)**
→ Ajouter : `"dramatic cinematic lighting, bold graphic elements, contemporary art direction"`
→ Midjourney : monter `--stylize` de 300 → 600

---

## 🎨 POST-PRODUCTION

Une fois l'image générée :

**Étape 1 : Vérification couleurs**
- Ouvrir dans Photoshop/Figma
- Vérifier couleurs avec Color Picker
- Si décalage > 10% : ajuster avec Hue/Saturation ou Color Balance

**Étape 2 : Composition texte**
- Importer dans Figma/Illustrator/Photoshop
- Ajouter texte selon hiérarchie typographique (`typography-system-pro.md`)
- Utiliser l'espace négatif prévu dans le prompt

**Étape 3 : Ajout logo**
- Placer logo Afrique Boussole (bottom-right ou top-left)
- Respecter règles `logo-usage.md` (taille min, clear space)

**Étape 4 : Validation**
- Vérifier checklist `validation-checklist.md`
- Contraste WCAG AA minimum (4.5:1)
- Lisibilité en small size (mobile)

---

## 📊 EXEMPLES ANNOTÉS

### **Exemple 1 : Flyer Webinaire**

**Brief :**
- Objectif : Inscriptions webinaire fundraising
- Audience : Entrepreneurs 25-45 ans
- Format : A4 + Instagram 4:5
- Mood : Confiant, aspirationnel

**Prompt conservative généré :**
```
African male entrepreneur age 38 sitting at modern desk reviewing financial documents with confident expression in contemporary Lagos office with floor-to-ceiling windows and city skyline view, rule of thirds composition with subject at right intersection and clean empty space in upper-left 40% for headline placement, medium shot at eye level 50mm lens f/2.8 shallow depth of field with blurred office background, soft natural window light from left creating gentle shadows with warm 3200K color temperature, color palette: navy blue #013C87 blazer over white shirt, forest green #1D7742 folder on desk, warm ivory #F7F4EC walls, professional confident atmosphere suggesting expertise and trustworthiness, natural unposed candid photography with authentic moment, photorealistic commercial style, sharp focus on subject with natural skin tones, 4K quality --ar 4:5 --style raw --v 6.1
```

**Résultat attendu :** Entrepreneur africain confiant dans bureau moderne, espace haut-gauche vide pour headline "Maîtrisez les stratégies de fundraising"

---

### **Exemple 2 : Affiche Événement**

**Brief :**
- Objectif : Promouvoir conférence tech
- Audience : Professionnels tech
- Format : A3 poster
- Mood : Dynamique, innovant

**Prompt creative généré :**
```
Diverse group of 4 African tech professionals collaborating energetically around large touchscreen display showing data visualizations in modern innovation lab with exposed concrete and glass, dynamic diagonal composition from lower-left to upper-right with clean negative space in top 30% for event title, wide angle shot 24mm lens from slightly low angle f/4 with all subjects in sharp focus, dramatic professional lighting with key light from above and blue rim lights, rich saturated color palette dominated by navy blue #013C87 clothing and green #1D7742 LED accent lights with subtle geometric overlay elements, dynamic innovative atmosphere with sense of forward momentum and collaboration, modern corporate photography mixed with light graphic elements, sharp focus with vibrant colors, cinematic lighting quality, 4K resolution --ar 3:2 --stylize 400 --v 6.1
```

**Résultat attendu :** Équipe tech dynamique, composition diagonale, espace haut pour titre événement, feel innovant et énergique

---

## 🔗 RÉFÉRENCES

**Fichiers à charger selon besoin :**
- `references/ai-prompt-engineering.md` — théorie complète, 8 blocs, templates
- `references/brand-system.md` — couleurs exactes (#013C87, #1D7742)
- `references/composition-system.md` — 7 systèmes composition
- `references/creative-strategy.md` — angles créatifs par objectif
- `references/photography-direction.md` — direction photo Afrique Boussole
- `references/typography-system-pro.md` — pour post-production texte

**Outils externes :**
- [Midjourney](https://www.midjourney.com/) — meilleur pour photos corporate
- [DALL-E 3](https://openai.com/dall-e-3) — meilleur pour précision géométrique
- [Flux Pro](https://fal.ai/) — meilleur pour patterns/backgrounds
- [Photoshop](https://www.adobe.com/photoshop) — post-production couleurs
- [Figma](https://www.figma.com/) — composition texte + image

---

## 💡 TIPS AVANCÉS

### **Tip 1 : Variations rapides**
Au lieu de réécrire tout le prompt, utiliser "remix mode" dans Midjourney pour ajuster 1 élément à la fois.

### **Tip 2 : Seed consistency**
Dans Midjourney, ajouter `--seed [nombre]` pour reproduire style similaire entre plusieurs générations.

### **Tip 3 : Image reference**
Utiliser `--sref [URL]` (Midjourney) pour référencer un style visuel existant.

### **Tip 4 : Multi-prompts**
Séparer avec `::` pour pondérer importance : `entrepreneur::2 office::1` (entrepreneur 2× plus important)

### **Tip 5 : Negative prompts**
Dans Stable Diffusion : spécifier ce qu'on NE veut PAS : `"blurry, low quality, cartoon, 3d render"`

---

**Version** : 1.0  
**Durée workflow** : 10-15 minutes par prompt  
**Output** : 3 prompts (conservative/creative/bold) prêts à soumettre  
**Dernière mise à jour** : Septembre 2026

---

End of prompt-generation-workflow.md
