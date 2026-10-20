from pathlib import Path
import json
from source_catalog import sources
from handbook import entries
from other_handbooks import new_handbooks
from avodot import avodot
from final_handbooks import final_handbooks
from coverage_expansion import additions, issur_handbook
from index_more import more
from index_next import next_entries
from coverage_core import core_additions
from coverage_013 import apply_expansion, letters_only
ROOT=Path(__file__).resolve().parent
policy={
 'format':'subject-handbook',
 'scope':'מפתח לעניינים המרכזיים בלבד. אין להוסיף תחומים או מונחים רק כדי להגדיל את ההיקף. מבוא לסוגיות המרכזיות: מבאר את הענין, סדרו, מקורותיו וחילוקיו העיקריים לפני הכניסה למשא ומתן של הסוגיה. אין להוסיף סעיפים לשם מיצוי כל פרט ודעה.',
 'fidelity':'הביאור נשען על האמור במקור המצוטט. אין להוסיף טעמים, מסקנות או מסגרות מושגיות שאינם מפורשים בו. ספקות נוסח ומחלוקות נשמרים בגלוי.',
 'principle':'בכל תחום מסבירים את הדברים, הפעולות והדינים הנצרכים להבנתו: מהו כל ענין, כיצד הוא נעשה, מתי הוא נוהג ומה פרטיו. אין להצטמצם לשמות חפצים או קרבנות בלבד.',
 'organization':'תחומים רחבים בלבד בראש הספרייה; בתוכם ענינים מסודרים, עם כותרות משנה המשתנות לפי הצורך.',
 'style':'הסברים בעלי תוכן ממשי בלשון בית המדרש; לא הערות קצרות בלבד, ולא פתיחות מאמריות שאין להן עוגן במקור.',
 'sources':'כל הסבר ערוך נבדל מלשון המחבר ומקושר למקורות שנקראו בפועל. אין להרחיב מן הזיכרון או להסיק הכרעת נוסח בלי ראיה.',
 'future_examples':{
  'טהרות':['טומאת מת','שרץ','נבילה','זב','טומאת אדם וכלים','דרכי הטהרה'],
  'אישות':['קידושין','נישואין','גירושין','יבום וחליצה'],
  'זרעים':['תרומה','מעשרות','חלה','ערלה','כלאים']
 },
 'status':'נכתבו מבואות נבחרים בששה תחומים. זהו מפתח מבואי ולא אנציקלופדיה; אין זו טענת כיסוי מלא.'
}
H={
 'id':'kodashim','title':'קדשים','subtitle':'מיני הקרבנות וסדרי העבודה',
 'method':'ההסברים ערוכים על פי הקדמת הרמב״ם לסדר קדשים ופירוש המשנה, ואינם ציטוט מלשונו. מקורות לכל סעיף נפתחים תחתיו. המקרא והמאירי נזכרים במפורש במקומות שנעזרנו בהם.',
 'limits':'נכתבו עיקרי הקרבנות ומבואות לסמיכה, שחיטה, קבלה, הולכה, זריקה, הקטרה, מליקה ותנופה. לא נתבארו כל פסולי העבודה, הנסכים, כל המנחות, מעילה ותמורה, סדר יום הכפורים או פסח שני. דיני כוונת העובד, כל שיעורי הדם, הולכה שלא ברגל וזמני הקטרת לילה עדיין צריכים הרחבה.',
 'entries':entries
}
at=next(i for i,e in enumerate(entries) if e['id']=='avodot')
H['entries']=[*entries[:at],*avodot,*entries[at:]]
# Reciprocal links from offerings to the actual service explanations.
for ent in H['entries']:
 if ent['id'] in ['olah','chattat','asham','shelamim','todah','nazir','public-shelamim','bekhor','maaser','pesach']:
  target=next((b for b in ent['blocks'] if b['id'] in ['service','outer']),ent['blocks'][-1])
  target['links']=list(dict.fromkeys([*target['links'],'av-shechitah','av-kabbalah','av-zerikah','av-haktarah']))
  if ent['id'] in ['shelamim','public-shelamim','asham']:target['links'].append('av-tenufah')
  if ent['id'] in ['olah','chattat','asham','shelamim','todah','nazir']:target['links'].append('av-semichah')
  for subsection in ent['blocks']:
   if subsection['id']=='bird':subsection['links']=list(dict.fromkeys([*subsection['links'],'av-melikah']))
handbooks=[H,*new_handbooks,*final_handbooks,issur_handbook]
# Keep each broad area in an intentional reading order; do not create a main tab per tractate.
orders={
 'kodashim':['olah','chattat','asham','shelamim','todah','nazir','public-shelamim','bekhor','maaser','pesach','minchah','k-nesachim','av-semichah','av-shechitah','av-kabbalah','av-holachah','av-zerikah','av-haktarah','av-melikah','av-tenufah','avodot','imurim','pesulim','k-meilah','k-temurah','public'],
 'tahorot':['t-met','t-sheretz','t-nevelah','t-zav','t-niddah','t-contact','t-ohel','t-ranks','t-kelim','t-hechsher','t-yadayim','t-tevilah','t-hazaah','t-safek'],
 'ishut':['i-kiddushin','i-nissuin','i-ketubah','i-shlichut','i-gerushin','i-lishmah','i-edei-get','i-yibum','i-chalitzah','i-maamar'],
 'zeraim':['z-peah','z-hafrashah','z-terumah','z-maaser-rishon','z-maaser-sheni','z-maaser-ani','z-demai','z-challah','z-orlah','z-bikkurim','z-kilayim','z-sheviit','z-biur','z-shemittat-kesafim','z-prozbul'],
 'moed':['s-melachot','s-hotzaah','s-eruv','s-techum','s-shvut','s-muktzeh','s-yomtov','s-bedikah','s-biur','s-pesach-night','s-chodesh','s-shofar','s-yom-kippur','s-sukkah','s-lulav','s-megillah','s-chol-hamoed'],
 'mammon':['d-nezikin','d-chovel','d-geneivah','d-gezel','d-shomrim','d-ribit','d-avedah','d-karka','d-mitaltelin','d-onaah','d-shutfin','d-harchakah','d-yerushah','d-chazakah','d-shevuot','d-edut','d-dayanim']}
for h in handbooks:
 h['entries']=[*h['entries'],*additions.get(h['id'],[]),*more.get(h['id'],[]),*next_entries.get(h['id'],[]),*core_additions.get(h['id'],[])]
 if h['id'] in orders:
  by_id={e['id']:e for e in h['entries']};assert set(by_id)==set(orders[h['id']]);h['entries']=[by_id[id] for id in orders[h['id']]]
 for ent in h['entries']:
  if ent['id']=='minchah':ent['group']='מנחות ונסכים'
  if ent['id'] in ['i-lishmah','i-edei-get']:ent['group']='מעשי האישות'
  if ent['id']=='t-yadayim':ent['group']='מדרגות ודיני הניטמאים'
  if h['id']=='zeraim':
   ent['group']='מתנות והפרשה' if ent['id'] in ['z-peah','z-hafrashah','z-terumah','z-maaser-rishon','z-maaser-sheni','z-maaser-ani','z-demai'] else 'חיובים בעיסה ובאילן' if ent['id'] in ['z-challah','z-orlah','z-bikkurim'] else 'כלאים ושביעית'
 # Use concise boundaries rather than promising exhaustive expansion.
 limits={
 'kodashim':'נכללו מיני הקרבנות, עיקרי העבודה, נסכים, פסולי מחשבה, מעילה ותמורה. לא נכללו כל מיני המנחות, סדר עבודת יום הכפורים, פסח שני, כל פסולי העבודה ופרטי זמני ההקטרה. זהו מבוא לסוגיות ולא ספר הלכות מקיף.',
 'tahorot':'נכללו מקורות הטומאה העיקריים, העברתה, דרגותיה, ידיים, הכשר, טבילה, הזאה וספקות נבחרים. פרטי אהל, נגעים, חשבון ימי נדה וזיבה, מקואות וספקות בכל מסכת אינם מכוסים. הצגת שיטת הרמב״ם אינה טענה להסכמת כל הראשונים.',
 'ishut':'נכללו קידושין ונישואין, כתובה, שליחות, נתינת הגט וכתיבתו לשמה, עדי מסירה, יבום וחליצה. לא נכללו כל העריות, צורות החופה ושיטותיהן, תנאים, מיאון ופרטי ממונות האישות. אין כאן סדר למעשה קידושין או גירושין.',
 'zeraim':'נכללו מתנות עניים, תרומות ומעשרות, דמאי, חלה, ערלה, ביכורים, כלאים, שביעית ופרוזבול. לא נכללו כל חיובי הארץ וחוץ לארץ, קביעת שנות הפירות, תערובות, פרטי זמני הביעור ופרטי הפדיון. השיעורים הקדומים לא הומרו למשקל או למטבע בני זמננו.',
 'moed':'נכללו מלאכה ושבות, עירובין ותחומין, מוקצה והכנה, בדיקת חמץ וביעורו, קידוש החודש ויסודות במצוות המועדים. לא נכללו כל המלאכות, תערובות חמץ, חשבון הלוח לפרטיו, תעניות, חנוכה ודיני אבלות. זוהי הכנה לסוגיות נבחרות ולא סדר הלכות למעשה.',
 'mammon':'נכללו נזיקין, גניבה וגזלה, שומרים, רבית, מציאה, קנין ואונאה, שכנים, סדר נחלות, חזקה, שבועות ובית דין. לא נכללו כל דיני אדם המזיק, פרטי תשלומי חובל, יאוש ותקנת השבים, חלוקת עיזבון לפרטיה, שטרות ופרטי דיני עדות. הסעיפים מעמידים את החילוקים הראשונים ואינם הוראה לדון מקרה מסוים.'}
 if h['id'] in limits:h['limits']=limits[h['id']]
 # Related-entry links stay within their broad area.
 links={'t-ohel':['t-met','t-contact'],'t-niddah':['t-zav','t-tevilah'],'z-biur':['z-sheviit'],'d-chovel':['d-nezikin'],'d-edut':['d-dayanim'],'s-bedikah':['s-biur','s-pesach-night'],'s-biur':['s-bedikah'],'d-geneivah':['d-gezel'],'d-gezel':['d-geneivah'],'d-onaah':['d-karka','d-mitaltelin'],'d-shutfin':['d-harchakah'],'d-harchakah':['d-shutfin'],'k-nesachim':['olah','shelamim','minchah'],'k-meilah':['asham','pesulim'],'k-temurah':['public'],'s-eruv':['s-hotzaah','s-techum'],'s-techum':['s-eruv'],'s-muktzeh':['s-yomtov'],'s-lulav':['s-sukkah'],'d-chazakah':['d-karka'],'d-karka':['d-chazakah','d-mitaltelin'],'d-shevuot':['d-dayanim','d-shomrim'],'z-prozbul':['z-shemittat-kesafim'],'z-shemittat-kesafim':['z-prozbul'],'z-demai':['z-hafrashah','z-maaser-rishon'],'z-bikkurim':['z-hafrashah'],'i-lishmah':['i-gerushin','i-edei-get'],'i-edei-get':['i-gerushin'],'t-yadayim':['t-ranks','t-safek'],'a-terefah':['a-shechitah'],'a-taam':['a-basar-chalav'],'a-hatarah':['a-neder'],'a-neder':['a-shevuah']}
 for ent in h['entries']:
  if ent['id'] in links:ent['blocks'][-1]['links']=list(dict.fromkeys([*ent['blocks'][-1]['links'],*links[ent['id']]]))

# Scope is the six approved broad areas; Shabbat and Moed are excluded entirely.
handbooks=[h for h in handbooks if h['id']!='moed']
# Bundle only sources used by the remaining introductions.
used_sources={ref['source'] for h in handbooks for e in h['entries'] for b in e['blocks'] for ref in b['refs']}
# Coverage supplements are applied later: include their refs before pruning the catalogue.
for filename in ('coverage_013_entries.json','coverage_013_details_a.json','coverage_013_details_b.json'):
 payload=json.loads((ROOT/filename).read_text(encoding='utf-8'))
 new_blocks=[b for e in payload.get('entries',[]) for b in e['blocks']]+[item['block'] for item in payload.get('additions',[])]
 used_sources.update(r['source'] for b in new_blocks for r in b['refs'])
# Retain directly cited source passages added by the sixth audit.
for reviewed in json.loads((ROOT/'SOURCE-REVIEW-0.13.5.json').read_text(encoding='utf-8'))['changes']:
 for r in reviewed.get('addRefs',[]):used_sources.add(r['source'])
 if reviewed.get('proof'):used_sources.add(reviewed['proof']['sourceId'])
sources={id:source for id,source in sources.items() if id in used_sources}

# Attribution correction after reading the Mishnah and Rambam passages together.
for h in handbooks:
 if h['id']=='ishut':
  for ent in h['entries']:
   if ent['id']=='i-edei-get':
    for block in ent['blocks']:block['by']='ביאור ערוך על פי המשנה והרמב״ם'

from fidelity_review import apply_review
apply_review(handbooks,sources)
from prose_refresh import apply_prose_refresh
apply_prose_refresh(handbooks)
from prose_revision import apply_prose_revision
apply_prose_revision(handbooks)
# Extend the reviewed core with independently anchored, in-depth introductions.
coverage_summary=apply_expansion(handbooks,sources)
print('source-anchored expansion:',coverage_summary)

# Sixth source-first audit: make the reviewed corrections in the built corpus,
# preserving the historical source and prose overlays without mutating quotations.
sixth=json.loads((ROOT/'SOURCE-REVIEW-0.13.5.json').read_text(encoding='utf-8'))
assert sixth['version']=='0.13.5'
block_index={e['id']+'/'+b['id']:b for h in handbooks for e in h['entries'] for b in e['blocks']}
assert len(sixth['changes'])==15
seen_sixth=set()
for edit in sixth['changes']:
 key=edit['blockId']
 assert key in block_index and key not in seen_sixth, ('sixth-audit block mismatch',key)
 block=block_index[key]
 assert edit['oldQuote'] in ' '.join(block['paragraphs']), ('sixth-audit stale original',key)
 assert edit['paragraphs'] and all(p.strip() for p in edit['paragraphs']), key
 block['paragraphs']=edit['paragraphs']
 for ref in edit.get('addRefs',[]):
  assert ref['source'] in sources, ('sixth-audit missing cited source',key,ref)
  if ref not in block['refs']:block['refs'].append(ref)
 proof=edit.get('proof')
 if proof:
  src=sources[proof['sourceId']]
  segment=proof['segment']
  assert 1<=segment<=len(src['segments']), (key,'bad source segment')
  assert letters_only(proof['sourceQuote']) in letters_only(src['segments'][segment-1]['text']), (key,'source passage drift')
  assert letters_only(proof['explanationQuote']) in letters_only(' '.join(block['paragraphs'])), (key,'explanation drift')
  proof_ref={'source':proof['sourceId'],'segments':[segment]}
  if not any(r['source']==proof_ref['source'] and segment in r['segments'] for r in block['refs']):
   block['refs'].append(proof_ref)
 seen_sixth.add(key)

# Source-anchored depth pass: expand thin introductions only where the exact
# cited source supplies an additional legal distinction or a concrete example.
depth=json.loads((ROOT/'DEPTH-REVIEW-0.13.5.json').read_text(encoding='utf-8'))
assert depth['version']=='0.13.5' and len(depth['updates'])==5
depth_seen=set()
for edit in depth['updates']:
 key=edit['blockId']
 assert key in block_index and key not in depth_seen, ('depth block',key)
 b=block_index[key]
 proof=edit['proof'];segment=proof['segment'];src=sources[proof['sourceId']]
 assert any(r['source']==proof['sourceId'] and segment in r['segments'] for r in b['refs']), ('depth cite',key)
 assert letters_only(proof['sourceQuote']) in letters_only(src['segments'][segment-1]['text']), ('depth source',key)
 assert letters_only(proof['explanationQuote']) in letters_only(' '.join(edit['paragraphs'])), ('depth prose',key)
 assert len(' '.join(edit['paragraphs']).split())>=90, ('still too short',key)
 b['paragraphs']=edit['paragraphs']
 depth_seen.add(key)


# Guide readers through closely related fundamental sugyot, rather than
# sending them back to the directory after every introduction.
reading_paths={
 'k-inner-chattat':['chattat','k-matanot','k-pigul','av-kabbalah','av-zerikah'],
 'k-matanot':['k-inner-chattat','k-pigul','av-zerikah','chattat'],
 'k-pigul':['k-matanot','k-inner-chattat','av-shechitah','av-kabbalah','av-holachah','av-zerikah'],
 'av-shechitah':['av-kabbalah','av-holachah','k-pigul'],
 'av-kabbalah':['av-shechitah','av-holachah','av-zerikah','k-inner-chattat'],
 'av-holachah':['av-kabbalah','av-zerikah','k-pigul'],
 'av-zerikah':['av-kabbalah','k-matanot','k-inner-chattat','k-pigul'],
 'k-meilah':['k-temurah','asham'],
 'i-ketubah':['i-kiddushin','i-gerushin'],
 'z-challah':['z-hafrashah']
}
entry_by_id={e['id']:e for h in handbooks for e in h['entries']}
for origin,targets in reading_paths.items():
 if origin not in entry_by_id: continue
 valid=[target for target in targets if target in entry_by_id and target!=origin]
 for block in entry_by_id[origin]['blocks']:
  if block is entry_by_id[origin]['blocks'][-1]:
   block['links']=list(dict.fromkeys([*block['links'],*valid]))
# Source-based editorial depth report. A short specific definition may be
# sufficient; the report flags candidates for review, not automatic filler.
depth_report={'edition':'0.13.5','purpose':'Editorial triage, not a claim of full Torah coverage','handbooks':[],'thin_candidates':[]}
for handbook in handbooks:
 total=0;short=0
 for entry_ in handbook['entries']:
  for block in entry_['blocks']:
   total+=1
   words=len(' '.join(block['paragraphs']).split())
   if words<60:
    short+=1
    depth_report['thin_candidates'].append({'handbook':handbook['id'],'entry':entry_['id'],'block':block['id'],'words':words,'sources':[r['source'] for r in block['refs']]})
 depth_report['handbooks'].append({'id':handbook['id'],'entries':len(handbook['entries']),'blocks':total,'under_60_words':short})
(ROOT/'EDITORIAL-DEPTH-REPORT.json').write_text(json.dumps(depth_report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


all_entries=[e for h in handbooks for e in h['entries']]
ids=[e['id'] for e in all_entries]
assert len(ids)==len(set(ids)), 'Entry IDs must be globally unique'
for h in handbooks:
 for e in h['entries']:
  assert e['blocks']
  for b in e['blocks']:
   assert b['refs'],(h['id'],e['id'],b['id'])
   for r in b['refs']:
    assert r['source'] in sources
    assert all(1<=n<=len(sources[r['source']]['segments']) for n in r['segments']),(e['id'],b['id'],r)
   assert all(l in set(ids) for l in b['links']), (e['id'],b['id'],b['links'])
# Verify exact passage extraction against the preserved raw source, not as an interpretation test.
for src in sources.values():
 d=json.loads((ROOT/'sources'/src['filename']).read_text())
 if 'provenance' in d:
  obj=json.loads((ROOT/'sources'/d['provenance']['file']).read_text())
  for key in d['provenance']['jsonPath']:obj=obj[key]
  obj=[obj] if isinstance(obj,str) else obj
  assert obj==d['he'],src['filename']
data={'schemaVersion':2,'version':'0.13.5','author':'DanTheMan','editorialPolicy':policy,'subjects':[{'id':id,'title':title,'status':status} for id,title,status in [('kodashim','קדשים','available'),('tahorot','טהרות','available'),('ishut','אישות','available'),('zeraim','זרעים','available'),('mammon','דיני ממונות','available'),('issur','איסור והיתר','available')]],'handbooks':handbooks,'sources':sources}
(ROOT/'plugin/data').mkdir(parents=True,exist_ok=True)
(ROOT/'plugin/data/library.js').write_text('window.MEVOOT='+json.dumps(data,ensure_ascii=False)+';\n')
(ROOT/'editorial.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(ROOT/'EDITORIAL-FORMAT.json').write_text(json.dumps(policy,ensure_ascii=False,indent=2))
def export(h):
 lines=['# '+h['title']+' — '+h['subtitle'],'',h['method'],'']
 for e in h['entries']:
  lines+=['## '+e['title'],'']
  for b in e['blocks']:
   lines+=['### '+b['title'],'']
   for text in b['paragraphs']:lines+=[text,'']
   for item in b['items']:lines+=['**'+item['label']+'** — '+item['text'],'']
   lines+=['מקורות: '+'; '.join(sources[r['source']]['citation']+' — מקטעים '+','.join(map(str,r['segments'])) for r in b['refs']),'']
   if b['by']!='ביאור ערוך על פי הרמב״ם':lines+=[b['by'],'']
 lines+=['## היקף ההסברים','',h['limits']]
 return '\n'.join(lines)
(ROOT/'Mevoot-Shas-Content.md').write_text('\n\n---\n\n'.join(export(h) for h in handbooks))
for h in handbooks:
 words=sum(len(text.split()) for e in h['entries'] for b in e['blocks'] for text in b['paragraphs'])+sum(len(i['text'].split()) for e in h['entries'] for b in e['blocks'] for i in b['items'])
 print(h['id'],len(h['entries']),'entries',sum(len(e['blocks']) for e in h['entries']),'blocks',words,'Hebrew words')
print(len(sources),'bundled sources')
