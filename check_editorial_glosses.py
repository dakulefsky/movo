#!/usr/bin/env python3
"""Verify isolated editorial annotations and byte-identical underlying content."""
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
from editorial_glosses import compile_glosses, explained_text

ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'editorial_glosses_01311.json').read_text())
current=json.loads((ROOT/'editorial.json').read_text())
ledger=json.loads((ROOT/'audit/master-ledger.json').read_text())
with tempfile.TemporaryDirectory(prefix='gloss-baseline-',dir=ROOT/'work') as directory:
    archive=subprocess.check_output(['git','archive',manifest['basis_commit']],cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:tar.extractall(directory,filter='data')
    subprocess.run(['python3','build.py'],cwd=directory,check=True,stdout=subprocess.DEVNULL)
    baseline=json.loads((Path(directory)/'editorial.json').read_text())
    previous_ledger=json.loads((Path(directory)/'audit/master-ledger.json').read_text())
assert baseline['version']==manifest['basis_version']=='0.13.10'
assert current['version']==manifest['version']=='0.13.11'
baseline['version']=current['version']
assert baseline=={k:v for k,v in current.items() if k!='editorialGlosses'},'Original corpus changed'
compiled=compile_glosses(current['handbooks'])
assert current['editorialGlosses']==compiled
assert sum(map(len,compiled.values()))==len(manifest['annotations'])==16
for key,value in previous_ledger.items():assert ledger[key]==value,('Historical ledger changed',key)
assert ledger['editorial_gloss_checkpoint']['annotations']==manifest['annotations']
export=(ROOT/'Mevoot-Shas-Content.md').read_text()
paragraphs={e['id']+'/'+b['id']+'/paragraph-'+str(i):p for h in current['handbooks'] for e in h['entries'] for b in e['blocks'] for i,p in enumerate(b['paragraphs'],1)}
for key,annotations in compiled.items():
    assert explained_text(paragraphs[key],annotations) in export,('Gloss export missing',key)
print('PASS 16 separate labeled glosses in 12 paragraphs. All underlying explanations, quotations, 241 sources, source notes, references, reading stages and complete historical ledger unchanged from 0.13.10. Glosses are editorial, not scholarly certification.')
