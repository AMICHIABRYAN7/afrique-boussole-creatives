# Afrique Boussole — Design System (Tokens & Components)

## Overview

The Design System provides a standardized set of tokens and reusable components that ensure visual consistency and accelerate design production.

---

## 1. COLOR TOKENS

### Primary Colors

```
--color-primary-blue:    #013C87
--color-primary-green:   #1D7742
```

### Neutral Colors

```
--color-neutral-white:   #FFFFFF
--color-neutral-ivory:   #F7F4EC
--color-neutral-dark:    #0A2555
--color-neutral-gray:    #666666
```

### Accent Colors

```
--color-accent-teal:     #2BA696
--color-accent-beige:    #D4B896
```

### Semantic Colors

```
--color-success:         #1D7742 (Brand Green)
--color-warning:         #D4B896 (Warm Beige)
--color-error:           #D64545
--color-info:            #2BA696 (Light Teal)
```

---

## 2. TYPOGRAPHY TOKENS

### Font Families

```
--font-primary:          'Inter'
--font-secondary:        'IBM Plex Mono' (optional)
--font-fallback:         'Helvetica Neue', Arial, sans-serif
```

### Font Sizes

```
--font-size-hero:        72px
--font-size-h1:          48px
--font-size-h2:          32px
--font-size-h3:          24px
--font-size-subtitle:    18px
--font-size-body:        16px
--font-size-small:       14px
--font-size-caption:     12px
--font-size-tiny:        10px
```

### Font Weights

```
--font-weight-regular:   400
--font-weight-medium:    500
--font-weight-semibold:  600
--font-weight-bold:      700
--font-weight-extrabold: 800
```

### Line Heights

```
--line-height-hero:      1.1
--line-height-headline:  1.2
--line-height-body:      1.6
--line-height-tight:     1.4
```

### Letter Spacing

```
--letter-spacing-tight:  -0.5px
--letter-spacing-normal: 0px
--letter-spacing-wide:   0.5px
--letter-spacing-wider:  1px
--letter-spacing-widest: 2px
```

---

## 3. SPACING SCALE

```
--space-xs:     4px
--space-sm:     8px
--space-md:     16px
--space-lg:     24px
--space-xl:     32px
--space-2xl:    48px
--space-3xl:    64px
```

### Usage

- Margins, padding, gaps
- Consistent throughout design
- Use scale values, not arbitrary numbers

---

## 4. BORDER RADIUS

```
--radius-none:    0px
--radius-sm:      4px
--radius-md:      8px
--radius-lg:      12px
--radius-round:   999px (circular)
```

### Usage

- Buttons: 4px (--radius-sm)
- Cards: 8px (--radius-md)
- Inputs: 4px (--radius-sm)
- Badges: 12px (--radius-lg) or circular

---

## 5. SHADOWS

### Subtle Shadow

```
box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
```

**Use** : Cards, subtle depth

### Medium Shadow

```
box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
```

**Use** : Interactive elements, moderate elevation

### Large Shadow

```
box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
```

**Use** : Modal overlays, significant elevation

---

## 6. OPACITY SCALE

```
--opacity-10:   10%
--opacity-20:   20%
--opacity-30:   30%
--opacity-50:   50%
--opacity-70:   70%
--opacity-100:  100%
```

### Usage

- Text/element overlays
- Background overlays on images
- Disabled states
- Hover/focus states

---

## 7. BUTTON COMPONENTS

### Button - Primary CTA

**Background** : Brand Green (#1D7742)
**Text Color** : White (#FFFFFF)
**Padding** : 12px 24px
**Border Radius** : 4px
**Font** : Inter, 16px, Weight 600
**Hover State** : Darker Green (#164D3A), slight scale (1.02)
**Focus State** : Visible outline (Brand Blue 2px)
**Minimum Size** : 44x44px (touch target)

```
┌────────────────────────┐
│  Sign Up for Webinar   │
└────────────────────────┘
```

### Button - Secondary

**Background** : Transparent, Brand Blue border (2px)
**Text Color** : Brand Blue (#013C87)
**Padding** : 10px 22px
**Border Radius** : 4px
**Hover State** : Brand Blue background, White text

### Button - Tertiary

**Background** : Transparent
**Text Color** : Brand Blue (#013C87)
**Underline** : Yes
**Padding** : 8px 16px
**Hover State** : Text underline, slight color change

---

## 8. TEXT INPUT COMPONENTS

### Text Input

**Border** : 1px solid Brand Blue
**Border Radius** : 4px
**Padding** : 12px 16px
**Font** : Inter, 16px
**Focus State** : Brand Blue border (2px), blue outline
**Placeholder Color** : Medium Gray (#999999)
**Background** : White

```
┌──────────────────────────┐
│ Enter your email address │
└──────────────────────────┘
```

---

## 9. CARD COMPONENTS

### Card

**Background** : White or Ivory
**Border Radius** : 8px
**Shadow** : Subtle (0px 2px 8px rgba(0,0,0,0.1))
**Padding** : 24px
**Border** : Optional 1px light gray on some uses

```
┌──────────────────────────┐
│ CARD HEADING             │
│ Supporting description   │
│ text and information.    │
└──────────────────────────┘
```

### Card - Compact

**Padding** : 16px
**Shadow** : None or very subtle
**Use** : Product lists, grid layouts

---

## 10. TAG / BADGE COMPONENTS

### Tag - Default

**Background** : Brand Blue (#013C87)
**Text** : White
**Padding** : 6px 12px
**Border Radius** : 12px (--radius-lg)
**Font** : Inter, 12px, Weight 500

```
[Strategic Growth]
```

### Tag - Secondary

**Background** : Ivory
**Text** : Brand Blue
**Border** : 1px Brand Blue
**Padding** : 6px 12px
**Border Radius** : 12px

---

## 11. DIVIDER / SEPARATOR

### Horizontal Rule

**Style** : Solid line
**Color** : Brand Blue (#013C87) or Light Gray
**Thickness** : 1px
**Margin** : 24px vertical (--space-lg)

---

## 12. ICON SYSTEM

### Icon Sizing

```
--icon-xs:      16px
--icon-sm:      24px
--icon-md:      32px
--icon-lg:      48px
--icon-xl:      64px
```

### Icon Usage

- Icons support or replace text (not decoration-only)
- Same color hierarchy as typography
- Stroke weight: Thin (1px) to regular (2px)
- Compass icon: Primary icon of Afrique Boussole
- Direction/navigation icons: Support journey narrative

---

## 13. LAYOUT GRID

### Desktop Grid

```
12-column grid
Column width: 60px
Gutter: 20px
Total width: 1200px
```

### Tablet Grid

```
8-column grid
Column width: 70px
Gutter: 16px
Total width: 768px
```

### Mobile Grid

```
4-column grid
Column width: varies
Gutter: 12px
Total width: 100% (max 540px)
```

---

## 14. BREAKPOINTS

```
--breakpoint-mobile:     320px
--breakpoint-tablet:     768px
--breakpoint-desktop:    1024px
--breakpoint-wide:       1440px
```

---

## 15. ANIMATION TOKENS

### Duration

```
--duration-fast:    200ms
--duration-normal:  300ms
--duration-slow:    500ms
```

### Easing

```
--ease-in-out:      cubic-bezier(0.4, 0, 0.2, 1)
--ease-out:         cubic-bezier(0, 0, 0.2, 1)
--ease-in:          cubic-bezier(0.4, 0, 1, 1)
```

### Transitions

- **Buttons** : Background 200ms ease-in-out
- **Text** : Color 200ms ease-in-out
- **Hover states** : Scale 200ms ease-in-out
- **Page transitions** : 300ms ease-in-out

---

## 16. ACCESSIBILITY TOKENS

### Color Contrast Ratios

```
--contrast-wcag-aaa: 7:1 (enhanced)
--contrast-wcag-aa:  4.5:1 (standard)
--contrast-large-aaa: 4.5:1 (large text)
--contrast-large-aa:  3:1 (large text)
```

### Focus States

```
All interactive elements must have visible focus state:
- Outline: 2px solid Brand Blue
- Outline offset: 2px
- Or: Box shadow with Brand Blue
```

### Touch Targets

```
Minimum size: 44x44px
Minimum spacing: 8px between interactive elements
```

---

## 17. RESPONSIVE TYPOGRAPHY

### Fluid Typography

**Desktop** : Use full font sizes from scale
**Tablet** : Reduce heading sizes by 10-15%
**Mobile** : Reduce heading sizes by 20-25%, increase body by 2-4px

**Example** :

```
H1:
  Desktop: 48px
  Tablet:  40px
  Mobile:  32px
```

---

## 18. DARK MODE (Optional)

If dark mode is needed:

```
--color-bg-dark:        #121212
--color-surface-dark:   #1E1E1E
--color-text-dark:      #FFFFFF
--color-text-secondary: #CCCCCC
```

---

## 19. COMPONENT LIBRARY INVENTORY

### Text Components

- [ ] Heading (H1, H2, H3, H4)
- [ ] Paragraph
- [ ] Label
- [ ] Caption
- [ ] Link (default, hover, visited)

### Button Components

- [ ] Primary Button
- [ ] Secondary Button
- [ ] Tertiary Button
- [ ] Button Group
- [ ] Icon Button

### Input Components

- [ ] Text Input
- [ ] Text Area
- [ ] Select Dropdown
- [ ] Checkbox
- [ ] Radio Button

### Container Components

- [ ] Card
- [ ] Modal
- [ ] Alert Box
- [ ] Tooltip
- [ ] Popover

### Navigation Components

- [ ] Navigation Bar
- [ ] Breadcrumb
- [ ] Pagination
- [ ] Tab Navigation

### Data Components

- [ ] Table
- [ ] List (ordered, unordered)
- [ ] Definition List

---

## 20. USAGE GUIDELINES

### When to Use Design System Tokens

**DO** :

- Use color tokens (--color-primary-blue) instead of hardcoding #013C87
- Use spacing tokens (--space-md) instead of arbitrary 15px
- Use typography tokens for consistency
- Reference tokens in documentation
- Update tokens in one place, changes cascade

**DON'T** :

- Invent new colors not in palette
- Use arbitrary spacing values
- Override tokens without strategic reason
- Create duplicate components

---

## 21. QUICK REFERENCE: COMPONENT DEFAULTS

| Component | Color | Size | Padding | Radius |
|-----------|-------|------|---------|--------|
| Primary Button | Brand Green | 16px font | 12/24px | 4px |
| Card | White/Ivory | N/A | 24px | 8px |
| Input | White border | 16px font | 12/16px | 4px |
| Tag | Brand Blue | 12px font | 6/12px | 12px |
| Icon | Brand Blue | 32px | N/A | N/A |

---

End of Design System.
