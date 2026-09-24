# 📚 SKILL INDEX - AFRIQUE BOUSSOLE CREATIVES

**Version** : 1.1  
**Date** : Septembre 2026  
**Status** : ✅ PRODUCTION-READY

---

## 🚀 DÉMARRAGE RAPIDE

### Commandes disponibles :

| Commande | Objectif | Questions | Livrable |
|----------|----------|-----------|----------|
| `/campagne` | Campagne multi-canal complète | 8 | 28 fichiers (4 concepts × 7 formats) |
| `/flyer` | Flyer print ou digital | 7 | A4 + formats digitaux |
| `/affiche` | Affiche événementielle | 7 | A3+ print + digital |
| `/comm` | Contenu social / storytelling | 7 | Carrousel + posts |
| `/prompt` | Prompt IA optimisé (NEW) | 6 | 3 prompts (conservative/creative/bold) |

---

## 📁 FICHIERS ESSENTIELS (LIRE EN PREMIER)

| Priorité | Fichier | Description |
|----------|---------|-------------|
| 🔴 CRITIQUE | `SKILL.md` | Orchestrateur principal — point d'entrée |
| 🔴 CRITIQUE | `workflows/slash-commands.md` | Questionnaires complets pour 5 commandes |
| 🔴 CRITIQUE | `workflows/asset-integration-mandatory.md` | Charge TOUS les assets avant génération |
| 🔴 CRITIQUE | `references/ai-prompt-engineering.md` | Système prompt IA (8 blocs, templates) (NEW) |
| 🟠 IMPORTANT | `workflows/prompt-generation-workflow.md` | Workflow 12 étapes génération prompts (NEW) |
| 🟠 IMPORTANT | `references/typography-system-pro.md` | Hiérarchie typo Inter complète |
| 🟠 IMPORTANT | `references/validation-checklist.md` | 50+ checks avant livraison |
| 🟡 UTILE | `QUICK-START.md` | Guide utilisateur simplifié |
| 🟡 UTILE | `WORKFLOW-TEST-SIMULATION.md` | Simulation complète /flyer |

---

## 🔁 FLUX D'EXÉCUTION (OBLIGATOIRE)

```
/command tapé
    ↓
ÉTAPE 0: Charger asset-integration-mandatory.md
         + typography-system-pro.md
         + brand-system.md
         + dossier assets/references/<type>/
    ↓
ÉTAPE 0.5 (optional): Générer prompt IA pour image (NEW)
    ↓
Annoncer: "✅ Assets chargés"
    ↓
Poser les 7-8 questions du questionnaire
    ↓
Résumer le brief, demander confirmation
    ↓
Générer avec assets obligatoirement
    ↓
Valider via validation-checklist.md (50+ checks)
    ↓
Livrer les fichiers
```

---

## 📂 STRUCTURE COMPLÈTE DU SKILL

```
afrique-boussole-creatives/
│
├── 🔴 SKILL.md                         ← LIRE EN PREMIER
├── 📋 SKILL-INDEX.md                   ← CE FICHIER (updated)
├── 📖 README.md                        ← Vue d'ensemble
├── 🚀 QUICK-START.md                   ← Démarrage rapide
├── 🧪 WORKFLOW-TEST-SIMULATION.md      ← Simulation /flyer
├── ✅ IMPLEMENTATION-STATUS.md         ← Bilan complet
├── ⚙️ SKILL-INITIALIZATION.md          ← Séquence de chargement
│
├── workflows/                          ← PROCESSUS & COMMANDES
│   ├── 🔴 slash-commands.md            ← Questionnaires + ÉTAPE 0 + /prompt (NEW)
│   ├── 🔴 asset-integration-mandatory.md ← Chargement assets forcé
│   ├── 🔴 prompt-generation-workflow.md ← Génération prompts IA (NEW)
│   ├── flyer-workflow.md               ← 10 étapes flyer
│   ├── poster-workflow.md              ← 11 étapes poster
│   ├── ad-workflow.md                  ← 11 étapes pub
│   ├── social-workflow.md              ← 12 étapes social
│   ├── campaign-workflow.md            ← 14 étapes campagne
│   └── adaptation-workflow.md         ← 12 étapes adaptation
│
├── references/                         ← GUIDES DÉTAILLÉS
│   ├── 🔴 ai-prompt-engineering.md     ← Système prompts IA (8 blocs) (NEW)
│   ├── 🔴 typography-system-pro.md     ← Système typo Inter professionnel
│   ├── 🔴 validation-checklist.md      ← 50+ checks avant livraison
│   ├── brand-system.md                 ← Couleurs, fonts, identité
│   ├── creative-strategy.md            ← 6 angles créatifs
│   ├── creative-framework.md           ← Pyramide hiérarchie
│   ├── composition-system.md           ← 7 systèmes de composition
│   ├── typography-system.md            ← Système typo standard
│   ├── photography-direction.md        ← Direction photo
│   ├── image-generation.md             ← Génération IA images
│   ├── campaign-formats.md             ← Formats & dimensions
│   ├── platform-guidelines.md          ← Règles par plateforme
│   ├── quality-control.md              ← QA framework
│   ├── anti-patterns.md                ← 30 erreurs à éviter
│   ├── logo-usage.md                   ← Règles logo
│   └── design-system.md               ← Tokens, composants
│
├── assets/                             ← 76 ASSETS ORGANISÉS (était 39, +37 NEW)
│   ├── brand/
│   │   ├── logos/     (7 fichiers : full, mark, dark, light)
│   │   ├── icons/     (1 fichier)
│   │   └── symbols/   (8 fichiers SVG : compass, arrow, pin, cross, needle, waypoint, route-line, coordinate) (NEW)
│   ├── team/          (5 photos équipe)
│   ├── projects/      (2 visuels projets)
│   ├── visual-system/
│   │   ├── compass/   (2 références boussole)
│   │   ├── africa-map/ (2 cartes : vector + isometric 3D)
│   │   ├── routes/    (7 fichiers SVG : curved, dotted, network, waypoints, etc.) (NEW)
│   │   ├── grids/     (7 fichiers SVG : isometric, hexagonal, cartesian, blueprint) (NEW)
│   │   ├── coordinates/ (7 fichiers SVG : crosshair, markers A/B, compass-rose, degree-marks) (NEW)
│   │   └── patterns/  (7 fichiers SVG : compass-repeat, triangles, hexagons, waves, etc.) (NEW)
│   ├── references/
│   │   ├── flyers/    (4 designs référence)
│   │   ├── posters/   (6 designs référence)
│   │   ├── social/    (4 designs référence)
│   │   ├── corporate/ (3 designs référence)
│   │   └── advertisements/ (5 designs référence)
│   └── templates/     (3 templates)
│
├── schemas/            ← STRUCTURES JSON
│   ├── creative-brief.schema.json
│   ├── campaign.schema.json
│   └── creative-output.schema.json
│
├── scripts/            ← OUTILS VALIDATION
│   ├── validate-brand.py
│   ├── validate-creative.py
│   └── generate-brief.py
│
└── examples/           ← CAS CONCRETS
    ├── flyer-example.md
    ├── poster-example.md
    └── campaign-example.md
```

---

## 📐 TYPOGRAPHIE (TOUJOURS INTER)

| Élément | Web | Print | Poids |
|---------|-----|-------|-------|
| H1 Titre | 48–72px | 96–144pt | Bold / Black |
| H2 Sous-titre | 32–40px | 48–64pt | SemiBold |
| Body | 16–18px | 20–24pt | Regular |
| CTA | 14–16px | 18–20pt | SemiBold |
| Caption | 12px | 14–16pt | Regular |

---

## � COULEURS BRAND (JAMAIS SUBSTITUÉES)

| Couleur | Hex | Usage |
|---------|-----|-------|
| Brand Blue | `#013C87` | Éléments primaires, logo, fond |
| Brand Green | `#1D7742` | CTA, liens, highlights |
| White | `#FFFFFF` | Fond, texte sur foncé |
| Black / Dark | `#000000` / `#1A1A1A` | Corps de texte |

---

## 🤖 AI PROMPT ENGINEERING (NEW MODULE)

### Système complet de génération de prompts IA optimisés

**Fichiers :**
- `references/ai-prompt-engineering.md` — Théorie des 8 blocs (SUBJECT/ENVIRONMENT/COMPOSITION/CAMERA/LIGHTING/COLOR/MOOD/TECHNICAL)
- `workflows/prompt-generation-workflow.md` — 12 étapes pratiques pour construire un prompt
- `/prompt` slash command — Interface questionnaire pour générer 3 variantes

**Architecture 8 blocs :**
```
[SUBJECT]    + [ENVIRONMENT]    + [COMPOSITION] + [CAMERA]
[LIGHTING]   + [COLOR]          + [MOOD]        + [TECHNICAL]
```

**3 variantes automatiques :**
- Conservative (90% réaliste) → pour corporate/institutionnel
- Creative (70% réaliste, 30% stylisé) → pour marketing/campagnes
- Bold (40% réaliste, 60% stylisé) → pour innovation/disruptif

**Plateforme IA supportées :**
- Midjourney v6.1 (meilleur pour photos corporate) → `--ar`, `--style`, `--v`
- DALL-E 3 (meilleur pour précision géométrique) → resolution, style keywords
- Flux Pro (meilleur pour patterns/backgrounds) → steps, guidance_scale
- Stable Diffusion XL (meilleur pour contrôle avancé) → negative prompts, ControlNet

**Intégration dans flux créatif :**
1. Utiliser `/prompt` pour générer prompts IA purs
2. Ou utiliser ÉTAPE 0.5 optionnelle dans `/flyer`, `/affiche`, `/comm` pour génération image avant composition
3. Générer l'image dans Midjourney/DALL-E/Flux
4. Revenir à la commande créative pour composer le texte par-dessus

---

## 📊 RÉSUMÉ EXÉCUTIF

| Aspect | Avant | Maintenant | Amélioration |
|--------|-------|-----------|--------------|
| **Commandes** | 4 | 5 | +25% |
| **Assets** | 39 | 76 | +95% (37 SVG) |
| **Fichiers references** | 13 | 14 | +1 (AI prompts) |
| **Fichiers workflows** | 6 | 7 | +1 (Prompt generation) |
| **Validation checks** | 50+ | 50+ | stable |
| **Plateforme IA** | N/A | 4 | Midjourney, DALL-E, Flux, SD |

---

## ✅ CHECKLIST COMPLÉTION

- [x] 4 slash commands créatifs (/campagne, /flyer, /affiche, /comm)
- [x] 1 slash command AI prompts (/prompt) — NEW
- [x] Système questionnaire-driven (7-8 questions par command)
- [x] Asset-driven design (39 → 76 assets organisés)
- [x] Mandatory asset loading (ÉTAPE 0 dans chaque command)
- [x] Professional typography system (Inter hierarchy)
- [x] 50+ validation checklist
- [x] AI prompt engineering module (8-bloc architecture)
- [x] 3 prompt variations (conservative/creative/bold)
- [x] 4 plateforme IA supportées
- [x] Complete documentation & workflows
- [x] Test simulation (/flyer walkthrough)

---

## 🎯 NEXT STEPS POUR UTILISATEURS

1. **Lire** : `SKILL.md` (orchestrateur)
2. **Choisir** : Commande slash (`/campagne`, `/flyer`, `/affiche`, `/comm`, ou `/prompt`)
3. **Répondre** : Questions du questionnaire (7-8 questions)
4. **Valider** : Brief récapitulatif
5. **Obtenir** : Créations professionnelles brand-compliant
6. **Itérer** : Ajustements si nécessaire (max 2-3 rounds)

**Pour générer images IA :**
1. Taper `/prompt` OU utiliser ÉTAPE 0.5 dans commande créative
2. Répondre 6 questions mini
3. Copier/coller prompts dans Midjourney/DALL-E/Flux
4. Générer images
5. Revenir composer le texte par-dessus

---

## 📞 SUPPORT RAPIDE

- **Slash commands** → `workflows/slash-commands.md`
- **Assets** → `assets/` (76 fichiers organisés)
- **IA prompts** → `/prompt` command ou `references/ai-prompt-engineering.md`
- **Validation** → `references/validation-checklist.md`
- **Questions brand** → `references/brand-system.md`
- **Questions typo** → `references/typography-system-pro.md`

---

**Version** : 1.1 (Updated)  
**Dernière mise à jour** : Septembre 2026  
**Status** : ✅ PRODUCTION-READY  
**Nouveau** : Module AI Prompt Engineering + /prompt command + 37 SVG assets

---

End of SKILL-INDEX.md
