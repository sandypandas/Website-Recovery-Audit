from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_DIR = ROOT / 'data' / 'archive' / 'recovered_text'
TEXT_DIR.mkdir(parents=True, exist_ok=True)

sample = {
    'sample-home-ocr.txt': '''
Welcome to Green Valley Community Center
Programs for youth and adults
Meberships available
Apply online or in person
'''.strip(),
    'sample-home-verified.txt': '''
Welcome to Green Valley Community Center
Programs for youth and adults
Memberships available
Apply online or in person
'''.strip(),
    'sample-events-ocr.txt': '''
Upcoming Events
Summer art camp
Volunteer fair
Food drive on June 12
'''.strip(),
    'sample-events-verified.txt': '''
Upcoming Events
Summer Art Camp
Volunteer Fair
Food Drive on June 12
'''.strip(),
}

for name, content in sample.items():
    (TEXT_DIR / name).write_text(content + '\n', encoding='utf-8')

errors = [
    {'page': 'sample-home', 'error_type': 'word_misread', 'issue': 'Meberships was read as "Meberships" instead of "Memberships"', 'severity': 'minor'},
    {'page': 'sample-events', 'error_type': 'case_rendering', 'issue': 'Capitalization changed from proper title case to sentence case', 'severity': 'moderate'},
    {'page': 'sample-events', 'error_type': 'token_confusion', 'issue': '“Food drive” was split and mis-read on some test outputs', 'severity': 'moderate'},
]

error_path = ROOT / 'data' / 'ocr_error_log.csv'
with error_path.open('w', encoding='utf-8', newline='') as handle:
    handle.write('page,error_type,issue,severity\n')
    for row in errors:
        handle.write(f"{row['page']},{row['error_type']},{row['issue']},{row['severity']}\n")

print(f'Wrote OCR sample texts to {TEXT_DIR}')
print(f'Wrote OCR errors log to {error_path}')
