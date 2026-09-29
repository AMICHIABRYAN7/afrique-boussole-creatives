# Brief Intake Workflow

**Version** : 2.0  
**Date** : Septembre 2026  
**Objectif** : Collecter intelligemment les informations manquantes pour un brief créatif, sans poser de questions inutiles

---

## PRINCIPES FONDAMENTAUX

### 1. Questions Adaptatives (Pas de formulaire fixe)

Ne **JAMAIS** appliquer un questionnaire à 7-8 questions systématiquement.

**Adapter les questions à ce qui manque vraiment.**

**Exemple 1 — Très peu d'infos**
```
User: "Fais un flyer Afrique Boussole."

Questions manquantes (critiques) :
1. Quel est le sujet / service / événement ?
2. Qui est l'audience cible ?
3. Quel est le message principal (1 phrase max) ?
4. Y a-t-il un CTA ? Si oui, lequel ?
5. Format préféré ? (A4, A5, digital, social)

Poser SEULEMENT ces 5 questions.
```

**Exemple 2 — Infos détaillées**
```
User: "Fais un flyer A4 pour notre formation en cybersécurité, 
       destiné aux PME, avec CTA « S'inscrire sur notre site »."

Questions encore manquantes (critiques) :
1. Quels éléments visuels obligatoires ? (date, lieu, prix, durée?)
2. Ambiance visuelle ? (corporate, dynamique, éducatif?)
3. Avez-vous des assets / images à utiliser ?

Poser SEULEMENT ces 3 questions.
```

### 2. Ne Jamais Re-demander une Info Déjà Fournie

Maintenir un contexte des réponses déjà données.

Si l'utilisateur a dit "A4", ne pas redemander le format.

### 3. Retenir le Contexte Entre les Tours

Une fois le brief collecté, marquer l'état :
- ✅ BRIEF COMPLET
- ⚠️ BRIEF PARTIEL (infos nécessaires mais non critiques manquantes)

Procéder dès que l'information critiq est suffisante.

---

## CHAMPS DE BRIEF

### Obligatoires (critiques)

| Champ | Description | Exemple |
|-------|-------------|---------|
| **Objectif** | Que veut-on accomplir ? | Lead generation, brand awareness, event promo |
| **Sujet** | Quel est le cœur de la création ? | Flyer webinaire, affiche événement, post social |
| **Audience** | À qui parle-t-on ? | PME, étudiants, entrepreneurs, public général |
| **Message Principal** | L'idée clé en 1 phrase | "Maîtrisez la cybersécurité en 8 semaines" |
| **CTA** | Quelle action voulez-vous ? | Cliquer, télécharger, s'inscrire, appeler |

### Importants (à chercher si manquants)

| Champ | Description |
|-------|-------------|
| **Ambiance** | Corporate, dynamique, éducatif, premium, urgent ? |
| **Format** | A4, A5, social 1:1/4:5/9:16, digital, print ? |
| **Informations requis** | Date, lieu, prix, durée, contact, site web ? |
| **Visuels** | Qu'y aura-t-il ? (photo de produit, équipe, abstract?) |

### Optionnels (à noter si fournis)

| Champ | Description |
|-------|-------------|
| **Assets à utiliser** | Images, logos, fichiers fournis |
| **Références** | Exemples visuels qu'ils aiment |
| **Délai** | Urgent ou pas ? |
| **Contraintes** | Budget, restrictions légales, etc. |

---

## FLUX D'EXÉCUTION

```
USER ASKS FOR A CREATIVE
    ↓
PARSE WHAT WAS PROVIDED
    ↓
DETERMINE CRITICAL GAPS
    ↓
ASK ONLY THE GAPS
    ↓
USER ANSWERS
    ↓
UPDATE CONTEXT (NEVER RE-ASK)
    ↓
EVALUATE: IS BRIEF COMPLETE?
    ↓
   YES → PROCEED TO ASSET DISCOVERY
   NO  → ASK REMAINING CRITICAL QUESTIONS
```

---

## EXAMPLE DIALOGS

### Dialog A — Minimal Input

**User:** "Fais un flyer Afrique Boussole"

**Agent Analysis:**
```
Provided: None (generic request)
Critical missing: Objective, Subject, Audience, Message, CTA, Format
Important missing: Ambiance, Required Info
→ Ask 5 targeted questions
```

**Agent Output:**
```
Pour créer le flyer parfait, j'ai besoin de quelques infos :

1️⃣ De quoi s'agit-il ? (événement, formation, produit, service...)
2️⃣ Qui est l'audience ? (PME, étudiants, grand public...)
3️⃣ Quel est le message clé en une phrase ?
4️⃣ Qu'est-ce que vous voulez que les gens fassent ? (cliquer, appeler, s'inscrire...)
5️⃣ Format préféré ? (A4 imprimé, A5, ou digital/social)
```

---

### Dialog B — Detailed Input

**User:** "Flyer A4 pour notre formation cybersécurité destinée aux PME, 
CTA c'est « S'inscrire sur notre site », ambiance professional/premium"

**Agent Analysis:**
```
Provided: 
  - Format: A4 ✓
  - Sujet: Formation cybersécurité ✓
  - Audience: PME ✓
  - Ambiance: Professional/Premium ✓
  - CTA: S'inscrire site web ✓
  - Message: (inferred from "formation cybersécurité")
  
Critical still missing: Informations obligatoires (dates, durée, prix?, site exact?)
Important missing: Visuels (qui sera dans la formation? photos profs? abstract?)
→ Ask only 2-3 remaining questions
```

**Agent Output:**
```
Parfait ! J'ai bien noté. Quelques infos finales pour que le flyer soit complet :

1️⃣ Quelles dates/durée ? (ex: "12-16 Février", "8 semaines", etc.)
2️⃣ Avez-vous des visuels à intégrer ? (photos de formateurs, logo specifique, images?)
3️⃣ (OPTIONNEL) Prix ou modalités particulières à afficher ?
```

---

### Dialog C — Nearly Complete

**User:** "Flyer A4, formation cybersécurité, PME, professional, 
CTA S'inscrire, dates 12-16 février, on a pas d'images à utiliser"

**Agent Analysis:**
```
Provided:
  - Format: A4 ✓
  - Sujet: Formation cybersécurité ✓
  - Audience: PME ✓
  - Ambiance: Professional ✓
  - CTA: S'inscrire ✓
  - Dates: 12-16 février ✓
  - Visuels: Aucun (use defaults) ✓
  
Status: ✅ BRIEF COMPLETE — proceed to asset discovery
```

**Agent Output:**
```
Excellent ! J'ai tout ce qu'il me faut. 

Je charge maintenant les assets Afrique Boussole et je vais créer 
un flyer A4 professionnel pour votre formation.

[PROCEED TO ASSET DISCOVERY & CREATIVE GENERATION]
```

---

## DECISION TREE FOR QUESTION COUNT

```
IF all critical fields provided
  → BRIEF COMPLETE
  → Proceed

IF 1-2 critical fields missing
  → Ask 1-2 targeted questions
  → Wait for answers
  → Re-evaluate

IF 3+ critical fields missing
  → Ask 3-5 targeted questions
  → Wait for answers
  → Re-evaluate

IF ambiguous answers
  → Ask clarification
  → One question at a time
```

---

## COMMON PITFALLS TO AVOID

❌ **NEVER:** "Tell me about your design preferences" (too vague)  
✅ **INSTEAD:** "Corporate or dynamic energy?" (binary choice)

❌ **NEVER:** Ask format AND style AND mood in one message  
✅ **INSTEAD:** Ask one at a time, or group tightly related  

❌ **NEVER:** "What else can I help you with?" (reopens the brief)  
✅ **INSTEAD:** Confirm completion and move forward

---

## AFTER BRIEF IS COMPLETE

Once the brief is sufficient:

1. **Summarize** : "Voici le brief : [recap]"
2. **Confirm** : "C'est correct ?"
3. **Proceed** : Asset discovery → Strategy → Composition → Generation → QA

Do not wait for explicit "go ahead" if brief is complete and confirmed.

---

End of Intake Workflow
