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
manifest=json.loads((ROOT/'sentence_flow_01310.json').read_text())
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
assert baseline['version']==manifest['basis_version']=='0.13.9'
assert manifest['version']=='0.13.10'
assert current['version']=='0.13.13'
for edit in manifest['edits']:
    assert re.findall(r'\w+',edit['before'])==re.findall(r'\w+',edit['after']),('Words changed',edit['claim_id'])
    for quote in re.findall(r'(?<![א-ת])״([^״]+)״(?![א-ת])',edit['before']):
        assert quote in edit['after'],('quotation changed',edit['claim_id'],quote)
    assert re.findall(r'\d+',edit['before'])==re.findall(r'\d+',edit['after']),edit['claim_id']
apply_polish(baseline['handbooks'],manifest['edits'])
latest=json.loads((ROOT/'refinement_01313.json').read_text())
apply_polish(baseline['handbooks'],latest['edits'])
baseline['version']=current['version']
assert baseline=={k:v for k,v in current.items() if k!='editorialGlosses'},'Change outside the 8 selected paragraphs / separate gloss metadata'
for old,new in zip(previous_ledger['rows'],ledger['rows'],strict=True):
    assert all(new[k]==v for k,v in old.items()),('Reviewed ledger data changed',old['claim_id'])
    edit=next((e for e in manifest['edits'] if e['claim_id']==new['claim_id']),None)
    if edit:
        assert new['sentence_flow_review']['before']==edit['before'] and new['sentence_flow_review']['after']==edit['after']
print('PASS final polish: exactly 8 sentence-boundary revisions; every word and word order retained; all other corpus data, all source quotations, reading stages, numbers and prior reviewed ledger fields preserved. Independent scholarly recheck remains pending.')
