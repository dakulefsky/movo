#!/usr/bin/env python3
"""Check follow-up scope, immutable history and receipts; not scholarly clearance."""
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
from record_source_gates import KEY, create_checkpoint
from source_gate_repairs import manifest, pre_source_gates_corpus

ROOT = Path(__file__).resolve().parent
plan = manifest()
current = json.loads((ROOT / 'editorial.json').read_text())
ledger = json.loads((ROOT / 'audit/master-ledger.json').read_text())
with tempfile.TemporaryDirectory(prefix='source-gates-', dir=ROOT / 'work') as directory:
    archive = subprocess.check_output(['git', 'archive', plan['basis_commit']], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(directory, filter='data')
    subprocess.run(['python3', 'build.py'], cwd=directory, check=True, stdout=subprocess.DEVNULL)
    baseline = json.loads((Path(directory) / 'editorial.json').read_text())
    prior = json.loads((Path(directory) / 'audit/master-ledger.json').read_text())
assert pre_source_gates_corpus(current) == baseline, 'Unrecorded corpus/source/metadata change'
assert set(ledger) == set(prior) | {KEY}, 'Unrecorded ledger keys'
for key, value in prior.items():
    if key != 'active_review_checkpoint':
        assert ledger[key] == value, ('Historical evidence changed', key)
assert ledger['active_review_checkpoint'] == KEY
assert ledger[KEY] == create_checkpoint(current, ledger), 'Stale or altered follow-up evidence'
assert len(ledger[KEY]['claim_records']) == 360
assert ledger[KEY]['fresh_catalog_urls_attempted'] == 146
assert len(plan['edits']) == 2 and len(plan['source_metadata']) == 5
for edit in plan['edits']:
    segment = next(s['text'] for s in current['sources'][edit['source_id']]['segments'] if s['number'] == edit['segment'])
    for quote in edit['supporting_quotations']:
        assert quote in segment, ('Quoted support absent from bundled segment', edit['claim_id'], quote)
    for receipt in edit['witness_receipts']:
        assert (ROOT / receipt).is_file(), receipt
for line in subprocess.check_output(['git', 'ls-tree', '-r', plan['basis_commit'], '--', 'sources'], cwd=ROOT, text=True).splitlines():
    meta, name = line.split('\t')
    assert subprocess.check_output(['git', 'hash-object', name], cwd=ROOT, text=True).strip() == meta.split()[2], name
assert all(r['current_disposition'] != 'verified' and r['six_gate_status'] == 'incomplete_not_verified'
           for r in ledger[KEY]['claim_records'])
print('PASS two paragraph edits, five source-reference labels, 360 current ledger units, 146 URL attempts; historical corpus/evidence preserved. No six-gate verification claimed.')
