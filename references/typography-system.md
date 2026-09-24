# Afrique Boussole — Typography System

## Overview

Typography is the voice of the visual design. It must be clear, professional, contemporary, and always readable.

This system ensures consistent typographic treatment across all Afrique Boussole creatives.

---

## 1. FONT FAMILY SELECTION

### Primary Font Stack: Inter

**Family** : Inter (Open Source, optimized for screens)

**Weights Used** :

- 400 (Regular) — Body text, descriptions
- 500 (Medium) — CTA labels, emphasis
- 600 (Semibold) — Subheadings, secondary emphasis
- 700 (Bold) — Headlines, primary emphasis
- 800 (Extrabold) — Hero text, maximum emphasis (use sparingly)

**Why Inter** :

- Geometric sans-serif (modern, professional)
- Optimized for readability on screens
- Excellent language support (including African diacritics)
- Neutral (not trendy, will age well)
- Works equally well in print and digital
- Free and widely available

**Fallback** :

```
font-family: 'Inter', 'Helvetica Neue', 'Arial', sans-serif;
```

### Secondary Font (Optional, Use Sparingly)

For very large, Hero text or distinctive headlines:

**IBM Plex Mono** (for data, quotes, or technical messaging)

```
font-family: 'IBM Plex Mono', monospace;
Weight: 400 or 600
Use case: Coordinates, statistics, technical information, or distinctive quotes
```

**Rule** : Use maximum 1 secondary font per design. Most designs use Inter only.

---

## 2. TYPOGRAPHIC HIERARCHY

### The 7-Level Hierarchy

| Level | Name | Size | Weight | Line Height | Use Case |
|-------|------|------|--------|-------------|----------|
| 1 | Hero / Campaign Text | 72–96px | 700–800 | 1.0–1.1 | Largest, most important headline |
| 2 | H1 / Main Headline | 48–64px | 700 | 1.1–1.2 | Primary message, main headline |
| 3 | H2 / Section Title | 32–40px | 600–700 | 1.2–1.3 | Secondary headline, section title |
| 4 | H3 / Subsection | 24–28px | 600 | 1.3–1.4 | Tertiary headline |
| 5 | Subtitle / Lead | 18–22px | 500–600 | 1.4–1.5 | Intro text, emphasis |
| 6 | Body / Regular | 14–18px | 400 | 1.6–1.8 | Main body text |
| 7 | Small / Caption | 10–14px | 400–500 | 1.4–1.6 | Metadata, captions, fine print |

### Minimum Sizes (Accessibility)

- **Body text** : Never below 14px (digital), 10pt (print)
- **Headlines** : Can go smaller for captions (10px minimum)
- **CTA labels** : Minimum 14px
- **Mobile viewing** : Increase base size by 2-4px for better readability

### Maximum Sizes (Professional)

- **Headlines** : Rarely exceed 96px (can become unreadable)
- **Hero text** : 72–96px maximum
- **Body text** : Never exceed 20px (creates awkward line breaks)

---

## 3. LINE HEIGHT AND SPACING

### Line Height (Leading)

**For Headlines** :

```
H1 (48–64px):   Line height 1.1–1.2  (52–76px)
H2 (32–40px):   Line height 1.2–1.3  (38–52px)
H3 (24–28px):   Line height 1.3–1.4  (31–39px)
```

**For Body Text** :

```
Body (14–18px): Line height 1.6–1.8  (22–32px)
```

### Letter Spacing (Tracking)

**Headlines** :

```
72–96px headlines:  +1–2px letter spacing
48–64px headlines:  +0.5–1px letter spacing
24–40px subtitles:  0–0.5px letter spacing
```

**Body** :

```
Body text: 0px (normal/default)
```

**Metadata/Captions** :

```
Small text: +0.3–0.5px (improves readability)
```

### Paragraph Spacing

```
Between paragraphs: 1.5x line height
Between sections: 2–3x line height
Between title and subtitle: 0.5–1x line height
```

### Word Spacing

Keep normal/default (1 space between words). Avoid forcing additional word spacing unless text is justified (avoid justified text in most cases).

---

## 4. TEXT COLOR SYSTEM

### Primary Text Colors

| Level | Text Color | Background | Contrast Ratio | Use Case |
|-------|-----------|-----------|------------------|----------|
| Headlines | #013C87 (Brand Blue) | #FFFFFF or #F7F4EC | 4.8:1 | Main headlines, emphasis |
| Secondary | #1D7742 (Brand Green) | #FFFFFF or #F7F4EC | 4.6:1 | Secondary headlines (sparingly) |
| Body | #0A2555 (Dark Navy) | #FFFFFF or #F7F4EC | 9.5:1 | Body text, descriptions |
| On Dark | #FFFFFF (White) | #013C87 or #1D7742 | 5.3:1 / 7.5:1 | Text on branded backgrounds |
| Metadata | #666666 (Medium Gray) | #FFFFFF or #F7F4EC | 7:1 | Captions, secondary info |
| Links | #2BA696 (Teal) | #FFFFFF or #F7F4EC | 4.2:1 | Hyperlinks (underline) |

### Text Color Rules

- **Maximum 3 text colors** in a single design
- **Never use a text color that doesn't meet WCAG AA (4.5:1)** for normal text
- **Headline color** : Always Brand Blue or Dark Navy (never light colors on light backgrounds)
- **Body text** : Always Dark Navy or White (maintain readability)
- **Avoid** : Light Gray on light backgrounds, Dark Navy on Brand Blue, multiple accent colors

### Color Combinations to Avoid

- Light Blue on White (insufficient contrast)
- Brand Green on Brand Blue (insufficient contrast)
- Light colors on light backgrounds
- Dark Navy on Brand Blue

---

## 5. FONT WEIGHT USAGE

### Weight 400 (Regular)

**Use for** : Body text, descriptions, explanations

**Never** : Headlines, CTA labels (except very small text)

**Example** :

```
"Learn strategic guidance for market entry across African economies."
(Body text for sub-headline)
```

### Weight 500 (Medium)

**Use for** : CTA labels, emphasis within body text, metadata

**Sparingly** : Can be used for very small headlines (not recommended)

**Example** :

```
"Sign Up For Webinar" (button label)
```

### Weight 600 (Semibold)

**Use for** : Subheadings, secondary emphasis, small headlines

**Example** :

```
"Key Market Insights" (subheading)
```

### Weight 700 (Bold)

**Use for** : Main headlines, primary emphasis

**Default weight** for H1 and H2

**Example** :

```
"Navigate African Markets with Confidence" (H1 headline)
```

### Weight 800 (Extrabold)

**Use for** : Hero text, maximum emphasis, very large headlines

**Caution** : Can appear heavy. Use only for largest headlines (72px+)

**Example** :

```
"STRATEGY FOR GROWTH" (Hero text, 96px)
```

### Weight Combinations Per Design

- **Recommended** : Weight 400 + Weight 700 (regular body + bold headlines)
- **Acceptable** : Weight 400 + Weight 600 (for subtle hierarchy)
- **Acceptable** : Weight 500 + Weight 700 (for modern, punchy feel)
- **Avoid** : More than 2 weights in a single design

---

## 6. ALIGNMENT AND JUSTIFICATION

### Left Align

**Default for body text** (most readable)

**Characteristics** :

- Ragged right edge
- Natural word spacing
- Best for readability
- Professional standard

**Use for** : Body text, lists, most copy

### Center Align

**Use for** :

- Formal documents
- Titles on landing pages
- Centered single headlines
- Symmetrical compositions

**Caution** :

- Less scannable than left-aligned
- Use sparingly
- Poor for body text

### Right Align

**Use for** :

- Directional emphasis (pointing right)
- Arabic or RTL languages (automatic)
- Very rare in Western design

**Caution** :

- Difficult to read
- Avoid for body text

### Justified Align

**Avoid** : Creates poor word spacing and hyphenation

**Only use if** : Professional publication with professional typesetting software

---

## 7. TYPOGRAPHY FOR DIFFERENT FORMATS

### Flyer Typography

```
HEADLINE:       Inter 56px, Weight 700, #013C87
SUBHEADING:     Inter 32px, Weight 600, #0A2555
BODY:           Inter 16px, Weight 400, #0A2555
CTA LABEL:      Inter 18px, Weight 600, #FFFFFF on #1D7742
METADATA:       Inter 12px, Weight 500, #666666
```

### Poster Typography

```
HEADLINE:       Inter 72–96px, Weight 700, #013C87
SUPPORTING:     Inter 40px, Weight 600, #0A2555
BODY:           Inter 18–22px, Weight 400, #0A2555
CTA:            Inter 24px, Weight 600, #FFFFFF on #1D7742
METADATA:       Inter 14px, Weight 400, #666666
```

### Social Media (1:1, 4:5, 9:16)

```
HEADLINE:       Inter 48–64px, Weight 700, #FFFFFF (on image overlay)
SUPPORTING:     Inter 28–32px, Weight 600, #FFFFFF or #013C87
CTA STICKER:    Inter 16–18px, Weight 600, #FFFFFF on #1D7742
```

### Digital Banner (1920x1080)

```
HEADLINE:       Inter 64px, Weight 700, #013C87
SUBHEADING:     Inter 32px, Weight 600, #0A2555
BODY:           Inter 18px, Weight 400, #0A2555
CTA BUTTON:     Inter 16px, Weight 600, #FFFFFF on #1D7742
```

### Email Newsletter

```
SUBJECT LINE:   Inter 18–20px, Weight 700, #013C87
SECTION TITLE:  Inter 24px, Weight 700, #013C87
BODY:           Inter 16px, Weight 400, #0A2555, Line height 1.8
CTA LINK:       Inter 16px, Weight 600, #2BA696, Underlined
```

---

## 8. READING COMFORT CHECKLIST

Before finalizing typography:

- [ ] Body text is at least 14px (16px recommended for web)
- [ ] Line height is minimum 1.6 for body text
- [ ] Line length is 45–75 characters (ideal)
- [ ] Headline contrast ratio is minimum 4.5:1
- [ ] Body text contrast ratio is minimum 4.5:1
- [ ] No more than 2 font weights used
- [ ] No more than 3 text colors used
- [ ] Text alignment is consistent throughout
- [ ] Letter spacing supports readability (not cramped)
- [ ] Hierarchy is visually obvious (size, weight, color)
- [ ] No text is skewed, distorted, or rotated excessively
- [ ] Font is web-safe or properly licensed
- [ ] Text is not overlaid on complex imagery without darkening background
- [ ] CTA text is visually prominent and easy to locate

---

## 9. MULTILINGUAL TYPOGRAPHY

### Language Support

**Primary** : French, English

**Supported** : Swahili, Arabic, other African languages (via font support)

### French Typography Specifics

- Space before: !, ?, :, ; (French convention)
- Line length accounts for longer text (French is ~15% longer than English)
- Accented characters (é, è, ê, ë, à, ù, ç) are supported in Inter

### English Typography

- No space before: !, ?, :, ;
- Slightly shorter line lengths possible
- All standard characters supported

### Arabic/RTL Languages

- Text direction: right-to-left
- Alignment: right-aligned
- Font still Inter (Inter supports Arabic)
- Line height and spacing: same as LTR

---

## 10. TYPOGRAPHY MISTAKES TO AVOID

### Mistake 1: Too Many Font Weights

```
❌ WRONG:
Headline: Weight 800
Subheading: Weight 700
Body: Weight 600
Metadata: Weight 500
(too much variation, hierarchy unclear)

✅ RIGHT:
Headline: Weight 700
Body: Weight 400
(clear, professional, restrained)
```

### Mistake 2: Text Too Small

```
❌ WRONG: Body text at 11px
✅ RIGHT: Body text at 16px minimum
```

### Mistake 3: Insufficient Line Height

```
❌ WRONG: Line height 1.2 for body text (cramped)
✅ RIGHT: Line height 1.6–1.8 for body text (readable)
```

### Mistake 4: Poor Contrast

```
❌ WRONG: Medium Gray text on Light Gray background (1.5:1 contrast)
✅ RIGHT: Dark Navy on White (9.5:1 contrast)
```

### Mistake 5: Mixing Serif and Sans-serif

```
❌ WRONG: Georgia headlines + Inter body (jarring combination)
✅ RIGHT: Inter headlines + Inter body (cohesive)
```

### Mistake 6: All Caps for Body Text

```
❌ WRONG: "LEARN MORE ABOUT OUR SERVICES IN AFRICAN MARKETS"
✅ RIGHT: "Learn More About Our Services in African Markets"
```

### Mistake 7: Rotated Text

```
❌ WRONG: Rotating text for "creative effect" (unreadable)
✅ RIGHT: Keeping text level and readable
```

---

## 11. QUICK REFERENCE: STANDARD SIZES

```
Hero / Campaign:     72–96px | Weight 700
H1 / Main Headline:  48–64px | Weight 700
H2 / Section Title:  32–40px | Weight 600–700
H3 / Subsection:     24–28px | Weight 600
Subtitle / Lead:     18–22px | Weight 500–600
Body / Regular:      14–18px | Weight 400
CTA Label:           14–18px | Weight 600
Caption / Small:     10–14px | Weight 400–500
```

---

End of Typography System.
