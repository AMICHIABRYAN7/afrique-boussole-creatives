# AI Prompt Engineering — Afrique Boussole Creatives

**Version** : 1.0  
**Date** : Septembre 2026  
**Objectif** : Générer des prompts optimisés pour IA générative (Midjourney, DALL-E, Flux, Stable Diffusion) qui produisent des visuels brand-compliant Afrique Boussole

---

## 🎯 PRINCIPE FONDAMENTAL

Un prompt IA efficace ne dit pas **"crée un flyer moderne"**.

Il encode **8 dimensions visuelles** dans une structure précise :

```
SUBJECT + ENVIRONMENT + COMPOSITION + LIGHTING + COLOR + MOOD + STYLE + TECHNICAL
```

Chaque dimension doit porter l'ADN visuel d'Afrique Boussole : **contemporain, corporate, africain, premium, non-cliché**.

---

## 📐 ARCHITECTURE D'UN PROMPT PROFESSIONNEL

### **Structure en 8 blocs**

```
[SUBJECT]
Quoi/qui dans l'image

[ENVIRONMENT]
Où se passe la scène

[COMPOSITION]
Comment les éléments sont arrangés

[CAMERA]
Angle, distance, focal

[LIGHTING]
Source, intensité, qualité lumière

[COLOR]
Palette dominante

[MOOD]
Émotion/atmosphère

[TECHNICAL]
Résolution, style, paramètres IA
```

---

## 🧱 BLOCS DÉTAILLÉS

### **1. SUBJECT (Sujet principal)**

**Règles Afrique Boussole (GAB SARL) :**
- ✅ Entrepreneurs, ingénieurs et techniciens africains en contexte professionnel
- ✅ Équipes mixtes (diversité ethnique, genre, âge)
- ✅ Technologies modernes GAB (serveurs, caméras IP, fibre optique, dashboards)
- ✅ Environnements urbains africains contemporains (Abidjan, Côte d'Ivoire)
- ✅ Concepts abstraits (cybersécurité, réseau, navigation, stratégie)

- ❌ PAS de clichés (savane, animaux sauvages, villages ruraux sans contexte business)
- ❌ PAS de tokenisme (1 personne noire dans groupe majoritairement blanc)
- ❌ PAS de poses exagérées (pointing, fake laughing)

**Templates :**
```
"African IT engineer [age 30-45] configuring servers in modern data center"
"Diverse team of 5 tech professionals collaborating around conference table"
"Close-up hands of African security expert analyzing IP camera dashboard"
"Abstract concept of secure network connectivity and strategy, geometric shapes"
```

---

### **2. ENVIRONMENT (Environnement)**

**Règles Afrique Boussole (GAB SARL) :**
- ✅ Bureaux tech et data centers modernes (Abidjan, Côte d'Ivoire)
- ✅ Co-working spaces contemporains et salles de formation (GAB Academy)
- ✅ Skyline urbain d'Abidjan (Plateau, ponts)
- ✅ Salles de supervision / contrôle de sécurité
- ✅ Espaces neutres épurés (fonds unis pour focus sur sujet)

**Templates :**
```
"in contemporary Abidjan high-rise tech office with floor-to-ceiling windows"
"in minimalist white IT lab space with natural light"
"against backdrop of modern Abidjan Plateau skyline at golden hour"
"in bright modern training room with African architectural details"
```

---

### **3. COMPOSITION (Organisation visuelle)**

**Référence** : `references/composition-system.md`

**Pour IA générative :**
- Rule of thirds → `"subject positioned at intersection of rule of thirds grid"`
- Centered → `"centered composition, symmetrical balance"`
- Split screen → `"split composition, left side [X], right side [Y]"`
- Diagonal → `"dynamic diagonal composition from bottom-left to top-right"`
- Z-layout → `"eye flow in Z-pattern, focal points at Z corners"`

**Espace pour texte :**
- `"clean negative space in upper third for text overlay"`
- `"blank area on right side for typography"`
- `"bottom 40% empty for copy placement"`

---

### **4. CAMERA (Cadrage & angle)**

**Options :**
- `"wide angle shot, 24mm lens"`
- `"medium shot, eye level, 50mm lens"`
- `"close-up portrait, 85mm lens, shallow depth of field"`
- `"overhead flat lay, directly above, 35mm"`
- `"slight low angle, heroic perspective"`
- `"bird's eye view, top-down 90 degrees"`

**Profondeur de champ :**
- `"f/1.8 shallow focus, blurred background"`
- `"f/8 sharp focus throughout, deep depth of field"`

---

### **5. LIGHTING (Lumière)**

**Règles Afrique Boussole :**
- ✅ Lumière naturelle douce (golden hour, window light)
- ✅ Studio lighting professionnel (softbox, rim light)
- ✅ Warm white balance (2800-4000K)

- ❌ PAS de lumière dure/ombres agressives
- ❌ PAS de néons froids/lumière clinique

**Templates :**
```
"soft natural light from large window, warm color temperature"
"studio lighting with softbox, gentle rim light, professional setup"
"golden hour sunlight, warm glow, soft shadows"
"diffused daylight, even illumination, no harsh shadows"
```

---

### **6. COLOR (Palette couleur)**

**Brand Palette** : `references/brand-system.md`

```
Primary Blue: #013C87
Primary Green: #1D7742
Neutrals: #FFFFFF, #F7F4EC
```

**Pour IA :**
- `"color palette: navy blue #013C87 and forest green #1D7742 accents"`
- `"dominated by deep blue tones, subtle green highlights"`
- `"warm ivory #F7F4EC background with navy blue #013C87 elements"`
- `"professional corporate color scheme, blue and green brand colors"`

**Saturation :**
- `"slightly desaturated, professional muted tones"`
- `"rich saturated colors, vibrant but not artificial"`

---

### **7. MOOD (Atmosphère & émotion)**

**Afrique Boussole tone :**
- ✅ Professionnel, confiant, inspirant
- ✅ Dynamique mais pas agressif
- ✅ Accessible mais pas décontracté
- ✅ Aspirationnel mais réaliste

**Templates :**
```
"professional and confident atmosphere"
"inspiring and aspirational mood, grounded in reality"
"dynamic energy, sense of forward movement"
"trustworthy and approachable corporate environment"
```

---

### **8. TECHNICAL (Paramètres techniques)**

### **Par plateforme IA :**

#### **Midjourney v6.1**
```
--ar 4:5          (Instagram feed)
--ar 9:16         (Stories/Reels)
--ar 16:9         (Landscape/LinkedIn)
--ar 3:2          (Print A4 proportions)
--style raw       (moins stylisé, plus photo)
--stylize 300     (balance réalisme/esthétique)
--v 6.1           (dernière version)
```

#### **DALL-E 3**
```
"photorealistic style, high resolution"
"natural photography, not CGI or illustration"
"professional commercial photography"
"4K quality, sharp focus"
```

#### **Flux Pro / Schnell**
```
"ultra detailed, 8K resolution"
"professional photography, DSLR camera"
"natural lighting, realistic textures"
"high dynamic range, color graded"
```

#### **Stable Diffusion XL**
```
"professional product photography, studio lighting, 8k uhd, high quality"
Negative: "cartoon, illustration, 3d render, blurry, low quality"
```

---

## 🎨 TEMPLATES PAR CAS D'USAGE

### **CAS 1 : Photo portrait expert/ingénieur (flyer/poster)**

```
African male IT engineer age 35-40 working confidently on laptop and server rack in modern Abidjan high-rise tech office with floor-to-ceiling windows overlooking city skyline, medium shot at eye level 50mm lens, soft natural window light from left side with warm color temperature, shallow depth of field f/2.8 with blurred background, clean negative space in right third for text overlay, color palette dominated by navy blue #013C87 suit and warm ivory #F7F4EC office tones with green #1D7742 server led accent, professional confident atmosphere with sense of forward momentum, photorealistic style, natural photography not CGI, 4K quality sharp focus --ar 4:5 --style raw --v 6.1
```

---

### **CAS 2 : Équipe collaborative (campagne corporate)**

```
Diverse team of 5 African professionals (3 women, 2 men, mixed ages 28-45) collaborating around modern conference table with laptops and documents, overhead bird's eye view 35mm lens looking down at 45-degree angle, even diffused daylight from skylight above, deep depth of field f/8 with all subjects in sharp focus, centered composition with symmetrical balance, professional corporate color scheme with navy blue #013C87 folders and forest green #1D7742 notebooks on white table, trustworthy and collaborative atmosphere, sense of teamwork and strategy, photorealistic commercial photography, natural skin tones, 8K ultra detailed --ar 16:9 --style raw --v 6.1
```

---

### **CAS 3 : Concept abstrait navigation/stratégie (affiche)**

```
Abstract 3D geometric composition suggesting navigation and strategic direction, floating navy blue #013C87 compass rose in center surrounded by curved green #1D7742 trajectory lines and coordinate grid overlays on warm ivory #F7F4EC background, diagonal composition from bottom-left to top-right creating dynamic flow, clean negative space in upper 40% for headline text, studio lighting with soft key light and subtle rim light, slightly desaturated professional muted tones, modern corporate aesthetic, sense of clarity and purpose, 3D render with realistic materials and soft shadows, 4K quality --ar 3:2 --stylize 400 --v 6.1
```

---

### **CAS 4 : Background subtil (social media post)**

```
Minimalist background with subtle cartesian coordinate grid pattern in light navy blue #013C87 at 10% opacity, soft gradient from warm ivory #F7F4EC top to white bottom, clean empty center area for text and graphics overlay, gentle directional lines suggesting movement from left to right, professional corporate aesthetic, calming trustworthy mood, vector-style illustration with smooth gradients, perfect for typography overlay, ultra clean 8K resolution --ar 1:1 --style raw --v 6.1
```

---

### **CAS 5 : Close-up mains + tech (detail shot)**

```
Close-up of African business person's hands typing on MacBook laptop showing data dashboard with blue and green charts on screen, shallow focus on hands with blurred background, warm skin tones under soft natural window light, navy blue #013C87 sleeve visible, green #1D7742 notebook partially in frame, professional manicured nails, sense of expertise and precision, photorealistic macro photography 85mm lens f/1.8, natural textures and details, commercial product photography quality, 4K sharp focus --ar 4:5 --style raw --v 6.1
```

---

## 🔄 SYSTÈME DE VARIATIONS

Pour chaque brief, générer **3 versions** :

### **1. CONSERVATIVE** (90% réaliste, 10% stylisé)
- Photo réaliste pure
- Lumière naturelle
- Couleurs naturelles avec accents brand subtils
- Composition classique (rule of thirds, centered)
- Pour : flyers institutionnels, corporate, événements officiels

### **2. CREATIVE** (70% réaliste, 30% stylisé)
- Photo réaliste avec éléments graphiques
- Lumière professionnelle + effets subtils
- Couleurs brand plus marquées
- Composition dynamique (diagonal, split)
- Pour : campagnes marketing, publicités, social media

### **3. BOLD** (40% réaliste, 60% stylisé)
- Mélange photo + illustration + 3D
- Lumière stylisée, effets visuels
- Palette brand dominante et saturée
- Composition avant-gardiste
- Pour : campagnes disruptives, thought leadership, innovation

---

## ⚙️ WORKFLOW GÉNÉRATION

```
1. Analyser le brief
   ↓
2. Identifier cas d'usage (portrait, équipe, concept, background, detail)
   ↓
3. Charger template correspondant
   ↓
4. Customiser les 8 blocs :
   - SUBJECT (adapter au brief)
   - ENVIRONMENT (choisir contexte)
   - COMPOSITION (selon hiérarchie visuelle)
   - CAMERA (selon distance needed)
   - LIGHTING (selon mood)
   - COLOR (injecter palette brand)
   - MOOD (selon objectif marketing)
   - TECHNICAL (paramètres IA + format)
   ↓
5. Générer 3 versions (conservative/creative/bold)
   ↓
6. Soumettre à IA générative
   ↓
7. Post-production : recolor aux couleurs exactes brand si nécessaire
   ↓
8. Composer avec texte séparément (ne PAS demander à l'IA de générer texte)
```

---

## 🚫 ANTI-PATTERNS PROMPTS

### ❌ Trop vague
```
"modern professional African business flyer"
→ L'IA ne sait pas : quel sujet ? quelle composition ? quelle lumière ? quel format ?
```

### ❌ Texte dans le prompt
```
"flyer with headline 'Transform Your Business' in big letters"
→ Les IA génèrent mal le texte. TOUJOURS séparer image et typo.
```

### ❌ Trop de concepts
```
"African entrepreneur with laptop in office with compass overlay and map background and charts and team photos and..."
→ Confusion visuelle. 1 concept principal max.
```

### ❌ Couleurs imprécises
```
"blue and green colors"
→ Préciser : "navy blue #013C87 and forest green #1D7742"
```

### ❌ Clichés africains
```
"African savanna sunset with acacia trees"
→ Non pertinent pour une marque corporate/business
```

---

## 🎯 CHECKLIST QUALITÉ PROMPT

Avant de soumettre, vérifier :

- [ ] Les 8 blocs sont présents (SUBJECT/ENVIRONMENT/COMPOSITION/CAMERA/LIGHTING/COLOR/MOOD/TECHNICAL)
- [ ] Couleurs brand mentionnées avec hex codes (#013C87, #1D7742)
- [ ] Espace pour texte spécifié ("negative space in upper third")
- [ ] Style africain contemporain (pas cliché)
- [ ] Paramètres techniques adaptés à l'IA cible (--ar, --style, etc.)
- [ ] Mood aligné avec objectif marketing
- [ ] Pas de demande de texte généré par l'IA
- [ ] Composition référencée (rule of thirds, diagonal, etc.)

---

## 📚 RESSOURCES COMPLÉMENTAIRES

**Références internes :**
- `references/brand-system.md` — palette couleurs exacte
- `references/composition-system.md` — 7 systèmes de composition
- `references/photography-direction.md` — direction photo Afrique Boussole
- `references/creative-strategy.md` — angles créatifs par objectif
- `workflows/prompt-generation-workflow.md` — workflow pas-à-pas

**Outils externes :**
- [Midjourney Prompt Guide](https://docs.midjourney.com/) — paramètres officiels
- [DALL-E Best Practices](https://platform.openai.com/docs/guides/images) — OpenAI docs
- [PromptHero](https://prompthero.com/) — bibliothèque prompts pros
- [Lexica.art](https://lexica.art/) — recherche visuels Stable Diffusion

---

**Version** : 1.0  
**Dernière mise à jour** : Septembre 2026  
**Maintenance** : À mettre à jour lors de nouvelles versions d'IA (Midjourney v7, DALL-E 4, etc.)

---

End of ai-prompt-engineering.md
