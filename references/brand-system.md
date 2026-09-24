# Afrique Boussole — Brand System

## Overview

Le Brand System d'Afrique Boussole définit l'identité visuelle complète et l'usage cohérent de tous les éléments de marque.

Ce système garantit la cohérence visuelle sur tous les touchpoints : flyers, affiches, publicités, web, réseaux sociaux, communications corporate.

---

## 1. COLOR PALETTE

### Primary Colors

```
BRAND BLUE
Hex: #013C87
RGB: 1, 60, 135
CMYK: 99, 56, 0, 47
```

**Utilisation** : Éléments principaux, textes headlines, backgrounds, accents, CTA primaires.

```
BRAND GREEN
Hex: #1D7742
RGB: 29, 119, 66
CMYK: 76, 0, 45, 53
```

**Utilisation** : Éléments secondaires, accents, highlights, backgrounds alternatifs, actions positives.

### Neutral Colors

```
WHITE
Hex: #FFFFFF
RGB: 255, 255, 255
CMYK: 0, 0, 0, 0
```

**Utilisation** : Backgrounds, texte sur fond foncé, espaces négatifs.

```
IVORY (Crème légère)
Hex: #F7F4EC
RGB: 247, 244, 236
CMYK: 3, 4, 8, 3
```

**Utilisation** : Backgrounds alternatifs, surfaces texturées, overlays subtils.

### Extended Palette

```
DARK NAVY (pour contraste profond)
Hex: #0A2555
RGB: 10, 37, 85
CMYK: 88, 57, 0, 67
```

**Utilisation** : Textes sur fonds clairs, borders, details fins.

```
LIGHT TEAL (accent subtil)
Hex: #2BA696
RGB: 43, 166, 150
CMYK: 74, 0, 10, 35
```

**Utilisation** : Highlights, success states, interactive elements.

```
WARM BEIGE (texture africaine)
Hex: #D4B896
RGB: 212, 184, 150
CMYK: 0, 13, 29, 17
```

**Utilisation** : Backgrounds texturés, overlays, motifs traditionnels.

### Color Roles and Usage

**Dominant Color** : Brand Blue #013C87 (≥ 60% de la palette visuelle)

**Secondary Color** : Brand Green #1D7742 (20-30% de la palette)

**Accent Color** : Light Teal #2BA696 (5-15% de la palette)

**Neutrals** : White, Ivory, Dark Navy (remainder)

#### Specific Color Assignments

| Élément | Couleur primaire | Alternative |
|---------|-----------------|-------------|
| Background principal | #FFFFFF ou #F7F4EC | #013C87 |
| Texte body | #0A2555 | #FFFFFF sur fond bleu |
| Headline 1 | #013C87 | #1D7742 |
| Headline 2 | #1D7742 | #013C87 |
| CTA Button | #1D7742 | #2BA696 |
| CTA Text | #FFFFFF | - |
| Logo | Full color | Monochrome blanc/bleu |
| Border/Divider | #013C87 | #1D7742 |
| Overlay 30% | #013C87 @ 30% opacity | - |
| Overlay 50% | #013C87 @ 50% opacity | - |

### Color Prohibitions

**NEVER** :

- Remplacer #013C87 par un bleu proche (Royal Blue, Cobalt, etc.)
- Remplacer #1D7742 par un vert proche (Forest Green, Dark Green, etc.)
- Inventer de nouvelles couleurs primaires "pour variation"
- Utiliser plus de 5 couleurs dans un même visuel
- Saturer les couleurs primaires
- Créer des dégradés entre Brand Blue et Brand Green sans raison
- Utiliser des couleurs qui contreviennent à l'accessibilité WCAG AA

### Accessible Color Combinations

**Text on Background** (minimum AA contrast 4.5:1)

- Dark Navy (#0A2555) sur White (#FFFFFF) : Excellent
- Dark Navy (#0A2555) sur Ivory (#F7F4EC) : Excellent
- White (#FFFFFF) sur Brand Blue (#013C87) : Excellent
- White (#FFFFFF) sur Brand Green (#1D7742) : Excellent
- Brand Blue (#013C87) sur White (#FFFFFF) : Good (4.8:1)
- Brand Green (#1D7742) sur White (#FFFFFF) : Good (4.6:1)

**Avoid** :

- Light Teal sur White (insufficient contrast)
- Brand Green sur Brand Blue (insufficient contrast for small text)

---

## 2. TYPOGRAPHY SYSTEM

### Font Families

#### Display Font (Headlines, Hero Text)

**Primary** : Inter (sans-serif, geometric, modern)

- Weights available: 400, 500, 600, 700, 800
- Use case: H1, campaign headlines, hero statements

**Fallback** : Helvetica Neue, Arial

#### Body Font (Text, Description)

**Primary** : Inter (same as display for consistency)

- Weights: 400 (regular), 500 (medium)
- Use case: Body text, descriptions, CTA labels

**Fallback** : Segoe UI, Roboto

#### Monospace Font (Technical, Data)

**Primary** : IBM Plex Mono

- Weight: 400, 600
- Use case: Coordinates, data points, technical info

**Fallback** : Courier New, Monaco

### Font Sizing and Hierarchy

```
H1 (Hero, Campaign) : 72px - 96px | Weight 700 | Line height 1.1
H2 (Section Title)   : 48px - 56px | Weight 700 | Line height 1.2
H3 (Subsection)      : 32px - 40px | Weight 600 | Line height 1.3
Subtitle             : 24px - 28px | Weight 500 | Line height 1.4
Body (Large)         : 18px - 20px | Weight 400 | Line height 1.6
Body (Regular)       : 14px - 16px | Weight 400 | Line height 1.6
CTA Label            : 14px - 16px | Weight 600 | Line height 1.5
Caption              : 12px - 14px | Weight 400 | Line height 1.5
Metadata             : 10px - 12px | Weight 500 | Line height 1.4
```

### Typography Rules

1. **Maximum 2 font weights per visual** (typically 400 + 700 or 500 + 700)
2. **Minimum line height 1.5** for readability
3. **No all-caps for body text** (except very short UI labels)
4. **Letter spacing** :
   - Headlines: +0.5px to +2px
   - Body: 0px (normal)
   - Metadata: +0.3px
5. **No more than 3 text colors** in a single design
6. **Contrast ratio minimum AA** (4.5:1 for normal text, 3:1 for large text)

### Typography Examples

**Flyer Headline** :
```
Inter, 72px, Weight 700, Color #013C87, Line height 1.1
Letter spacing +1px
```

**Body Text** :
```
Inter, 16px, Weight 400, Color #0A2555, Line height 1.6
```

**CTA Button** :
```
Inter, 16px, Weight 600, Color #FFFFFF, Bgcolor #1D7742
Padding 12px 24px, Border radius 4px
```

### Localization and Accessibility

- Support African languages (French, English, Swahili, etc.)
- Ensure font supports diacritics
- Test with screen readers
- Provide text alternatives for displayed data/numbers

---

## 3. LOGO USAGE

### Logo Versions

#### Full Logo (Primary)

```
Horizontal lockup with wordmark
Minimum height: 40px (for digital)
Minimum height: 15mm (for print)
```

#### Logo Mark Only (Icon)

```
Compass or symbol-only version
Minimum size: 24px (digital), 8mm (print)
```

#### Monochrome White

```
For use on dark backgrounds
Colors: #FFFFFF only
Maintain proportions of full logo
```

#### Monochrome Dark

```
For use on light backgrounds
Colors: #013C87 or #0A2555
Maintain proportions of full logo
```

### Logo Placement Rules

1. **Clear Space** : Maintain minimum clear space around logo = 1/4 of logo height
2. **Minimum Size** : Never display below 40px (digital) or 15mm (print)
3. **Never Rotate** unless in specific branded context (max 15° for dynamic designs)
4. **Never Stretch or Compress** : Always maintain aspect ratio
5. **Never Recolor** outside approved color palette
6. **Never Add Effects** : No drop shadows, glows, or 3D effects unless specified in guidelines
7. **Positioning** : Bottom right (most common), top left (alternative), center (hero only)

### Approved Backgrounds for Logo

- White (#FFFFFF)
- Ivory (#F7F4EC)
- Brand Blue (#013C87) — logo must be white or light
- Brand Green (#1D7742) — logo must be white
- Photography (logo must have white or dark border for contrast)

### Prohibited Uses

- Logo smaller than minimum size
- Logo stretched or squished
- Logo rotated at angles other than approved
- Logo with drop shadows or 3D effects
- Logo recolored to non-brand colors
- Logo on low-contrast backgrounds
- Multiple logos in same design
- Logo competing with other design elements

---

## 4. SUPPORTING VISUAL ELEMENTS

### Compass Icon System

The compass is the primary geometric element of Afrique Boussole's visual identity.

**Usage** :

- Navigation markers
- Directional indicators
- Sub-branding
- Corner treatments
- Structural elements

**Proportions** :

- Cardinal points: N, S, E, W marked
- Center point: Emphasized
- Stroke weight: Proportional to element size
- Color: Brand Blue (#013C87) or White

**Do NOT** :

- Use arbitrary compass variations
- Use compass as pure decoration without purpose
- Overuse compass in single design (max 2-3 instances)
- Mix different compass styles in same design

### Map and Geographical Elements

**Africa Map** :

- Clean, simplified outline
- Used to emphasize geographic scope
- Color: Brand Blue or Green
- Scale: Always readable

**Coordinates and Route Lines** :

- Suggest journey, strategy, navigation
- Use thin lines (1-2px)
- Never overly complex
- Grid lines for structure

**Route Markers** :

- Pins, points, connections
- Indicate direction or location
- Color: Brand Blue or Accent Teal

### Pattern System

**Primary Pattern** : Geographic grid lines (subtle background)

**Secondary Pattern** : Compass rose repetition (very subtle)

**Usage** :

- Backgrounds
- Separators
- Texture overlay (max 20% opacity)

**Do NOT** :

- Use African textile patterns without strategic reason
- Create patterns that distract from content
- Mix more than 2 pattern types in one design

---

## 5. PHOTOGRAPHY DIRECTION

### Subject Matter

**Approved** :

- African professionals in modern workplaces
- Entrepreneurs, business leaders
- African cities and architecture (contemporary)
- Infrastructure and connectivity
- Transportation and mobility
- Business meetings and collaboration
- Technology and innovation
- Maps, data visualization
- African landscapes (premium)
- Teams and diversity

**Avoid** :

- Stereotypical "African" imagery
- Poverty or hardship as visual narrative
- Colonial-era photography or aesthetics
- Clichéd safari or tribal imagery
- Generic stock photos of any region

### Photographic Style

**Lighting** : Natural, professional, well-lit. Golden hour acceptable for landscape.

**Composition** : Rule of thirds, depth of field, professional framing.

**Color Grade** : Warm but professional. Avoid oversaturation or desaturation.

**Focus** : Sharp and deliberate. Motion blur acceptable for movement themes.

**People** : Authentic expressions, diverse backgrounds, professional attire (unless context suggests otherwise).

**Environment** : Modern, clean, purposeful. Avoid cluttered or messy backgrounds.

### Image Integration in Designs

- Photography should support headline, not replace it
- Overlay text only on dark/blurred areas
- Maintain text readability (WCAG AA minimum)
- Use vignettes or semi-transparent overlays strategically
- Ensure image and text alignment

---

## 6. DESIGN SYSTEM TOKENS

### Spacing Scale

```
4px   (micro: small gaps, fine details)
8px   (xs: minor spacing)
16px  (sm: small padding/margins)
24px  (md: medium spacing)
32px  (lg: large spacing)
48px  (xl: major divisions)
64px  (2xl: section breaks)
```

### Border Radius

```
0px   (none: sharp corners)
4px   (sm: subtle roundness)
8px   (md: moderate roundness)
12px  (lg: generous roundness)
```

### Shadows

**Subtle Shadow** :
```
0px 2px 8px rgba(0, 0, 0, 0.1)
```

**Medium Shadow** :
```
0px 4px 12px rgba(0, 0, 0, 0.15)
```

**Use** : Interactive elements, cards, overlays

**Caution** : Avoid excessive shadows on flat designs.

### Opacity Scale

```
10%   (very subtle overlay or background)
30%   (noticeable but transparent)
50%   (semi-transparent, readable)
70%   (mostly opaque)
100%  (fully opaque)
```

---

## 7. ACCESSIBILITY STANDARDS

### Color Contrast

- **Text on background** : Minimum WCAG AA 4.5:1 for normal text, 3:1 for large text
- **Test combinations** : Use WCAG contrast checker
- **Avoid relying solely on color** : Use text labels, patterns, or icons for distinction

### Text Readability

- **Line length** : 45-75 characters optimal
- **Line height** : Minimum 1.5
- **Font size** : Minimum 14px body text
- **Weight** : Avoid thin fonts for body text

### Interactive Elements

- **Minimum size** : 44x44px (touch targets)
- **Visible focus states** : Clear indication of keyboard focus
- **Link styling** : Underlined or clearly distinguished from body text

### Alternative Text and Labels

- **Image alt text** : Describe purpose and content
- **Icon labels** : Provide text equivalent
- **Data visualization** : Include table or text description

---

## 8. BRAND VOICE IN VISUAL DESIGN

The visual design must convey:

- **Orientation** : Use compass, maps, directional elements
- **Strategy** : Use clean lines, structured composition, hierarchical information
- **Navigation** : Use pathways, routes, connections
- **Expertise** : Professional photography, precise typography, premium production
- **Africa Contemporary** : Modern aesthetic, diverse representation, authentic context
- **Connection** : Relational elements, networks, interactions
- **Mobilité** : Movement, flow, progression
- **Development** : Growth trajectory, positive direction, innovation
- **Territory** : Geographic scope, boundary definition, local context
- **Innovation** : Forward-thinking design, digital aesthetics, modern solutions
- **Professionalism** : Corporate polish, attention to detail, quality production
- **Trust** : Consistent identity, clear communication, transparent information
- **International Openness** : Global aesthetic, multi-cultural representation, accessible design

---

## 9. ANTI-PATTERNS

### DO NOT

- Invent new primary colors
- Use more than 2 font families
- Apply logo effects (shadows, 3D, distortion)
- Resize logo without maintaining aspect ratio
- Use photography that is generic, clichéd, or low-quality
- Mix serif and sans-serif fonts without intention
- Create text smaller than 12px for body content
- Use color as sole method of information distinction
- Apply excessive effects or filters
- Create designs that feel like templates
- Overuse decorative elements
- Ignore safe area on mobile formats
- Place CTA in secondary position
- Use more than 3 text colors
- Create insufficient contrast ratios
- Ignore accessibility guidelines

---

## 10. COLOR REFERENCE (QUICK LOOKUP)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Brand Blue | #013C87 | 1, 60, 135 | Primary elements, headlines, backgrounds |
| Brand Green | #1D7742 | 29, 119, 66 | Secondary, CTA, accents |
| White | #FFFFFF | 255, 255, 255 | Backgrounds, text on dark |
| Ivory | #F7F4EC | 247, 244, 236 | Alt backgrounds |
| Dark Navy | #0A2555 | 10, 37, 85 | Text, borders, details |
| Light Teal | #2BA696 | 43, 166, 150 | Highlights, success, accents |
| Warm Beige | #D4B896 | 212, 184, 150 | Textures, overlays |

---

## 11. ASSET MANAGEMENT

All brand assets are stored in `/assets/` directory:

- `/assets/brand/logos/` — Logo files (all versions)
- `/assets/brand/icons/` — Icon library
- `/assets/brand/symbols/` — Compass, map, directional elements
- `/assets/visual-system/` — Patterns, grids, geometric elements
- `/assets/references/` — Example designs and case studies

**Note** : Do not invent or create brand assets that do not officially exist. Use placeholders clearly marked as such.

---

## 12. IMPLEMENTATION CHECKLIST

Before finalizing any design, verify:

- [ ] Colors used match Brand System exactly
- [ ] Logo respects clear space and sizing rules
- [ ] Typography follows hierarchy system
- [ ] Text contrast meets WCAG AA minimum
- [ ] Photography style aligns with direction
- [ ] No more than 5 colors in total palette
- [ ] No more than 2 font weights
- [ ] Supporting elements serve clear purpose
- [ ] Design feels Afrique Boussole (not generic)
- [ ] Mobile version is readable and functional

---

End of Brand System.
