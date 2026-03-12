# Professional SRS Template Generator

Generate beautiful, clean, and professional System Requirements Specification (SRS) documents in PDF format.

## ✨ Features

- **Beautiful Design**: Professional layout with color-coded sections and clean typography
- **Smart Omission**: Empty fields are automatically excluded from the final PDF - no "Not Specified" text
- **Easy to Use**: Simple Python template that you fill in with your data
- **Comprehensive**: Covers all standard SRS sections based on industry best practices
- **Well-Structured**: Organized sections with clear hierarchy and visual appeal

## 📋 What's Included

The template includes all standard SRS sections:

1. **Cover Page** - Project name, version, company, author, date, status
2. **Purpose** - Document purpose, intended audience, and scope
3. **Product Overview** - Description, benefits, goals, and objectives
4. **Constraints, Assumptions, Dependencies** - Project limitations and requirements
5. **Functional Requirements** - What the system must do
6. **External Interface Requirements** - User interfaces, hardware, software, and communication interfaces
7. **System Features** - Core features required for the system to function
8. **Non-Functional Requirements** - Performance, safety, security, and quality requirements
9. **User Requirements** - User stories in "As a [user], I want [function], so that [reason]" format
10. **Acceptance Criteria** - Criteria for determining project completion
11. **Additional Information** - Any other relevant notes

## 🚀 Quick Start

### Option 1: Use the Blank Template (Recommended)

1. Open `blank_template.py` in a text editor
2. Fill in your project information (leave empty fields blank)
3. Save the file
4. Run:
   ```bash
   python3 blank_template.py
   ```
5. Your PDF will be generated as `SRS_Document.pdf`

### Option 2: Use the Example Template

1. Open `create_srs.py` to see a fully filled example
2. Run:
   ```bash
   python3 create_srs.py
   ```
3. This generates an example PDF showing all possible sections

### Option 3: View the Sample

Run the generator with sample data to see what the output looks like:
```bash
python3 srs_template_generator.py
```
This creates `SRS_Example.pdf` with sample e-commerce platform data.

## 📝 How to Fill the Template

### Basic Information
```python
data = {
    'project_name': 'My Awesome Project',
    'version': '1.0',
    'company': 'My Company',
    'author': 'John Doe',
    'status': 'Draft',
    # ...
}
```

### Text Fields
Just add your text as a string:
```python
'purpose': 'This document specifies the requirements for...',
'product_description': 'The system will provide...',
```

### Lists
Add items as a Python list:
```python
'product_benefits': [
    'Increased efficiency',
    'Reduced costs',
    'Better user experience'
],
```

Leave empty for lists you don't need:
```python
'product_benefits': [],  # This section will be omitted from the PDF
```

### Requirements Tables
Functional requirements and system features use a structured format:
```python
'functional_requirements': [
    {
        'id': 'FR-001',
        'description': 'System shall allow users to login',
        'priority': 'Must Have'
    },
    {
        'id': 'FR-002',
        'description': 'System shall send email notifications',
        'priority': 'Highly Desired'
    },
],
```

Priority options:
- `'Must Have'` - Critical requirements
- `'Highly Desired'` - Important but not critical
- `'Nice to Have'` - Optional enhancements

### User Stories
Format user stories in the standard "As a... I want... So that..." structure:
```python
'user_stories': [
    {
        'user': 'administrator',
        'function': 'manage user accounts',
        'reason': 'I can control system access'
    },
    {
        'user': 'customer',
        'function': 'track my orders',
        'reason': 'I know when to expect delivery'
    },
],
```

## 🎨 Document Styling

The generated PDF includes:

- **Professional Color Scheme**: Navy blue headers with clean gray text
- **Clear Hierarchy**: Large section headers with underlines, medium subsection headers
- **Readable Typography**: Justified body text with appropriate line spacing
- **Formatted Tables**: Requirements displayed in clean, color-coded tables
- **Bullet Lists**: Attractive bullet points for list items
- **Cover Page**: Professional title page with key document information

## 📂 File Structure

```
.
├── srs_template_generator.py  # Core PDF generation engine
├── blank_template.py          # Empty template for your project
├── create_srs.py              # Customizable template with instructions
└── README.md                  # This file
```

## 💡 Tips for Best Results

1. **Be Specific**: Provide detailed descriptions for better documentation
2. **Use Priorities**: Clearly mark requirements as "Must Have", "Highly Desired", or "Nice to Have"
3. **Include IDs**: Use consistent ID numbering (FR-001, FR-002, etc.) for requirements
4. **Write Clear User Stories**: Follow the "As a [user], I want to [action], so that [benefit]" format
5. **Only Fill What You Need**: Empty sections won't appear in the final PDF

## 🔧 Customization

### Changing Output Filename
Edit the `output_filename` variable:
```python
output_filename = "My_Custom_SRS.pdf"
```

### Adding More Requirements
Simply add more items to the lists:
```python
'functional_requirements': [
    {'id': 'FR-001', 'description': '...', 'priority': 'Must Have'},
    {'id': 'FR-002', 'description': '...', 'priority': 'Must Have'},
    {'id': 'FR-003', 'description': '...', 'priority': 'Highly Desired'},
    # Add as many as you need
],
```

### Modifying Sections
The `srs_template_generator.py` file contains all the styling and section generation logic. You can customize:
- Colors (search for `HexColor`)
- Fonts (search for `fontName`)
- Spacing (search for `spaceAfter`, `spaceBefore`)
- Table styles (in the `_add_requirements_table` method)

## ⚠️ Important Notes

- **Empty Fields**: Leave fields as empty strings `''` or empty lists `[]` to omit them from the PDF
- **No "Not Specified"**: The template intelligently omits empty fields - you'll never see "Not Specified" in your PDF
- **Python 3 Required**: Make sure you're using Python 3.7 or later
- **Dependencies**: ReportLab is required (it should already be installed)

## 📖 Example Output

When you run the generator, you'll get:

1. **Professional Cover Page** with your project information
2. **Well-Organized Sections** with only the content you provided
3. **Clean Tables** for requirements with ID, description, and priority
4. **Attractive Lists** for benefits, constraints, assumptions, etc.
5. **Structured User Stories** clearly showing user needs

## 🆘 Troubleshooting

**Problem**: Module not found error
```bash
pip install reportlab
```

**Problem**: Empty PDF or missing sections
- Make sure you've filled in at least some fields
- Check that strings aren't just whitespace
- Verify lists aren't empty `[]` if you want them included

**Problem**: Formatting looks wrong
- Ensure you're using the correct data types (strings for text, lists for multiple items)
- Check that requirement dictionaries include 'id', 'description', and 'priority'

## 📄 License

This template generator is provided as-is for creating professional SRS documents.

## 🤝 Support

For issues or questions:
1. Check the example files (`create_srs.py` and `srs_template_generator.py`)
2. Verify your data structure matches the examples
3. Ensure all required dependencies are installed

---

**Ready to create your SRS document?** Start with `blank_template.py` and fill in your project details!
