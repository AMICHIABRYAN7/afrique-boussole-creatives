#!/usr/bin/env python3
"""
build-asset-manifest.py

Auto-scans Afrique Boussole assets directory and updates/builds the manifest.json.

Behavior:
- Scans all asset folders (brand, visual-system, references, team)
- Detects supported file types (.svg, .png, .jpg, .jpeg, .jfif, .gif, .webp)
- Preserves existing metadata (id, type, tags, usage, priority, status)
- Adds new assets with default metadata
- Updates generated timestamp
- Does NOT silently delete valid entries — preserves all active assets

Usage:
    python build-asset-manifest.py
    
    Optional:
    python build-asset-manifest.py --output path/to/manifest.json
    python build-asset-manifest.py --scan-dir path/to/assets
"""

import os
import json
from pathlib import Path
from datetime import datetime
import argparse
import sys


SUPPORTED_FORMATS = {'.svg', '.png', '.jpg', '.jpeg', '.jfif', '.gif', '.webp'}

ASSET_TYPE_MAPPING = {
    'brand/logos': {'type': 'brand_asset', 'category': 'logo'},
    'brand/icons': {'type': 'brand_asset', 'category': 'icon'},
    'brand/symbols': {'type': 'brand_asset', 'category': 'symbol'},
    'visual-system/compass': {'type': 'brand_asset', 'category': 'compass'},
    'visual-system/africa-map': {'type': 'brand_asset', 'category': 'map'},
    'visual-system/routes': {'type': 'brand_asset', 'category': 'route'},
    'visual-system/grids': {'type': 'brand_asset', 'category': 'grid'},
    'visual-system/coordinates': {'type': 'brand_asset', 'category': 'coordinate'},
    'visual-system/patterns': {'type': 'brand_asset', 'category': 'pattern'},
    'references/flyers': {'type': 'creative_reference', 'category': 'flyer'},
    'references/posters': {'type': 'creative_reference', 'category': 'poster'},
    'references/advertisements': {'type': 'creative_reference', 'category': 'advertisement'},
    'references/social': {'type': 'creative_reference', 'category': 'social'},
    'references/photography': {'type': 'creative_reference', 'category': 'photography'},
    'references/corporate': {'type': 'creative_reference', 'category': 'corporate'},
    'templates/posters': {'type': 'creative_reference', 'category': 'poster_template'},
    'templates/marketing': {'type': 'creative_reference', 'category': 'marketing_template'},
    'templates': {'type': 'creative_reference', 'category': 'template'},
    'projects': {'type': 'brand_asset', 'category': 'project'},
    'team': {'type': 'source_image', 'category': 'team'},
    'archive': {'type': 'archive_asset', 'category': 'archive'},
}

DEFAULT_PRIORITY = {
    'logo': 10,
    'emblem': 9,
    'symbol': 7,
    'map': 7,
    'route': 6,
    'grid': 5,
    'coordinate': 5,
    'pattern': 5,
    'compass': 6,
    'flyer': 5,
    'poster': 5,
    'advertisement': 5,
    'social': 5,
    'photography': 5,
    'team': 5,
}


def generate_asset_id(folder_path, filename):
    """Generate a unique asset ID based on folder and filename."""
    # Extract category from path
    parts = folder_path.split(os.sep)
    
    # Build ID from path components
    if 'visual-system' in parts:
        idx = parts.index('visual-system')
        category = parts[idx + 1] if idx + 1 < len(parts) else 'visual'
    elif 'references' in parts:
        idx = parts.index('references')
        category = parts[idx + 1] if idx + 1 < len(parts) else 'reference'
    elif 'brand' in parts:
        idx = parts.index('brand')
        category = parts[idx + 1] if idx + 1 < len(parts) else 'brand'
    else:
        category = parts[-1] if parts else 'asset'
    
    # Clean filename for ID
    name_base = os.path.splitext(filename)[0]
    name_clean = name_base.lower().replace(' ', '_').replace('-', '_')
    
    # Create ID
    asset_id = f"{category}_{name_clean}"
    
    return asset_id


def get_asset_metadata(file_path, relative_path):
    """Extract and generate metadata for an asset."""
    filename = os.path.basename(file_path)
    folder_path = os.path.dirname(relative_path)
    
    # Normalize paths for comparison (use forward slashes)
    folder_path_normalized = folder_path.replace('\\', '/')
    
    # Determine type and category
    asset_type = 'unknown'
    category = 'other'
    
    # Try exact match first, then partial match
    for path_pattern, meta in ASSET_TYPE_MAPPING.items():
        if path_pattern in folder_path_normalized or folder_path_normalized.startswith(path_pattern):
            asset_type = meta['type']
            category = meta['category']
            break
    
    # Generate ID
    asset_id = generate_asset_id(folder_path, filename)
    
    # Determine priority
    priority = DEFAULT_PRIORITY.get(category, 5)
    
    # Generate name from filename
    name = filename.replace('_', ' ').replace('-', ' ').rsplit('.', 1)[0].title()
    
    # Default tags
    tags = [category]
    if asset_type == 'brand_asset':
        tags.extend(['brand', 'official'])
    elif asset_type == 'creative_reference':
        tags.append('reference')
    
    metadata = {
        'id': asset_id,
        'path': relative_path,
        'type': asset_type,
        'category': category,
        'name': name,
        'description': f"{name} — {category} asset",
        'tags': tags,
        'usage': [],
        'priority': priority,
        'status': 'active'
    }
    
    return metadata


def scan_assets(assets_dir):
    """Scan assets directory and collect all supported files."""
    assets = []
    
    for root, dirs, files in os.walk(assets_dir):
        # Skip .git and other hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for filename in files:
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Check if supported format
            if file_ext in SUPPORTED_FORMATS:
                file_path = os.path.join(root, filename)
                
                # Create relative path from assets dir
                relative_path = os.path.relpath(file_path, assets_dir)
                
                # Normalize path separators to forward slashes for JSON
                relative_path = relative_path.replace(os.sep, '/')
                
                metadata = get_asset_metadata(file_path, relative_path)
                assets.append(metadata)
    
    return assets


def load_existing_manifest(manifest_path):
    """Load existing manifest if it exists."""
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Could not load existing manifest: {e}")
            return None
    return None


def merge_manifests(scanned_assets, existing_manifest):
    """
    Merge scanned assets with existing manifest.
    
    Rules:
    - Preserve existing metadata (type, tags, usage, priority, status) if asset ID matches
    - Add new assets from scan
    - Keep assets marked as inactive/archived
    """
    
    # Build lookup from scanned assets by path
    scanned_by_path = {asset['path']: asset for asset in scanned_assets}
    
    # Build lookup from existing by ID
    existing_by_id = {}
    if existing_manifest and 'assets' in existing_manifest:
        for asset in existing_manifest['assets']:
            existing_by_id[asset['id']] = asset
    
    # Merge
    merged_assets = []
    
    # First, add/update scanned assets
    for path, scanned_asset in scanned_by_path.items():
        asset_id = scanned_asset['id']
        
        # Check if this asset existed before
        if asset_id in existing_by_id:
            existing = existing_by_id[asset_id]
            
            # Preserve important metadata from existing
            scanned_asset['type'] = existing.get('type', scanned_asset['type'])
            scanned_asset['category'] = existing.get('category', scanned_asset['category'])
            scanned_asset['tags'] = existing.get('tags', scanned_asset['tags'])
            scanned_asset['usage'] = existing.get('usage', scanned_asset['usage'])
            scanned_asset['priority'] = existing.get('priority', scanned_asset['priority'])
            scanned_asset['status'] = existing.get('status', scanned_asset['status'])
            scanned_asset['name'] = existing.get('name', scanned_asset['name'])
            scanned_asset['description'] = existing.get('description', scanned_asset['description'])
            
            # Remove from existing to track which were found
            del existing_by_id[asset_id]
        
        merged_assets.append(scanned_asset)
    
    # Then, add assets from existing that were not in scan (archived/inactive)
    for asset_id, existing_asset in existing_by_id.items():
        if existing_asset.get('status') in ['inactive', 'archived', 'deprecated']:
            merged_assets.append(existing_asset)
    
    return merged_assets


def build_manifest(assets):
    """Build the full manifest structure."""
    manifest = {
        'schema_version': '1.0',
        'generated': datetime.now().strftime('%Y-%m-%d'),
        'total_assets': len(assets),
        'assets': sorted(assets, key=lambda x: (-x['priority'], x['id']))
    }
    return manifest


def save_manifest(manifest, manifest_path):
    """Save manifest to JSON file."""
    try:
        os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Error saving manifest: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Build/update Afrique Boussole asset manifest'
    )
    parser.add_argument(
        '--scan-dir',
        default='assets',
        help='Directory to scan for assets (default: assets)'
    )
    parser.add_argument(
        '--output',
        default='assets/manifest.json',
        help='Output manifest path (default: assets/manifest.json)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Resolve paths relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    scan_dir = os.path.join(project_root, args.scan_dir)
    manifest_path = os.path.join(project_root, args.output)
    
    if args.verbose:
        print(f"📁 Project root: {project_root}")
        print(f"📁 Scanning: {scan_dir}")
        print(f"📁 Output: {manifest_path}")
    
    # Check if scan directory exists
    if not os.path.isdir(scan_dir):
        print(f"❌ Asset directory not found: {scan_dir}")
        return 1
    
    # Load existing manifest
    print("📖 Loading existing manifest...")
    existing_manifest = load_existing_manifest(manifest_path)
    
    # Scan assets
    print(f"🔍 Scanning {scan_dir}...")
    scanned_assets = scan_assets(scan_dir)
    
    if args.verbose:
        print(f"   Found {len(scanned_assets)} assets")
    
    # Merge with existing
    print("🔀 Merging with existing manifest...")
    merged_assets = merge_manifests(scanned_assets, existing_manifest)
    
    # Build manifest
    print("🔧 Building manifest...")
    manifest = build_manifest(merged_assets)
    
    # Save manifest
    print(f"💾 Saving to {manifest_path}...")
    if save_manifest(manifest, manifest_path):
        print(f"✅ Manifest updated: {len(manifest['assets'])} total assets")
        print(f"   Schema version: {manifest['schema_version']}")
        print(f"   Generated: {manifest['generated']}")
        return 0
    else:
        print("❌ Failed to save manifest")
        return 1


if __name__ == '__main__':
    sys.exit(main())
