# 🚀 ASSETS PROJETS CLIENTS

## Projets documentés

### LASTED
- **LASTED_2-removebg-preview (1).png** : Logo sans fond
- **logo.svg** : Version vectorielle

---

## 📁 Structure projet type

Pour chaque nouveau projet client :

```
projects/
└── {nom-client}/
    ├── logos/
    ├── mockups/
    ├── exports/
    └── sources/
```

---

## 📝 Naming convention

```
{projet}_{type}_{version}.{ext}

Exemples :
- lasted_logo_v2.png
- lasted_mockup_homepage_final.jpg
- lasted_banner_1200x630.png
```

---

## 🎯 Checklist livraison client

- [ ] Logo (SVG + PNG haute résolution)
- [ ] Favicon (ICO + PNG multi-tailles)
- [ ] Open Graph image (1200x630px)
- [ ] Assets réseaux sociaux (profil + cover)
- [ ] Mockups présentations
- [ ] Guide d'utilisation marque

---

## 📦 Package export standard

```
client-{nom}/
├── 01-logo/
│   ├── logo.svg
│   ├── logo-dark.svg
│   ├── logo@2x.png
│   └── logo@1x.png
├── 02-favicon/
│   ├── favicon.ico
│   └── favicon-32x32.png
├── 03-social/
│   ├── og-image.png
│   ├── twitter-card.png
│   └── linkedin-banner.png
└── 04-docs/
    └── brand-guidelines.pdf
```

---

## 🔒 Droits & propriété

- **Copyright** : Vérifier contrat client
- **Usage** : Portfolio (accord client requis)
- **Confidentialité** : NDA si applicable

---

## 💡 Tips

- Toujours garder sources éditables (.ai, .psd, .fig)
- Versionner avec Git LFS si fichiers lourds
- Créer ZIP final pour livraison client
