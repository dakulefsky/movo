"""Selected, guarded repairs from the adjudicated audit; never edits the ledger.

The manifest is an explicit reviewed selection, not a run-time sweep of proposals.
Original source snapshots and historical audit claim_text remain immutable.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def apply_adjudicated_repairs(handbooks, sources):
    blocks = {e['id'] + '/' + b['id']: b
              for h in handbooks for e in h['entries'] for b in e['blocks']}
    manifest = json.loads((ROOT / 'adjudicated_repairs.json').read_text())
    for edit in manifest['edits']:
        entry, block, unit = edit['claim_id'].split('/')
        index = int(unit.removeprefix('paragraph-')) - 1
        paragraphs = blocks[entry + '/' + block]['paragraphs']
        assert paragraphs[index] == edit['before'], ('adjudicated repair drift', edit['claim_id'])
        paragraphs[index] = edit['after']
    return len(manifest['edits'])


def attach_adjudicated_prooftexts(handbooks, sources):
    from source_catalog import source
    blocks = {e['id'] + '/' + b['id']: b
              for h in handbooks for e in h['entries'] for b in e['blocks']}
    records = json.loads((ROOT / 'adjudicated_prooftexts.json').read_text())
    for item in records:
        raw = json.loads((ROOT / 'sources' / item['filename']).read_text())
        witness = json.loads((ROOT / 'sources' / raw['witness']['capture']).read_text())
        assert witness['page_sha256'] == raw['witness']['page_sha256']
        assert witness['url'] == raw['witness']['url']
        assert all(text in witness['rendered_text'] for text in raw['he']), item['id']
        assert item['id'] not in sources, ('duplicate prooftext', item['id'])
        src = source(item['id'], item['filename'], item['author'])
        src['url'] = raw['witness']['url']
        src['note'] = item['note']
        sources[item['id']] = src
        for key in item['blocks']:
            blocks[key]['refs'].append({'source':item['id'], 'segments':list(range(1,len(src['segments'])+1))})
    # Same ordinary consent rule; cross-reference its separate father-authority scope.
    b = blocks['i-kiddushin/meaning']
    assert 'a-kiddushin-2-1' in sources
    if not any(r['source']=='a-kiddushin-2-1' for r in b['refs']):
        b['refs'].append({'source':'a-kiddushin-2-1','segments':[1]})
    # Preserve raw API labels, but make the local/canonical crosswalk visible
    # wherever the old record is opened, including from the all-sources catalogue.
    for id, note in {
        'a-challah-1-1':'מיפוי מספור: הקובץ השמור תחת חלה א, א כולל גם פירוש המוצג בעדות ויקיטקסט בחלה א, ב. אין לזהות מספר מקטע מקומי עם מספר משנה; מקור מקביל נפרד מצורף לביאור חמשת המינים.',
        'i-get-9-3':'מיפוי מספור: הפירוש השמור כאן בשם גיטין ט, ג מוצג בויקיטקסט בגיטין ט, ב. נוסח הקובץ וכותרתו ההיסטורית לא שונו; מקור מקביל נפרד צורף לביאורי הגירושין.',
        'review-shomrim':'מיפוי מספור: הקובץ השמור בשם שבועות ח, א כולל פירושים לכמה משניות. דין מודה בקנס שבמקטע 4 מוצג בעדות הפרק המלא במשנה ח, ד. מקור נפרד צורף לביאור גניבה וגזלה.'
    }.items():
        assert id in sources, ('crosswalk source missing',id)
        sources[id]['note'] = (sources[id]['note'] + ' ' + note).strip()
    return len(records)
