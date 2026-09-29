# Afrique Boussole Scripts

Automation scripts for maintaining and inspecting Afrique Boussole assets.

## Scripts

### build-asset-manifest.py

Auto-scans the `assets/` directory and updates `assets/manifest.json`.

**Purpose:**
- Detect new assets added to folders
- Generate stable asset IDs
- Preserve existing metadata (tags, usage, priority, status)
- Prevent silent deletion of archived/inactive assets
- Keep manifest.json up-to-date

**Usage:**

```bash
# Standard scan (from project root)
python scripts/build-asset-manifest.py

# Verbose output
python scripts/build-asset-manifest.py --verbose

# Custom output path
python scripts/build-asset-manifest.py --output path/to/manifest.json

# Custom assets directory
python scripts/build-asset-manifest.py --scan-dir path/to/assets
```

**Supported formats:**
`.svg`, `.png`, `.jpg`, `.jpeg`, `.jfif`, `.gif`, `.webp`

**Behavior:**
- Scans all subdirectories under `assets/`
- Extracts asset type and category from folder path
- Generates unique ID based on folder + filename
- Preserves existing entries (metadata, status, tags)
- Archives inactive/deprecated entries
- Updates manifest timestamp

**Output:**
```
📖 Loading existing manifest...
🔍 Scanning assets...
   Found XX assets
🔀 Merging with existing manifest...
🔧 Building manifest...
💾 Saving to assets/manifest.json...
✅ Manifest updated: X total assets
```

---

### build-contact-sheets.py

Generates visual contact sheets for rapid inspection of asset libraries.

**Purpose:**
- Create grid layouts of reference images
- Enable quick visual scanning without opening individual files
- Generate HTML index for easy browsing
- Support different asset categories

**Requirements:**
Pillow/PIL library

```bash
pip install Pillow
```

**Usage:**

```bash
# Standard generation (from project root)
python scripts/build-contact-sheets.py

# Verbose output
python scripts/build-contact-sheets.py --verbose

# Custom output directory
python scripts/build-contact-sheets.py --output-dir path/to/sheets

# Custom thumbnail size
python scripts/build-contact-sheets.py --thumbnail-size 300

# Limit images per sheet
python scripts/build-contact-sheets.py --max-per-sheet 20

# Skip HTML index
python scripts/build-contact-sheets.py --no-index
```

**Supported categories:**
- Flyers (3 columns)
- Posters (3 columns)
- Advertisements (3 columns)
- Social media (4 columns)
- Photography (3 columns)

**Output:**

Contact sheets are saved to `assets/contact-sheets/`:
```
contact-sheet-flyers.jpg
contact-sheet-posters.jpg
contact-sheet-advertisements.jpg
contact-sheet-social.jpg
contact-sheet-photography.jpg
index.html
```

Open `index.html` in a browser to browse all contact sheets.

**Output example:**
```
📊 Generating contact sheets...
  🔄 Flyer References...
    ✅ Generated: contact-sheet-flyers.jpg (11 images)
  🔄 Poster References...
    ✅ Generated: contact-sheet-posters.jpg (6 images)
  ...
📄 Generating HTML index...
✅ Index created: index.html
✅ Contact sheets generated in assets/contact-sheets
   Total sheets: 5
```

---

## Integration into Workflows

### Automatic Manifest Updates

Add to CI/CD pipeline or run regularly:

```bash
# Update manifest whenever assets folder changes
python scripts/build-asset-manifest.py
```

### Contact Sheet Generation

Generate before design reviews:

```bash
# Create fresh visual reference library
python scripts/build-contact-sheets.py --verbose
```

### Combined Workflow

```bash
#!/bin/bash
# Update everything
python scripts/build-asset-manifest.py --verbose
python scripts/build-contact-sheets.py --verbose
git add assets/manifest.json assets/contact-sheets/
git commit -m "Update asset manifest and contact sheets"
```

---

## Asset Organization

Scripts work with this folder structure:

```
assets/
├── manifest.json
├── contact-sheets/
│   ├── index.html
│   ├── contact-sheet-*.jpg
│   └── ...
├── brand/
│   ├── logos/
│   ├── icons/
│   └── symbols/
├── visual-system/
│   ├── compass/
│   ├── africa-map/
│   ├── routes/
│   ├── grids/
│   ├── coordinates/
│   └── patterns/
├── references/
│   ├── flyers/
│   ├── posters/
│   ├── advertisements/
│   ├── social/
│   └── photography/
└── team/
```

---

## Adding New Assets

1. **Add files to the appropriate folder** under `assets/`
2. **Run manifest script** to detect and catalog:
   ```bash
   python scripts/build-asset-manifest.py
   ```
3. **Edit manifest.json** if custom metadata needed:
   - tags
   - usage
   - priority
   - description

4. **Regenerate contact sheets** if visual library:
   ```bash
   python scripts/build-contact-sheets.py
   ```

---

## Troubleshooting

### Pillow not installed (contact sheets)

```bash
# Install with pip
pip install Pillow

# Or with conda
conda install pillow
```

### Manifest not updating

- Check file permissions in `assets/` folder
- Ensure files use supported formats (.svg, .png, .jpg, etc.)
- Verify paths don't contain special characters
- Run with `--verbose` flag for debugging

### Contact sheets not generating

- Check that `assets/references/` folders exist
- Ensure images are readable
- Verify Pillow is installed: `python -c "from PIL import Image"`
- Check disk space for output

---

## Performance Notes

- **build-asset-manifest.py**: Fast (~1-2 seconds for 85+ assets)
- **build-contact-sheets.py**: Slower for large libraries (~5-10 seconds)
  - Speed depends on image count and thumbnail size
  - Can be limited with `--max-per-sheet` flag

---

## Development

### Adding New Asset Categories

Edit `ASSET_TYPE_MAPPING` in `build-asset-manifest.py`:

```python
ASSET_TYPE_MAPPING = {
    'path/to/folder': {'type': 'brand_asset', 'category': 'my_category'},
}
```

### Customizing Contact Sheet Layout

Edit `CONTACT_SHEET_CONFIG` in `build-contact-sheets.py`:

```python
CONTACT_SHEET_CONFIG = {
    'my_category': {
        'source_dir': 'assets/references/my_category',
        'output_name': 'contact-sheet-my_category.jpg',
        'title': 'My Category References',
        'columns': 3,  # Adjust grid
    },
}
```

---

## License

These scripts are part of the Afrique Boussole Creative Intelligence Skill.

See LICENSE in the project root.
