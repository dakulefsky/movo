from pathlib import Path
import json,html,re,shutil,zipfile,hashlib
ROOT=Path(__file__).resolve().parent
OLD=Path('/workspace/scratch/b9a09bf45b5e/projects/shas/sources')
def clean(s):return html.unescape(re.sub('<[^>]*>','',s)).strip()
sources={}
def source(id,filename,author,refs=None):
 target=ROOT/'sources'/filename
 if not target.exists():shutil.copy2(OLD/filename,target)
 d=json.loads(target.read_text());raw=d['he']; raw=[raw] if isinstance(raw,str) else raw
 sources[id]={'id':id,'author':author,'ref':d['ref'],'citation':d['heRef'],'filename':filename,'url':'https://www.sefaria.org/'+d['ref'].replace(' ','_'),'edition':[{k:v.get(k,'') for k in ['versionTitle','versionSource','license','language']} for v in d.get('versions',[]) if v.get('language')=='he'],'segments':[{'number':i+1,'text':clean(s)} for i,s in enumerate(raw)],'note':''}
 return sources[id]
source('intro','sefaria-kodashim.json','רמב״ם / הקדמת המעתיק')
sources['intro']['note']='מקטעים 1–11 הם הקדמת המעתיק, ולא דברי הרמב״ם. כותרת הקדמת הרמב״ם במקטע 12; דבריו מתחילים במקטע 13. המספור כאן הוא מספור המקטעים בנוסח הדיגיטלי, ולא מספור של המחבר. הנוסח הוא תרגום עברי ישן שבמהדורת וילנא, ולא המקור הערבי. במקטע 36 מופיעה גם המלה ״נדה״, ובהמשך אותו מקטע מפורש ״הזב והזבה״. הלשון הושארה כמות שהיא; המאמר אינו מסיק ממנה חיוב קרבן לנדה. לא נערכה כאן הכרעת נוסח.'
for ref in ['1-1','2-1','2-2','2-3','4-6','5-1','5-6']:
 source('z'+ref,'sefaria-foundation-rambam-zevachim-'+ref+'.json','רמב״ם')
for ref in ['3.1','5.3','5.4','5.5','5.7','5.8']:
 source('z'+ref.replace('.','-'),'Rambam_on_Mishnah_Zevachim.'+ref+'.json','רמב״ם')
for ref in ['1-1','2-1','5-1','6-1']:
 source('m'+ref,'sefaria-foundation-rambam-menachot-'+ref+'.json','רמב״ם')
source('mishnah5','mishnah-zevachim-5.json','משנה')
source('meiri','sefaria-meiri-pesachim.json','מאירי')
sources['z2-1']['note']='במקור יש סוגריים עגולים ומרובעים ובהם שני נוסחים בענין קידוש ידים ורגלים לאחר טומאת הגוף. הם נשמרו ללא הכרעה; המאמר אינו מבאר דין זה.'
sources['m1-1']['note']='בסוף הקטע נזכרת ברייתא בסדר המנחה, אך גוף הברייתא אינו מופיע במקטע השמור הזה. אין כאן השלמה שלה מתוך השערה. תוספת המסומנת ״יעב״ץ״ נשמרה כסימונה במקור.'
for ref in ['6.4','6.5']:
 source('z'+ref.replace('.','-'),'Rambam_on_Mishnah_Zevachim.'+ref+'.json','רמב״ם')
source('mishnah6','Mishnah_Zevachim.6.json','משנה')
source('keritot4','Mishnah_Keritot.4.1.json','משנה')
source('bekhorot2','Rambam_on_Mishnah_Bekhorot.2.1.json','רמב״ם')
source('maaser9','Rambam_on_Mishnah_Bekhorot.9.7.json','רמב״ם')
source('maaser-mishnah','Mishnah_Bekhorot.9.7.json','משנה')
source('bread7','Rambam_on_Mishnah_Menachot.7.1.json','רמב״ם')
source('pesach5','Rambam_on_Mishnah_Pesachim.5.1.json','רמב״ם')
source('bekhor-torah','Exodus.13.12.json','תורה')
# New areas: only source snapshots and exact selected texts are reused.
source('t-intro','sefaria-tahorot.json','רמב״ם')
sources['t-intro']['note']='הקדמת הרמב״ם לסדר טהרות, בנוסח העברי הדיגיטלי השמור. המספור כאן הוא לפי מקטעיו. תוספות, סוגריים והערות שבנוסח נשמרו. במקטע 23 יש לשון קשה במשפט הפותח ״והדין אשר יכלול אבות הטומאה״; לא הוכרעה כאן הגהה. ההסבר נסמך על המאמר המפורש המובא שם בהמשך: ״דאב מטמא אדם וכלים...״. הצגת השיטות היא על פי הרמב״ם, ואין היא טענה להסכמת כל הראשונים.'
for i in range(1,5):source('t-kelim-'+str(i),'Rambam_on_Mishnah_Kelim.1.'+str(i)+'.json','רמב״ם')
source('t-hechsher','Rambam_on_Mishnah_Makhshirin.1.1.json','רמב״ם')
for ref in ['1-7','1-8','9-1']:source('t-mik-'+ref,'sefaria-foundation-rambam-mikvaot-'+ref+'.json','רמב״ם')
source('t-hazaah','Numbers.19.12.json','תורה')
for b,refs in {'kiddushin':['1-1','2-1','3-12'],'yevamot':['1-1','2-1','12-1','12-6'],'terumot':['1-1','3-6','4-3'],'maaser_sheni':['1-1','2-1','4-3','5-6','5-10'],'maasrot':['1-1','1-5'],'challah':['1-1','2-5','2-7'],'orlah':['1-1','3-9'],'kilayim':['1-7','8-1'],'sheviit':['7-1','8-1','10-1']}.items():
 for r in refs:source('a-'+b+'-'+r,'area-'+b+'-'+r+'.json','רמב״ם')
for b,refs in {'terumot':['1-1','3-6','4-3'],'kiddushin':['1-1','3-12'],'yevamot':['12-6'],'challah':['1-1','2-5','2-6','2-7'],'kilayim':['8-1'],'sheviit':['10-1']}.items():
 for r in refs:source('am-'+b+'-'+r,'mishnah-area-'+b+'-'+r+'.json','משנה')
source('i-meiri','sefaria-meiri-ketubot.json','מאירי')
source('i-ket-5-2','Rambam_on_Mishnah_Ketubot.5.2.json','רמב״ם')
source('i-ket-4-7','sefaria-foundation-rambam-ketubot-4-7.json','רמב״ם')
for r in ['1-1','8-1','9-3']:source('i-get-'+r,'sefaria-foundation-rambam-gittin-'+r+'.json','רמב״ם')
for id,f in [('z-levi','Numbers.18.21.json'),('z-trumat-maaser','Numbers.18.26.json'),('z-maaser-verses','Deuteronomy.14.22-26.json'),('z-orlah-verses','Leviticus.19.23-24.json'),('z-sheviit-verses','Leviticus.25.4-5.json')]:source(id,f,'תורה')
# The avodot sections use the actual texts below, read before drafting.
for ref in ['1.4','4.1','4.2','9.1']:
 source('av-z-'+ref,'Rambam_on_Mishnah_Zevachim.'+ref+'.json','רמב״ם')
 source('av-mz-'+ref,'Mishnah_Zevachim.'+ref+'.json','משנה')
for ref in ['9.7','9.8','9.9','5.6','5.7']:
 source('av-m-'+ref,'Rambam_on_Mishnah_Menachot.'+ref+'.json','רמב״ם')
 source('av-mm-'+ref,'Mishnah_Menachot.'+ref+'.json','משנה')
source('av-olah-verses','Leviticus.1.7-9.json','תורה')
sources['av-z-4.1']['note']='בנוסח השמור מופיעים קטע מוסגר והערה המייחסת אותו לגליון. שניהם נשמרו כלשונם. זוהי הערת המהדורה השמורה ולא הכרעת נוסח חדשה של התוסף. ההסבר כאן נסמך על מחלוקת המשנה ועל המסקנה המפורשת בפירוש הרמב״ם.'
sources['av-z-1.4']['note']='ההסבר אינו מכריע בלשון ״חוץ לעזרה״ שבביאור מקום שאינו צריך להלך, ואינו משחזר ממנה מסלול עבודה. הנוסח נשמר לעיון; עיקר ההסבר כאן הוא מחלוקת התנאים בדין ההולכה ופסיקת הרמב״ם.'
source('av-chullin','Rambam_on_Mishnah_Chullin.2.1.json','רמב״ם')

# Selective introductory index: actual source passages read before drafting.
source('n-Shabbat-7.2','Rambam_on_Mishnah_Shabbat.7.2.json','רמב״ם')
source('n-m-Shabbat-7.2','Mishnah_Shabbat.7.2.json','משנה')
source('n-Shabbat-1.1','Rambam_on_Mishnah_Shabbat.1.1.json','רמב״ם')
source('n-m-Shabbat-1.1','Mishnah_Shabbat.1.1.json','משנה')
source('n-Beitzah-5.2','Rambam_on_Mishnah_Beitzah.5.2.json','רמב״ם')
source('n-m-Beitzah-5.2','Mishnah_Beitzah.5.2.json','משנה')
source('n-Sukkah-1.1','Rambam_on_Mishnah_Sukkah.1.1.json','רמב״ם')
source('n-m-Sukkah-1.1','Mishnah_Sukkah.1.1.json','משנה')
source('n-Pesachim-10.1','Rambam_on_Mishnah_Pesachim.10.1.json','רמב״ם')
source('n-m-Pesachim-10.1','Mishnah_Pesachim.10.1.json','משנה')
source('n-Bava_Kamma-1.1','Rambam_on_Mishnah_Bava_Kamma.1.1.json','רמב״ם')
source('n-m-Bava_Kamma-1.1','Mishnah_Bava_Kamma.1.1.json','משנה')
source('n-Bava_Metzia-2.1','Rambam_on_Mishnah_Bava_Metzia.2.1.json','רמב״ם')
source('n-m-Bava_Metzia-2.1','Mishnah_Bava_Metzia.2.1.json','משנה')
source('n-Bava_Metzia-7.8','Rambam_on_Mishnah_Bava_Metzia.7.8.json','רמב״ם')
source('n-m-Bava_Metzia-7.8','Mishnah_Bava_Metzia.7.8.json','משנה')
source('n-Bava_Metzia-7.9','Rambam_on_Mishnah_Bava_Metzia.7.9.json','רמב״ם')
source('n-m-Bava_Metzia-7.9','Mishnah_Bava_Metzia.7.9.json','משנה')
source('n-Bava_Metzia-8.1','Rambam_on_Mishnah_Bava_Metzia.8.1.json','רמב״ם')
source('n-m-Bava_Metzia-8.1','Mishnah_Bava_Metzia.8.1.json','משנה')
source('n-Bava_Metzia-4.1','Rambam_on_Mishnah_Bava_Metzia.4.1.json','רמב״ם')
source('n-m-Bava_Metzia-4.1','Mishnah_Bava_Metzia.4.1.json','משנה')
source('n-Kiddushin-1.5','Rambam_on_Mishnah_Kiddushin.1.5.json','רמב״ם')
source('n-m-Kiddushin-1.5','Mishnah_Kiddushin.1.5.json','משנה')
source('n-Sanhedrin-3.1','Rambam_on_Mishnah_Sanhedrin.3.1.json','רמב״ם')
source('n-m-Sanhedrin-3.1','Mishnah_Sanhedrin.3.1.json','משנה')
sources['n-Sanhedrin-3.1']['note']='בנוסח השמור מופיע ״ר׳ (יהודה) [מאיר]״. שתי הקריאות נשמרו; לא הוכרעה כאן הגהה. ההסבר אינו נסמך על השם שבמקום המסופק.'

# Only passages actually cited by this expansion are entered into the offline catalogue.
from coverage_expansion import additions, issur
_cited={ref['source'] for entries in [*additions.values(),issur] for ent in entries for block in ent['blocks'] for ref in block['refs']}
for id in sorted(_cited):
 if id in sources:continue
 if id=='c-nesachim-verses':source(id,'next-Numbers.15.4-10.json','תורה');continue
 if id=='c-temurah-verse':source(id,'next-Leviticus.27.10.json','תורה');continue
 assert id.startswith('c-'),id
 tail=id[2:];m=tail.startswith('m-');tail=tail[2:] if m else tail
 book,loc=tail.rsplit('-',1)
 filename=('Mishnah_' if m else 'Rambam_on_Mishnah_')+book+'.'+loc+'.json'
 source(id,('next-'+filename) if (ROOT/'sources'/('next-'+filename)).exists() else filename,'משנה' if m else 'רמב״ם')
sources['c-Chullin-3.1']['note']='סוגריים, הצעות הגהה ותוספות שבנוסח הדיגיטלי נשמרו. אין כאן הכרעת נוסח או אימות אנטומי מחודש של כל פרט; המבוא אינו מסיק דין מן המקומות המסופקים.'
sources['c-Peah-1.2']['note']='הרמב״ם מביא שני נוסחים, ״ענוה״ ו״ענבה״, ומפרש את שניהם. שניהם נשמרו ללא הכרעת נוסח חדשה.'

source('review-shomrim','next-Rambam_on_Mishnah_Shevuot.8.1.json','רמב״ם')
source('review-zavim','next-Rambam_on_Mishnah_Zavim.1.1.json','רמב״ם')
source('review-nissuin-m','next-Mishnah_Ketubot.4.4.json','משנה')

# Introductory additions: only references actually used in the explanations.
from index_more import more
_p_refs={ref['source'] for entries in more.values() for ent in entries for block in ent['blocks'] for ref in block['refs']}
for id in sorted(_p_refs):
 if id in sources:continue
 if id=='p-meiri-bitul':source(id,'index7-Meiri_on_Pesachim.6b.json','מאירי');continue
 if id=='p-meiri-geneivah':source(id,'index7-Meiri_on_Bava_Kamma.79b.json','מאירי');continue
 if id=='p-gezel-verse':source(id,'index7-Leviticus.5.23.json','תורה');continue
 assert id.startswith('p-'),id
 tail=id[2:];m=tail.startswith('m-');tail=tail[2:] if m else tail
 book,loc=tail.rsplit('-',1)
 source(id,'index7-'+('Mishnah_' if m else 'Rambam_on_Mishnah_')+book+'.'+loc+'.json','משנה' if m else 'רמב״ם')
sources['p-meiri-bitul']['note']='במקטעים 3–4 המאירי דן בשתי גרסאות ובפירושים שונים לסוגיה. דבריו והכרעתו נשמרו כלשונם; אין כאן הכרעת נוסח נוספת של עורך התוסף. ההסבר אינו משחזר נוסח גמרא מתוך השערה.'
sources['p-Rosh_Hashanah-3.1']['note']='סוגריים עגולים ומרובעים נשמרו. בפסקה האחרונה הרמב״ם דן גם בלשון יום כ״ט ערבית, שקיעה וצאת הכוכבים; המבוא אינו מכריע בכל פרטי חשבון הזמן ואינו מחליף את לשון המקור בנוסח אחר.'

from index_next import next_entries
for _book,_loc in [('Bava_Kamma','8.1'),('Sanhedrin','3.6')]:
 for _m in [False,True]:
  source('q-'+('m-' if _m else '')+_book+'-'+_loc,'index8-'+('Mishnah_' if _m else 'Rambam_on_Mishnah_')+_book+'.'+_loc+'.json','משנה' if _m else 'רמב״ם')
sources['q-Bava_Kamma-8.1']['note']='הפירוש כולל בהמשך דיון בסמיכה ובגביית חיובים בארץ ובחוץ לארץ, וכן לשון ״שבת ובושת ורפוי וצער וקנס״. הנוסח נשמר ולא הוחלף ב״נזק״. המבוא עוסק בהבחנה בין חמשת התשלומים ואינו מסיק מלשון זו סיווג חדש של כולם כקנס או הוראה בדבר סמכות הגבייה.'

# Core coverage: register only sources actually cited by the short introductions.
from coverage_core import core_additions
_v_refs={ref['source'] for entries in core_additions.values() for ent in entries for block in ent['blocks'] for ref in block['refs']}
for id in sorted(_v_refs):
 if id in sources:continue
 special={'v-niddah-verse':('Leviticus.15.19','תורה'),'v-zavah-verses':('Leviticus.15.25-29','תורה'),'v-ramban-biur':('Ramban_on_Leviticus.25.7','רמב״ן')}
 if id in special:
  _ref,_author=special[id];source(id,'coverage9-'+_ref+'.json',_author);continue
 tail=id[2:];m=tail.startswith('m-');tail=tail[2:] if m else tail
 book,loc=tail.rsplit('-',1)
 source(id,'coverage9-'+('Mishnah_' if m else 'Rambam_on_Mishnah_')+book+'.'+loc+'.json','משנה' if m else 'רמב״ם')
sources['v-Niddah-4.7']['note']='הסוגריים ״(אלה) [ד״נ אליה]״ ולשונות הבדיקות והווסת נשמרו. המבוא משתמש בחילוק המפורש בין זבה גדולה לשומרת יום, ואינו מכריע כאן חשבון וסתות או חשבון ימי נדה וזיבה למעשה.'
sources['v-Oholot-3.1']['note']='המבוא משתמש בתיאור המפורש של אדם המאהיל על המת ושל אדם וטומאה תחת אהל. המשך הפירוש דן בצירוף חצאי שיעורים ובטומאה רצוצה; הוא שמור במלואו אך אינו מתמצה בהסבר הקצר.'
sources['v-Oholot-3.7']['note']='סוגריים וקריאות חלופיות שבנוסח הדיגיטלי נשמרו. דוגמת הביב אינה הוראה כללית על כל כיסוי או פתח; יש לעיין בתנאי המקרה שבמשנה ובפירוש.'

# Fidelity review: preserve genuine source differences without deciding an emendation.
sources['a-yevamot-2-1']['note']='בנוסח נשמרה המלה ״(אין)״ בסוגריים בתוך דוגמת לאה ורחל. הביאור נשען על המסקנה המפורשת ״שיחלוץ לוי ללאה ולא ייבם אותה״ ועל סיום הפירוש ״חומרא משני צדדין״; אין כאן הכרעת הגהה במלה שבסוגריים.'
sources['c-Gittin-9.4']['note']='בפירוש השמור נכתב ״רבי אליעזר״, ואילו במשנה המצוטטת נכתב ״רבי אלעזר״. שתי לשונות המקורות נשמרו ללא תיקון; שם התנא בביאור הולך אחר המשנה.'

sources['a-sheviit-10-1']['note']='בפירוש השמור ״שלא בשטר״ מתפרש כשטר שאין בו אחריות נכסים, ו״בשטר״ כשטר שיש בו אחריות. הלשון נשמרה בלי להחליפה בפירוש אחר. הביאור הקצר עוסק בחילוק בין מלוה להקפת חנות ואינו מכריע כאן את פירוש שתי הלשונות.'
sources['a-kilayim-8-1']['note']='מקטע 2 בנוסח השמור מסתיים בשלוש נקודות. לא הושלם טקסט חסר מתוך השערה; הביאור אינו מסיק דין מן ההמשך שאינו מופיע במקטע.'

sources['t-kelim-2']['note']='הנוסח כולל סוגריים במשפט על היסט נבילה, וכן משפט ״וכאשר הועתק ... והוא מועתק ממנה״ שלשונו קשה מול התנאי המפורש שלפניו. הכול נשמר ללא תיקון. הביאור נסמך על התנאי ״והוא מחובר באב״ ועל המשפט המפורש שאחרי הפירוש מן הנבילה אינו מטמא בגדים.'
sources['t-kelim-4']['note']='במקטע 1 מופיעות סמוך זו לזו לשונות שונות בדין בועל זבה. הן נשמרו ללא הכרעת נוסח. המקור מצוטט במבוא לצורך ההגדרות המפורשות של משכב, מושב ומרכב בסופו, ולא לצורך הכרעה במשפטים הקשים האלה.'
