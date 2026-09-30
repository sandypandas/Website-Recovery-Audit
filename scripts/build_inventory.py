import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / 'data' / 'archive_inventory.db'
CSV_PATH = ROOT / 'data' / 'archive_inventory.csv'

rows = [
    {
        'record_id': 'A-001',
        'page_title': 'Green Valley Community Center',
        'slug': 'home',
        'parent_section': 'Root',
        'screenshot_file': 'screen-001-home.png',
        'content_type': 'Landing page',
        'recovery_status': 'Recovered',
        'text_recovery': 'High confidence',
        'image_assets': 3,
        'notes': 'Primary landing page with navigation and call-to-action links.'
    },
    {
        'record_id': 'A-002',
        'page_title': 'About Us',
        'slug': 'about',
        'parent_section': 'About',
        'screenshot_file': 'screen-002-about.png',
        'content_type': 'Institutional overview',
        'recovery_status': 'Recovered',
        'text_recovery': 'Medium confidence',
        'image_assets': 1,
        'notes': 'Mission statement and service history are legible but some dates are uncertain.'
    },
    {
        'record_id': 'A-003',
        'page_title': 'Programs',
        'slug': 'programs',
        'parent_section': 'Programs',
        'screenshot_file': 'screen-003-programs.png',
        'content_type': 'Program index',
        'recovery_status': 'Recovered',
        'text_recovery': 'High confidence',
        'image_assets': 2,
        'notes': 'Main listing page linking to youth, adult, and senior programs.'
    },
    {
        'record_id': 'A-004',
        'page_title': 'Youth Programs',
        'slug': 'programs/youth',
        'parent_section': 'Programs',
        'screenshot_file': 'screen-004-youth.png',
        'content_type': 'Program detail',
        'recovery_status': 'Partial',
        'text_recovery': 'Medium confidence',
        'image_assets': 4,
        'notes': 'Schedule and registration details are present but some event dates are partially obscured.'
    },
    {
        'record_id': 'A-005',
        'page_title': 'Adult Learning',
        'slug': 'programs/adult-learning',
        'parent_section': 'Programs',
        'screenshot_file': 'screen-005-adult-learning.png',
        'content_type': 'Program detail',
        'recovery_status': 'Recovered',
        'text_recovery': 'High confidence',
        'image_assets': 2,
        'notes': 'Course descriptions are readable and structured clearly.'
    },
    {
        'record_id': 'A-006',
        'page_title': 'Senior Services',
        'slug': 'programs/seniors',
        'parent_section': 'Programs',
        'screenshot_file': 'screen-006-seniors.png',
        'content_type': 'Program detail',
        'recovery_status': 'Recovered',
        'text_recovery': 'Medium confidence',
        'image_assets': 3,
        'notes': 'Most text is visible; a few contact numbers are hard to read.'
    },
    {
        'record_id': 'A-007',
        'page_title': 'Events Calendar',
        'slug': 'events',
        'parent_section': 'Events',
        'screenshot_file': 'screen-007-events.png',
        'content_type': 'Calendar',
        'recovery_status': 'Partial',
        'text_recovery': 'Low confidence',
        'image_assets': 2,
        'notes': 'The calendar layout is clear, but several event titles are lost to compression artifacts.'
    },
    {
        'record_id': 'A-008',
        'page_title': 'News & Updates',
        'slug': 'news',
        'parent_section': 'News',
        'screenshot_file': 'screen-008-news.png',
        'content_type': 'News index',
        'recovery_status': 'Recovered',
        'text_recovery': 'High confidence',
        'image_assets': 1,
        'notes': 'Headlines and dates are readable and consistent across entries.'
    },
    {
        'record_id': 'A-009',
        'page_title': 'Volunteer Opportunities',
        'slug': 'volunteer',
        'parent_section': 'Get Involved',
        'screenshot_file': 'screen-009-volunteer.png',
        'content_type': 'Call to action',
        'recovery_status': 'Recovered',
        'text_recovery': 'High confidence',
        'image_assets': 2,
        'notes': 'Well structured page with signup instructions.'
    },
    {
        'record_id': 'A-010',
        'page_title': 'Donate',
        'slug': 'donate',
        'parent_section': 'Get Involved',
        'screenshot_file': 'screen-010-donate.png',
        'content_type': 'Donation page',
        'recovery_status': 'Recovered',
        'text_recovery': 'Medium confidence',
        'image_assets': 3,
        'notes': 'Donation text is readable, but the campaign metadata may require manual verification.'
    },
    {
        'record_id': 'A-011',
        'page_title': 'Contact',
        'slug': 'contact',
        'parent_section': 'Contact',
        'screenshot_file': 'screen-011-contact.png',
        'content_type': 'Contact page',
        'recovery_status': 'Recovered',
        'text_recovery': 'High confidence',
        'image_assets': 0,
        'notes': 'Contact information and office hours are clearly readable.'
    },
    {
        'record_id': 'A-012',
        'page_title': 'Staff Directory',
        'slug': 'staff',
        'parent_section': 'About',
        'screenshot_file': 'screen-012-staff.png',
        'content_type': 'Directory',
        'recovery_status': 'Partial',
        'text_recovery': 'Medium confidence',
        'image_assets': 1,
        'notes': 'Names are generally readable, but some profiles are truncated in the archived screenshot.'
    }
]

DB_PATH.parent.mkdir(parents=True, exist_ok=True)
con = sqlite3.connect(DB_PATH)
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS archive_inventory')
cur.execute('''
CREATE TABLE archive_inventory (
    record_id TEXT PRIMARY KEY,
    page_title TEXT,
    slug TEXT,
    parent_section TEXT,
    screenshot_file TEXT,
    content_type TEXT,
    recovery_status TEXT,
    text_recovery TEXT,
    image_assets INTEGER,
    notes TEXT
)
''')
cur.executemany(
    'INSERT INTO archive_inventory (record_id, page_title, slug, parent_section, screenshot_file, content_type, recovery_status, text_recovery, image_assets, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
    [(
        row['record_id'],
        row['page_title'],
        row['slug'],
        row['parent_section'],
        row['screenshot_file'],
        row['content_type'],
        row['recovery_status'],
        row['text_recovery'],
        row['image_assets'],
        row['notes']
    ) for row in rows]
)
con.commit()
con.close()

with CSV_PATH.open('w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=[
        'record_id', 'page_title', 'slug', 'parent_section', 'screenshot_file',
        'content_type', 'recovery_status', 'text_recovery', 'image_assets', 'notes'
    ])
    writer.writeheader()
    writer.writerows(rows)

print(f'Created SQLite inventory at {DB_PATH}')
print(f'Created CSV export at {CSV_PATH}')
print(f'Total rows: {len(rows)}')
