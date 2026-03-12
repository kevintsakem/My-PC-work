# 🚀 QUICK START GUIDE

## Generate Your SRS Document in 3 Steps

### Step 1: Choose Your Starting Point

**For a blank template:**
- Open `blank_template.py`
- This is completely empty and ready for your content

**For an example to customize:**
- Open `create_srs.py`
- This has sample data showing how to fill each field

### Step 2: Fill in Your Information

Edit the Python file and replace the placeholder text:

```python
data = {
    'project_name': 'Your Project Name',  # ← Put your project name here
    'version': '1.0',                     # ← Version number
    'company': 'Your Company',            # ← Company name
    # ... continue filling in fields
}
```

**Important Rules:**
- ✅ Leave fields empty to omit them: `'field_name': ''`
- ✅ Empty lists will be omitted: `'list_name': []`
- ✅ Only fill what you need - empty = invisible in PDF
- ❌ Don't worry about "Not Specified" - it won't appear!

### Step 3: Generate Your PDF

Run the Python script:

```bash
python3 blank_template.py
```

Or if you're using the example:

```bash
python3 create_srs.py
```

**Done!** Your professional SRS PDF is ready: `SRS_Document.pdf`

---

## 📋 Field Types Cheat Sheet

### Simple Text
```python
'project_name': 'Mobile Banking App',
'purpose': 'This document describes...',
```

### Lists
```python
'product_benefits': [
    'Benefit 1',
    'Benefit 2',
    'Benefit 3'
],
```

### Requirements (with ID and Priority)
```python
'functional_requirements': [
    {
        'id': 'FR-001',
        'description': 'System shall allow user login',
        'priority': 'Must Have'
    },
],
```

### User Stories
```python
'user_stories': [
    {
        'user': 'customer',
        'function': 'view order history',
        'reason': 'I can track my purchases'
    },
],
```

---

## 🎯 Priority Levels

Use these for requirements:
- **'Must Have'** - Critical, non-negotiable
- **'Highly Desired'** - Important but not critical
- **'Nice to Have'** - Optional enhancements

---

## 💡 Pro Tips

1. **Start Small**: Fill in cover page + a few sections first
2. **Test Often**: Run the script after adding each section
3. **Check the Example**: Look at `SRS_Example.pdf` to see the output
4. **Be Detailed**: More detail = better documentation

---

## 🆘 Need Help?

1. Look at `SRS_Example.pdf` - this shows a complete document
2. Check `README.md` - comprehensive documentation
3. Examine `create_srs.py` - fully filled example

**Common Issue**: Empty PDF?
→ Make sure you filled in at least the cover page fields!

---

## 📁 Your Files

- `blank_template.py` ← **START HERE** (empty template)
- `create_srs.py` ← Example with sample data
- `srs_template_generator.py` ← The engine (don't edit)
- `README.md` ← Full documentation
- `SRS_Example.pdf` ← Sample output to see what's possible

---

**Ready?** Open `blank_template.py` and start filling in your project details! 🎉
