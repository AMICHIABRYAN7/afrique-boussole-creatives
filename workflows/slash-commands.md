# 🎨 SYSTÈME DE COMMANDES SLASH - DIRECTEUR CRÉATIF IA

**Version** : 3.0  
**Dernière mise à jour** : Septembre 2026  
**Objectif** : Transformer le skill en véritable moteur de création visuelle autonome et intelligent.

---

## 📋 **COMMANDES DISPONIBLES**

| Commande | Fonction | Résultat |
|---|---|---|
| `/crea` | Générer une création complète depuis une description | Production d'un visuel final (HTML/CSS, SVG ou mockups détaillés) |
| `/variations` | Produire trois directions artistiques différentes | 3 concepts distincts pour un même brief |
| `/reference` | Analyser une affiche existante | Extraction des principes (compo, typo, couleurs) sans copie servile |
| `/adapt` | Décliner sur plusieurs formats | Adaptation intelligente (pas de simple redimensionnement) |
| `/campaign` | Produire une campagne complète | Déclinaison multicanale cohérente |
| `/audit` | Détecter les problèmes graphiques | Inspection visuelle et corrections |

---

## 🚀 `/crea` - CRÉER UN VISUEL (WORKFLOW INTELLIGENT)

**Déclenchement** : Utilisateur tape `/crea [description]`

**Description** : Moteur de création intelligent. Finis les questionnaires rigides à 8 questions. L'IA analyse, déduit, et ne pose des questions que si c'est strictement indispensable.

### **WORKFLOW D'EXÉCUTION `/crea`**

#### **1. Compréhension & Déduction**
- L'IA analyse la demande.
- Déduit le format (ex: "pour instagram" = 1080x1080).
- Déduit la cible et l'objectif.
- *Ne pose une question que si l'objectif ou le public est totalement opaque.*

#### **2. Sélection des Références (Asset Intelligence)**
- Chargement silencieux de `gab-sarl-company-profile.md` (pour les infos réelles).
- Choix automatique du bon logo (clair ou dark).
- Sélection de la bonne palette (#013C87, #1D7742).

#### **3. Construction des Concepts (Creative Strategy)**
- Au lieu d'imposer un template, l'IA choisit en mémoire 2 à 3 directions artistiques (ex: Minimaliste vs Photographique vs Géométrique).
- Sélection rapide du concept le plus adapté.

#### **4. Production du Visuel (Render Engine)**
- Génération effective du livrable.
- L'IA rédige les textes, place le logo, génère les mockups (via code HTML/Tailwind, SVG ou instructions prompt + script).

#### **5. Contrôle Qualité Automatique (Quality Assurance)**
- Vérification automatique : contraste, présence du footer GAB SARL obligatoire, typographie (Inter).

---

## 🔀 `/variations` - EXPLORER LES DIRECTIONS

**Déclenchement** : Utilisateur tape `/variations [sujet]`

- Produit exactement 3 approches :
  1. **Institutionnelle** (focus logo, couleurs pures, sérieux).
  2. **Dynamique** (focus image, composition diagonale, impact).
  3. **Créative** (focus typographie, minimaliste ou géométrique).

---

## 🔍 `/reference` - ANALYSE ET INSPIRATION

**Déclenchement** : Utilisateur tape `/reference [lien/nom image]`

- L'IA analyse l'image fournie dans les assets.
- Elle extrait la grille de composition (Top-Down, Split, Z-Layout).
- Elle identifie les ratios de taille de texte.
- *Résultat* : L'IA applique cette "recette" géométrique à une nouvelle création aux couleurs de GAB SARL.

---

## 📐 `/adapt` - DÉCLINAISON MULTI-FORMATS

**Déclenchement** : Utilisateur tape `/adapt [nom de la création] en [format cible]`

- Ex: `/adapt flyer-seminaire en Instagram Story`
- Repositionnement intelligent des éléments.
- Changement des tailles de police (pas d'écrasement ou d'étirement).

---

## 📣 `/campaign` - ORCHESTRATION CAMPAGNE

**Déclenchement** : Utilisateur tape `/campaign [objectif]`

- Combine `/variations` et `/adapt`.
- Crée le fil rouge visuel.
- Délivre un calendrier et les assets finaux pour 3+ canaux (ex: Print + LinkedIn + Facebook).

---

## 🚨 `/audit` - CONTRÔLE QUALITÉ VISUEL

**Déclenchement** : Utilisateur tape `/audit [nom du visuel]`

- Analyse technique automatique :
  - Lisibilité (contraste WCAG).
  - Tailles de textes (hiérarchie).
  - Présence et sécurité du logo (clear space).
  - Marges et bords perdus.
- Propose et *applique* les corrections.

---

> *Note au système : Ces commandes remplacent les anciens questionnaires rigides. Le but est d'être proactif, d'assumer des choix de direction artistique, et de livrer un résultat visuel le plus rapidement possible tout en respectant strictement l'identité GAB SARL.*
