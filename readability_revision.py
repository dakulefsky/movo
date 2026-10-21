"""Guarded Hebrew readability pass after source-fidelity repairs.

Only explicitly selected explanation paragraphs change. Historical quotations,
reference maps, titles, examples and legal distinctions are not globally replaced.
"""
import json
from pathlib import Path


def apply_readability_revision(handbooks):
    manifest = json.loads(Path(__file__).with_name('readability_0137.json').read_text())
    blocks = {entry['id']+'/'+block['id']: block
              for handbook in handbooks for entry in handbook['entries'] for block in entry['blocks']}
    seen = set()
    for edit in manifest['edits']:
        entry, block, unit = edit['claim_id'].split('/')
        assert unit.startswith('paragraph-'), edit['claim_id']
        index = int(unit.removeprefix('paragraph-'))-1
        paragraphs = blocks[entry+'/'+block]['paragraphs']
        assert edit['claim_id'] not in seen, ('duplicate readability edit',edit['claim_id'])
        assert paragraphs[index] == edit['before'], ('readability original drift',edit['claim_id'])
        paragraphs[index] = edit['after']
        seen.add(edit['claim_id'])
    assert len(seen) == manifest['changed_paragraphs']
    return len(seen)
