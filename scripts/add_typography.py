"""
Overlay typography on GPT/DALL-E generated cover image.
Output: KDP-ready 1800x2700 px JPEG with title, subtitle, author.
"""
from PIL import Image, ImageDraw, ImageFont
import os

INPUT = "c:/Users/a/Desktop/书/ChatGPT Image 2026年5月22日 23_22_41.png"
OUTPUT = "c:/Users/a/Desktop/书/output/cover_final.jpg"
FONTS = "C:/Windows/Fonts"
W, H = 1800, 2700

# Colors
TITLE_COLOR = (240, 236, 228)
SUB_COLOR = (170, 165, 157)
AUTHOR_COLOR = (150, 146, 140)

# Load fonts
try:
    title_font = ImageFont.truetype(os.path.join(FONTS, "bahnschrift.ttf"), 170)
except:
    title_font = ImageFont.truetype(os.path.join(FONTS, "impact.ttf"), 155)

try:
    subtitle_font = ImageFont.truetype(os.path.join(FONTS, "Candaral.ttf"), 48)
except:
    subtitle_font = ImageFont.truetype(os.path.join(FONTS, "georgia.ttf"), 44)

try:
    author_font = ImageFont.truetype(os.path.join(FONTS, "Candara.ttf"), 38)
except:
    author_font = ImageFont.truetype(os.path.join(FONTS, "arial.ttf"), 38)

# Load and resize
img = Image.open(INPUT).convert("RGB")
img = img.resize((W, H), Image.LANCZOS)
draw = ImageDraw.Draw(img)
cx = W // 2

# Title
title_lines = ["ALWAYS ONLINE,", "NEVER HERE"]
title_y = 950
for i, line in enumerate(title_lines):
    bbox = draw.textbbox((0, 0), line, font=title_font)
    tw = bbox[2] - bbox[0]
    # Subtle shadow
    draw.text((cx - tw // 2 + 2, title_y + i * 200 + 2), line, fill=(0, 0, 0), font=title_font)
    draw.text((cx - tw // 2, title_y + i * 200), line, fill=TITLE_COLOR, font=title_font)

# Subtitle
subtitle_lines = [
    "A Philosophy of Attention, Presence, and Survival",
    "for the Exhausted Generation",
]
sub_y = title_y + 440
for line in subtitle_lines:
    bbox = draw.textbbox((0, 0), line, font=subtitle_font)
    sw = bbox[2] - bbox[0]
    draw.text((cx - sw // 2, sub_y), line, fill=SUB_COLOR, font=subtitle_font)
    sub_y += 58

# Author
bbox = draw.textbbox((0, 0), "MOON", font=author_font)
aw = bbox[2] - bbox[0]
draw.text((cx - aw // 2, H - 200), "MOON", fill=AUTHOR_COLOR, font=author_font)

# Save
img.save(OUTPUT, "JPEG", quality=95, dpi=(300, 300))
size_kb = os.path.getsize(OUTPUT) / 1024
print(f"Cover saved: {OUTPUT}")
print(f"Size: {W}x{H} px (6x9 inch at 300 DPI)")
print(f"File: {size_kb:.0f} KB")
