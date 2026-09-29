# Asset System — Organization & Discovery

**Version** : 1.0  
**Date** : Septembre 2026  
**Purpose** : Organize and discover Afrique Boussole assets intelligently

---

## Asset Manifest

All assets are catalogued in: `assets/manifest.json`

The manifest allows:
- Programmatic discovery
- Filtering by type/category/tags
- Selection by relevance
- Automatic integration with generation workflows

---

## Three Asset Types

### 1. Brand Assets

Official Afrique Boussole assets that may appear in final creatives:

| Category | Files | Usage | Priority |
|----------|-------|-------|----------|
| **Logos** | Full, mark, monochrome | Primary branding element | 10 |
| **Compass** | Various compass designs | Directional marker, decoration | 9 |
| **Africa Map** | Vector, isometric 3D | Geographic reference | 8 |
| **Icons** | Official icon set | UI, callouts | 7 |
| **Symbols** | Direction arrows, pins, routes | Directional elements | 8 |
| **Patterns** | Grids, geometric repeats | Backgrounds, textures | 6 |

**Rule**: Use the real file. Never ask an image model to recreate them.

### 2. Creative References

Professional example designs for inspiration and principle extraction:

| Category | Qty | Purpose |
|----------|-----|---------|
| Flyers | 4+ | Layout, hierarchy, text/image ratio |
| Posters | 6+ | Distance readability, dominant hook |
| Ads | 5+ | Hook-interest-value-proof-CTA flow |
| Social | 4+ | Format-specific optimization |

**Rule**: Extract principles. Never copy layout, text, or brand from references.

### 3. Source Images

Images intended to appear in final creatives:

- User-provided photos (portraits, products, events)
- Stock photography (curated)
- Generated images (from AI)
- Stock illustrations

---

## Asset Organization

```
assets/
│
├── manifest.json ............ Programmatic catalog
├── asset-index.md ........... Human-readable index
│
├── brand/
│   ├── logos/
│   │   ├── afrique-boussole-logo.svg
│   │   ├── afrique-boussole-logo-dark.svg
│   │   ├── afrique-boussole-emblem.svg
│   │   ├── afrique-boussole-emblem-dark.svg
│   │   └── ...other logos
│   ├── icons/
│   └── symbols/
│       ├── compass-icon-simple.svg
│       ├── compass-icon-detailed.svg
│       ├── direction-arrow.svg
│       ├── location-pin.svg
│       └── ...other symbols
│
├── visual-system/
│   ├── compass/ ............. Compass design references
│   ├── africa-map/ ........... Africa map assets
│   ├── routes/ .............. Pathway and route elements
│   ├── grids/ ............... Grid and structure systems
│   ├── coordinates/ ......... Location and marker systems
│   └── patterns/ ............ Repeating pattern elements
│
├── references/
│   ├── flyers/ .............. 4+ flyer reference designs
│   ├── posters/ ............. 6+ poster reference designs
│   ├── advertisements/ ...... 5+ ad reference designs
│   ├── social/ .............. 4+ social media examples
│   ├── photography/ ......... Stock/example photography
│   └── corporate/ ........... Corporate communication examples
│
├── team/ .................... Team member photos
├── projects/ ................ Project-specific visuals
└── templates/ ............... Design templates
```

---

## Manifest Schema

### Example Entry

```json
{
  "id": "brand_logo_primary",
  "path": "assets/brand/logos/afrique-boussole-logo.svg",
  "type": "brand_asset",
  "category": "logo",
  "name": "Afrique Boussole Primary Logo",
  "description": "Official full logo with wordmark",
  "tags": ["logo", "brand", "primary", "official"],
  "usage": ["final_composition", "all_formats"],
  "priority": 10,
  "status": "active",
  "variants": ["dark", "monochrome", "mark"],
  "file_size_kb": 45,
  "supported_formats": ["svg", "png"],
  "minimum_size_px": 40,
  "clear_space_ratio": 0.25
}
```

### Field Definitions

| Field | Purpose |
|-------|---------|
| `id` | Unique identifier for the asset |
| `path` | Relative path within assets/ |
| `type` | brand_asset / creative_reference / source_image |
| `category` | logo / compass / flyer / poster / etc. |
| `name` | Human-readable name |
| `description` | What it is and when to use |
| `tags` | Searchable tags for filtering |
| `usage` | Where can it appear (final_composition / background / reference / etc.) |
| `priority` | 1-10 (higher = more critical) |
| `status` | active / archived / deprecated |
| `variants` | Related asset variations |
| `file_size_kb` | For load optimization |
| `supported_formats` | svg / png / jpg / etc. |
| `minimum_size_px` | Don't use smaller than this |
| `clear_space_ratio` | For logos (e.g., 0.25 = 1/4 height) |

---

## Asset Selection Process

### Step 1: Identify Category

Based on brief, determine asset category needed:
- Flyer design → Look in `references/flyers/`, brand logos, visual-system/
- Social post → Look in `references/social/`, symbols, patterns
- Campaign → Multiple categories

### Step 2: Query Manifest

Filter manifest by:
- `type`: brand_asset vs reference_asset
- `category`: logo, compass, flyer, poster, etc.
- `tags`: relevant keywords
- `priority`: higher priority first

### Step 3: Select 3–5 References

For references:
- Choose **diverse** compositions (don't pick 3 identical layouts)
- Prioritize **professional** quality
- Include **at least one** that's visually different (to inspire variation)

### Step 4: Mark as Used

When an asset is selected:
- Document its role in the design
- Note if it will be integrated directly (brand asset) or used for principles only (reference)

---

## Manifest Script

Run `scripts/build-asset-manifest.py` to:
- Scan all asset folders
- Detect new files
- Update manifest.json
- Validate paths
- Generate asset-index.md

```bash
python scripts/build-asset-manifest.py
```

---

## Asset Index (Human Readable)

File: `assets/asset-index.md`

Generated automatically from manifest. Lists:
- All brand assets with descriptions
- All reference categories with counts
- Visual system elements
- Quick selection guide

---

## Asset Addition Workflow

When adding new assets:

1. Place file in appropriate subdirectory
2. Run `build-asset-manifest.py`
3. Verify entry in manifest.json
4. Update asset-index.md
5. Test asset selection in a real creative workflow

---

## Brand Asset Preservation

### Rule 1: Use Real Files

When a brand asset exists (logo, compass, etc.):
- ✅ Use the real SVG/PNG file
- ❌ Never ask image model to recreate it
- ❌ Never substitute with a similar-looking asset

### Rule 2: Integration Methods

**Method A**: Direct integration (pass to image generator)
- If host supports `CAP_BRAND_ASSET_INPUT` → Pass the actual file

**Method B**: Reference in prompt
- If host doesn't support file passing → Describe in prompt ("Include official ABC logo")

**Method C**: Deterministic composition
- After image generation → Place exact logo deterministically
- Ensures pixel-perfect positioning and colors

### Rule 3: Color Fidelity

Official colors **must** be exact:
- Primary Blue: `#013C87` (never substitute)
- Primary Green: `#1D7742` (never substitute)

If a logo file is used, its embedded colors are already correct.

---

## Reference Assets: Principle Extraction

### Do Extract:

✅ Composition system (where elements placed)  
✅ Hierarchy (size ratios, visual weight)  
✅ Spacing and white space usage  
✅ Typography rhythm and scale  
✅ Image-to-text ratio  
✅ CTA positioning and styling  
✅ Color balance and contrast  

### Never Copy:

❌ Exact layout (recreate differently while preserving principles)  
❌ Brand or text (use your own)  
❌ Proprietary elements (logos, specific photos)  
❌ Exact color palette (adapt to Afrique Boussole colors)  

---

## Quick Selection Guide

### For a Flyer:
1. Brand logo → `assets/brand/logos/`
2. References → `assets/references/flyers/` (select 3 different layouts)
3. Optional visual → `assets/visual-system/` (compass, patterns, etc.)

### For a Poster:
1. Brand logo → `assets/brand/logos/`
2. References → `assets/references/posters/` (select 3, different distances)
3. Backgrounds → `assets/visual-system/patterns/` or `assets/visual-system/grids/`

### For Social Media:
1. Brand logo or icon → `assets/brand/`
2. References → `assets/references/social/` (select 3 formats)
3. Optional elements → `assets/visual-system/symbols/`

### For Campaign (Multi-format):
1. Brand logo → `assets/brand/logos/`
2. Hero visual → `assets/references/` (pick master reference)
3. Supporting elements → `assets/visual-system/`
4. All references → `assets/references/` (all categories)

---

## Asset Limitations

### What We DON'T Have (Use Placeholders)

If an asset doesn't exist:
- Use explicit placeholder: `[IMAGE_REQUIRED: Product photo 800x600]`
- Never invent an image
- Document what's needed for future sourcing

### Sourcing New Assets

When new assets are needed:
1. Document the requirement
2. Source or create the asset
3. Add to appropriate subdirectory
4. Update manifest
5. Test in creative workflow

---

## Archive and Deprecation

Assets can be marked:
- `status: active` — Use normally
- `status: archived` — Keep for reference, don't use
- `status: deprecated` — Old version, use new one instead

Do NOT delete assets from disk. Mark as archived/deprecated.

---

End of Asset System
