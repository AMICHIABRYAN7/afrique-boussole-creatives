# 📦 INVENTAIRE DES ASSETS - AFRIQUE BOUSSOLE CREATIVES

**Date de création** : 24 septembre 2026  
**Structure organisée automatiquement par Kiro AI**

---

## 📂 STRUCTURE GÉNÉRALE

```
assets/
├── brand/
│   ├── logos/          # Identité visuelle principale
│   └── icons/          # Icônes et favicons
├── team/               # Photos d'équipe
├── visuals/            # Visuels 3D et conceptuels
├── projects/           # Assets projets clients
├── templates/          # Templates réutilisables
├── references/         # Références et inspiration
└── visual-system/      # Système de design
```

---

## 🎨 BRAND / LOGOS

### **Logos Afrique Boussole**
| Fichier | Type | Usage |
|---------|------|-------|
| `afrique-boussole-logo.svg` | Logo principal | Version claire, fond blanc |
| `afrique-boussole-logo-dark.svg` | Logo dark mode | Version sombre |
| `afrique-boussole-emblem.svg` | Emblème seul | Icône/favicon/watermark |
| `afrique-boussole-emblem-dark.svg` | Emblème dark | Version noire |
| `logo.png` | Logo raster | Export bitmap 1024x1024 |

**Notes** :
- Formats vectoriels SVG privilégiés pour print/web
- PNG haute résolution pour réseaux sociaux
- Respecter zone de protection (espace minimal autour du logo)

---

## 👥 TEAM

Photos professionnelles des membres de l'équipe :

| Fichier | Rôle | Format |
|---------|------|--------|
| `team_director_general_1788911292003-Tm0lKkVp.jpg` | Directeur Général | Portrait HD |
| `team_tech_director_1788911305837-BLn5O_Av.jpg` | Directeur Technique | Portrait HD |
| `team_academy_director_1788911321642-RGJiGfpA.jpg` | Directeur Académie | Portrait HD |
| `team_security_lead_1788911332683-C0chyj0L.jpg` | Responsable Sécurité | Portrait HD |

**Usage** :
- Page "À propos" / "Notre équipe"
- Signatures emails professionnelles
- Présentations clients
- LinkedIn / Réseaux sociaux

**Spécifications** :
- Format : JPEG haute qualité
- Dimensions : ~1200x1200px
- Fond neutre professionnel

---

## 🎬 VISUALS

Rendus 3D et visuels conceptuels pour communication :

| Fichier | Description | Usage |
|---------|-------------|-------|
| `gab_3d_compass_africa_1788834669102-DNCQshGT.jpg` | Boussole 3D + Afrique | Hero sections, bannières |
| `gab_3d_tech_hub_1788834690273-BgEVo-eO.jpg` | Hub technologique 3D | Présentation services tech |
| `vsl_video_poster_1788911346619-BtmEfH9l.jpg` | Poster vidéo VSL | Thumbnail YouTube/Vimeo |

**Notes** :
- Visuels générés (probablement via IA/3D)
- Haute résolution pour impression
- Identité visuelle cohérente (tons bleus/verts)

---

## 🚀 PROJECTS

Assets liés aux projets clients spécifiques :

| Fichier | Projet | Notes |
|---------|--------|-------|
| `LASTED_2-removebg-preview (1).png` | Projet LASTED | Logo sans fond |
| `logo.svg` | Logo projet | Format vectoriel |

**Usage** :
- Portfolio
- Case studies
- Présentations clients

---

## 📋 NAMING CONVENTIONS

### **Pour les futurs assets** :

#### **Logos**
```
{nom-marque}-logo-{variation}.{ext}
Exemple : afrique-boussole-logo-dark.svg
```

#### **Photos équipe**
```
team_{role}_{timestamp}-{id}.jpg
Exemple : team_director_general_1788911292003-Tm0lKkVp.jpg
```

#### **Visuels**
```
{type}_{description}_{timestamp}-{id}.{ext}
Exemple : vsl_video_poster_1788911346619-BtmEfH9l.jpg
```

#### **Projets**
```
{nom-projet}_{type}_{version}.{ext}
Exemple : LASTED_logo_v2.png
```

---

## ✅ CHECKLIST QUALITÉ

Avant d'ajouter un nouvel asset :

- [ ] Nom de fichier descriptif (pas de "IMG_1234.jpg")
- [ ] Format approprié (SVG pour logos, JPG pour photos)
- [ ] Optimisé pour le web (compression sans perte de qualité)
- [ ] Droits d'utilisation vérifiés
- [ ] Documenté dans cet inventaire

---

## 🔄 WORKFLOWS RECOMMANDÉS

### **Export logo pour web**
```bash
# Depuis Illustrator/Figma
- Export SVG : Optimize + Minify
- Export PNG : @2x (2048px) et @1x (1024px)
```

### **Optimisation photos équipe**
```bash
# ImageMagick / Photoshop
- Dimensions : 1200x1200px
- Format : JPEG qualité 85%
- Profil : sRGB
```

### **Compression avant commit**
```bash
# TinyPNG / ImageOptim
- JPG : 80-90% qualité
- PNG : Palette optimisée
- SVG : Minifié (svgo)
```

---

## 📊 STATISTIQUES

**Total assets** : 16 fichiers  
**Brand** : 6 fichiers  
**Team** : 4 fichiers  
**Visuals** : 3 fichiers  
**Projects** : 2 fichiers  

**Formats** :
- SVG : 7 fichiers
- JPG : 7 fichiers
- PNG : 2 fichiers

**Taille totale** : ~15-20 MB (estimation)

---

## 🎯 PROCHAINES ÉTAPES

1. **Ajouter** :
   - Favicon.ico (16x16, 32x32, 64x64)
   - Open Graph images (1200x630px)
   - Templates réseaux sociaux
   - Mockups produits/services

2. **Créer** :
   - README.md dans chaque sous-dossier
   - Guidelines d'utilisation marque
   - Templates exports automatiques

3. **Optimiser** :
   - Compresser toutes les images
   - Générer versions WebP
   - Créer sprites SVG si nécessaire

---

**Maintenu par** : Équipe créative Afrique Boussole  
**Dernière mise à jour** : 24/09/2026
