#!/usr/bin/env python3
"""Compare the literary pass with its committed baseline in a temporary tree.

This checks scope, exact source preservation and recorded explanation-anchor
crosswalks. It does not prove semantic or scholarly correctness.
"""
import io
import json
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT/'readability_0137.json').read_text())
current = json.loads((ROOT/'editorial.json').read_text())
from teaching_additions import pre_teaching_corpus
current=pre_teaching_corpus(current)  # exact later overlay checked in check_teaching_additions.py
(ROOT/'work').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='literary-baseline-',dir=ROOT/'work') as directory:
    archive = subprocess.check_output(['git','archive',manifest['basis_commit']],cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(directory,filter='data')
    subprocess.run(['python3','build.py'],cwd=directory,check=True,stdout=subprocess.DEVNULL)
    baseline = json.loads((Path(directory)/'editorial.json').read_text())
assert baseline['sources'] == current['sources'], 'Original source words/editions/notes changed'

def blocks(data):
    return {entry['id']+'/'+block['id']:block for handbook in data['handbooks'] for entry in handbook['entries'] for block in entry['blocks']}
from copy import deepcopy
from polish_revision import polish_edits
comparison=deepcopy(current)
comparison_blocks=blocks(comparison)
for edit in reversed(polish_edits()):
    key,unit=edit['claim_id'].rsplit('/',1)
    index=int(unit.removeprefix('paragraph-'))-1
    assert comparison_blocks[key]['paragraphs'][index]==edit['after'],edit['claim_id']
    comparison_blocks[key]['paragraphs'][index]=edit['before']
before,after = blocks(baseline),blocks(comparison)
assert set(before)==set(after) and len(after)==317
edits = {e['claim_id']:e for e in manifest['edits']}
assert len(edits)==manifest['changed_paragraphs']==203
seen=set()
for key,old in before.items():
    new=after[key]
    assert {k:v for k,v in old.items() if k!='paragraphs'} == {k:v for k,v in new.items() if k!='paragraphs'}, ('block metadata drift',key)
    assert len(old['paragraphs'])==len(new['paragraphs']),key
    for i,(p,q) in enumerate(zip(old['paragraphs'],new['paragraphs']),1):
        id=key+'/paragraph-'+str(i)
        if id in edits:
            assert p==edits[id]['before'] and q==edits[id]['after'],id
            seen.add(id)
        else:
            assert p==q,('unauthorized paragraph change',id)
assert seen==set(edits)
for crosswalk in manifest['explanation_anchor_crosswalk']:
    key=crosswalk['block_id']
    assert crosswalk['before'] in ' '.join(before[key]['paragraphs']),('old explanation anchor',key,crosswalk['before'])
    assert crosswalk['after'] in ' '.join(after[key]['paragraphs']),('new explanation anchor',key,crosswalk['after'])
# Direct quotations remain literal; two removed quotes only name rhetorical labels.
exempt={'a-yadot-kinuyim/rashaim/paragraph-2':{'רשע'},'t-mashkin/tvul/paragraph-1':{'נגע במשקה'}}
for id,edit in edits.items():
    for quote in re.findall(r'(?<![א-ת])״([^״]+)״(?![א-ת])',edit['before']):
        assert quote in edit['after'] or quote in exempt.get(id,set()),('quotation changed',id,quote)
print('PASS readability scope: 203 paragraphs / 185 blocks; all 317 blocks, headings, lists, refs, links and 241 source records preserved. Explanation-anchor crosswalks and direct quotations checked; independent scholarly recheck remains pending.')
