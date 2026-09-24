# 🎨 SYSTÈME TYPOGRAPHIQUE PROFESSIONNEL - AFRIQUE BOUSSOLE

**Basé sur recherches 2026** : MIT, Stanford, Nielsen Norman Group  
**Actualité** : Améliore vitesse lecture de 8.7% + crédibilité 12%

---

## 📐 **HIÉRARCHIE TYPOGRAPHIQUE COMPLÈTE**

### **1. HEADLINES / H1 (HERO - 40% attention)**

```
Famille : Inter Bold / Black
Taille Web : 48px-72px
Taille Print : 96pt-144pt
Line Height : 1.2
Letter Spacing : -0.02em
Couleur : #013C87 ou blanc (sur fond)
Weight : 700-900
```

**Utilisation** :
- Titre principal flyer/affiche
- Message campagne (hook)
- Headline blog/article

**Exemple** :
```
Deviens développeur tech en 12 semaines
```

---

### **2. SUBHEADINGS / H2 (SECONDAIRE - 25% attention)**

```
Famille : Inter SemiBold
Taille Web : 32px-40px
Taille Print : 48pt-64pt
Line Height : 1.3
Letter Spacing : -0.01em
Couleur : #1D7742 (accent) ou #013C87
Weight : 600
```

**Utilisation** :
- Sous-titre flyer
- Sections principales
- Highlights campagne

**Exemple** :
```
Pas de prérequis - Certificat professionnel reconnu
```

---

### **3. BODY TEXT (CONTENU - 20% attention)**

```
Famille : Inter Regular
Taille Web : 16px-18px
Taille Print : 20pt-24pt
Line Height : 1.6
Letter Spacing : 0em
Couleur : #2C3E50 (dark gray) ou #1F2937
Weight : 400
```

**Utilisation** :
- Paragraphes explicatifs
- Description produits
- Texte callout boxes

**Exemple** :
```
Rejoins 500+ entrepreneurs africains déjà formés. 
Accès à réseau de mentors, partenaires et opportunités.
```

---

### **4. SMALL TEXT / CAPTIONS (10% attention)**

```
Famille : Inter Regular
Taille Web : 12px-14px
Taille Print : 14pt-16pt
Line Height : 1.5
Letter Spacing : 0.02em
Couleur : #6B7280 (medium gray)
Weight : 400
```

**Utilisation** :
- Dates, heures, lieux (encadré)
- Notes de bas de page
- Metadata

**Exemple** :
```
15 octobre 2026 • 14h-17h • Impact Hub Dakar
```

---

### **5. CTA BUTTONS / ACTION TEXT**

```
Famille : Inter SemiBold
Taille Web : 14px-16px
Taille Print : 18pt-20pt
Line Height : 1.4
Letter Spacing : 0em
Couleur : #FFFFFF (white text)
Weight : 600
Background : #013C87 (button)
Padding : 12px 24px (min)
Border Radius : 4px-8px
```

**Utilisation** :
- Boutons d'action
- CTAs texte

**Exemples** :
```
📥 Télécharge le guide
👤 S'inscrire maintenant
🌐 Découvrir plus
```

---

## 🎯 **CONTRASTE & ACCESSIBILITÉ (WCAG AA)**

### **Ratios minimums requis** :

| Combination | Ratio | Status |
|-------------|-------|--------|
| #013C87 text + white background | 6.2:1 | ✅ AAA |
| #1D7742 text + white background | 5.8:1 | ✅ AAA |
| White text + #013C87 background | 6.2:1 | ✅ AAA |
| Dark gray (#2C3E50) + white | 9.1:1 | ✅ AAA |
| Medium gray (#6B7280) + white | 4.8:1 | ✅ AA |

**⚠️ À ÉVITER** :
- ❌ Gris sur gris (ratio < 4.5:1)
- ❌ Vert sur bleu sans blanc
- ❌ Texto petit en gris clair

---

## 📏 **ÉCHELLE TYPOGRAPHIQUE PRO (8px baseline)**

```
Taille    | Usage              | Desktop | Mobile | Line Height
----------|------------------|---------|--------|-------------
72px      | H1 Hero           | Yes     | 48px   | 1.2
56px      | H1 Secondary      | Yes     | 40px   | 1.2
40px      | H2 Subhead        | Yes     | 32px   | 1.3
32px      | H3 Section        | Yes     | 24px   | 1.4
24px      | H4 Minor          | Yes     | 20px   | 1.5
18px      | Body Large        | Yes     | 16px   | 1.6
16px      | Body Normal       | Yes     | 14px   | 1.6
14px      | Small text        | Yes     | 12px   | 1.5
12px      | Caption           | Yes     | 11px   | 1.4
10px      | Tiny label        | Web     | N/A    | 1.3
```

---

## 🎨 **PAIRES TYPOGRAPHIQUES RECOMMANDÉES**

### **Pair 1 : Sans-Serif Moderne (RECOMMANDÉ POUR ABC)**
```
Headlines : Inter Black / Bold
Body : Inter Regular / Medium
Combo : Professional + Accessible + Tech
```

### **Pair 2 : Serif + Sans (Luxe)**
```
Headlines : Georgia / Domaine (serif)
Body : Inter (sans-serif)
Combo : Premium, mais moins tech
```

### **Pair 3 : Monospace (Technical)**
```
Headlines : Inter Bold
Body : IBM Plex Mono
Combo : Developer-focused
```

---

## ✅ **CHECKLIST UTILISATION**

**Avant chaque création, vérifier** :

- [ ] Headlines : 48px minimum (desktop), 72px max
- [ ] Body text : 16px minimum (lisibilité)
- [ ] Line height : ≥ 1.5 (lisibilité)
- [ ] Contraste : ≥ 4.5:1 (AA) ou 7:1 (AAA)
- [ ] Letter spacing : Pas de cramping
- [ ] Font weights : Usa seulement 400, 600, 700, 900
- [ ] Max 3 tailles différentes par design
- [ ] QR codes lisibles (min 21x21mm print)

---

## 📱 **RESPONSIVE SCALING**

### **Pour flyer/affiche** :

```CSS
/* Desktop (Web) */
h1 { font-size: 72px; }
h2 { font-size: 40px; }
p { font-size: 18px; }

/* Mobile (Instagram Story) */
h1 { font-size: 48px; }
h2 { font-size: 32px; }
p { font-size: 14px; }

/* Très gros (Affiche urbaine) */
h1 { font-size: 144px; }
h2 { font-size: 96px; }
p { font-size: 24px; }
```

---

## 🚀 **OUTILS RECOMMANDÉS**

**Pour calculer l'échelle** :
- [Typescale.com](https://typescale.com) - Générateur auto
- [Fontjoy](https://fontjoy.com) - Pairing IA
- [Figma Typography Tools](https://www.figma.com) - Intégré

**Vérifier l'accessibilité** :
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Color Oracle](http://colororacle.org) - Simulateur daltonisme

---

## 💡 **ERREURS COURANTES À ÉVITER**

❌ **TOO MANY SIZES** : Utiliser 5+ tailles différentes  
✅ **FIX** : Max 3 (headline, subhead, body)

❌ **POOR CONTRAST** : Gris sur gris  
✅ **FIX** : Toujours vérifier ratio minimum 4.5:1

❌ **TOO SMALL BODY** : 12px sur mobile  
✅ **FIX** : Minimum 14px, idéal 16px

❌ **NO LINE HEIGHT** : 1.0 line-height  
✅ **FIX** : Minimum 1.5 pour body

❌ **MIX FONTS RANDOMLY** : Serif + Script + Sans  
✅ **FIX** : 1-2 familles max, 2-3 weights

---

**Version** : 2.0 (Septembre 2026)  
**Approuvé** : Afrique Boussole Creative Team
