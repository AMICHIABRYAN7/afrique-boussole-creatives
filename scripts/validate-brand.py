#!/usr/bin/env python3
"""
Afrique Boussole Brand Validation Script
Checks that brand system is correctly structured and complete
"""

import os
import json
from pathlib import Path

# Brand colors to verify
BRAND_COLORS = {
    "primary_blue": "#013C87",
    "primary_green": "#1D7742",
    "neutral_white": "#FFFFFF",
    "neutral_ivory": "#F7F4EC",
    "neutral_dark": "#0A2555"
}

# Required brand files
REQUIRED_FILES = [
    "references/brand-system.md",
    "references/creative-strategy.md",
    "references/creative-framework.md",
    "references/composition-system.md",
    "references/typography-system.md",
    "references/photography-direction.md",
    "references/image-generation.md",
    "references/campaign-formats.md",
    "references/platform-guidelines.md",
    "references/quality-control.md",
    "references/anti-patterns.md",
    "references/logo-usage.md",
    "references/design-system.md"
]

# Required directories
REQUIRED_DIRS = [
    "assets/brand/logos",
    "assets/brand/icons",
    "assets/brand/symbols",
    "assets/visual-system/compass",
    "assets/visual-system/africa-map",
    "assets/visual-system/grids",
    "assets/visual-system/routes",
    "assets/visual-system/coordinates",
    "assets/visual-system/patterns",
    "assets/references/posters",
    "assets/references/flyers",
    "assets/references/social",
    "assets/references/advertisements",
    "assets/references/corporate",
    "assets/templates",
    "workflows",
    "schemas",
    "scripts",
    "examples"
]

def check_file_exists(file_path, base_dir):
    """Check if a file exists"""
    full_path = os.path.join(base_dir, file_path)
    return os.path.isfile(full_path)

def check_dir_exists(dir_path, base_dir):
    """Check if a directory exists"""
    full_path = os.path.join(base_dir, dir_path)
    return os.path.isdir(full_path)

def check_brand_references(base_dir):
    """Check if brand colors are mentioned in brand-system.md"""
    brand_file = os.path.join(base_dir, "references/brand-system.md")
    if not os.path.isfile(brand_file):
        return False, "Brand system file not found"
    
    with open(brand_file, 'r') as f:
        content = f.read()
    
    missing_colors = []
    for color_name, hex_value in BRAND_COLORS.items():
        if hex_value not in content:
            missing_colors.append(f"{color_name} ({hex_value})")
    
    if missing_colors:
        return False, f"Missing color references: {', '.join(missing_colors)}"
    
    return True, "All brand colors referenced"

def validate_json_schemas(base_dir):
    """Validate that JSON schemas are valid"""
    schemas_dir = os.path.join(base_dir, "schemas")
    if not os.path.isdir(schemas_dir):
        return False, "Schemas directory not found"
    
    schema_files = []
    errors = []
    
    for filename in os.listdir(schemas_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(schemas_dir, filename)
            try:
                with open(file_path, 'r') as f:
                    json.load(f)
                schema_files.append(filename)
            except json.JSONDecodeError as e:
                errors.append(f"{filename}: {str(e)}")
    
    if errors:
        return False, f"Invalid JSON schemas: {'; '.join(errors)}"
    
    if len(schema_files) < 3:
        return False, f"Expected 3+ schema files, found {len(schema_files)}"
    
    return True, f"Valid JSON schemas: {', '.join(schema_files)}"

def validate_workflows(base_dir):
    """Check that workflow files exist"""
    workflows_dir = os.path.join(base_dir, "workflows")
    if not os.path.isdir(workflows_dir):
        return False, "Workflows directory not found"
    
    expected_workflows = [
        "flyer-workflow.md",
        "poster-workflow.md",
        "ad-workflow.md",
        "social-workflow.md",
        "campaign-workflow.md",
        "adaptation-workflow.md"
    ]
    
    found = []
    missing = []
    
    for workflow in expected_workflows:
        file_path = os.path.join(workflows_dir, workflow)
        if os.path.isfile(file_path):
            found.append(workflow)
        else:
            missing.append(workflow)
    
    if missing:
        return False, f"Missing workflows: {', '.join(missing)}"
    
    return True, f"All {len(found)} workflows present"

def run_validation(base_dir):
    """Run complete validation"""
    print("=" * 60)
    print("AFRIQUE BOUSSOLE BRAND VALIDATION")
    print("=" * 60)
    
    # Check base directory exists
    if not os.path.isdir(base_dir):
        print(f"ERROR: Base directory not found: {base_dir}")
        return False
    
    all_passed = True
    
    # Check required files
    print("\n[1] Checking required files...")
    missing_files = []
    for file_path in REQUIRED_FILES:
        if not check_file_exists(file_path, base_dir):
            missing_files.append(file_path)
            all_passed = False
    
    if missing_files:
        print(f"    ❌ Missing {len(missing_files)} files:")
        for f in missing_files:
            print(f"       - {f}")
    else:
        print(f"    ✓ All {len(REQUIRED_FILES)} reference files present")
    
    # Check required directories
    print("\n[2] Checking required directories...")
    missing_dirs = []
    for dir_path in REQUIRED_DIRS:
        if not check_dir_exists(dir_path, base_dir):
            missing_dirs.append(dir_path)
            all_passed = False
    
    if missing_dirs:
        print(f"    ❌ Missing {len(missing_dirs)} directories:")
        for d in missing_dirs:
            print(f"       - {d}")
    else:
        print(f"    ✓ All {len(REQUIRED_DIRS)} directories present")
    
    # Check brand references
    print("\n[3] Checking brand system references...")
    passed, message = check_brand_references(base_dir)
    if passed:
        print(f"    ✓ {message}")
    else:
        print(f"    ❌ {message}")
        all_passed = False
    
    # Check JSON schemas
    print("\n[4] Validating JSON schemas...")
    passed, message = validate_json_schemas(base_dir)
    if passed:
        print(f"    ✓ {message}")
    else:
        print(f"    ❌ {message}")
        all_passed = False
    
    # Check workflows
    print("\n[5] Validating workflows...")
    passed, message = validate_workflows(base_dir)
    if passed:
        print(f"    ✓ {message}")
    else:
        print(f"    ❌ {message}")
        all_passed = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ VALIDATION PASSED: Skill structure is complete")
        print("=" * 60)
        return True
    else:
        print("❌ VALIDATION FAILED: Please address issues above")
        print("=" * 60)
        return False

if __name__ == "__main__":
    import sys
    
    # Get base directory (script directory parent)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Run validation
    passed = run_validation(base_dir)
    sys.exit(0 if passed else 1)
