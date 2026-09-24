# Afrique Boussole — Anti-Patterns

## Overview

This document explicitly defines what NOT to do.

Anti-patterns are common design mistakes that undermine brand identity, readability, and strategic effectiveness.

---

## 1. COLOR ANTI-PATTERNS

### Anti-Pattern 1: Substituting Brand Colors

**What happens** : Brand Blue #013C87 replaced with Royal Blue, Cobalt, or "similar" blue

**Why it fails** :

- Breaks brand recognition
- Inconsistent across campaign
- Dilutes brand equity
- Looks amateurish ("I didn't have the exact color")

**What to do** :

- Always use exact hex values: #013C87 and #1D7742
- If palette expansion needed, add APPROVED secondary colors
- Never substitute arbitrarily

---

### Anti-Pattern 2: Using More Than 5 Colors

**What happens** : Rainbow palette, every element a different color

**Why it fails** :

- Chaotic and unprofessional
- No clear hierarchy
- Overwhelming to view
- Feels like a template

**What to do** :

- Limit palette to 3-5 colors total
- Use Brand Blue + Brand Green + neutrals as default
- Add accent colors only if strategic

---

### Anti-Pattern 3: Insufficient Color Contrast

**What happens** : Light gray text on light gray background, low contrast ratio

**Why it fails** :

- Text unreadable
- Violates WCAG accessibility standards
- Excludes vision-impaired audience
- Looks broken or unintentional

**What to do** :

- Test all text color combinations against WCAG AA standard (4.5:1 minimum)
- Use color contrast checker tools
- Dark Navy on White or White on Brand Blue = good options

---

### Anti-Pattern 4: Oversaturated or Desaturated Colors

**What happens** : Brand colors pushed to extreme saturation or completely washed out

**Why it fails** :

- Doesn't match brand colors
- Looks artificial or low-quality
- Hard on the eyes
- Inconsistent with reference materials

**What to do** :

- Use color values as specified in brand system
- Light color correction is acceptable, extreme saturation is not
- If styling photos, maintain natural appearance

---

### Anti-Pattern 5: Gradient Between Brand Blue and Brand Green

**What happens** : Gradient from #013C87 to #1D7742 for "creative effect"

**Why it fails** :

- Text on gradient becomes unreadable
- Doesn't appear intentional or strategic
- Strains the eye
- Looks like low-quality web design from 2000s

**What to do** :

- Use solid colors or gradients within same color family
- If gradient needed, use Brand Blue to lighter blue or Brand Green to lighter green
- Ensure text remains readable (place on non-gradient area or use solid color overlay)

---

## 2. TYPOGRAPHY ANTI-PATTERNS

### Anti-Pattern 6: Text Too Small

**What happens** : Body text 11px, headlines 32px

**Why it fails** :

- Text unreadable on mobile
- Violates readability standards
- Excludes vision-impaired users
- Frustrates audience

**What to do** :

- Minimum 14px for digital body text (16px recommended)
- Minimum 10pt for print body text
- Minimum 48px for headlines (smaller tests at thumbnail size)

---

### Anti-Pattern 7: Too Many Font Weights or Families

**What happens** : Headline (Weight 800, Serif), Subheading (Weight 700, Sans), Body (Weight 500, Different Sans), Labels (Weight 600, Serif)

**Why it fails** :

- Chaotic and unprofessional
- No clear hierarchy
- Looks hastily assembled
- Violates typography system

**What to do** :

- Maximum 2 font weights per design (typically 400 + 700)
- Use one font family (Inter is default)
- If secondary font needed, use only for specific context (monospace for data)

---

### Anti-Pattern 8: All Caps Body Text

**What happens** : Entire paragraph in uppercase letters

**Why it fails** :

- Significantly harder to read
- Looks like shouting
- Reduces reading speed
- Violates readability standards

**What to do** :

- Use regular sentence case for body text
- All-caps acceptable for: very short headlines, labels, acronyms only

---

### Anti-Pattern 9: Insufficient Line Height

**What happens** : Body text with line height 1.2 or less

**Why it fails** :

- Text cramped and hard to read
- Lines run together
- Reduces comprehension
- Looks unprofessional

**What to do** :

- Minimum line height 1.5 for body text
- Recommended 1.6-1.8 for online content
- Tighter line height acceptable for headlines (1.1-1.2)

---

### Anti-Pattern 10: Rotated Text (More Than 0°)

**What happens** : Headline rotated 45° or at arbitrary angle for "creativity"

**Why it fails** :

- Text completely unreadable
- No strategic reason
- Looks broken or amateurish
- Violates accessibility

**What to do** :

- Keep text horizontal
- Never rotate for aesthetic effect without strategic purpose
- If must rotate, angle ≤ 15° maximum

---

### Anti-Pattern 11: Text Overlaid on Busy, Uncontrasty Image

**What happens** : White text on photo of light-colored landscape, completely illegible

**Why it fails** :

- Message unreadable
- Strategic message lost
- Looks broken
- Audience can't understand content

**What to do** :

- Darken image background (overlay, gradient, blur)
- Place text on high-contrast area
- Use text shadow or background panel (subtle, professional)
- Test readability before finalizing

---

## 3. COMPOSITION ANTI-PATTERNS

### Anti-Pattern 12: Multiple Competing Focal Points

**What happens** : Image, headline, button, logo all fighting for attention

**Why it fails** :

- Eye doesn't know where to look first
- No clear hierarchy
- Message unclear
- Feels cluttered

**What to do** :

- Designate ONE primary focal point
- Make it 2-3x larger or more colorful than others
- Others play supporting roles
- Test with eye flow

---

### Anti-Pattern 13: Cramped Composition (No Breathing Room)

**What happens** : Every millimeter filled with content, no negative space

**Why it fails** :

- Overwhelming to viewer
- Looks desperate or unprofessional
- Reduces focus on primary message
- Violates design principles

**What to do** :

- Reserve 15-25% of canvas as intentional negative space
- Group related elements, leave space between groups
- Use margins and padding consistently
- Let design breathe

---

### Anti-Pattern 14: Random, Unaligned Placement

**What happens** : Elements placed arbitrarily, no grid or alignment system

**Why it fails** :

- Looks amateurish and chaotic
- No visual coherence
- Scanning difficult
- Feels unintentional

**What to do** :

- Use grid system (8px, 4px, or 16px)
- Align all elements to grid
- Consistent margins and spacing
- Invisible structure, visible professionalism

---

### Anti-Pattern 15: Poor Aspect Ratio Adaptation

**What happens** : A4 flyer simply shrunk to fit 1:1 social media (image stretched, text illegible)

**Why it fails** :

- Image distorted
- Text unreadable
- Doesn't feel intentional
- Wastes visual real estate

**What to do** :

- Recompose for each format (don't just shrink)
- Crop image appropriately
- Reposition text and elements
- Test readability on intended platform

---

## 4. IMAGE ANTI-PATTERNS

### Anti-Pattern 16: Generic Stock Photography

**What happens** : Using obvious stock photo (everyone at laptop smiling, generic office)

**Why it fails** :

- Could be for ANY company
- Not authentic to Afrique Boussole
- Audience recognizes it as stock
- Undermines credibility

**What to do** :

- Use authentic, specific photography
- Commission original if budget allows
- Choose stock carefully (not obviously generic)
- Ensure image supports message uniquely

---

### Anti-Pattern 17: Low Quality or Blurry Images

**What happens** : Out-of-focus photo, pixelated, poor lighting

**Why it fails** :

- Looks unprofessional
- Reflects poorly on brand
- Message unclear
- Feels rushed or cheap

**What to do** :

- Use high-resolution images minimum 1080px
- Ensure sharp focus on subject
- Professional lighting
- Test before publishing

---

### Anti-Pattern 18: Stereotypical or Clichéd Imagery

**What happens** : Safari animals, "tribal" patterns, poverty, stereotypical African imagery

**Why it fails** :

- Reduces Africa to clichés
- Offensive or reductive
- Not contemporary or professional
- Undermines strategic positioning

**What to do** :

- Use modern, professional imagery
- Authentic representation of contemporary Africa
- Diverse, not stereotyped
- Strategic tie-in to message

---

### Anti-Pattern 19: Image Competing With Headline

**What happens** : Image is so striking it dominates, headline becomes secondary

**Why it fails** :

- Primary message gets lost
- Eye goes to image first, misses message
- Strategic communication fails
- Hierarchy broken

**What to do** :

- Image should support headline, not compete
- If image is very strong, pair with equally strong headline
- Or place image as background with text overlay
- Test hierarchy before finalizing

---

## 5. MESSAGE AND CONTENT ANTI-PATTERNS

### Anti-Pattern 20: Unclear or Vague Message

**What happens** : "Explore opportunities" or "Learn more" (about what?)

**Why it fails** :

- Audience doesn't understand value proposition
- CTA is confusing
- Strategic goal not communicated
- Message gets lost

**What to do** :

- Be specific: "Download our African Market Guide" (what they get)
- Primary message must be clear within 2 seconds
- Use concrete benefits, not vague language

---

### Anti-Pattern 21: Multiple Competing CTAs

**What happens** : "Sign up," "Learn more," "Download," "Contact us" all equally prominent

**Why it fails** :

- Audience confused about what to do
- Conversion rate drops
- Undermines strategic objective
- Looks indecisive

**What to do** :

- ONE primary CTA
- Optional secondary CTA if truly necessary (but not competing)
- Primary CTA visually prominent
- Clear action, clear benefit

---

### Anti-Pattern 22: False or Exaggerated Claims

**What happens** : "99% success rate" or "Guaranteed results" without basis

**Why it fails** :

- Damages trust when discovered
- Potentially illegal (FTC violations)
- Feels dishonest
- Undermines brand credibility

**What to do** :

- Only include TRUE statements
- Back claims with evidence (if claiming data)
- Use placeholders if data unavailable ("Trusted by X+ clients" not "99% success rate")
- Never invent testimonials or statistics

---

### Anti-Pattern 23: Missing or Unclear CTA

**What happens** : No clear next action, or CTA is buried and unclear

**Why it fails** :

- Audience doesn't know what to do
- Objective not achieved
- Conversion rate zero
- Wasted creative effort

**What to do** :

- Every creative needs clear CTA
- CTA must be action-specific ("Sign up now," not "Click here")
- CTA must be visually prominent
- CTA must be easily accessible/clickable

---

## 6. DESIGN SYSTEM ANTI-PATTERNS

### Anti-Pattern 24: Inconsistent Brand Appearance Across Materials

**What happens** : Flyer uses blue background, poster uses green, social uses gray; colors don't match

**Why it fails** :

- Breaks brand recognition
- Looks like different companies
- Confuses audience
- Undermines cohesion

**What to do** :

- Consistent color palette across all materials
- Consistent typography treatment
- Consistent logo usage
- Consistent visual style

---

### Anti-Pattern 25: Excessive Effects and Decorations

**What happens** : Drop shadows, glows, 3D effects, distortions, excessive gradients

**Why it fails** :

- Looks amateurish or dated
- Distracts from message
- Reduces professionalism
- Violates modern design standards

**What to do** :

- Minimal effects (drop shadow subtle and purposeful)
- No 3D effects unless specifically strategic
- No distortions unless artistic intent
- Let content speak, don't decorate excessively

---

### Anti-Pattern 26: Misaligned or Inconsistent Spacing

**What happens** : Elements have random spacing, no system, inconsistent margins

**Why it fails** :

- Looks chaotic and unintentional
- Feels unprofessional
- Scanning difficult
- Breaks visual coherence

**What to do** :

- Use spacing scale (4px, 8px, 16px, 24px, 32px, etc.)
- Consistent margins throughout
- Related elements group together
- Unrelated elements separated consistently

---

## 7. PLATFORM AND TECHNICAL ANTI-PATTERNS

### Anti-Pattern 27: Incorrect Dimensions or Aspect Ratio

**What happens** : Image provided at 1024x768 for 1:1 social (stretched and distorted)

**Why it fails** :

- Image distorted
- Not optimized for platform
- Looks careless
- Technical failure

**What to do** :

- Always provide correct dimensions for intended platform
- Maintain aspect ratio (never stretch)
- Test on actual platform before publishing

---

### Anti-Pattern 28: Text Unreadable at Intended Size

**What happens** : Headline at 18px (unreadable at thumbnail size)

**Why it fails** :

- Message unclear on platform
- Message lost in feed
- Engagement suffers
- Objective not met

**What to do** :

- Test readability at actual viewing size
- 1:1 social: Minimum 28px headline (readable at 200px width)
- 16:9 web: Minimum 48px headline (readable at 1920px width)
- Print: Scale appropriately to viewing distance

---

### Anti-Pattern 29: Large File Size (Slow Loading)

**What happens** : Image 15MB, takes 30 seconds to load

**Why it fails** :

- Audience abandons before seeing content
- Poor user experience
- Bounces website
- Conversion drops

**What to do** :

- Optimize image file size (JPEG compression, appropriate resolution)
- Web: <2MB ideal
- Mobile: <1MB preferred
- Test load time before publishing

---

### Anti-Pattern 30: Inaccessible Design (No Captions, Alt Text, Etc.)

**What happens** : Video no captions, image no alt text, low contrast

**Why it fails** :

- Excludes vision-impaired and hearing-impaired users
- Violates WCAG accessibility standards
- Potentially violates law (ADA, etc.)
- Reduces audience reach

**What to do** :

- All images: Alt text provided
- All video: Captions or subtitles
- Color contrast: WCAG AA minimum
- Keyboard navigation supported
- Readable by screen readers

---

## 8. SUMMARY: TOP 10 CRITICAL ANTI-PATTERNS

If you do only ONE thing, avoid these:

1. **Substituting brand colors** with unapproved alternatives
2. **Text too small** to read
3. **Multiple competing focal points** (unclear hierarchy)
4. **Generic stock photography** that could be for any brand
5. **Insufficient contrast** (text unreadable)
6. **No clear CTA** (audience doesn't know what to do)
7. **Too many colors** (>5 total)
8. **Cramped composition** (no breathing room)
9. **False or exaggerated claims** (damages trust)
10. **Design feels like a template** (not authentically Afrique Boussole)

---

End of Anti-Patterns.
