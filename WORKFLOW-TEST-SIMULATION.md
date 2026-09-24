# 🧪 WORKFLOW TEST SIMULATION - SLASH COMMANDS

**Dernière mise à jour** : Septembre 2026

**But** : Démontrer le flow complet d'une slash command avec asset loading obligatoire.

---

## 📋 TEST SCENARIO 1: `/flyer` COMMAND

### **USER INPUT**
```
/flyer
```

### **ÉTAPE 0: ASSET LOADING** (Automatique, invisible à l'utilisateur)

**Agent Actions** :
1. ✅ Charger `workflows/asset-integration-mandatory.md`
   - Parse le fichier
   - Extrait palette : #013C87 (blue), #1D7742 (green), #FFFFFF, #000000
   - Extrait hiérarchie typo : H1 72px Bold, H2 40px SemiBold, Body 18px Regular, CTA 16px SemiBold
   - Note patterns de CTA placement observés

2. ✅ Charger `references/typography-system-pro.md`
   - Confirme specs: Inter font, line-heights, accessibility
   - Mémorise: H1 72px, H2 40px, Body 18px, CTA 16px (web)

3. ✅ Consulter `assets/references/flyers/` (4 designs)
   - Church Flyer: Observe composition, CTA style, hierarchy
   - E-FLYER: Note layout, hierarchy pattern
   - Registration: Observe field layout, CTA placement
   - Youth Service: Note hierarchy, visual balance

4. ✅ Vérifier disponibilité: logos, compass, africa-map

**Agent → User** (visible message):
```
✅ ASSETS LOADED FOR /FLYER

Palette extraite:
🔵 Brand Blue: #013C87
🟢 Brand Green: #1D7742
⚪ White/Black: #FFFFFF / #000000

Typography system active:
📋 H1: 72px Bold (web)
📋 H2: 40px SemiBold
📋 Body: 18px Regular
📋 CTA: 16px SemiBold

References loaded:
📁 4 flyer designs analyzed
🎨 Palette patterns identified
📐 Composition systems understood

READY → Passons au questionnaire !
```

---

### **ÉTAPE 1-7: QUESTIONNAIRE UTILISATEUR**

**Agent → User** :
```
❓ QUESTIONNAIRE FLYER - Question 1/7

📋 Quel TYPE de flyer souhaitez-vous créer ?

a) 🎉 Événement (conférence, workshop, webinaire)
b) 🎓 Formation / Programme éducatif
c) 🛍️ Produit / Service commercial
d) 🤝 Recrutement / Offre d'emploi
e) 📢 Annonce / Communication générale
f) 🎁 Promotion / Offre spéciale

→ Tape 'a', 'b', 'c', 'd', 'e', ou 'f'
```

**User Answer** : `a) Événement`

**Agent → User** :
```
✅ Réponse enregistrée : Événement

❓ Question 2/7 - RÈGLE DES 2 SECONDES ⏱️

Si quelqu'un voit votre flyer 2 secondes, il doit comprendre :

**QUOI** : Quel est l'événement ?
→ Réponse en 3-5 mots max

**OÙ** : Lieu ou plateforme ?
→ Réponse précise

**QUAND** : Date et heure ?
→ Format : JJ/MM/YYYY à HH:MM

→ Donne-moi ces 3 infos essentielles
```

**User Answer** :
```
QUOI : Webinaire "Développer une startup tech"
OÙ : En ligne (Zoom)
QUAND : 15/10/2026 à 18:00
```

**Agent → User** :
```
✅ 2-second rule captured

❓ Question 3/7 - PUBLIC CIBLE 👥

Qui va lire ce flyer ?

- Où le verront-ils ? (email, social, affichage, etc.)
- Profil ? (étudiants, entrepreneurs, professionnels)
- Niveau ? (débutants, intermédiaires, experts)
- Pain point ? (problème qu'ils ont)

→ Décris ton audience idéale
```

**User Answer** :
```
Entrepreneurs africains 25-40 ans en zone francophone
Verront le flyer sur LinkedIn et par email
Cherchent à lancer une startup tech mais manquent de roadmap
Niveau : Débutants à intermédiaires
```

**Agent → User** :
```
✅ Audience profiled

❓ Question 4/7 - MESSAGE PRINCIPAL 💬

Quel est le BÉNÉFICE principal ? (en 1 phrase, max 15 mots)

Structure : Verbe d'action + Résultat

Exemples :
✅ "Décrochez votre premier job tech en 3 mois"
✅ "Maîtrisez Python sans prérequis mathématiques"

→ Ton message bénéfice ?
```

**User Answer** :
```
"Transformez votre idée en startup tech viable en 8 semaines"
```

**Agent → User** :
```
✅ Message principal capturé

❓ Question 5/7 - CALL-TO-ACTION 📲

Quelle est l'action la PLUS FACILE à faire maintenant ?

Hiérarchie de friction :
1. 📱 Scanner QR code (easiest)
2. 📧 Envoyer un email
3. 🌐 Visiter une URL
4. 📞 Appeler
5. 📝 Remplir un formulaire long

→ Quelle action préfères-tu ?
```

**User Answer** : `Scanner QR code`

**Agent → User** :
```
✅ CTA sélectionné : QR code

❓ Question 6/7 - PREUVES / CRÉDIBILITÉ ✅

Avez-vous des éléments de crédibilité ?

Exemples :
- 📊 Chiffres (X participants passés, X% réussite)
- 🏆 Certifications / Partenariats
- 💬 Témoignage d'ancien participant
- 🎓 Expert / Expertise de l'équipe

(OPTIONNEL - peut être vide)

→ Quels éléments crédibilité veux-tu afficher ?
```

**User Answer** :
```
"100+ startups lancées avec notre accompagnement"
"Partenariat avec TechHub Afrique"
```

**Agent → User** :
```
✅ Preuves sociales : 2 éléments

❓ Question 7/7 - FORMAT & DISTRIBUTION 📐

Format d'impression/distribution ?

PRINT :
- A5 (148 x 210 mm)
- A4 (210 x 297 mm)

DIGITAL :
- 1080 x 1920 px (Story)
- 1080 x 1080 px (Post carré)
- 1200 x 630 px (Link preview)

→ Quel format ?
```

**User Answer** : `A4 + 1080x1080px version`

---

### **ÉTAPE 8: BRIEF SYNTHESIS & VALIDATION**

**Agent → User** :
```
✅ QUESTIONNAIRE COMPLET

Voici ton BRIEF RÉSUMÉ :

🎯 TYPE : Événement webinaire
📅 EVENT : "Développer une startup tech" - 15/10/2026 18:00 (Zoom)
👥 AUDIENCE : Entrepreneurs 25-40 ans, zone FR, débutants/intermediate
💬 KEY MESSAGE : "Transformez votre idée en startup tech viable en 8 semaines"
📲 CTA : QR code → landing page inscription
✨ CREDIBILITY : 100+ startups lancées + TechHub Afrique partnership
📐 FORMATS : A4 print + 1080x1080px digital

⚠️ NOTE IMPORTANTE :
Les assets suivants seront utilisés OBLIGATOIREMENT :
✓ Brand colors (#013C87, #1D7742)
✓ Inter typography (H1 72px, H2 40px, Body 18px, CTA 16px)
✓ Logo Afrique Boussole (corner, 8% height)
✓ Patterns extraits des 4 designs flyer référence
✓ Palette composée extraite

→ Tout bon ? Confirme pour générer ! (oui/non)
```

**User Answer** : `Oui, parfait !`

---

### **ÉTAPE 9: CREATIVE GENERATION**

**Agent Actions** (hidden) :
1. **Charge contexte** :
   - Typography specs: H1 72px Bold, H2 40px, Body 18px
   - Colors: Blue #013C87, Green #1D7742
   - Logo path: `/assets/brand/logos/afrique-boussole-logo.svg`
   - Reference designs analyzed

2. **Crée la hiérarchie** :
   - LEVEL 1 (HOOK): "Transformez votre idée en startup viable" (72px, Bold, #013C87)
   - LEVEL 2 (EVENT): "Webinaire 15 octobre • 18h • Zoom" (32px, SemiBold, #000000)
   - LEVEL 3 (VALUE): "En 8 semaines, obtenez la feuille de route, le pitch deck, et les premières levées" (18px, Regular)
   - LEVEL 4 (PROOF): "100+ startups lancées • Partenaire TechHub Afrique" (14px, Regular, #666)
   - LEVEL 5 (CTA): [QR CODE] "S'inscrire maintenant" (16px, SemiBold, #1D7742 button)

3. **Génère visuels** :
   - Background: Compass motif (subtle, 20% opacity)
   - Main image: Entrepreneur sketch or photo (brand-aligned)
   - Color blocks: Blue and green accents
   - All text: Inter font, correct sizing

4. **Formats créés** :
   - A4 PDF (210x297mm, 300dpi)
   - Instagram 1:1 PNG (1080x1080px, 72dpi)

**Agent → User** :
```
🎨 CRÉATION GÉNÉRÉE

J'ai créé ton flyer en utilisant :
✅ Brand colors (#013C87 primary, #1D7742 CTA)
✅ Inter typography (hierarchy respected)
✅ Compass visual element (brand system)
✅ Logo Afrique Boussole (bottom-right, 8%)
✅ Patterns from 4 reference flyers

FORMATS LIVRÉS :
📄 A4 Print PDF (300dpi) - "flyer-webinar-startup_A4_final.pdf"
📱 Instagram 1:1 PNG (1080x1080) - "flyer-webinar-startup_INSTA_1x1.png"

VALIDATION CHECKLIST COMPLÉTÉE :
✓ Brand compliance (colors, logo, fonts)
✓ Message clarity (readable in 2 seconds)
✓ Hierarchy visual (Hook → Message → Value → Proof → CTA)
✓ Image quality (professional)
✓ No typos/errors
✓ Contrast WCAG AA ✓
✓ Assets used (mandatory)

→ Quels ajustements souhaites-tu ? (couleurs, texte, layout, etc.)
```

---

### **ÉTAPE 10: ITERATION (OPTIONAL)**

**User Request** : "Peut-on rendre le CTA plus visible ? Et ajouter 'GRATUIT' ?"

**Agent Actions** :
1. Augmente CTA button size de 16px → 18px SemiBold
2. Ajoute "GRATUIT" en orange badge à côté du QR
3. Augmente contraste CTA button

**Agent → User** :
```
✅ RÉVISION V2 GÉNÉRÉE

Changements :
✓ CTA button agrandie (18px SemiBold)
✓ "GRATUIT" badge orange ajouté
✓ Contraste CTA amélioré

Fichiers UPDATED :
📄 flyer-webinar-startup_A4_v2_final.pdf
📱 flyer-webinar-startup_INSTA_1x1_v2.png

→ Autres modifications ? Ou on valide cette version ?
```

**User** : `Parfait ! C'est bon.`

**Agent → User** :
```
🎉 FLYER VALIDÉ & PRÊT

Fichiers finaux prêts à télécharger :
📄 flyer-webinar-startup_A4_v2_final.pdf
📱 flyer-webinar-startup_INSTA_1x1_v2.png

📊 RAPPORT FINAL :
✅ Format : A4 (210x297mm) + Instagram 1:1
✅ Resolution : 300dpi (print), 72dpi (digital)
✅ Colors : #013C87 blue, #1D7742 green, white
✅ Typography : Inter (H1 72px, H2 32px, Body 18px, CTA 18px)
✅ Assets used : Logo, compass, brand palette ✓
✅ Validation : 100% checklist passed ✓

Prochaines étapes :
→ Imprimer A4 ou publier Instagram 1:1
→ QR code active avant 15/10/2026
→ Email campaign recommandée 2 semaines avant

Besoin d'autre chose ?
```

---

## 📋 TEST SCENARIO 2: `/campagne` COMMAND

**USER INPUT** : `/campagne`

### **ÉTAPE 0: ASSET LOADING**

**Agent Actions** (same as above, but loads ALL assets):
1. ✅ `asset-integration-mandatory.md`
2. ✅ `typography-system-pro.md`
3. ✅ `assets/references/flyers/` (4 designs)
4. ✅ `assets/references/posters/` (6 designs)
5. ✅ `assets/references/social/` (4 designs)
6. ✅ `assets/templates/` (3 templates)
7. ✅ Logos, compass, africa-map

**Agent → User** :
```
✅ ASSETS LOADED FOR /CAMPAGNE

Full campaign asset library loaded :
📁 Flyers : 4 designs analyzed
📁 Posters : 6 designs analyzed
📁 Social : 4 designs analyzed
📁 Templates : 3 designs analyzed
🎨 Visual system : Compass, maps, patterns
📖 Typography : Complete hierarchy system
🎯 Brand palette : Colors, logos, elements

READY → Créons une campagne multi-canal !
```

### **QUESTIONNAIRE: 8 QUESTIONS** (Same as `/campagne` in slash-commands.md)

[Similar structure to flyer test, but 8 questions instead of 7]

### **OUTPUT: CAMPAIGN WITH 4 VARIATIONS × 7 FORMATS**

```
🎨 CAMPAGNE MULTI-CANAL GÉNÉRÉE

4 CONCEPTS CRÉATIFS :
1️⃣ Variation AUTHORITY (Expert credentials)
2️⃣ Variation OPPORTUNITY (Growth potential)
3️⃣ Variation HUMAN IMPACT (Success story)
4️⃣ Variation NAVIGATION (Clear pathway)

7 FORMATS GÉNÉRÉS :
Flyer A4 + Poster A3 + Social 1:1 + Social 4:5 + Social 9:16 + 
Email 600x800 + Web banner 1200x628

TOTAL LIVRABLES : 28 fichiers
(4 concepts × 7 formats)

✅ Tous les assets utilisés obligatoirement
✅ Palette cohérente dans tous les formats
✅ Hierarchy maintenue à travers variations
✅ Checklist validation 100%
```

---

## ✅ VALIDATION CHECKPOINT

**Before any creative is delivered :**

File : `references/validation-checklist.md` is ALWAYS checked :

```
✅ ÉTAPE 1: CONFORMITÉ MARQUE
- Colors exact ? (#013C87, #1D7742)
- Typography Inter ? (H1/H2/Body/CTA sizes)
- Logo correct ? (position, size, version)

✅ ÉTAPE 2: HIÉRARCHIE & COMPOSITION
- Lisible en 2 sec ? (message clair)
- Point focal évident ? (un seul)
- Hierarchy visuelle claire ? (pri/sec/support)

✅ ÉTAPE 3: IMAGES
- Résolution appropriée ? (300dpi print, 72 digital)
- Qualité professionnelle ? (pas clichés)
- Cohérence visuelle ? (palette compatible)

✅ ÉTAPE 4: CONTENU
- Pas erreurs typo ? (français correct)
- Pas faux chiffres ? (vérifiés)
- CTA clair ? (spécifique, pas "clique ici")

✅ ÉTAPE 5-10: CTA, FORMAT, ACCESSIBILITY, ASSETS, ANTI-PATTERNS, APPROVAL

[TOTAL : 50+ checks]

🎉 IF ALL GREEN → READY TO DELIVER
```

---

## 🔄 FLOW SUMMARY

```
User → /command
         ↓
Agent → ÉTAPE 0: Load all assets (invisible)
         ↓
Agent → Announce "Assets loaded"
         ↓
Agent → QUESTIONS 1-7 (or 1-8 for /campagne)
         ↓
User → Answers all questions
         ↓
Agent → VALIDATION: Show brief + confirm
         ↓
User → Confirms brief
         ↓
Agent → GENERATION: Create visuals using assets
         ↓
Agent → VALIDATION: Run 50+ checklist checks
         ↓
Agent → DELIVER: Show files + offer iterations
         ↓
[Optional] User → Request changes
           Agent → Update & revalidate
         ↓
END → Final files ready to download
```

---

## 📊 KEY METRICS

| Aspect | Target | Result |
|--------|--------|--------|
| **Assets Loaded** | All mandatory | ✅ 100% |
| **Questions Asked** | 7-8 per command | ✅ Complete |
| **Brand Compliance** | 100% | ✅ #013C87, #1D7742, Inter |
| **Typography Accuracy** | Exact specs | ✅ H1/H2/Body/CTA matched |
| **Validation Checks** | 50+ items | ✅ All passed |
| **Formats Delivered** | Multiple per creative | ✅ Print + Digital |
| **Iteration Rounds** | 2-3 max | ✅ Quick turnaround |

---

**This simulation shows the complete workflow for slash commands with mandatory asset loading, questionnaire-driven generation, and comprehensive validation.**

End of WORKFLOW-TEST-SIMULATION.md
