#!/usr/bin/env python3
"""Verify exact continuation scope, source receipts and historical evidence."""
import io, json, subprocess, tarfile, tempfile, hashlib, re
from pathlib import Path
from source_overhaul import manifest, pre_overhaul_corpus
ROOT=Path(__file__).resolve().parent
plan=manifest(); current=json.loads((ROOT/'editorial.json').read_text())
ledger=json.loads((ROOT/'audit/master-ledger.json').read_text())
(ROOT/'work').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='overhaul-baseline-',dir=ROOT/'work') as directory:
    with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',plan['basis_commit']],cwd=ROOT))) as tar:
        tar.extractall(directory,filter='data')
    subprocess.run(['python3','build.py'],cwd=directory,check=True,stdout=subprocess.DEVNULL)
    baseline=json.loads((Path(directory)/'editorial.json').read_text())
    previous=json.loads((Path(directory)/'audit/master-ledger.json').read_text())
assert pre_overhaul_corpus(current)==baseline,'Unrecorded content, source, ordering or metadata change'
for key,value in previous.items(): assert ledger[key]==value,('Historical ledger changed',key)
for line in subprocess.check_output(['git','ls-tree','-r',plan['basis_commit'],'--','sources'],cwd=ROOT,text=True).splitlines():
    meta,name=line.split('\t');assert subprocess.check_output(['git','hash-object',name],cwd=ROOT,text=True).strip()==meta.split()[2],name
for item in plan['prooftexts']:
    raw=json.loads((ROOT/'sources'/item['filename']).read_text())
    receipt=json.loads((ROOT/raw['witness']['receipt']).read_text())
    text='\n'.join(v['text'] for v in receipt['content'] if v['type']=='text')
    visible=re.sub(r'【\d+†([^】]+)】',r'\1',text)
    assert all(t in visible for t in raw['he']),('Source extraction differs from fetched witness',item['id'])
entries=[e for h in current['handbooks'] for e in h['entries']]
blocks=[b for e in entries for b in e['blocks']]
assert len(entries)==98 and len(blocks)==317 and sum(len(b['paragraphs'])+len(b['items']) for b in blocks)==360
assert len(current['sources'])==251
assert len(plan['edits'])==8 and len({e['claim_id'].rsplit('/',1)[0] for e in plan['edits']})==7
checkpoint=ledger['continuation_20261026']
expected={e['id']+'/'+b['id']+'/paragraph-'+str(n):t for e in entries for b in e['blocks'] for n,t in enumerate(b['paragraphs'],1)}
expected.update({e['id']+'/'+b['id']+'/item-'+str(n):v['label']+': '+v['text'] for e in entries for b in e['blocks'] for n,v in enumerate(b['items'],1)})
records={r['claim_id']:r for r in checkpoint['claim_records']}
assert len(records)==360 and set(records)==set(expected)
for key,text in expected.items():
    assert records[key]['current_hebrew']==text and records[key]['current_sha256']==hashlib.sha256(text.encode()).hexdigest(),key
    assert records[key]['six_gate_status']=='incomplete_not_verified' and records[key]['current_disposition']!='verified',key
assert checkpoint['independently_six_gate_verified_blocks']==0
assert checkpoint['editorial_sha256']==hashlib.sha256((ROOT/'editorial.json').read_bytes()).hexdigest()
print('PASS exact 8-paragraph /7-block continuation; five witnessed prooftexts; all 246 prior sources and complete historical ledger preserved. No six-gate verification claimed.')
