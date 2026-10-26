#!/usr/bin/env python3
"""Exact whole-corpus comparison for five teaching bridges and new prooftexts."""
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
from teaching_additions import manifest, pre_teaching_corpus

ROOT=Path(__file__).resolve().parent
plan=manifest();current=json.loads((ROOT/'editorial.json').read_text());ledger=json.loads((ROOT/'audit/master-ledger.json').read_text())
expected={'i-nissuin/stages/paragraph-1','a-neder/meaning/paragraph-1','minchah/nature/paragraph-1','i-ketubah/scope/paragraph-1','z-demai/distinction/paragraph-1'}
assert {e['claim_id'] for e in plan['edits']}==expected and len(plan['edits'])==5
with tempfile.TemporaryDirectory(prefix='teaching-baseline-',dir=ROOT/'work') as directory:
    archive=subprocess.check_output(['git','archive',plan['basis_commit']],cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:tar.extractall(directory,filter='data')
    subprocess.run(['python3','build.py'],cwd=directory,check=True,stdout=subprocess.DEVNULL)
    baseline=json.loads((Path(directory)/'editorial.json').read_text())
    previous=json.loads((Path(directory)/'audit/master-ledger.json').read_text())
assert pre_teaching_corpus(current)==baseline,'Change beyond five exact paragraphs, five prooftexts and two attribution labels'
for k,v in previous.items():assert ledger[k]==v,('Historical ledger changed',k)
for line in subprocess.check_output(['git','ls-tree','-r',plan['basis_commit'],'--','sources'],cwd=ROOT,text=True).splitlines():
    metadata,name=line.split('\t');actual=subprocess.check_output(['git','hash-object',name],cwd=ROOT,text=True).strip();assert actual==metadata.split()[2],name
entries=[e for h in current['handbooks'] for e in h['entries']];blocks=[b for e in entries for b in e['blocks']]
assert len(entries)==98 and len(blocks)==317 and sum(len(b['paragraphs'])+len(b['items']) for b in blocks)==360
from source_overhaul import pre_overhaul_corpus
assert len(baseline['sources'])==241 and len(pre_overhaul_corpus(current)['sources'])==246
assert baseline['editorialGlosses']==current['editorialGlosses']
print('PASS five source-supported teaching bridges, five separate prooftexts, two attribution labels; exact whole-corpus scope, all historical sources and ledger fields preserved; 98 entries /317 blocks /360 units. No scholarly certification.')
