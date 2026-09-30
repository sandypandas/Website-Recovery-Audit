from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / 'images' / 'site-sitemap.png'
MERMAID_PATH = ROOT / 'data' / 'site-sitemap.mmd'

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
MERMAID_PATH.parent.mkdir(parents=True, exist_ok=True)

mermaid_text = '''
flowchart TD
    A[Home] --> B[About]
    A --> C[Programs]
    C --> C1[Youth Programs]
    C --> C2[Adult Learning]
    C --> C3[Senior Services]
    A --> D[Events]
    A --> E[News]
    E --> E1[Announcements]
    E --> E2[Archive]
    A --> F[Volunteer]
    A --> G[Donate]
    A --> H[Contact]
    H --> H1[Locations]
    H --> H2[Staff]
'''
MERMAID_PATH.write_text(mermaid_text.strip() + '\n', encoding='utf-8')

W, H = 1280, 760
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

font = ImageFont.load_default()
node_fill = '#eaf2ff'
line_color = '#2f3d4a'
text_color = '#1f2937'

positions = {
    'A': (80, 140),
    'B': (300, 60),
    'C': (300, 180),
    'C1': (560, 80),
    'C2': (560, 190),
    'C3': (560, 300),
    'D': (300, 330),
    'E': (300, 460),
    'E1': (560, 430),
    'E2': (560, 530),
    'F': (300, 580),
    'G': (90, 580),
    'H': (90, 330),
    'H1': (300, 680),
    'H2': (100, 680),
}

box_w = 170
box_h = 54

for key, (x, y) in positions.items():
    x0, y0 = x, y
    x1, y1 = x0 + box_w, y0 + box_h
    draw.rounded_rectangle((x0, y0, x1, y1), radius=12, fill=node_fill, outline=line_color, width=2)
    label = key.replace('A', 'Home') if key == 'A' else key
    label = {
        'B': 'About', 'C': 'Programs', 'D': 'Events', 'E': 'News', 'F': 'Volunteer',
        'G': 'Donate', 'H': 'Contact', 'C1': 'Youth', 'C2': 'Adult', 'C3': 'Seniors',
        'E1': 'Announcements', 'E2': 'Archive', 'H1': 'Locations', 'H2': 'Staff'
    }.get(key, label)
    text_w, text_h = draw.textbbox((0, 0), label, font=font)[2:]
    draw.text((x0 + 10, y0 + 15), label, fill=text_color, font=font)

arrows = [
    ('A', 'B'), ('A', 'C'), ('C', 'C1'), ('C', 'C2'), ('C', 'C3'), ('A', 'D'), ('A', 'E'),
    ('E', 'E1'), ('E', 'E2'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('H', 'H1'), ('H', 'H2')
]

for a, b in arrows:
    x1, y1 = positions[a][0] + box_w // 2, positions[a][1] + box_h // 2
    x2, y2 = positions[b][0] + box_w // 2, positions[b][1] + box_h // 2
    draw.line((x1, y1, x2, y2), fill=line_color, width=2)
    draw.polygon([(x2, y2), (x2-8, y2-6), (x2-8, y2+6)], fill=line_color)

img.save(OUT_PATH)
print(f'Created Mermaid source at {MERMAID_PATH}')
print(f'Created PNG sitemap at {OUT_PATH}')
