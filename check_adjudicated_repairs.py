#!/usr/bin/env python3
"""Check repair scope and evidence preservation; does not certify source fidelity.

Generate comparison inventory only in a disposable directory, never over reviews.
Run after build.py. Historical reviews and claim_text stay unchanged in the ledger.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
BASIS = 'aa8d284e6e0b72844850408e3f47d311949b3cc2'
def read(name):
    return json.loads((ROOT / name).read_text())
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

original = json.loads(git('show', BASIS + ':audit/master-ledger.json'))
ledger = read('audit/master-ledger.json')
assert len(ledger['rows']) == 360 and ledger['block_count'] == 317
edits = {e['claim_id']: e for e in read('adjudicated_repairs.json')['edits']}
assert len(edits) == 32
readability = read('readability_0137.json')['edits']
final_texts = {r['claim_id']: r['claim_text'] for r in original['rows']}
for edit in [*edits.values(), *readability, *read('polish_0139.json')['edits']]:
    assert final_texts[edit['claim_id']] == edit['before'], ('overlay chain drift',edit['claim_id'])
    final_texts[edit['claim_id']] = edit['after']
# Immutable historical fields, including rejected proposals and all review evidence.
for before, after in zip(original['rows'], ledger['rows']):
    assert all(after[k] == v for k,v in before.items()), before['claim_id']
# Verify byte-for-byte preservation of every historical source file.
for line in git('ls-tree','-r',BASIS,'--','sources').decode().splitlines():
    metadata, filename = line.split('\t')
    assert git('hash-object', filename).decode().strip() == metadata.split()[2], filename

(ROOT / 'work').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='comparison-', dir=ROOT / 'work') as temporary:
    folder = Path(temporary)
    for filename in ('generate_audit_ledger.py', 'editorial.json'):
        shutil.copy2(ROOT / filename, folder / filename)
    subprocess.run(['python3',str(folder / 'generate_audit_ledger.py')],check=True)
    generated = json.loads((folder / 'audit/master-ledger.json').read_text())
    assert generated['claim_units'] == 360 and generated['block_count'] == 317
    for old, current in zip(original['rows'], generated['rows']):
        id = old['claim_id']
        assert current['claim_id'] == id
        assert current['claim_text'] == final_texts[id], id
        # All earlier source words and local locators remain attached.
        for source in old['source_refs']:
            assert source in current['source_refs'], (id,source['source_id'])
# Guard the legally significant counterexamples, independently of full-string checks.
data = read('editorial.json')
blocks = {e['id']+'/'+b['id']: b for h in data['handbooks'] for e in h['entries'] for b in e['blocks']}
def prose(key): return ' '.join(blocks[key]['paragraphs'])
assert 'שלא יראנו לוקט' in prose('z-orlah/chutz') and 'כלאי הכרם' in prose('z-orlah/chutz')
assert 'שהם עצמם אבות הטומאה' not in prose('t-hechsher/conditions')
assert 'בעוד המשקה על האוכל' in prose('t-hechsher/conditions')
assert 'אין לערב בין שעבוד נכסי הלווה' in prose('d-karka/ways')
assert 'קרקעות הבעל' in prose('i-ketubah/shiabud')
assert 'ולא נמסר בפני שני עדים כשרים' in prose('i-edei-get/distinction')
assert 'משום מזויף מתוכו' in prose('i-edei-get/distinction')
assert 'קידושי בת בידי אביה' in prose('i-kiddushin/meaning')
assert 'משעת הנפילה עד סוף' in prose('a-taam/distinction')
assert 'אינה ניתרת מאליה בניעור המאוחר' in prose('a-taam/distinction')
assert 'מצטרף למניין השישים, אך הוא עצמו אסור' in prose('a-taam/udder')
assert 'בהרכב הראשון של שלושה' in prose('d-edut/meaning')
assert 'בהרכב שהורחב לחמישה' in prose('d-edut/meaning')
assert 'יש הבדל בין המקורות' in prose('d-edut/meaning')
assert 'ובעיקר תוספות יום טוב נתפרש' in prose('minchah/exceptions')
assert len(blocks['minchah/exceptions']['paragraphs']) == 2
assert 'מנחה רגילה' in blocks['minchah/exceptions']['paragraphs'][0]
print('PASS: 32 adjudicated repairs + 203 guarded readability revisions + 14 sentence polishes; 317 blocks / 360 claims; all historical sources and reviewed evidence preserved. No scholarly certification.')
