#!/usr/bin/env python3
"""
System Requirements Specification (SRS) Template Generator
Generates beautiful, professional PDF documents for SRS documentation.
Only includes fields that are provided - omits empty fields automatically.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os


class SRSTemplateGenerator:
    """Generates professional SRS documents with clean, attractive formatting."""
    
    def __init__(self, output_filename="SRS_Document.pdf"):
        self.output_filename = output_filename
        self.doc = SimpleDocTemplate(
            output_filename,
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )
        self.story = []
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Create custom paragraph styles for beautiful formatting."""
        
        # Title style - large, bold, centered
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            textColor=colors.HexColor('#1a365d'),
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='Subtitle',
            parent=self.styles['Normal'],
            fontSize=14,
            textColor=colors.HexColor('#2d3748'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Oblique'
        ))
        
        # Section heading style
        self.styles.add(ParagraphStyle(
            name='SectionHeading',
            parent=self.styles['Heading1'],
            fontSize=16,
            textColor=colors.HexColor('#1a365d'),
            spaceAfter=12,
            spaceBefore=16,
            fontName='Helvetica-Bold',
            borderPadding=(0, 0, 8, 0),
            borderColor=colors.HexColor('#3182ce'),
            borderWidth=0,
            leftIndent=0,
            underlineColor=colors.HexColor('#3182ce'),
            underlineWidth=2,
            underlineGap=2,
            underlineOffset=-4
        ))
        
        # Subsection heading style
        self.styles.add(ParagraphStyle(
            name='SubsectionHeading',
            parent=self.styles['Heading2'],
            fontSize=13,
            textColor=colors.HexColor('#2c5282'),
            spaceAfter=8,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Body text style
        self.styles.add(ParagraphStyle(
            name='SRSBodyText',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#2d3748'),
            spaceAfter=10,
            alignment=TA_JUSTIFY,
            leading=14
        ))
        
        # Field label style
        self.styles.add(ParagraphStyle(
            name='FieldLabel',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#4a5568'),
            fontName='Helvetica-Bold',
            spaceAfter=4
        ))
        
        # Field value style
        self.styles.add(ParagraphStyle(
            name='FieldValue',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#2d3748'),
            spaceAfter=10,
            leftIndent=10
        ))
        
        # Table header style
        self.styles.add(ParagraphStyle(
            name='TableHeader',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.white,
            fontName='Helvetica-Bold',
            alignment=TA_CENTER
        ))
    
    def _add_cover_page(self, title, version, company, date, author, status):
        """Create an attractive cover page."""
        # Add some space from top
        self.story.append(Spacer(1, 1.5*inch))
        
        # Main title
        if title:
            self.story.append(Paragraph(title, self.styles['CustomTitle']))
            self.story.append(Spacer(1, 0.3*inch))
        
        # Document type subtitle
        self.story.append(Paragraph(
            "System Requirements Specification",
            self.styles['Subtitle']
        ))
        
        # Create information table
        data = []
        if version:
            data.append(['Version:', version])
        if date:
            data.append(['Date:', date])
        else:
            data.append(['Date:', datetime.now().strftime('%B %d, %Y')])
        if author:
            data.append(['Author:', author])
        if company:
            data.append(['Company:', company])
        if status:
            data.append(['Status:', status])
        
        if data:
            self.story.append(Spacer(1, 0.5*inch))
            table = Table(data, colWidths=[1.5*inch, 3.5*inch])
            table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 11),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#2c5282')),
                ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#2d3748')),
                ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
            ]))
            self.story.append(table)
        
        self.story.append(PageBreak())
    
    def _add_section(self, title):
        """Add a major section heading."""
        self.story.append(Spacer(1, 0.15*inch))
        # Create styled section header
        para = Paragraph(title, self.styles['SectionHeading'])
        self.story.append(para)
        # Add a colored line under the section
        line_table = Table([['']], colWidths=[6.5*inch])
        line_table.setStyle(TableStyle([
            ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#3182ce')),
        ]))
        self.story.append(line_table)
        self.story.append(Spacer(1, 0.1*inch))
    
    def _add_subsection(self, title):
        """Add a subsection heading."""
        self.story.append(Paragraph(title, self.styles['SubsectionHeading']))
    
    def _add_field(self, label, value):
        """Add a labeled field with value (only if value exists)."""
        if value and str(value).strip():
            self.story.append(Paragraph(f"<b>{label}:</b>", self.styles['FieldLabel']))
            self.story.append(Paragraph(str(value), self.styles['FieldValue']))
    
    def _add_paragraph(self, text):
        """Add a body paragraph."""
        if text and str(text).strip():
            self.story.append(Paragraph(str(text), self.styles['SRSBodyText']))
    
    def _add_list_items(self, items, title=None):
        """Add a bulleted list of items."""
        if not items or (isinstance(items, list) and len(items) == 0):
            return
        
        if title:
            self._add_subsection(title)
        
        if isinstance(items, str):
            items = [items]
        
        bullet_list = []
        for item in items:
            if item and str(item).strip():
                bullet_list.append(ListItem(
                    Paragraph(str(item), self.styles['SRSBodyText']),
                    leftIndent=20,
                    bulletColor=colors.HexColor('#3182ce'),
                    value='circle'
                ))
        
        if bullet_list:
            self.story.append(ListFlowable(bullet_list, bulletType='bullet'))
            self.story.append(Spacer(1, 0.1*inch))
    
    def _add_requirements_table(self, requirements, title):
        """Add a formatted requirements table."""
        if not requirements or len(requirements) == 0:
            return
        
        self._add_subsection(title)
        
        # Prepare table data
        data = [['ID', 'Description', 'Priority']]
        
        for req in requirements:
            if isinstance(req, dict):
                req_id = req.get('id', '')
                desc = req.get('description', '')
                priority = req.get('priority', '')
            else:
                req_id = ''
                desc = str(req)
                priority = ''
            
            if desc:  # Only add if description exists
                data.append([
                    Paragraph(str(req_id), self.styles['Normal']) if req_id else '',
                    Paragraph(str(desc), self.styles['Normal']),
                    Paragraph(str(priority), self.styles['Normal']) if priority else ''
                ])
        
        if len(data) > 1:  # If we have more than just the header
            table = Table(data, colWidths=[0.8*inch, 4*inch, 1.2*inch])
            table.setStyle(TableStyle([
                # Header styling
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3182ce')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                ('TOPPADDING', (0, 0), (-1, 0), 10),
                
                # Body styling
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('ALIGN', (0, 1), (0, -1), 'CENTER'),
                ('ALIGN', (1, 1), (1, -1), 'LEFT'),
                ('ALIGN', (2, 1), (2, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
                ('TOPPADDING', (0, 1), (-1, -1), 8),
                ('LEFTPADDING', (0, 0), (-1, -1), 6),
                ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                
                # Grid
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
                ('LINEBELOW', (0, 0), (-1, 0), 2, colors.HexColor('#2c5282')),
                
                # Alternating row colors
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
            ]))
            self.story.append(table)
            self.story.append(Spacer(1, 0.15*inch))
    
    def generate(self, data):
        """
        Generate the complete SRS document.
        
        Args:
            data: Dictionary containing all SRS fields
        """
        
        # COVER PAGE
        self._add_cover_page(
            title=data.get('project_name'),
            version=data.get('version'),
            company=data.get('company'),
            date=data.get('date'),
            author=data.get('author'),
            status=data.get('status')
        )
        
        # TABLE OF CONTENTS (optional - would require more complex implementation)
        
        # 1. PURPOSE
        if data.get('purpose') or data.get('intended_audience') or data.get('scope'):
            self._add_section("1. Purpose")
            
            if data.get('purpose'):
                self._add_paragraph(data.get('purpose'))
            
            if data.get('intended_audience'):
                self._add_field("Intended Audience", data.get('intended_audience'))
            
            if data.get('scope'):
                self._add_field("Scope", data.get('scope'))
        
        # 2. PRODUCT OVERVIEW
        if (data.get('product_description') or data.get('product_benefits') or 
            data.get('product_goals') or data.get('product_objectives')):
            
            self._add_section("2. Product Overview")
            
            if data.get('product_description'):
                self._add_subsection("Product Description")
                self._add_paragraph(data.get('product_description'))
            
            if data.get('product_benefits'):
                self._add_list_items(data.get('product_benefits'), "Benefits")
            
            if data.get('product_goals'):
                self._add_list_items(data.get('product_goals'), "Goals")
            
            if data.get('product_objectives'):
                self._add_list_items(data.get('product_objectives'), "Objectives")
        
        # 3. CONSTRAINTS, ASSUMPTIONS, AND DEPENDENCIES
        if (data.get('constraints') or data.get('assumptions') or 
            data.get('dependencies')):
            
            self._add_section("3. Constraints, Assumptions, and Dependencies")
            
            if data.get('constraints'):
                self._add_list_items(data.get('constraints'), "Constraints")
            
            if data.get('assumptions'):
                self._add_list_items(data.get('assumptions'), "Assumptions")
            
            if data.get('dependencies'):
                self._add_list_items(data.get('dependencies'), "Dependencies")
        
        # 4. FUNCTIONAL REQUIREMENTS
        if data.get('functional_requirements'):
            self._add_section("4. Functional Requirements")
            self._add_requirements_table(
                data.get('functional_requirements'),
                "Functional Requirements"
            )
        
        # 5. EXTERNAL INTERFACE REQUIREMENTS
        if (data.get('user_interfaces') or data.get('hardware_interfaces') or 
            data.get('software_interfaces') or data.get('communication_interfaces')):
            
            self._add_section("5. External Interface Requirements")
            
            if data.get('user_interfaces'):
                self._add_list_items(data.get('user_interfaces'), "User Interfaces")
            
            if data.get('hardware_interfaces'):
                self._add_list_items(data.get('hardware_interfaces'), "Hardware Interfaces")
            
            if data.get('software_interfaces'):
                self._add_list_items(data.get('software_interfaces'), "Software Interfaces")
            
            if data.get('communication_interfaces'):
                self._add_list_items(data.get('communication_interfaces'), "Communication Interfaces")
        
        # 6. SYSTEM FEATURES
        if data.get('system_features'):
            self._add_section("6. System Features")
            self._add_requirements_table(
                data.get('system_features'),
                "Required System Features"
            )
        
        # 7. NON-FUNCTIONAL REQUIREMENTS
        if (data.get('performance_requirements') or data.get('safety_requirements') or 
            data.get('security_requirements') or data.get('quality_requirements')):
            
            self._add_section("7. Non-Functional Requirements")
            
            if data.get('performance_requirements'):
                self._add_list_items(data.get('performance_requirements'), "Performance Requirements")
            
            if data.get('safety_requirements'):
                self._add_list_items(data.get('safety_requirements'), "Safety Requirements")
            
            if data.get('security_requirements'):
                self._add_list_items(data.get('security_requirements'), "Security Requirements")
            
            if data.get('quality_requirements'):
                self._add_list_items(data.get('quality_requirements'), "Quality Requirements")
        
        # 8. USER REQUIREMENTS / USER STORIES
        if data.get('user_stories'):
            self._add_section("8. User Requirements")
            
            for i, story in enumerate(data.get('user_stories'), 1):
                if isinstance(story, dict):
                    user = story.get('user', '')
                    function = story.get('function', '')
                    reason = story.get('reason', '')
                    
                    if user or function or reason:
                        self._add_subsection(f"User Story {i}")
                        if user:
                            self._add_field("As a", user)
                        if function:
                            self._add_field("I want to", function)
                        if reason:
                            self._add_field("So that", reason)
                elif story:
                    self._add_paragraph(str(story))
        
        # 9. ACCEPTANCE CRITERIA
        if data.get('acceptance_criteria'):
            self._add_section("9. Acceptance Criteria")
            self._add_list_items(data.get('acceptance_criteria'))
        
        # 10. ADDITIONAL INFORMATION
        if data.get('additional_notes'):
            self._add_section("10. Additional Information")
            self._add_paragraph(data.get('additional_notes'))
        
        # Build the PDF
        self.doc.build(self.story)
        return self.output_filename


# Example usage and template structure
if __name__ == "__main__":
    # This is the data structure for the SRS template
    # Empty or None fields will be automatically omitted from the final PDF
    
    sample_data = {
        # Cover Page Information
        'project_name': 'E-Commerce Platform',
        'version': '1.0',
        'company': 'TechCorp Solutions',
        'date': 'January 29, 2026',
        'author': 'Product Team',
        'status': 'Draft',
        
        # 1. Purpose Section
        'purpose': 'This Software Requirements Specification (SRS) document provides a complete description of the requirements for the E-Commerce Platform. It is intended to guide the development team in creating a robust, scalable online shopping platform.',
        'intended_audience': 'Development team, project managers, QA testers, stakeholders, and maintenance personnel',
        'scope': 'The platform will enable users to browse products, make purchases, manage accounts, and track orders. It will include admin functionality for inventory management and order processing.',
        
        # 2. Product Overview
        'product_description': 'A comprehensive e-commerce platform that enables online retail operations with features for product catalog management, shopping cart, secure payment processing, and order fulfillment.',
        'product_benefits': [
            'Increased revenue through 24/7 online sales capability',
            'Reduced operational costs through automation',
            'Enhanced customer experience with personalized recommendations',
            'Real-time inventory management',
            'Comprehensive analytics and reporting'
        ],
        'product_goals': [
            'Process 10,000 concurrent users without performance degradation',
            'Achieve 99.9% uptime',
            'Complete checkout process in under 3 minutes',
            'Support multiple payment methods and currencies'
        ],
        'product_objectives': [
            'Launch MVP within 6 months',
            'Achieve PCI DSS compliance',
            'Integrate with existing ERP system',
            'Support mobile and desktop platforms'
        ],
        
        # 3. Constraints, Assumptions, and Dependencies
        'constraints': [
            'Budget limited to $500,000',
            'Must comply with GDPR and CCPA regulations',
            'Development must be completed within 6 months',
            'Must use existing company authentication system',
            'Must support minimum browser versions: Chrome 90+, Firefox 88+, Safari 14+'
        ],
        'assumptions': [
            'Users have reliable internet connectivity',
            'Third-party payment gateway APIs will remain stable',
            'Product catalog will not exceed 100,000 items initially',
            'Customer service team will be trained on the new system'
        ],
        'dependencies': [
            'Payment gateway API (Stripe/PayPal)',
            'Email service provider (SendGrid)',
            'Cloud hosting infrastructure (AWS)',
            'Existing ERP system integration',
            'SSL certificate provider'
        ],
        
        # 4. Functional Requirements
        'functional_requirements': [
            {
                'id': 'FR-001',
                'description': 'System shall allow users to create accounts using email and password',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-002',
                'description': 'System shall support OAuth authentication via Google and Facebook',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-003',
                'description': 'Users shall be able to search products by keyword, category, and filters',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-004',
                'description': 'System shall provide product recommendations based on browsing history',
                'priority': 'Highly Desired'
            },
            {
                'id': 'FR-005',
                'description': 'Users shall be able to add products to cart and modify quantities',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-006',
                'description': 'System shall calculate taxes and shipping costs automatically',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-007',
                'description': 'System shall process payments via credit card, PayPal, and digital wallets',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-008',
                'description': 'Users shall receive order confirmation emails automatically',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-009',
                'description': 'Admin users shall be able to manage product inventory and pricing',
                'priority': 'Must Have'
            },
            {
                'id': 'FR-010',
                'description': 'System shall support promotional codes and discounts',
                'priority': 'Highly Desired'
            }
        ],
        
        # 5. External Interface Requirements
        'user_interfaces': [
            'Responsive web interface compatible with desktop and mobile devices',
            'Admin dashboard for inventory and order management',
            'Customer account portal for order history and profile management',
            'Shopping cart interface with real-time updates'
        ],
        'hardware_interfaces': [
            'Integration with barcode scanners for warehouse operations',
            'Mobile device camera for QR code scanning'
        ],
        'software_interfaces': [
            'REST API integration with payment gateway (Stripe API v2023)',
            'Integration with existing ERP system via SOAP web services',
            'Email service API (SendGrid v3)',
            'Cloud storage API (AWS S3) for product images'
        ],
        'communication_interfaces': [
            'HTTPS protocol for all client-server communications',
            'WebSocket connections for real-time cart updates',
            'SMTP for email notifications',
            'SMS gateway for order notifications (Twilio API)'
        ],
        
        # 6. System Features
        'system_features': [
            {
                'id': 'SF-001',
                'description': 'User authentication and authorization system',
                'priority': 'Must Have'
            },
            {
                'id': 'SF-002',
                'description': 'Product catalog management system',
                'priority': 'Must Have'
            },
            {
                'id': 'SF-003',
                'description': 'Shopping cart and checkout functionality',
                'priority': 'Must Have'
            },
            {
                'id': 'SF-004',
                'description': 'Payment processing integration',
                'priority': 'Must Have'
            },
            {
                'id': 'SF-005',
                'description': 'Order management and tracking system',
                'priority': 'Must Have'
            },
            {
                'id': 'SF-006',
                'description': 'Customer review and rating system',
                'priority': 'Highly Desired'
            },
            {
                'id': 'SF-007',
                'description': 'Inventory management system',
                'priority': 'Must Have'
            },
            {
                'id': 'SF-008',
                'description': 'Reporting and analytics dashboard',
                'priority': 'Highly Desired'
            }
        ],
        
        # 7. Non-Functional Requirements
        'performance_requirements': [
            'System shall support 10,000 concurrent users',
            'Page load time shall not exceed 2 seconds under normal load',
            'Search queries shall return results in less than 1 second',
            'Checkout process shall complete within 30 seconds',
            'Database queries shall execute in less than 100ms'
        ],
        'safety_requirements': [
            'System shall automatically backup data every 6 hours',
            'System shall maintain transaction logs for audit purposes',
            'System shall implement graceful degradation in case of service failures',
            'System shall provide data recovery mechanisms'
        ],
        'security_requirements': [
            'All passwords shall be encrypted using bcrypt with minimum 12 rounds',
            'Payment information shall be tokenized and never stored locally',
            'System shall implement rate limiting to prevent DDoS attacks',
            'All communications shall use TLS 1.3 encryption',
            'System shall comply with PCI DSS standards',
            'Session tokens shall expire after 30 minutes of inactivity',
            'System shall implement CSRF protection on all forms',
            'SQL injection prevention through parameterized queries'
        ],
        'quality_requirements': [
            'System shall maintain 99.9% uptime (excluding planned maintenance)',
            'Code coverage shall be minimum 80% for unit tests',
            'System shall be scalable to handle 200% increase in traffic',
            'System shall support internationalization for minimum 5 languages',
            'User interface shall meet WCAG 2.1 Level AA accessibility standards'
        ],
        
        # 8. User Requirements / User Stories
        'user_stories': [
            {
                'user': 'a customer',
                'function': 'browse products by category',
                'reason': 'I can easily find items I am interested in purchasing'
            },
            {
                'user': 'a registered user',
                'function': 'save items to a wishlist',
                'reason': 'I can purchase them later without searching again'
            },
            {
                'user': 'a customer',
                'function': 'track my order status in real-time',
                'reason': 'I know when to expect delivery'
            },
            {
                'user': 'an administrator',
                'function': 'manage product inventory',
                'reason': 'I can keep stock levels accurate and prevent overselling'
            },
            {
                'user': 'a customer',
                'function': 'receive personalized product recommendations',
                'reason': 'I can discover products relevant to my interests'
            }
        ],
        
        # 9. Acceptance Criteria
        'acceptance_criteria': [
            'All functional requirements marked as "Must Have" are implemented and tested',
            'System passes security audit and penetration testing',
            'Performance benchmarks meet or exceed specified requirements',
            'User acceptance testing completed with 95% satisfaction rate',
            'All critical and high-priority bugs resolved',
            'Documentation completed including user manuals and API documentation',
            'System successfully processes test transactions through payment gateway',
            'Integration testing with ERP system completed successfully'
        ],
        
        # 10. Additional Information
        'additional_notes': 'This SRS document will be reviewed and updated quarterly or as significant changes to requirements occur. All stakeholders should be notified of updates. The development team should follow Agile methodology with two-week sprints. Regular sprint reviews will be conducted to ensure alignment with these requirements.'
    }
    
    # Generate the PDF
    generator = SRSTemplateGenerator("SRS_Example.pdf")
    output_file = generator.generate(sample_data)
    print(f"SRS document generated successfully: {output_file}")
