#!/usr/bin/env python3
"""
BLANK SRS TEMPLATE - Fill in your project details below
Only fill in the sections you need - empty fields will be omitted from the PDF
"""

from srs_template_generator import SRSTemplateGenerator


# ====================================================================================
# FILL IN YOUR PROJECT INFORMATION BELOW
# ====================================================================================
# Instructions:
# 1. Replace placeholder text with your actual project information
# 2. Leave fields empty (None or '') if you don't need them
# 3. For lists, use [] to leave empty, or add items: ['item1', 'item2']
# 4. Save the file and run: python3 blank_template.py
# ====================================================================================

data = {
    # ============================================
    # COVER PAGE INFORMATION
    # ============================================
    'project_name': '',  # Your project name
    'version': '',  # e.g., '1.0', '2.3', 'Draft v0.5'
    'company': '',  # Your company/organization name
    'date': '',  # Leave empty for today's date, or specify: 'January 29, 2026'
    'author': '',  # Your name or team name
    'status': '',  # e.g., 'Draft', 'Final', 'Approved', 'In Review'
    
    # ============================================
    # 1. PURPOSE SECTION
    # ============================================
    'purpose': '',  # Why was this SRS created? What does it cover?
    
    'intended_audience': '',  # Who will use this document?
    
    'scope': '',  # What is the scope of the software system?
    
    # ============================================
    # 2. PRODUCT OVERVIEW
    # ============================================
    'product_description': '',  # Describe the product
    
    'product_benefits': [],  # List of benefits, e.g., ['Benefit 1', 'Benefit 2']
    
    'product_goals': [],  # List of goals
    
    'product_objectives': [],  # List of objectives
    
    # ============================================
    # 3. CONSTRAINTS, ASSUMPTIONS, AND DEPENDENCIES
    # ============================================
    'constraints': [],  # List of constraints (budget, timeline, technology, etc.)
    
    'assumptions': [],  # List of assumptions
    
    'dependencies': [],  # List of dependencies (APIs, services, systems, etc.)
    
    # ============================================
    # 4. FUNCTIONAL REQUIREMENTS
    # ============================================
    # Format: [{'id': 'FR-001', 'description': 'Description', 'priority': 'Must Have'}, ...]
    # Priority options: 'Must Have', 'Highly Desired', 'Nice to Have'
    'functional_requirements': [],
    
    # ============================================
    # 5. EXTERNAL INTERFACE REQUIREMENTS
    # ============================================
    'user_interfaces': [],  # List of user interface descriptions
    
    'hardware_interfaces': [],  # List of hardware interfaces
    
    'software_interfaces': [],  # List of software interfaces/APIs
    
    'communication_interfaces': [],  # List of communication protocols
    
    # ============================================
    # 6. SYSTEM FEATURES
    # ============================================
    # Format: [{'id': 'SF-001', 'description': 'Description', 'priority': 'Must Have'}, ...]
    'system_features': [],
    
    # ============================================
    # 7. NON-FUNCTIONAL REQUIREMENTS
    # ============================================
    'performance_requirements': [],  # List of performance requirements
    
    'safety_requirements': [],  # List of safety requirements
    
    'security_requirements': [],  # List of security requirements
    
    'quality_requirements': [],  # List of quality requirements
    
    # ============================================
    # 8. USER REQUIREMENTS / USER STORIES
    # ============================================
    # Format: [{'user': 'user type', 'function': 'what they want', 'reason': 'why'}, ...]
    # Example: {'user': 'customer', 'function': 'search products', 'reason': 'I can find items'}
    'user_stories': [],
    
    # ============================================
    # 9. ACCEPTANCE CRITERIA
    # ============================================
    'acceptance_criteria': [],  # List of acceptance criteria
    
    # ============================================
    # 10. ADDITIONAL INFORMATION
    # ============================================
    'additional_notes': '',  # Any additional information
}


# ====================================================================================
# GENERATE THE PDF (Don't modify below this line)
# ====================================================================================
if __name__ == "__main__":
    output_filename = "SRS_Document.pdf"
    generator = SRSTemplateGenerator(output_filename)
    
    try:
        result = generator.generate(data)
        print("=" * 70)
        print("SUCCESS!")
        print("=" * 70)
        print(f"✓ SRS document generated: {result}")
        print(f"✓ Professional layout with clean formatting")
        print(f"✓ Empty fields automatically omitted")
        print("=" * 70)
    except Exception as e:
        print("=" * 70)
        print("ERROR!")
        print("=" * 70)
        print(f"✗ Failed to generate SRS document: {e}")
        import traceback
        traceback.print_exc()
