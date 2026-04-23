from PIL import Image
img = Image.open('static/images/logo2.JPG').convert('RGB')
colors = img.getcolors(img.size[0] * img.size[1])
colors.sort(reverse=True, key=lambda x: x[0])
found = 0
for count, (r, g, b) in colors:
    # Filter out pure whites/blacks/greys to find the distinct blue/color
    if r > 240 and g > 240 and b > 240: continue # near white
    if r < 15 and g < 15 and b < 15: continue # near black
    diff = max(abs(r-g), abs(r-b), abs(g-b))
    if diff < 20: continue # near grey
    print(f"#{r:02x}{g:02x}{b:02x}")
    found += 1
    if found >= 10: break
