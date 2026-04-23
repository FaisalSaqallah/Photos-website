import re

with open('static/style.css', 'r') as f:
    content = f.read()

replacements = {
    r'#0066cc': '#329bbb',
    r'#0099ff': '#50cced',
    r'#004c99': '#186379',
    r'#0059b3': '#217f9c',
    r'135deg, #186379 0%, #329bbb 100%': '135deg, #186379 0%, #329bbb 100%', # ignore if already done, just setting mapping
    r'0, 102, 204': '50, 155, 187',
    r'#e6f2ff': '#eef8fb',
    r'#cce5ff': '#cae8f0',
    r'#b3d9ff': '#a4d8e7',
    r'#f9fcff': '#f7fbfc',
    r'#0052a3': '#267b96'
}

# The gradient was originally #0066cc to #0099ff
for old, new in replacements.items():
    content = re.sub(old, new, content, flags=re.IGNORECASE)

with open('static/style.css', 'w') as f:
    f.write(content)

