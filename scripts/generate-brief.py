#!/usr/bin/env python3
"""
Generate Creative Brief from Template
Creates structured creative briefs for production
"""

import json
from datetime import datetime

TEMPLATE = {
    "project_name": "Sample Campaign",
    "date_created": datetime.now().strftime("%Y-%m-%d"),
    "client": "Afrique Boussole",
    "brief_prepared_by": "Your Name",
    "objective": "lead_generation",
    "objective_details": "Generate qualified leads for Market Intelligence program",
    "audience": {
        "primary": "African entrepreneurs with 2-10 years business experience",
        "secondary": "C-suite executives, decision-makers",
        "age_range": "28-50",
        "geographic": "Sub-Saharan Africa, Focus: East and West Africa",
        "characteristics": ["Decision-makers", "Business owners", "Strategy-focused"]
    },
    "context": {
        "where_used": ["social_media", "email", "web"],
        "when_used": "Q4 2024",
        "urgency": "high"
    },
    "strategic_insight": {
        "problem": "African entrepreneurs lack access to reliable market intelligence",
        "opportunity": "Provide strategic guidance for market expansion",
        "competitive_context": "Differentiate through authenticity and expertise",
        "afrique_boussole_positioning": "Trusted advisor for African business growth"
    },
    "creative_direction": {
        "suggested_angle": "authority",
        "tone": "Professional, confident, inspiring",
        "visual_direction": "Professional photography of African entrepreneurs",
        "must_include_elements": ["Afrique Boussole logo", "Program name"],
        "must_avoid_elements": ["Stereotypes", "Generic stock photos", "African clichés"]
    },
    "messaging": {
        "primary_message": "Market Intelligence for African Growth",
        "secondary_message": "Expert guidance from professionals who understand your markets",
        "proof_points": ["15+ years in African markets", "500+ entrepreneurs served"],
        "key_benefits": ["Reduce market risk", "Identify opportunities", "Accelerate growth"]
    },
    "cta": {
        "primary_action": "sign_up",
        "cta_copy": "Join Our Community",
        "cta_url": "https://afrique-boussole.com/community",
        "secondary_action": "download"
    },
    "formats": ["social_1x1", "social_4x5", "email_header"],
    "brand_requirements": {
        "logo_required": True,
        "logo_size": "small",
        "color_palette": ["blue_green"],
        "brand_elements_to_include": ["Compass element"]
    },
    "technical_specs": {
        "resolution": "web_72dpi",
        "color_space": "rgb",
        "file_formats": ["jpeg", "png"]
    },
    "deadline": {
        "design_due": datetime.now().strftime("%Y-%m-%d"),
        "final_delivery": "2024-09-30",
        "go_live_date": "2024-10-01"
    },
    "approval_process": {
        "approvers": ["Strategy Lead", "Brand Manager"],
        "revision_rounds": 2
    },
    "additional_notes": "Ensure all claims are backed by data. No invented statistics."
}

def generate_brief(output_file=None):
    """Generate a creative brief from template"""
    brief = TEMPLATE.copy()
    
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(brief, f, indent=2)
        print(f"Creative brief generated: {output_file}")
        print("\nTemplate structure created. Please fill in your specific information.")
    else:
        print(json.dumps(brief, indent=2))
    
    return brief

def print_brief_instructions():
    """Print instructions for filling out brief"""
    print("=" * 70)
    print("HOW TO FILL OUT YOUR CREATIVE BRIEF")
    print("=" * 70)
    
    instructions = """
REQUIRED FIELDS (must be completed):

1. PROJECT_NAME
   - Descriptive project/campaign identifier
   - Example: "Q4 Market Intelligence Campaign"

2. OBJECTIVE
   - Primary business goal
   - Options: lead_generation, brand_awareness, event_promotion, 
     product_launch, educational, etc.

3. AUDIENCE
   - Primary: Who are we reaching? (specific, not generic)
   - Age range, geographic focus, key characteristics
   - Example: "African entrepreneurs, ages 28-45, in tech/fintech"

4. PRIMARY_MESSAGE
   - The single most important message (the headline)
   - Should be specific and benefit-focused
   - Example: "Strategic Intelligence for African Growth"

5. CREATIVE_DIRECTION.SUGGESTED_ANGLE
   - Which creative territory: authority, opportunity, human_impact, 
     navigation, data_expertise, education, or "open"
   - If "open", creator chooses best angle

6. CTA (CALL-TO-ACTION)
   - Action type: sign_up, download, register, contact, etc.
   - CTA copy: Exact button text (e.g., "Join Our Community")
   - CTA URL: Where should they go?

7. FORMATS
   - Which output formats needed (social_1x1, email_header, etc.)
   - Multiple formats allowed

OPTIONAL BUT RECOMMENDED:

- Strategic insight (problem, opportunity, positioning)
- Messaging proof points and key benefits
- Brand requirements and technical specifications
- Timeline and approval process

TIPS FOR BEST RESULTS:

✓ Be specific, not vague ("entrepreneurs, tech sector, 28-45")
✓ One clear message per creative (focus is key)
✓ Explain why this matters to your audience
✓ Only include true proof points (no invented stats)
✓ Specify CTA clearly (not just "Learn more")
✓ Give realistic timeline for revision rounds
"""
    
    print(instructions)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print_brief_instructions()
        elif sys.argv[1] == "--create":
            output = sys.argv[2] if len(sys.argv) > 2 else "creative-brief.json"
            generate_brief(output)
        else:
            print("Usage:")
            print("  python generate-brief.py --help")
            print("  python generate-brief.py --create [output_file]")
    else:
        print_brief_instructions()
        print("\nGenerated template JSON:")
        print("-" * 70)
        generate_brief()
