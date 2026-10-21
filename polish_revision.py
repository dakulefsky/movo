"""Exact, claim-scoped sentence polish after the audited reading structure."""
import json
from pathlib import Path


def polish_edits():
    return json.loads(Path(__file__).with_name('polish_0139.json').read_text())['edits']


def apply_polish(handbooks):
    blocks={e['id']+'/'+b['id']:b for h in handbooks for e in h['entries'] for b in e['blocks']}
    edits=polish_edits()
    assert len(edits)==len({e['claim_id'] for e in edits})==14
    for edit in edits:
        entry,block,unit=edit['claim_id'].split('/')
        assert unit.startswith('paragraph-'),edit['claim_id']
        index=int(unit.removeprefix('paragraph-'))-1
        paragraphs=blocks[entry+'/'+block]['paragraphs']
        assert paragraphs[index]==edit['before'],('polish baseline drift',edit['claim_id'])
        paragraphs[index]=edit['after']
    return len(edits)
