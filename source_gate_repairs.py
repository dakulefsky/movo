"""Guarded follow-up edits; original source snapshots remain immutable."""
from copy import deepcopy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def manifest():
    return json.loads((ROOT / 'source_gate_repairs_20261026.json').read_text())

def _blocks(data):
    return {e['id'] + '/' + b['id']: b
            for h in data['handbooks'] for e in h['entries'] for b in e['blocks']}

def apply_source_gates(handbooks, sources):
    plan = manifest()
    blocks = _blocks({'handbooks': handbooks})
    for edit in plan['edits']:
        key, unit = edit['claim_id'].rsplit('/', 1)
        n = int(unit.removeprefix('paragraph-')) - 1
        assert blocks[key]['paragraphs'][n] == edit['before'], edit['claim_id']
        blocks[key]['paragraphs'][n] = edit['after']
    for edit in plan['source_metadata']:
        source = sources[edit['source_id']]
        assert source[edit['field']] == edit['before'], edit['source_id']
        source[edit['field']] = edit['after']
    return len(plan['edits'])

def pre_source_gates_corpus(data):
    result = deepcopy(data)
    blocks = _blocks(result)
    plan = manifest()
    for edit in plan['edits']:
        key, unit = edit['claim_id'].rsplit('/', 1)
        n = int(unit.removeprefix('paragraph-')) - 1
        assert blocks[key]['paragraphs'][n] == edit['after'], edit['claim_id']
        blocks[key]['paragraphs'][n] = edit['before']
    for edit in plan['source_metadata']:
        source = result['sources'][edit['source_id']]
        assert source[edit['field']] == edit['after'], edit['source_id']
        source[edit['field']] = edit['before']
    return result
