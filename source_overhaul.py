"""Guarded source-fidelity continuation, after the historical editorial layers."""
from copy import deepcopy
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def manifest():
    return json.loads((ROOT/'source_overhaul_20261026.json').read_text())

def source_record(item):
    raw=json.loads((ROOT/'sources'/item['filename']).read_text())
    receipt=json.loads((ROOT/raw['witness']['receipt']).read_text())
    assert raw['witness']['url']==item['url']
    assert item['url'] in json.dumps(receipt,ensure_ascii=False)
    return dict(id=item['id'],author='רמב״ם',ref=raw['ref'],citation=raw['heRef'],
                filename=item['filename'],url=item['url'],edition=raw['versions'],
                segments=[dict(number=n,text=t) for n,t in enumerate(raw['he'],1)],note=item['note'])

def _blocks(handbooks):
    return {e['id']+'/'+b['id']:b for h in handbooks for e in h['entries'] for b in e['blocks']}

def apply_overhaul(handbooks,sources):
    plan=manifest(); blocks=_blocks(handbooks)
    for edit in plan['edits']:
        key,unit=edit['claim_id'].rsplit('/',1); index=int(unit.removeprefix('paragraph-'))-1
        assert blocks[key]['paragraphs'][index]==edit['before'],('overhaul baseline drift',edit['claim_id'])
        blocks[key]['paragraphs'][index]=edit['after']
    for item in plan['prooftexts']:
        assert item['id'] not in sources
        sources[item['id']]=source_record(item)
        for key,segments in item['targets'].items():
            blocks[key]['refs'].append(dict(source=item['id'],segments=segments))
    return len(plan['edits'])

def pre_overhaul_corpus(data):
    """Strict inverse allows historical preservation checks to inspect their layer."""
    result=deepcopy(data); plan=manifest(); blocks=_blocks(result['handbooks'])
    for item in reversed(plan['prooftexts']):
        assert result['sources'].pop(item['id'])==source_record(item),item['id']
        for key,segments in item['targets'].items():
            assert blocks[key]['refs'].pop()==dict(source=item['id'],segments=segments),key
    for edit in plan['edits']:
        key,unit=edit['claim_id'].rsplit('/',1); index=int(unit.removeprefix('paragraph-'))-1
        assert blocks[key]['paragraphs'][index]==edit['after'],edit['claim_id']
        blocks[key]['paragraphs'][index]=edit['before']
    return result
