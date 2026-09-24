# 🚀 **INITIALISATION DU SKILL - ASSETS OBLIGATOIRES**

**À charger AVANT TOUTE UTILISATION**

---

## 📋 **SÉQUENCE DE CHARGEMENT AUTOMATIQUE**

```
┌─────────────────────────────────────────┐
│ 1️⃣  SKILL DÉCLENCHÉ (Utilisateur)     │
│     User: /campagne, /flyer, etc.      │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 2️⃣  CHARGER PRIORITÉ CRITIQUE:        │
│     - SKILL.md (orchestrateur)         │
│     - slash-commands.md (questions)    │
│     - asset-integration-mandatory.md   │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 3️⃣  CHARGER ASSETS PERTINENTS:        │
│     - references/flyers/ (4 min)       │
│     - references/posters/ (6 min)      │
│     - references/social/ (4 min)       │
│     - references/typography-*.md       │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 4️⃣  POSER QUESTIONNAIRE:              │
│     - 7-8 questions ciblées             │
│     - Valider réponses                  │
│     - Synthétiser brief                 │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 5️⃣  ANALYSER ASSETS:                  │
│     - Extraire typographie             │
│     - Extraire palette couleur         │
│     - Analyser hiérarchie              │
│     - Identifier patterns              │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 6️⃣  GÉNÉRER AVEC ASSETS:              │
│     - Appliquer typographie            │
│     - Respecter palette                │
│     - Utiliser hiérarchie              │
│     - Matcher patterns                 │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 7️⃣  VALIDER QUALITÉ:                  │
│     - Vérifier conformité assets       │
│     - Vérifier accessibilité           │
│     - Vérifier dimensions              │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 8️⃣  LIVRER + RÉFÉRENCER:              │
│     "Inspiré par [Assets X,Y,Z]"       │
│     Fichiers export: PNG, JPG, PDF     │
└─────────────────────────────────────────┘
```

---

## 📂 **STRUCTURE ASSETS REQUIS**

**Avant chaque utilisation, vérifier**:

```
assets/
├── references/
│   ├── flyers/ ............................ [4+ fichiers]
│   │   ├── Church Flyer Design.jfif
│   │   ├── E-FLYER DESIGN.jfif
│   │   ├── Registration flyer.jfif
│   │   └── Youth Service Church flyer.jfif
│   │
│   ├── posters/ ........................... [6+ fichiers]
│   │   ├── batch poster.jfif
│   │   ├── Church poster.jfif
│   │   ├── Poster Design (1).jfif
│   │   ├── SUNDAY SERVICE.jfif
│   │   ├── TEDx Landmark Design.jfif
│   │   └── Thank you poster.jfif
│   │
│   ├── social/ ........................... [4+ fichiers]
│   │   ├── Church Social Media design.jfif
│   │   ├── Pr Social Ad Essence.jfif
│   │   ├── ⏳ 10 Days to Go.jfif
│   │   └── Contabilidade Social.jfif
│   │
│   └── typography-system-pro.md ......... [REQUIS ✅]
│
├── templates/ ........................... [3+ fichiers]
│   ├── Company Policy Layout.jfif
│   ├── Recruitment & Consulting.jfif
│   └── Diseño Presentación.jfif
│
├── brand/logos/ ........................ [7 fichiers ✅]
├── team/ ............................... [5 fichiers ✅]
├── visuals/ ............................ [4 fichiers ✅]
├── projects/ ........................... [2 fichiers ✅]
└── visual-system/ ...................... [4+ subdirs ✅]
```

**STATUS** :
- ✅ FLYERS : 4 fichiers présents
- ✅ POSTERS : 6 fichiers présents
- ✅ SOCIAL : 4 fichiers présents
- ✅ TEMPLATES : 3 fichiers présents
- ✅ TYPOGRAPHIE : typography-system-pro.md
- ✅ TOTAL : 22+ assets de référence

---

## 🎯 **RÈGLES D'UTILISATION OBLIGATOIRES**

### **RÈGLE 1 : CHARGER LES ASSETS TOUJOURS**

```
❌ JAMAIS :
"L'utilisateur tape /flyer → je pose questions → je génère"

✅ TOUJOURS :
"L'utilisateur tape /flyer → je charge slash-commands.md 
  + asset-integration-mandatory.md + assets/references/flyers/
  → je pose questions → j'analyse assets → je génère"
```

### **RÈGLE 2 : ANALYSER AVANT GÉNÉRER**

```
Pour chaque création, extraire des assets:

✓ Typographie : sizes, weights, hierarchy
✓ Couleurs : palette, ratios, contraste
✓ Layout : hierarchy, spacing, positions
✓ CTA : style, placement, format
✓ Images : ratio, position, style

PUIS appliquer à la génération
```

### **RÈGLE 3 : MENTIONNER LES ASSETS**

```
Chaque livraison doit inclure:

"✨ Cette création s'inspire des meilleures 
   pratiques de:
   - Registration flyer.jfif (CTA placement)
   - E-FLYER DESIGN.jfif (typographie)
   - palette analysée depuis [Asset X]"
```

### **RÈGLE 4 : VALIDÉ AVANT LIVRAISON**

```
Checklist finale:

□ Typographie respecte assets ?
□ Couleurs respectent palette ?
□ Hiérarchie suit patterns assets ?
□ CTA style cohérent ?
□ Accessibilité WCAG AA+ ?
□ Dimensions correctes ?

SI OUI → Livrer
SI NON → Régénérer
```

---

## 🔄 **DÉTERMINATION AUTOMATIQUE DES ASSETS**

### **Basé sur réponses utilisateur**:

```
User répond /flyer:
↓
Q1: Type = Événement
  → Charger: registration flyer.jfif (priorité haute)
  → Charger: Church Flyer Design.jfif

Q2: Cible = Campus (pressé)
  → Charger: E-FLYER DESIGN.jfif (lisible rapide)
  → Charger: Youth Service (engagement)

Q3: Message = [Description]
  → Analyser: comment autres assets font passer messages?
  → Taille headline? Placement? Simplification?

Q4: CTA = S'inscrire
  → Vérifier: comment assets plaçent CTA?
  → Registration flyer.jfif = CTA placement modèle
  → Church Flyer = CTA style modèle

Q5-7: Autres
  → Cross-référencer tous les assets
  → Créer hybrid inspiré de meilleurs éléments

RÉSULTAT:
→ Brief synthétisé
→ Assets chargés en mémoire
→ Specs typographiques extraites
→ Palette couleur déterminée
→ Ready to generate
```

---

## 💾 **FICHIERS À CHARGER SYSTÉMATIQUEMENT**

### **TIER 1 - ABSOLUMENT PRIORITAIRE** (charger TOUJOURS):

```
✅ workflows/slash-commands.md
✅ workflows/asset-integration-mandatory.md
✅ references/typography-system-pro.md
✅ references/brand-system.md
```

### **TIER 2 - SELON COMMANDE** :

```
Si /flyer → assets/references/flyers/ (4 fichiers)
Si /affiche → assets/references/posters/ (6 fichiers)
Si /comm → assets/references/social/ (4 fichiers)
Si /campagne → Tout ce qui précède
```

### **TIER 3 - CONTEXTE ENRICHI** :

```
Si questions comportent "type" → assets/templates/
Si questions comportent "cible" → analyser social/team/visuals
Si questions comportent "marque" → assets/brand/logos/
```

---

## 🎨 **EXTRACTION TYPOGRAPHIQUE AUTOMATIQUE**

**Format attendu pour chaque asset chargé** :

```
FICHIER: Registration flyer.jfif
─────────────────────────────────

📏 TYPOGRAPHIE DÉTECTÉE:
   Headline: ~56-72px, Inter Bold, #013C87
   Subhead: ~32px, Inter SemiBold, #1D7742
   Body: ~16px, Inter Regular, #2C3E50
   CTA Button: ~16px, Inter SemiBold, white text on #013C87

🎨 PALETTE DÉTECTÉE:
   Dominant: #013C87 (70% espace)
   Secondary: #1D7742 (20% espace)
   Accent: #FFFFFF (10% espace)
   Contraste: ✓ AAA (7.2:1)

📐 HIÉRARCHIE:
   CTA Position: Bottom, Floating
   Image Ratio: 40% top
   Text Block: 60% layout
   Spacing: 24px gutters

→ APPLIQUER CES SPECS À GÉNÉRATION
```

---

## ✅ **CHECKLIST PRE-GÉNÉRATION**

**Avant de générer TOUT créatif, cocher**:

```
ASSETS CHARGÉS ?
☐ Dossier assets/ accessible
☐ Sous-dossiers chargés (flyers/posters/social/templates)
☐ Typographie doc chargé
☐ Specs extraites des assets

QUESTIONS POSÉES ?
☐ Q1-Q7 questionnaire complétées
☐ Réponses validées utilisateur
☐ Brief synthétisé

ASSETS ANALYSÉS ?
☐ Typographie extraite
☐ Palette analysée
☐ Hiérarchie identifiée
☐ Patterns détectés

GÉNÉRATION PRÊTE ?
☐ Specs typographiques appliquées
☐ Couleurs respectent palette
☐ Hiérarchie suit patterns
☐ CTA cohérent
☐ Accessibilité vérifiée
☐ Dimensions correctes

☐ GÉNÉRER
☐ VALIDER
☐ LIVRER avec références assets
```

---

## 🚫 **ERREURS À ÉVITER ABSOLUMENT**

```
❌ NE PAS faire:
   - Générer sans charger slash-commands.md
   - Générer sans analyser assets
   - Oublier d'extraire typographie
   - Ignorer palette couleur extraite
   - Oublier d'appliquer hiérarchie
   - Livrer sans mentionner assets

✅ TOUJOURS faire:
   - Charger assets AVANT questions
   - Analyser AVANT générer
   - Mentionner assets dans output
   - Valider conformité assets
   - Créditer design patterns utilisés
```

---

## 📞 **DEBUG EN CAS DE PROBLÈME**

```
Si génération n'utilise pas assets :
→ Relancer avec:
   "Régénère en forçant assets: [asset names]"
   "Utilise typographie de [asset X]"
   "Applique palette de [asset Y]"

Si assets mal détectés :
→ Relancer avec:
   "Analyse typography-system-pro.md"
   "Applique Inter Bold 48px headlines"
   "Utilise palette #013C87 + #1D7742"

Si qualité insuffisante :
→ Relancer avec:
   "Génère d'après Registration flyer.jfif"
   "Copie hiérarchie de E-FLYER DESIGN.jfif"
   "Utilise CTA style de Church Flyer Design.jfif"
```

---

## 🎯 **RÉSULTAT ATTENDU**

**Chaque création générée DOIT avoir** :

```
✅ Typographie cohérente avec assets
✅ Palette couleur respectée (60-30-10)
✅ Hiérarchie visuelle suivie
✅ CTA placement/style conforme
✅ Accessibilité WCAG AA+
✅ Dimensions correctes
✅ Reference assets mentionnée

QUALITÉ = Niveau agence créative pro 🎨
```

---

**CRITICALITÉ** : 🔴 **MUST IMPLEMENT**  
**VERSION** : 1.0 (Septembre 2026)  
**VALIDATION** : Avant chaque génération
