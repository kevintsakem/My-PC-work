#!/usr/bin/env python3
"""
Interactive SRS Template Filler
Easy-to-use interface for generating SRS documents.
Simply fill in the fields you want - leave others empty.
"""

from srs_template_generator import SRSTemplateGenerator


def create_srs_document():
    """
    Interactive function to create an SRS document.
    Customize this function with your project data.
    """
    
    # ====================
    # CUSTOMIZE YOUR SRS DOCUMENT BELOW
    # ====================
    # Leave any field empty (None or '') to exclude it from the PDF
    
    data = {
        # ============================================
        # COVER PAGE INFORMATION
        # ============================================
        'project_name': 'Your Project Name Here',  # e.g., 'Mobile Banking App'
        'version': '1.0',
        'company': 'Your Company Name',
        'date': 'January 29, 2026',  # Or leave empty for today's date
        'author': 'Your Name / Team Name',
        'status': 'Draft',  # e.g., 'Draft', 'Final', 'Approved', 'In Review'
        
        # ============================================
        # 1. PURPOSE SECTION
        # ============================================
        'purpose': '''Write a comprehensive description of the purpose of this SRS document.
Explain what the document covers and why it was created.''',
        
        'intended_audience': '''Who will use this document?
(e.g., Development team, QA, stakeholders, clients)''',
        
        'scope': '''Define the scope of the software system.
What will it do? What are its boundaries?''',
        
        # ============================================
        # 2. PRODUCT OVERVIEW
        # ============================================
        'product_description': '''Provide a detailed description of the product.
What is it? What problem does it solve?''',
        
        'product_benefits': [
            'Benefit 1',
            'Benefit 2',
            'Benefit 3',
            # Add more benefits or leave empty: []
        ],
        
        'product_goals': [
            'Goal 1',
            'Goal 2',
            # Add more goals or leave empty: []
        ],
        
        'product_objectives': [
            'Objective 1',
            'Objective 2',
            # Add more objectives or leave empty: []
        ],
        
        # ============================================
        # 3. CONSTRAINTS, ASSUMPTIONS, AND DEPENDENCIES
        # ============================================
        'constraints': [
            'Constraint 1 (e.g., budget, timeline, technology)',
            'Constraint 2',
            # Add more or leave empty: []
        ],
        
        'assumptions': [
            'Assumption 1',
            'Assumption 2',
            # Add more or leave empty: []
        ],
        
        'dependencies': [
            'Dependency 1 (e.g., third-party APIs, services)',
            'Dependency 2',
            # Add more or leave empty: []
        ],
        
        # ============================================
        # 4. FUNCTIONAL REQUIREMENTS
        # ============================================
        # Use this format for each requirement:
        # {'id': 'FR-001', 'description': 'Description here', 'priority': 'Must Have'}
        'functional_requirements': [
            {
                'id': 'FR-001',
                'description': 'System shall...',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-002',
                'description': 'System shall...',
                'priority': 'Highly Desired'
            },
            # Add more requirements or leave empty: []
            # Priority options: 'Must Have', 'Highly Desired', 'Nice to Have'
        ],
        
        # ============================================
        # 5. EXTERNAL INTERFACE REQUIREMENTS
        # ============================================
        'user_interfaces': [
            'Description of user interface 1',
            'Description of user interface 2',
            # Add more or leave empty: []
        ],
        
        'hardware_interfaces': [
            'Hardware interface 1',
            'Hardware interface 2',
            # Add more or leave empty: []
        ],
        
        'software_interfaces': [
            'Software interface / API 1',
            'Software interface / API 2',
            # Add more or leave empty: []
        ],
        
        'communication_interfaces': [
            'Communication protocol 1',
            'Communication protocol 2',
            # Add more or leave empty: []
        ],
        
        # ============================================
        # 6. SYSTEM FEATURES
        # ============================================
        'system_features': [
            {
                'id': 'SF-001',
                'description': 'System feature description',
                'priority': 'Must Have'
            },
            # Add more features or leave empty: []
        ],
        
        # ============================================
        # 7. NON-FUNCTIONAL REQUIREMENTS
        # ============================================
        'performance_requirements': [
            'Performance requirement 1',
            'Performance requirement 2',
            # Add more or leave empty: []
        ],
        
        'safety_requirements': [
            'Safety requirement 1',
            'Safety requirement 2',
            # Add more or leave empty: []
        ],
        
        'security_requirements': [
            'Security requirement 1',
            'Security requirement 2',
            # Add more or leave empty: []
        ],
        
        'quality_requirements': [
            'Quality requirement 1',
            'Quality requirement 2',
            # Add more or leave empty: []
        ],
        
        # ============================================
        # 8. USER REQUIREMENTS / USER STORIES
        # ============================================
        # Use this format: As a [user], I want to [function], so that [reason]
        'user_stories': [
            {
                'user': 'customer',
                'function': 'create an account',
                'reason': 'I can make purchases'
            },
            {
                'user': 'administrator',
                'function': 'manage users',
                'reason': 'I can control access'
            },
            # Add more user stories or leave empty: []
        ],
        
        # ============================================
        # 9. ACCEPTANCE CRITERIA
        # ============================================
        'acceptance_criteria': [
            'Acceptance criterion 1',
            'Acceptance criterion 2',
            # Add more criteria or leave empty: []
        ],
        
        # ============================================
        # 10. ADDITIONAL INFORMATION
        # ============================================
        'additional_notes': '''Any additional information, notes, or comments that don't fit
in the other sections. This is optional.''',
    }
    
    # ====================
    # GENERATE THE PDF
    # ====================
    output_filename = "System_Requirements_Specification.pdf"
    generator = SRSTemplateGenerator(output_filename)
    
    try:
        result = generator.generate(data)
        print(f"✓ Success! SRS document generated: {result}")
        print(f"\nThe PDF has been created with a clean, professional layout.")
        print(f"Empty fields were automatically omitted from the document.")
        return result
    except Exception as e:
        print(f"✗ Error generating SRS document: {e}")
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("SRS Document Generator")
    print("=" * 60)
    print("\nGenerating your System Requirements Specification...")
    print("\nIMPORTANT: Edit this script to customize your document.")
    print("Fill in only the fields you need - empty fields will be omitted.\n")
    
    create_srs_document()
