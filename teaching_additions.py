"""Five source-backed teaching bridges; historical text/evidence remain immutable."""
from copy import deepcopy
import hashlib
import html
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent

def manifest():
    return json.loads((ROOT/'teaching_additions_01315.json').read_text())

def prooftext_record(item):
    raw=json.loads((ROOT/'sources'/item['filename']).read_text())
    capture=json.loads((ROOT/'sources'/raw['witness']['capture']).read_text())
    assert hashlib.sha256(capture['rendered_text'].encode()).hexdigest()==capture['page_sha256']==raw['witness']['page_sha256']
    assert capture['url']==item['url']==raw['witness']['url']
    assert all(text in capture['rendered_text'] for text in raw['he']),item['id']
    receipt=json.loads((ROOT/capture['review_receipt']).read_text())
    def strings(value):
        if isinstance(value,str):yield value
        elif isinstance(value,dict):
            for child in value.values():yield from strings(child)
        elif isinstance(value,list):
            for child in value:yield from strings(child)
    assert any(capture['rendered_text'] in value for value in strings(receipt)),('capture not in archived receipt',item['id'])
    clean=lambda text:html.unescape(re.sub('<[^>]*>','',text)).strip()
    return {'id':item['id'],'author':item['author'],'ref':raw['ref'],'citation':raw['heRef'],'filename':item['filename'],'url':item['url'],'edition':raw['versions'],'segments':[{'number':i,'text':clean(text)} for i,text in enumerate(raw['he'],1)],'note':item['note']}

def apply_teaching(handbooks,sources):
    plan=manifest();blocks={e['id']+'/'+b['id']:b for h in handbooks for e in h['entries'] for b in e['blocks']}
    assert len(plan['edits'])==len(plan['prooftexts'])==5
    for edit in plan['edits']:
        key,unit=edit['claim_id'].rsplit('/',1);index=int(unit.removeprefix('paragraph-'))-1;b=blocks[key]
        assert b['paragraphs'][index]==edit['before'] and b['refs']==edit['refs_before'],('teaching baseline drift',key)
        assert b['by']==edit['by_before'],key
        b['paragraphs'][index]=edit['after'];b['by']=edit['by_after']
    for item in plan['prooftexts']:
        assert item['id'] not in sources,item['id']
        sources[item['id']]=prooftext_record(item)
        blocks[item['block_id']]['refs'].append({'source':item['id'],'segments':item['segments']})
    return 5

def pre_teaching_corpus(data):
    """Strict inverse for earlier-layer checks; the new checker checks the full delta."""
    from source_overhaul import pre_overhaul_corpus
    result=pre_overhaul_corpus(data);plan=manifest()
    assert result['version']==plan['version']=='0.13.15'
    blocks={e['id']+'/'+b['id']:b for h in result['handbooks'] for e in h['entries'] for b in e['blocks']}
    by_block={item['block_id']:item for item in plan['prooftexts']}
    for edit in plan['edits']:
        key,unit=edit['claim_id'].rsplit('/',1);index=int(unit.removeprefix('paragraph-'))-1;b=blocks[key];item=by_block[key]
        assert b['paragraphs'][index]==edit['after'],('teaching output drift',key)
        assert b['refs']==edit['refs_before']+[{'source':item['id'],'segments':item['segments']}],key
        assert b['by']==edit['by_after'],key
        b['paragraphs'][index]=edit['before'];b['refs']=deepcopy(edit['refs_before']);b['by']=edit['by_before']
    for item in plan['prooftexts']:
        assert result['sources'].pop(item['id'])==prooftext_record(item),item['id']
    result['version']=plan['basis_version']
    return result
