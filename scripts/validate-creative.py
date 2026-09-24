#!/usr/bin/env python3
"""
Creative Quality Validation Script
Checks creative output against Afrique Boussole quality standards
"""

import json
import os
from pathlib import Path

# Quality checklist items
QA_CHECKLIST = {
    "brand": [
        "Logo present and correctly placed",
        "Brand colors (#013C87, #1D7742) used",
        "Typography is Inter (or approved font)",
        "Visual identity consistent"
    ],
    "hierarchy": [
        "Focal point obvious",
        "Primary message dominates",
        "Secondary elements clearly secondary",
        "CTA positioned as endpoint"
    ],
    "composition": [
        "Elements align to grid",
        "Balance appropriate",
        "Negative space 15-25%",
        "Margins consistent"
    ],
    "readability": [
        "Message readable in 2 seconds",
        "Headline legible at viewing distance",
        "Body text scannable",
        "CTA unmistakable"
    ],
    "image": [
        "Image high resolution (1080px+)",
        "Focus sharp",
        "Exposure correct",
        "On-brand content"
    ],
    "typography": [
        "No kerning issues",
        "Font size minimum met",
        "Line height ≥1.5 for body",
        "No orphans/widows"
    ],
    "accessibility": [
        "Color contrast WCAG AA (4.5:1)",
        "No text too small (14px minimum)",
        "Alt text provided",
        "No color-only information"
    ],
    "professionalism": [
        "No typos or grammar errors",
        "No placeholder text",
        "No amateurish effects",
        "Consistency throughout"
    ]
}

# Critical fail indicators
CRITICAL_FAILS = [
    "Brand color substituted with non-brand color",
    "Text unreadable at intended viewing size",
    "Multiple competing focal points",
    "Factually false claims",
    "Placeholder text still present",
    "CTA completely unclear"
]

def create_qa_report(project_name, format_type, review_data=None):
    """Create a QA report"""
    report = {
        "project": project_name,
        "format": format_type,
        "checklist": {
            "brand": {"passed": 0, "total": len(QA_CHECKLIST["brand"]), "items": QA_CHECKLIST["brand"]},
            "hierarchy": {"passed": 0, "total": len(QA_CHECKLIST["hierarchy"]), "items": QA_CHECKLIST["hierarchy"]},
            "composition": {"passed": 0, "total": len(QA_CHECKLIST["composition"]), "items": QA_CHECKLIST["composition"]},
            "readability": {"passed": 0, "total": len(QA_CHECKLIST["readability"]), "items": QA_CHECKLIST["readability"]},
            "image": {"passed": 0, "total": len(QA_CHECKLIST["image"]), "items": QA_CHECKLIST["image"]},
            "typography": {"passed": 0, "total": len(QA_CHECKLIST["typography"]), "items": QA_CHECKLIST["typography"]},
            "accessibility": {"passed": 0, "total": len(QA_CHECKLIST["accessibility"]), "items": QA_CHECKLIST["accessibility"]},
            "professionalism": {"passed": 0, "total": len(QA_CHECKLIST["professionalism"]), "items": QA_CHECKLIST["professionalism"]}
        },
        "critical_failures": [],
        "notes": ""
    }
    
    return report

def print_qa_checklist():
    """Print the QA checklist for manual review"""
    print("=" * 70)
    print("AFRIQUE BOUSSOLE CREATIVE QA CHECKLIST")
    print("=" * 70)
    
    for category, items in QA_CHECKLIST.items():
        print(f"\n[{category.upper()}]")
        for i, item in enumerate(items, 1):
            print(f"  [ ] {i}. {item}")
    
    print("\n" + "=" * 70)
    print("CRITICAL FAIL INDICATORS (if ANY true, reject and revise)")
    print("=" * 70)
    for i, fail in enumerate(CRITICAL_FAILS, 1):
        print(f"  [ ] {i}. {fail}")
    
    print("\n" + "=" * 70)

def generate_qa_template(project_name, format_type, output_file=None):
    """Generate a QA template JSON file"""
    report = create_qa_report(project_name, format_type)
    
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"QA template saved to: {output_file}")
    else:
        print(json.dumps(report, indent=2))

def validate_creative_specs(specs_dict):
    """Validate creative specifications"""
    required_fields = [
        "project_name",
        "format_type",
        "dimensions",
        "primary_message",
        "cta",
        "brand_compliance"
    ]
    
    missing = [f for f in required_fields if f not in specs_dict or not specs_dict[f]]
    
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    
    return True, "All required specifications present"

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--checklist":
            print_qa_checklist()
        elif sys.argv[1] == "--template":
            project = sys.argv[2] if len(sys.argv) > 2 else "Sample Project"
            format_type = sys.argv[3] if len(sys.argv) > 3 else "social_1x1"
            output = sys.argv[4] if len(sys.argv) > 4 else None
            generate_qa_template(project, format_type, output)
        else:
            print("Usage:")
            print("  python validate-creative.py --checklist")
            print("  python validate-creative.py --template [project_name] [format] [output_file]")
    else:
        print_qa_checklist()
