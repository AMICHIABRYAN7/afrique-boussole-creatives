#!/usr/bin/env python3
"""
build-contact-sheets.py

Generates visual contact sheets for rapid inspection of asset libraries.

Contact sheets are created for:
- Flyers
- Posters
- Advertisements
- Social media
- Photography

Each contact sheet is a grid of thumbnails with labels for quick visual scanning.

Requires: PIL (Pillow)

Installation:
    pip install Pillow

Usage:
    python build-contact-sheets.py
    
    Optional:
    python build-contact-sheets.py --output-dir assets/contact-sheets
    python build-contact-sheets.py --thumbnail-size 200
    python build-contact-sheets.py --max-per-sheet 12
"""

import os
import json
from pathlib import Path
from datetime import datetime
import argparse
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


CONTACT_SHEET_CONFIG = {
    'flyers': {
        'source_dir': 'assets/references/flyers',
        'output_name': 'contact-sheet-flyers.jpg',
        'title': 'Flyer References',
        'columns': 3,
    },
    'posters': {
        'source_dir': 'assets/references/posters',
        'output_name': 'contact-sheet-posters.jpg',
        'title': 'Poster References',
        'columns': 3,
    },
    'advertisements': {
        'source_dir': 'assets/references/advertisements',
        'output_name': 'contact-sheet-advertisements.jpg',
        'title': 'Advertisement References',
        'columns': 3,
    },
    'social': {
        'source_dir': 'assets/references/social',
        'output_name': 'contact-sheet-social.jpg',
        'title': 'Social Media References',
        'columns': 4,
    },
    'photography': {
        'source_dir': 'assets/references/photography',
        'output_name': 'contact-sheet-photography.jpg',
        'title': 'Photography References',
        'columns': 3,
    },
}

SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.jfif', '.png', '.gif', '.webp'}

PADDING = 20
THUMBNAIL_SIZE = 200
MAX_PER_SHEET = 12
QUALITY = 85


def load_manifest(manifest_path):
    """Load the asset manifest."""
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Could not load manifest: {e}")
    return None


def collect_images(source_dir, max_images=None):
    """Collect image files from source directory."""
    images = []
    
    if not os.path.isdir(source_dir):
        return images
    
    for filename in os.listdir(source_dir):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in SUPPORTED_FORMATS:
            full_path = os.path.join(source_dir, filename)
            if os.path.isfile(full_path):
                images.append({
                    'path': full_path,
                    'name': os.path.splitext(filename)[0]
                })
    
    # Sort by name for consistency
    images.sort(key=lambda x: x['name'])
    
    # Limit if specified
    if max_images and len(images) > max_images:
        images = images[:max_images]
    
    return images


def create_contact_sheet(images, config, thumbnail_size, output_path):
    """Create a contact sheet from images."""
    
    if not images:
        print(f"  ⚠️  No images found for {config['title']}")
        return None
    
    columns = config.get('columns', 3)
    rows = (len(images) + columns - 1) // columns
    
    # Thumbnail dimensions
    thumb_w, thumb_h = thumbnail_size, thumbnail_size
    
    # Label height
    label_h = 30
    
    # Sheet dimensions
    sheet_w = columns * thumb_w + (columns + 1) * PADDING
    sheet_h = rows * (thumb_h + label_h) + (rows + 1) * PADDING + 80  # Extra for title
    
    # Create image
    sheet = Image.new('RGB', (sheet_w, sheet_h), color=(255, 255, 255))
    draw = ImageDraw.Draw(sheet)
    
    # Try to load a font
    try:
        title_font = ImageFont.truetype("arial.ttf", 24)
        label_font = ImageFont.truetype("arial.ttf", 10)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
    
    # Draw title
    title = config.get('title', 'Contact Sheet')
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    title_x = (sheet_w - title_w) // 2
    draw.text((title_x, PADDING), title, fill=(0, 0, 0), font=title_font)
    
    # Draw thumbnails
    y_offset = PADDING + 60
    
    for idx, image_info in enumerate(images):
        col = idx % columns
        row = idx // columns
        
        x = PADDING + col * (thumb_w + PADDING)
        y = y_offset + row * (thumb_h + label_h + PADDING)
        
        # Load and resize image
        try:
            img = Image.open(image_info['path'])
            img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            
            # Paste onto sheet
            sheet.paste(img, (x, y))
            
            # Draw label
            label_y = y + thumb_h + 5
            label_text = image_info['name'][:25]  # Truncate long names
            draw.text((x, label_y), label_text, fill=(64, 64, 64), font=label_font)
            
        except Exception as e:
            # Draw placeholder for failed images
            draw.rectangle([x, y, x + thumb_w, y + thumb_h], outline=(200, 200, 200))
            draw.text((x + 10, y + 10), "Error", fill=(255, 0, 0), font=label_font)
    
    # Add metadata footer
    footer = f"Generated {datetime.now().strftime('%Y-%m-%d')} | {len(images)} images"
    draw.text((PADDING, sheet_h - 30), footer, fill=(150, 150, 150), font=label_font)
    
    # Save
    try:
        sheet.save(output_path, quality=QUALITY, optimize=True)
        return output_path
    except Exception as e:
        print(f"  ❌ Error saving contact sheet: {e}")
        return None


def generate_contact_sheets(project_root, output_dir, thumbnail_size, max_per_sheet):
    """Generate all contact sheets."""
    
    if not PIL_AVAILABLE:
        print("⚠️  Pillow not installed. Contact sheets cannot be generated.")
        print("   Install with: pip install Pillow")
        return []
    
    os.makedirs(output_dir, exist_ok=True)
    
    generated = []
    
    print(f"📊 Generating contact sheets...")
    
    for category, config in CONTACT_SHEET_CONFIG.items():
        source_dir = os.path.join(project_root, config['source_dir'])
        output_path = os.path.join(output_dir, config['output_name'])
        
        print(f"  🔄 {config['title']}...")
        
        # Collect images
        images = collect_images(source_dir, max_per_sheet)
        
        if not images:
            print(f"    ⚠️  No images found in {source_dir}")
            continue
        
        # Create sheet
        result = create_contact_sheet(images, config, thumbnail_size, output_path)
        
        if result:
            print(f"    ✅ Generated: {os.path.basename(result)} ({len(images)} images)")
            generated.append({
                'category': category,
                'path': result,
                'count': len(images)
            })
        else:
            print(f"    ❌ Failed to generate")
    
    return generated


def create_index_html(output_dir, contact_sheets):
    """Create an HTML index of contact sheets."""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Afrique Boussole — Contact Sheets</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            padding: 40px 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #013C87;
            margin-bottom: 10px;
            font-size: 2em;
        }
        .subtitle {
            color: #666;
            margin-bottom: 40px;
            font-size: 0.95em;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            text-decoration: none;
            color: inherit;
            cursor: pointer;
        }
        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .card-content {
            padding: 15px;
        }
        .card-title {
            font-weight: 600;
            color: #013C87;
            margin-bottom: 5px;
        }
        .card-meta {
            font-size: 0.85em;
            color: #999;
        }
        .footer {
            margin-top: 60px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #999;
            font-size: 0.9em;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Afrique Boussole Contact Sheets</h1>
        <p class="subtitle">Quick visual reference library for design assets</p>
        
        <div class="gallery">
"""
    
    for sheet in contact_sheets:
        category_title = sheet['category'].replace('_', ' ').title()
        file_path = os.path.basename(sheet['path'])
        
        html_content += f"""
            <a href="{file_path}" class="card">
                <img src="{file_path}" alt="{category_title}">
                <div class="card-content">
                    <div class="card-title">{category_title}</div>
                    <div class="card-meta">{sheet['count']} images</div>
                </div>
            </a>
"""
    
    html_content += """
        </div>
        
        <div class="footer">
            <p>Generated on """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
            <p>Afrique Boussole Creative Intelligence Skill</p>
        </div>
    </div>
</body>
</html>
"""
    
    index_path = os.path.join(output_dir, 'index.html')
    try:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return index_path
    except Exception as e:
        print(f"⚠️  Could not create index HTML: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Generate Afrique Boussole contact sheets for asset inspection'
    )
    parser.add_argument(
        '--output-dir',
        default='assets/contact-sheets',
        help='Output directory for contact sheets (default: assets/contact-sheets)'
    )
    parser.add_argument(
        '--thumbnail-size',
        type=int,
        default=THUMBNAIL_SIZE,
        help=f'Thumbnail size in pixels (default: {THUMBNAIL_SIZE})'
    )
    parser.add_argument(
        '--max-per-sheet',
        type=int,
        default=MAX_PER_SHEET,
        help=f'Maximum images per sheet (default: {MAX_PER_SHEET})'
    )
    parser.add_argument(
        '--no-index',
        action='store_true',
        help='Skip HTML index generation'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Resolve paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    output_dir = os.path.join(project_root, args.output_dir)
    
    if args.verbose:
        print(f"📁 Project root: {project_root}")
        print(f"📁 Output directory: {output_dir}")
        print(f"📐 Thumbnail size: {args.thumbnail_size}px")
        print(f"🔢 Max per sheet: {args.max_per_sheet}")
        print()
    
    if not PIL_AVAILABLE:
        print("❌ Pillow is required but not installed.")
        print("   Install with: pip install Pillow")
        return 1
    
    # Generate contact sheets
    generated = generate_contact_sheets(
        project_root,
        output_dir,
        args.thumbnail_size,
        args.max_per_sheet
    )
    
    if not generated:
        print("⚠️  No contact sheets generated")
        return 1
    
    # Generate index
    if not args.no_index:
        print()
        print("📄 Generating HTML index...")
        index_path = create_index_html(output_dir, generated)
        if index_path:
            print(f"✅ Index created: {os.path.basename(index_path)}")
    
    print()
    print(f"✅ Contact sheets generated in {output_dir}")
    print(f"   Total sheets: {len(generated)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
