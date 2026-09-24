# 🔒 **INTÉGRATION OBLIGATOIRE DES ASSETS - SYSTÈME AUTOMATIQUE**

**IMPORTANCE CRITIQUE** : Chaque création du Skill DOIT utiliser les assets  
**Mise en place** : Septembre 2026  
**Version** : 3.0

---

## ⚠️ **RÈGLE ABSOLUE**

```
🚫 SI UN CRÉATEUR NE CHARGE PAS LES ASSETS → CRÉATION INCOMPLÈTE
✅ CHAQUE CRÉATION DOIT INCLURE OBLIGATOIREMENT LES ASSETS PERTINENTS
```

---

## 📦 **ASSETS DISPONIBLES — GAB SARL / AFRIQUE BOUSSOLE**

> Source de vérité entreprise : `references/gab-sarl-company-profile.md`

### **🔷 LOGOS OFFICIELS** (priorité absolue)
```
📍 Location: assets/brand/logos/
    (OU: public/assets/ dans le projet React)

Versions disponibles :
✅ afrique-boussole-logo.svg        → Logo complet couleur (fond clair)
✅ afrique-boussole-logo-dark.svg   → Logo complet version sombre (fond foncé)
✅ afrique-boussole-emblem.svg      → Emblème seul couleur (pas de texte)
✅ afrique-boussole-emblem-dark.svg → Emblème seul version sombre
✅ logo.png                         → Version PNG polyvalente

Règles d'usage :
→ Fond blanc/clair        : afrique-boussole-logo.svg
→ Fond bleu/sombre        : afrique-boussole-logo-dark.svg
→ Espace restreint        : afrique-boussole-emblem.svg
→ Jamais déformer, colorer autrement ou rogner le logo
```

### **🖼️ VISUELS 3D OFFICIELS** (éléments signature)
```
📍 Location: assets/visuals/

1. gab_3d_compass_africa_*.jpg
   → Boussole 3D holographique Afrique — IMAGE SIGNATURE
   → Utiliser pour: Hero sections, affiches institutionnelles, fond de carte

2. gab_3d_tech_hub_*.jpg
   → Hub technologique 3D — GAB Academy & Pôle IT
   → Utiliser pour: Flyers formation, supports GAB Academy

3. vsl_video_poster_*.jpg
   → Poster de présentation vidéo VSL
   → Utiliser pour: Covers vidéo, miniatures YouTube/LinkedIn

Règles d'usage :
→ Toujours haute résolution (300 DPI pour print)
→ Filtrer si nécessaire : contrast-110 saturate-125
→ Overlay couleur brand autorisé (gradient #013C87/25%)
```

### **🧭 SYSTÈME VISUEL — BOUSSOLE & NAVIGATION**
```
📍 Location: assets/visual-system/compass/
→ Éléments de boussole : rose des vents, aiguilles, cadrans, cercles
→ Utiliser pour: Fonds décoratifs, coins de flyers, éléments graphiques

📍 Location: assets/visual-system/coordinates/
→ Systèmes de coordonnées : crosshair, degrés, marqueurs A/B
→ Utiliser pour: Fonds tech, overlays, visuels Pôle IT & Sécurité

📍 Location: assets/visual-system/grids/
→ Grilles : blueprint, cartesian, dots, hexagonal, isometric
→ Utiliser pour: Fonds Pôle IT, visuels tech, affiches modernes

📍 Location: assets/visual-system/patterns/
→ Patterns : contours Afrique, compass repeat, géométriques, hexagones
→ Utiliser pour: Textures de fond, filigranes, motifs culturels contemporains

📍 Location: assets/visual-system/routes/
→ Routes : lignes courbes, pointillées, réseau de connexions, waypoints
→ Utiliser pour: Visuels connectivité, fibre optique, réseaux, télécoms
```

### **📸 PHOTOS ÉQUIPE** (portraits officiels)
```
📍 Location: assets/visuals/ (OU: src/assets/images/ dans projet React)

team_director_general_*.jpg   → Kouamé Jean-Marc B. — DG & Fondateur
team_tech_director_*.jpg      → Awa Touré-Koné — Directrice Technique
team_academy_director_*.jpg   → Dr. Ibrahim Diarra — Directeur GAB Academy
team_security_lead_*.jpg      → Mamadou Sissoko — Responsable Sécurité

Règles :
→ Utiliser UNIQUEMENT pour supports officiels (plaquettes, LinkedIn, CV entreprise)
→ Toujours avec légende : Nom, Titre, département
→ Ne jamais rogner les visages
```

---

## 🚀 **SYSTÈME AUTOMATIQUE - WHEN SLASH COMMAND TRIGGERED**

### **ÉTAPE 1 : DÉTECTION COMMANDE**

```
User tape: /campagne → KIRO charge slash-commands.md
           /flyer    → KIRO charge slash-commands.md
           /affiche  → KIRO charge slash-commands.md
           /comm     → KIRO charge slash-commands.md
```

### **ÉTAPE 2 : QUESTIONNAIRE + ASSET MATCHING PAR PÔLE GAB SARL**

Après chaque réponse, l'agent détermine automatiquement les assets à utiliser :

```
Si Pôle IT & Réseaux :
  → Logo : afrique-boussole-logo.svg
  → Visual principal : gab_3d_tech_hub_*.jpg
  → Fond : grids/ (blueprint, cartesian, isometric)
  → Overlay : coordinates/ (crosshair, degree-marks)
  → Palette dominante : #013C87 (bleu) sur blanc

Si Pôle Sécurité Électronique :
  → Logo : afrique-boussole-logo.svg (ou dark si fond sombre)
  → Fond : grids/ + coordinates/ (tech, précision)
  → Routes : routes/route-network.svg (connectivité)
  → Palette dominante : #1D7742 (vert) + #013C87 (bleu)
  → Ton : sérieux, protection, fiabilité

Si Pôle Management / Capital Humain :
  → Logo : afrique-boussole-logo.svg
  → Photos équipe si pertinent : team_director_general_*.jpg
  → Fond : pattern-geometric-triangles.svg OU fond uni blanc
  → Palette : #013C87 dominant, sobre, professionnel

Si Pôle Marketing Digital :
  → Logo : afrique-boussole-emblem.svg (plus dynamique)
  → Patterns : pattern-compass-repeat.svg, pattern-africa-outlines.svg
  → Palette : Mix #013C87 + #1D7742, dynamique
  → Format : 1080×1080px (Instagram), 1080×1920px (Story)

Si GAB Academy (Formation) :
  → Logo : afrique-boussole-logo.svg
  → Visual principal : gab_3d_tech_hub_*.jpg (salle formation)
  → Devise obligatoire : « Se former pour mieux Servir »
  → Filière à mettre en valeur (IT / Sécurité / Marketing / Management / Langues)
  → Certifications cibles à mentionner (Cisco, Adobe, PMP, TOEIC…)
  → CTA : S'inscrire | academy@afriqueboussole.ci

Si Institutionnel GAB SARL :
  → Logo : afrique-boussole-logo.svg (version complète obligatoire)
  → Visual signature : gab_3d_compass_africa_*.jpg
  → Les 5 pôles doivent apparaître (ou être mentionnés)
  → Footer COMPLET obligatoire (tel + email + site + adresse)
  → Ton : autorité, sérieux, panafricain

Si Événement / Séminaire :
  → Logo + date + lieu OBLIGATOIRES
  → Boussole compass SVG pour décoration
  → CTA : "S'inscrire" avec lien ou WhatsApp
  → Format selon distribution (A4 print / IG story digital)
```


### **ÉTAPE 3 : BRIEF + ASSETS REFERENCE**

```
SYNTHÈSE FINALE AVEC ASSETS :

📋 BRIEF
   ✓ Objectif
   ✓ Cible
   ✓ Message
   ✓ CTA

📦 ASSETS RECOMMANDÉS
   ✓ Références chargées
   ✓ Éléments d'inspiration
   ✓ Palettes couleur identifiées
   ✓ Typographies détectées

🎨 ANGLES CRÉATIFS (basés sur assets)
   ✓ Angle 1 : Inspiré de [Asset X]
   ✓ Angle 2 : Inspiré de [Asset Y]
   ✓ Angle 3 : Combinaison [X+Z]
```

### **ÉTAPE 4 : GÉNÉRATION + ASSETS INTÉGRÉS**

```
CRÉATION FINALE INCLUANT :

✅ Palette couleur extraite des assets
✅ Typographie analysée des assets
✅ Hiérarchie visuelle d'après assets
✅ CTA style cohérent avec assets
✅ Layout structure d'après assets
✅ Spacing/Padding d'après assets

EXEMPLE :
"J'ai analysé les 4 flyers de référence.
 Tous utilisent:
 - Palettes 2-3 couleurs max
 - Typographie Inter/sans-serif
 - Ratio 60% image, 40% texte
 - CTA bouton 44px+ (mobile-friendly)

Ta création respecte ces normes + ta marque ABC."
```

---

## 📋 **CHECKLIST OBLIGATOIRE PAR COMMANDE**

### **POUR /FLYER** :

- [ ] ✅ Charger 4 références flyers
- [ ] ✅ Analyser hiérarchie visuelle (titre %, image %, texte %)
- [ ] ✅ Extraire palette couleur
- [ ] ✅ Analyser typographie (sizes, weights)
- [ ] ✅ Identifier pattern CTA (bouton? QR? URL?)
- [ ] ✅ Vérifier accessibilité contraste
- [ ] ✅ Inclure dans brief "inspiré par [Asset X]"
- [ ] ✅ Génération respecte ces standards
- [ ] ✅ Proposer variations d'après 2-3 assets

### **POUR /AFFICHE** :

- [ ] ✅ Charger 6 références posters
- [ ] ✅ Vérifier "distance de lecture" (1m vs 5m vs 10m)
- [ ] ✅ Analyser taille texte par distance
- [ ] ✅ Mesurer simplification message (3-7 mots)
- [ ] ✅ Contraste vérifié pour lecture loin
- [ ] ✅ Image/contenu ratio analysé
- [ ] ✅ Identifier "attention stopper" (what stops eyes?)
- [ ] ✅ Génération 60-30-10 ratio exact

### **POUR /COMM** :

- [ ] ✅ Charger 4 références social
- [ ] ✅ Analyser "hook" (première 2 secondes)
- [ ] ✅ Extraire structure narrative (Hook→Solution→CTA)
- [ ] ✅ Vérifier format Instagram (1080x1080 ou 1080x1920)
- [ ] ✅ Typographie lisible micro (14px min)
- [ ] ✅ Couleurs contrastées pour scroll rapide
- [ ] ✅ CTA clair et actionnable
- [ ] ✅ Générer carousel 6-8 slides d'après patterns

### **POUR /CAMPAGNE** :

- [ ] ✅ Charger tous les assets (flyers + posters + social)
- [ ] ✅ Créer variation pour chaque canal
- [ ] ✅ Respecter specs dimensions chaque plateforme
- [ ] ✅ Cohérence visuelle cross-channel
- [ ] ✅ Typographie harmonisée
- [ ] ✅ Palette unique pour toute campagne
- [ ] ✅ 3-5 variations créatives proposées

---

## 🔍 **ANALYSE AUTOMATIQUE DES ASSETS**

Lors du chargement, KIRO extrait:

### **TYPOGRAPHIE DÉTECTÉE**

```
Heading Size Ranges : [32px-72px]
Body Size Ranges : [14px-18px]
Weights Used : [400, 600, 700]
Line Heights : [1.3-1.6]
Letter Spacing : [-0.02em, 0.02em]

→ APPLIQUERA AUX CRÉATIONS UTILISATEUR
```

### **COULEUR PALETTE**

```
Couleur Dominante : [hex, rgb, usage %]
Couleur Secondaire : [hex, rgb, usage %]
Accent Couleur : [hex, rgb, usage %]
Neutre : [hex, rgb, usage %]

Ratio 60-30-10 ? : [Oui/Non]
Contraste WCAG : [AAA/AA/Fail]

→ RECOMMANDRA PALETTE SIMILAIRE
```

### **HIÉRARCHIE VISUELLE**

```
Élément Dominant (60% attention)
Élément Secondaire (25% attention)
Élément Support (10% attention)
Élément Contextuel (5% attention)

→ GÉNÉRATION RESPECTERA CETTE HIÉRARCHIE
```

### **LAYOUT PATTERNS**

```
Image Position : [Top/Left/Center/Bottom]
Text Placement : [Overlay/Beside/Below]
CTA Position : [Bottom/Floating/Separate]
Margin Pattern : [Spacing Values]
Grid System : [Detected or Not]

→ APPLIQUERA PATTERN SIMILAIRE
```

---

## ⚡ **ACTIVATION AUTOMATIQUE**

### **TRIGGER POINTS** :

```
1. User tape /commande
   ↓
2. Kiro charge slash-commands.md + asset-integration-mandatory.md
   ↓
3. Kiro charge dossier assets/ pertinent
   ↓
4. Kiro pose questions questionnaire
   ↓
5. Kiro analyse réponses + charge assets correspondants
   ↓
6. Kiro extrait specs (typo, couleur, hiérarchie)
   ↓
7. Kiro génère avec ces specs
   ↓
8. Kiro valide: "Génération respecte [X] assets"
   ↓
9. Livraison finale avec reference assets
```

---

## 🎯 **EXEMPLE RÉEL: /FLYER DÉCORTIQUÉ**

### **User Input** :
```
/flyer
→ Événement
→ Campus (pressé)
→ Inscription workshop IA
→ S'inscrire maintenant
```

### **KIRO Automatiquement** :

```
🔍 DÉTECTION : Type flyer événement + contexte urgence

📦 CHARGE ASSETS :
   ✓ Church Flyer Design.jfif (hiérarchie)
   ✓ Registration flyer.jfif (CTA inscription)
   ✓ Youth Service Church flyer (énergie)
   ✓ E-FLYER DESIGN (typographie moderne)

📊 EXTRACTION :
   Typographie: Inter Bold 48px headline, Inter Regular 16px body
   Couleurs: 2 principales (bleu + accent)
   Layout: 40% image, 60% texte + CTA
   Hiérarchie: Date → Titre → Description → CTA

✨ GÉNÉRATION :
   - Respecte 40/60 ratio
   - Utilise Inter font (détecté dans assets)
   - Palettes similaires (bleu + accent)
   - CTA "S'inscrire" 44px+ mobile-friendly
   - Temps lecture: 2-5 secondes

✅ LIVRAISON :
   "Généré d'après analyse:
    - Registration flyer.jfif (CTA style)
    - Church Flyer Design.jfif (hiérarchie)
    - E-FLYER DESIGN.jfif (typo)"
```

---

## 🛡️ **SÉCURITÉ : FORCER L'UTILISATION**

### **Check automatique post-génération** :

```python
if NOT all([
    typography_from_assets,
    color_palette_from_assets,
    hierarchy_from_assets,
    cta_style_from_assets
]):
    → RÉGÉNÉRER avec assets
    → Afficher warning "Assets non respectés"
    → Forcer reload
```

### **Validation avant livraison** :

```
✓ Typographie respecte assets ?
✓ Couleurs respectent palette ?
✓ Hiérarchie suit 60-30-10 rule ?
✓ CTA similar à assets ?
✓ Format dimensions correct ?
✓ Accessibilité WCAG AA+ ?

Si Non → RÉGÉNÉRER automatiquement
Si Oui → LIVRER avec credit assets
```

---

## 📢 **COMMUNICATION AUTOMATIQUE**

À chaque création, ajouter:

```
✨ CRÉÉ D'APRÈS ASSETS PROFESSIONNELS

Cette création s'inspire des meilleures 
pratiques de :
- [Asset X] pour structure
- [Asset Y] pour typographie
- [Asset Z] pour palette couleur

Résultat: qualité agence pro 🎨
```

---

## 🚀 **IMPLÉMENTATION**

### **FAIT** :
- ✅ 25 images d'assets collectées
- ✅ Organisées par catégorie (flyers/posters/social/templates)
- ✅ Typographie système créé (headlines, body, CTA)
- ✅ Ce document d'intégration obligatoire

### **À VÉRIFIER** :
- KIRO charge automatiquement ce fichier au démarrage
- Questionnaire intègre questions + asset-loading
- Génération utilise assets en entrée
- Output mentionne assets utilisés

---

**CRITICAL** : Ce système assure qualité professionnelle  
**OBLIGATION** : Chaque création utilise les assets  
**RÉSULTAT** : Visuels cohérents + pro dès le départ

---

**Version** : 3.0 (Septembre 2026)  
**Priorité** : 🔴 CRITIQUE - Applique avant toute génération
