(()=>{'use strict';
const D=window.MEVOOT,$=id=>document.getElementById(id);
// Entry IDs are globally unique. Cross-handbook links must resolve in the full library.
const allEntriesById=new Map(D.handbooks.flatMap(handbook=>handbook.entries.map(entry=>[entry.id,entry])));
let H=null;
const el=(tag,text)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;return n;};
const btn=(text,fn)=>{const b=el('button',text);b.type='button';b.onclick=fn;return b;};
const norm=s=>String(s).normalize('NFKD').replace(/[\u0591-\u05bd\u05bf-\u05c7]/g,'').replace(/[״׳'"־\-–—.,:;!?()[\]]/g,' ').replace(/\s+/g,' ').trim().toLowerCase();
let activeSource=null,activeSegments=[],serial=0,nativeIterator=null,font=24,current=null;
let hasFontPreference=false;
try{const saved=Number(localStorage.getItem('mevoot-v2-font'));if(saved){font=saved;hasFontPreference=true;}}catch{}
function setFont(n,persist=false){font=Math.min(36,Math.max(16,n));document.documentElement.style.setProperty('--reader-size',font+'px');if(persist)try{localStorage.setItem('mevoot-v2-font',font);}catch{}}
setFont(font);
$('smaller').onclick=()=>{hasFontPreference=true;setFont(font-1,true)};$('larger').onclick=()=>{hasFontPreference=true;setFont(font+1,true)};
function applyTheme(theme){
 if(!theme?.colorScheme)return;
 const root=document.documentElement;
 window.MevootTheme.apply(theme);
 const t=theme.typography||{};
 if(t.fontFamily)root.style.setProperty('--font-main',JSON.stringify(t.fontFamily)+',MevootText,serif');
 if(t.uiFontFamily)root.style.setProperty('--font-ui',JSON.stringify(t.uiFontFamily)+',MevootUI,system-ui,sans-serif');
 if(!hasFontPreference&&Number.isFinite(t.fontSize))setFont(t.fontSize);
 if(Number.isFinite(t.lineHeight)&&t.lineHeight>0)root.style.setProperty('--reader-line-height',String(t.lineHeight));
 Promise.resolve(document.fonts.ready).then(()=>window.MevootTheme.ready());
}
window.addEventListener('plugin.boot',event=>applyTheme(event.detail?.theme));
if(window.Otzaria?.on)window.Otzaria.on('theme.changed',applyTheme);

const descriptions={kodashim:'מיני הקרבנות · סדרי העבודה · חלקי הקרבן',tahorot:'מקורות הטומאה · דרכי הטומאה והטהרה',ishut:'קידושין ונישואין · גירושין · יבום וחליצה',zeraim:'תרומות ומעשרות · מתנות עניים · שביעית',mammon:'נזיקין · שומרים · קניינים · בית דין',issur:'שחיטה וטרפות · תערובות · נדרים ושבועות'};
for(const subject of D.subjects){
 const card=btn('',()=>openSubject(subject.id));card.className='subject-card';card.dataset.subject=subject.id;
 const name=el('span',subject.title);name.className='subject-title';const action=el('span','לתוכן העניינים');action.className='card-action';
 const handbook=D.handbooks.find(h=>h.id===subject.id);const count=el('span',(handbook?.entries.length||0)+' מבואות');count.className='card-count';
 card.append(name,el('small',descriptions[subject.id]||''),count,action);$('subjects').append(card);
 const option=el('option',subject.title);option.value=subject.id;$('subject-switch').append(option);
}
function showView(view){for(const id of ['home','directory','entry'])$(id+'-view').hidden=id!==view;$('reading').dataset.view=view;}
function resetSearch(){ $('search').value='';search();$('search-panel').hidden=true;$('search-toggle').setAttribute('aria-expanded','false'); }
function pushRoute(hash){if(location.hash!==hash)history.pushState(null,'',location.pathname+location.search+hash);}
function focusView(){ $('scroll-content').scrollTop=0;$('reading').focus({preventScroll:true}); }
function showHome(){H=null;current=null;$('article').replaceChildren();showView('home');$('subject-switch').value='';document.querySelectorAll('[data-subject]').forEach(b=>b.removeAttribute('aria-current'));renderContinue();}
function renderContinue(){
 const panel=$('continue-panel'),button=$('continue-button');panel.hidden=true;
 try{const previous=JSON.parse(localStorage.getItem('mevoot-last-entry')||'null');if(!previous||typeof previous.id!=='string')return;
 const handbook=D.handbooks.find(h=>h.entries.some(e=>e.id===previous.id));if(!handbook)return;
 const entry=handbook.entries.find(e=>e.id===previous.id);
 button.textContent='המשך לקרוא: '+entry.title+' ←';button.onclick=()=>navigate(entry.id);panel.hidden=false;
 }catch{}
}
function fillDirectory(h){
 $('toc-title').textContent=h.title;$('directory-breadcrumb').textContent=h.title;$('directory-subtitle').textContent=h.subtitle;$('directory-count').textContent=h.entries.length+' מבואות לעיון';$('toc').setAttribute('aria-label','תוכן העניינים — '+h.title);$('toc').replaceChildren();
 const groups=new Map();for(const e of h.entries){if(!groups.has(e.group)){const section=el('section');section.className='topic-group';section.append(el('h2',e.group));groups.set(e.group,section);$('toc').append(section);}const link=el('a',e.title);link.href='#'+e.id;if(e.id===current)link.setAttribute('aria-current','page');link.onclick=event=>{event.preventDefault();navigate(e.id);};groups.get(e.group).append(link);}
 for(const section of groups.values()){const count=section.querySelectorAll('a').length;const small=el('small',count+' עניינים');section.querySelector('h2').append(small);}
}
function displaySubject(id){const h=D.handbooks.find(h=>h.id===id);if(!h){showHome();return;}H=h;current=null;$('article').replaceChildren();showView('directory');fillDirectory(h);$('subject-switch').value=h.id;document.querySelectorAll('[data-subject]').forEach(b=>{if(b.dataset.subject===h.id)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current');});}
function openSubject(id){resetSearch();displaySubject(id);pushRoute('#subject/'+id);focusView();}
for(const id of ['home-button','directory-home','entry-home'])$(id).onclick=()=>{resetSearch();showHome();pushRoute('');focusView();};
$('subject-switch').onchange=()=>{if($('subject-switch').value)openSubject($('subject-switch').value);else $('home-button').click();};
$('directory-toggle').onclick=$('back-subject').onclick=()=>openSubject(H.id);
$('search-toggle').onclick=()=>{const open=$('search-panel').hidden;$('search-panel').hidden=!open;$('search-toggle').setAttribute('aria-expanded',String(open));if(open)$('search').focus();};
$('home-search').onclick=()=>{$('search-toggle').click();if(!$('search-panel').hidden)$('scroll-content').scrollTop=0;};
$('read-all').onclick=()=>document.querySelectorAll('.chapter').forEach(x=>x.open=true);
function refControls(refs){const d=el('details');d.className='refs';d.append(el('summary','לעיון במקורות'));for(const r of refs){const src=D.sources[r.source];d.append(btn(src.citation+' · מקטעים '+r.segments.join(', '),()=>showSource(src.id,r.segments)));}return d;}
function render(id,blockId){
 H=D.handbooks.find(h=>h.entries.some(e=>e.id===id));if(!H){showHome();return;}
 const e=H.entries.find(x=>x.id===id);current=e.id;showView('entry');$('subject-switch').value=H.id;
 $('reading-meta').textContent=H.title+' · '+e.group+' · '+e.blocks.length+' סעיפים';
 try{localStorage.setItem('mevoot-last-entry',JSON.stringify({id:e.id}));}catch{}
 $('article').replaceChildren(el('h2',e.title));$('entry-label').textContent=e.title;$('back-subject').textContent=H.title;
 document.querySelectorAll('[data-subject]').forEach(b=>{if(b.dataset.subject===H.id)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current');});
for(const b of e.blocks){const d=el('details');d.className='chapter';d.id=e.id+'--'+b.id;d.open=e.blocks.indexOf(b)===0;d.append(el('summary',b.title));for(const p of b.paragraphs)d.append(el('p',p));if(b.items.length){const list=el('dl');list.className='fact-list';for(const i of b.items){list.append(el('dt',i.label),el('dd',i.text));}d.append(list);}const by=el('div',b.by);by.className='by';d.append(by);d.append(refControls(b.refs));if(b.links.length){const related=el('nav');related.className='related';related.setAttribute('aria-label','ענינים קשורים');for(const id of b.links){const next=allEntriesById.get(id);if(next)related.append(btn(next.title,()=>navigate(id)));}d.append(related);}$('article').append(d);}
const n=H.entries.indexOf(e),pager=el('nav');pager.className='pager';pager.setAttribute('aria-label','מעבר בין הענינים');if(n>0)pager.append(btn('הקודם: '+H.entries[n-1].title,()=>navigate(H.entries[n-1].id)));if(n<H.entries.length-1)pager.append(btn('הבא: '+H.entries[n+1].title,()=>navigate(H.entries[n+1].id)));$('article').append(pager);
fillDirectory(H);
if(blockId){const b=$(e.id+'--'+blockId);if(b){b.open=true;requestAnimationFrame(()=>b.scrollIntoView({block:'start'}));}}
}
function navigate(id,blockId){resetSearch();render(id,blockId);if(!current)return;pushRoute('#'+current+(blockId?'--'+blockId:''));if(!blockId)focusView();else $('reading').focus({preventScroll:true});}
function route(){resetSearch();const hash=decodeURIComponent(location.hash.slice(1));if(hash.startsWith('subject/'))displaySubject(hash.slice(8));else if(hash){const [id,block]=hash.split('--');render(id,block);}else showHome();}
window.addEventListener('hashchange',route);window.addEventListener('popstate',route);
$('expand').onclick=()=>document.querySelectorAll('.chapter').forEach(x=>x.open=true);
$('collapse').onclick=()=>document.querySelectorAll('.chapter').forEach(x=>x.open=false);
function blockText(b){return [b.title,...b.paragraphs,...b.items.flatMap(i=>[i.label,i.text])].join(' ');}
function excerpt(text,words){const sentence=text.split(/(?<=[.!?])\s+/).find(p=>norm(p).includes(words[0]))||text;return sentence.length>230?sentence.slice(0,230)+'…':sentence;}
function search(){const q=norm($('search').value),words=q.split(' ').filter(Boolean);$('results').replaceChildren();$('results').hidden=!q;if(!q){$('search-status').textContent='';return;}let count=0;const scope=$('search-scope').value;
if(scope!=='sources')for(const h of D.handbooks){for(const e of h.entries){for(const b of e.blocks){const text=blockText(b);if(words.every(w=>norm(h.title+' '+e.title+' '+text).includes(w))){const hit=btn(h.title+' · '+e.title+' · '+b.title,()=>navigate(e.id,b.id));hit.append(el('small',excerpt(text,words)));$('results').append(hit);count++;}}}}
if(scope!=='introductions')for(const src of Object.values(D.sources)){for(const seg of src.segments){if(words.every(w=>norm(seg.text).includes(w))){const hit=btn('מקור: '+src.citation+' · מקטע '+seg.number,()=>showSource(src.id,[seg.number]));hit.append(el('small',seg.text.slice(0,200)+'…'));$('results').append(hit);count++;}}}
$('search-status').textContent=count?count+' תוצאות '+(scope==='introductions'?'במבואות':scope==='sources'?'במקורות':'במבואות ובמקורות'):'לא נמצאו תוצאות. נסו כתיב אחר או מלים מעטות יותר.';}
$('search').oninput=search;$('search-scope').onchange=search;$('clear').onclick=()=>{$('search').value='';search();$('search').focus();};
function resetNative(){serial++;const old=nativeIterator;nativeIterator=null;if(old?.return)Promise.resolve(old.return()).catch(()=>{});$('native-results').replaceChildren();$('native-status').textContent='';}
function showSource(id,numbers){resetNative();activeSource=D.sources[id];activeSegments=numbers||activeSource.segments.map(x=>x.number);$('source-title').textContent=activeSource.citation;$('source-note').textContent=activeSource.note||'לשון המקור נשמרה מן הנוסח הדיגיטלי. סוגריים ותוספות שבנוסח לא הוסרו. המספור הוא לפי המקטעים השמורים.';$('source-edition').textContent=activeSource.author+' · '+activeSource.ref+' · '+activeSource.edition.map(x=>x.versionTitle+' / '+x.license+' / '+x.versionSource).join('; ');$('source-segments').replaceChildren();
for(const seg of activeSource.segments.filter(x=>activeSegments.includes(x.number))){const sec=el('section');sec.className='source-segment';sec.append(el('h3','מקטע '+seg.number),el('p',seg.text),btn('איתור קטע זה באוצריא',()=>native(seg.text)));$('source-segments').append(sec);}
$('whole-source').hidden=activeSegments.length===activeSource.segments.length;$('whole-source').onclick=()=>showSource(id);if(!$('source-dialog').open)$('source-dialog').showModal();$('source-dialog').scrollTop=0;}
$('close-source').onclick=()=>{$('source-dialog').close();resetNative();};$('source-dialog').addEventListener('close',resetNative);
$('all-sources').onclick=()=>{resetNative();$('source-title').textContent='כל המקורות השמורים';$('source-note').textContent='הטקסטים זמינים כאן במלוא ההיקף שנשמר: ההקדמות השמורות, המשניות והפירושים המצוטטים. אין זו ספריית פירוש המשנה כולו.';$('source-edition').textContent='';$('source-segments').replaceChildren(...Object.values(D.sources).map(s=>btn(s.citation,()=>showSource(s.id))));$('whole-source').hidden=true;$('source-dialog').showModal();};
function plainText(text){const template=document.createElement('template');template.innerHTML=String(text);return template.content.textContent||'';}
async function native(text){resetNative();const run=serial;if(!window.Otzaria?.call){$('native-status').textContent='פתיחה בספרייה זמינה בתוך אוצריא בלבד. לשון המקור זמינה כאן ללא רשת.';return;}
const query=norm(text).split(' ').filter(Boolean).slice(0,12).join(' ');$('native-status').textContent='מחפשים את לשון הקטע בספרייה המקומית…';
try{const hits=[],seen=new Set();const stream=window.Otzaria.call('search.query',{query,mode:'exact',limit:40});const iterator=stream[Symbol.asyncIterator]();nativeIterator=iterator;for await(const chunk of {[Symbol.asyncIterator]:()=>iterator}){if(run!==serial)break;for(const h of chunk.results||[]){if(!Number.isInteger(h.index)||h.index<0||!['ok',undefined].includes(h.textStatus)||!norm(plainText(h.text||'')).includes(query)||!(h.bookUid||Number.isInteger(h.id)||h.bookId))continue;const key=(h.bookUid||[h.source||'',h.type||'',h.id??h.bookId].join(':'))+':'+h.index;if(!seen.has(key)){seen.add(key);hits.push({...h,text:plainText(h.text)});}}}
if(run===serial)nativeIterator=null;if(run!==serial||!$('source-dialog').open)return;if(!hits.length){$('native-status').textContent='לא נמצאה התאמה ללשון הקטע. ייתכן שהספר אינו מותקן, שאינו מאונדקס או שנוסחו שונה. אפשר לקרוא את המקור השמור כאן.';return;}
$('native-status').textContent='נמצאו התאמות ללשון הקטע. בחרו לפי שם הספר ומראה המקום; התאמת הלשון לבדה אינה מאמתת את הזיהוי.';
for(const h of hits){const row=el('section');row.append(el('h3',h.book||h.bookId||'ספר בספרייה'),el('small',h.reference||''),el('p',h.text));const open=btn('פתיחת ההתאמה באוצריא',async()=>{open.disabled=true;try{const identity=h.bookUid?{bookUid:h.bookUid}:Number.isInteger(h.id)?{id:h.id,...(h.type?{type:h.type}:{}),...(h.source?{source:h.source}:{})}:{bookId:h.bookId,...(h.type?{type:h.type}:{})};const response=await window.Otzaria.call('reader.openBook',{...identity,index:h.index,searchQuery:query,navigateToPositionIfReused:true});if(run!==serial)return;const ok=response&&typeof response==='object'?response.success===true&&response.data===true:response===true;if(!ok)throw Error('not opened');$('native-status').textContent='הקטע נפתח באוצריא.';}catch{if(run===serial)$('native-status').textContent='לא ניתן לפתוח את הקטע. ייתכן שהספר אינו זמין או שהרשאת פתיחת ספרים חסרה. המקור השמור נשאר זמין כאן.';}finally{open.disabled=false;}});row.append(open);$('native-results').append(row);}
}catch{if(run===serial)$('native-status').textContent='החיפוש באוצריא לא הצליח. בדקו את הרשאות התוסף ואת זמינות החיפוש המקומי. המקור השמור זמין כאן.';}}

$('about').onclick=()=>{resetNative();$('source-title').textContent='על ההסברים והמקורות';$('source-note').textContent=H?H.method:'המבואות ערוכים על פי המקורות המצוינים בכל סעיף. לשון המקור מובאת בנפרד מן הביאור. עיקר היסוד בפירוש המשנה ובהקדמות הרמב״ם, ובצדם מקורות נוספים המצוינים במקומם.';$('source-edition').textContent='עריכה: DanTheMan · גרסה '+D.version;$('source-segments').replaceChildren(el('h3','היקף ההסברים'),el('p',H?H.limits:'נכללו עניינים מרכזיים בשישה תחומים. זהו מפתח מבואי, ואין בו כיסוי של כל ענייני הש״ס.'),el('h3','דרך העריכה'),el('p',D.editorialPolicy.principle),el('p',D.editorialPolicy.style));$('whole-source').hidden=true;$('source-dialog').showModal();};
route();
})();
