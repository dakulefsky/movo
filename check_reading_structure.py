#!/usr/bin/env python3
"""Verify complete preservation of the pre-structure corpus in a temporary tree."""
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parent
plan = json.loads((ROOT/'reading_structure_0138.json').read_text())
current = json.loads((ROOT/'editorial.json').read_text())
(ROOT/'work').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='structure-baseline-',dir=ROOT/'work') as directory:
    archive = subprocess.check_output(['git','archive',plan['basis_commit']],cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(directory,filter='data')
    subprocess.run(['python3','build.py'],cwd=directory,check=True,stdout=subprocess.DEVNULL)
    baseline = json.loads((Path(directory)/'editorial.json').read_text())
assert current['version'] == '0.13.13'
from polish_revision import apply_polish
apply_polish(baseline['handbooks'])
assert current['sources'] == baseline['sources'], 'Source text/edition/note changed'
assert len(plan['entries']) == 98
count=0
for old_handbook,new_handbook in zip(baseline['handbooks'],current['handbooks'],strict=True):
    assert {k:v for k,v in old_handbook.items() if k!='entries'} == {k:v for k,v in new_handbook.items() if k!='entries'}
    for old,new in zip(old_handbook['entries'],new_handbook['entries'],strict=True):
        assert old == {k:v for k,v in new.items() if k!='readingSections'}, ('Audited content changed',old['id'])
        sections=new['readingSections']
        assert sections == plan['entries'][new['id']]['sections']
        assert [s['id'] for s in sections] == [id for id in ['meaning','practice','distinctions'] if any(s['id']==id for s in sections)]
        assert all(s['blocks'] for s in sections), 'Empty teaching stage'
        ordered=[id for s in sections for id in s['blocks']]
        assert len(ordered)==len(set(ordered)) and set(ordered)=={b['id'] for b in new['blocks']}
        assert sections[0]['blocks'][0]==new['blocks'][0]['id']
        count+=len(ordered)
assert count==317
ledger=json.loads((ROOT/'audit/master-ledger.json').read_text())
for row in ledger['rows']:
    section=next(s for s in plan['entries'][row['entry_id']]['sections'] if row['block_id'] in s['blocks'])
    assert row['reading_structure']['stage']==section['id'],row['claim_id']
print('PASS reading structure: all 98 entries / 317 blocks classified exactly once; every paragraph, item, source, source note, citation, title and related link identical to 0.13.7 after the separately guarded 27 sentence refinements. No scholarly certification.')
