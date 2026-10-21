"""Compile separate editorial glosses without modifying the audited paragraphs."""
import hashlib
import json
import re
from pathlib import Path


def compile_glosses(handbooks):
    manifest=json.loads(Path(__file__).with_name('editorial_glosses_01311.json').read_text())
    paragraphs={e['id']+'/'+b['id']+'/paragraph-'+str(i):p
                for h in handbooks for e in h['entries'] for b in e['blocks'] for i,p in enumerate(b['paragraphs'],1)}
    compiled={}
    seen=set()
    for annotation in manifest['annotations']:
        key=annotation['claim_id'];text=paragraphs[key]
        assert hashlib.sha256(text.encode()).hexdigest()==annotation['paragraph_sha256'],('Gloss baseline drift',key)
        assert all(ord(c)<=0xffff for c in text),('Review UTF-16 offsets',key)
        anchor=annotation['anchor'];position=-1
        for _ in range(annotation['occurrence']):
            position=text.find(anchor,position+1)
            assert position>=0,('Missing gloss anchor',key,anchor)
        end=position+len(anchor)
        quotations=re.finditer(r'(?<![א-ת])״[^״]+״(?![א-ת])',text)
        assert not any(q.start()<end<q.end() for q in quotations),('Gloss inside quotation',key,anchor)
        identity=(key,end);assert identity not in seen;seen.add(identity)
        assert annotation['label'] in ('תרגום העורך','ביאור העורך')
        compiled.setdefault(key,[]).append({'end':end,'term':annotation['term'],'text':annotation['explanation'],'label':annotation['label']})
    for annotations in compiled.values():annotations.sort(key=lambda a:a['end'])
    return compiled


def explained_text(text,annotations):
    for annotation in reversed(annotations):
        end=annotation['end'];text=text[:end]+' ('+annotation['label']+': '+annotation['text']+')'+text[end:]
    return text
