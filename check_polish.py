#!/usr/bin/env python3
"""Check the exact sentence-only delta and preserve all previously reviewed data."""
import io
import json
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile
from polish_revision import apply_polish, polish_edits

ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'polish_0139.json').read_text())
current=json.loads((ROOT/'editorial.json').read_text())
ledger=json.loads((ROOT/'audit/master-ledger.json').read_text())
(ROOT/'work').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='polish-baseline-',dir=ROOT/'work') as directory:
    archive=subprocess.check_output(['git','archive',manifest['basis_commit']],cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(directory,filter='data')
    subprocess.run(['python3','build.py'],cwd=directory,check=True,stdout=subprocess.DEVNULL)
    baseline=json.loads((Path(directory)/'editorial.json').read_text())
    previous_ledger=json.loads((Path(directory)/'audit/master-ledger.json').read_text())
assert baseline['version']==manifest['basis_version']=='0.13.8'
assert current['version']==manifest['version']=='0.13.9'
for edit in polish_edits():
    for quote in re.findall(r'(?<![א-ת])״([^״]+)״(?![א-ת])',edit['before']):
        assert quote in edit['after'],('quotation changed',edit['claim_id'],quote)
    assert re.findall(r'\d+',edit['before'])==re.findall(r'\d+',edit['after']),edit['claim_id']
apply_polish(baseline['handbooks'])
baseline['version']=current['version']
assert baseline==current,'Change outside the 14 selected paragraphs'
for old,new in zip(previous_ledger['rows'],ledger['rows'],strict=True):
    assert all(new[k]==v for k,v in old.items()),('Reviewed ledger data changed',old['claim_id'])
    edit=next((e for e in polish_edits() if e['claim_id']==new['claim_id']),None)
    if edit:
        assert new['sentence_polish']['before']==edit['before'] and new['sentence_polish']['after']==edit['after']
print('PASS final polish: exactly 14 sentence revisions; all other corpus data, all source quotations, reading stages, numbers and prior reviewed ledger fields preserved. Independent scholarly recheck remains pending.')
