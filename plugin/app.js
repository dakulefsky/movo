(()=>{'use strict';
const D=window.MEVOOT,$=id=>document.getElementById(id);
let H=D.handbooks[0];
const el=(tag,text)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;return n;};
const btn=(text,fn)=>{const b=el('button',text);b.type='button';b.onclick=fn;return b;};
const norm=s=>String(s).normalize('NFKD').replace(/[\u0591-\u05bd\u05bf-\u05c7]/g,'').replace(/[״׳'"־\-–—.,:;!?()[\]]/g,' ').replace(/\s+/g,' ').trim().toLowerCase();
let activeSource=null,activeSegments=[],serial=0,nativeIterator=null,font=21,current='olah';
let hasFontPreference=false;
try{const saved=Number(localStorage.getItem('mevoot-v1-font'));if(saved){font=saved;hasFontPreference=true;}}catch{}
function setFont(n){font=Math.min(30,Math.max(17,n));document.documentElement.style.setProperty('--reader-size',font+'px');try{localStorage.setItem('mevoot-v1-font',font);}catch{}}
setFont(font);
$('smaller').onclick=()=>{hasFontPreference=true;setFont(font-1)};$('larger').onclick=()=>{hasFontPreference=true;setFont(font+1)};
function applyTheme(theme){
 if(!theme?.colorScheme)return;
 const root=document.documentElement,cs=theme.colorScheme;
 for(const key of ['primary','onPrimary','surface','onSurface','onSurfaceVariant','surfaceContainerLow','surfaceContainerHigh','surfaceContainerHighest','secondaryContainer','onSecondaryContainer','outline','outlineVariant','scrim']){
  if(typeof cs[key]==='string')root.style.setProperty('--color-'+key.replace(/[A-Z]/g,x=>'-'+x.toLowerCase()),cs[key]);
 }
 root.style.colorScheme=theme.mode==='dark'?'dark':'light';
 const t=theme.typography||{};
 if(t.fontFamily)root.style.setProperty('--font-main',JSON.stringify(t.fontFamily)+',serif');
 if(t.uiFontFamily)root.style.setProperty('--font-ui',JSON.stringify(t.uiFontFamily)+',system-ui,sans-serif');
 if(!hasFontPreference&&Number.isFinite(t.fontSize))setFont(t.fontSize);
 if(Number.isFinite(t.lineHeight)&&t.lineHeight>0)root.style.setProperty('--reader-line-height',String(t.lineHeight));
}
window.addEventListener('plugin.boot',event=>applyTheme(event.detail?.theme));
if(window.Otzaria?.on)window.Otzaria.on('theme.changed',applyTheme);

for(const s of D.subjects){const b=btn(s.title+(s.status==='planned'?' · בהכנה':''),()=>{const h=D.handbooks.find(h=>h.id===s.id);if(h)navigate(h.entries[0].id);});b.dataset.subject=s.id;b.disabled=s.status==='planned';$('subjects').append(b);}
function refControls(refs){const d=el('details');d.className='refs';d.append(el('summary','מקורות — לשון המחברים'));for(const r of refs){const src=D.sources[r.source];d.append(btn(src.citation+' · מקטעים '+r.segments.join(', '),()=>showSource(src.id,r.segments)));}return d;}
function render(id,blockId){H=D.handbooks.find(h=>h.entries.some(e=>e.id===id))||D.handbooks[0];const e=H.entries.find(x=>x.id===id)||H.entries[0];current=e.id;const title=el('h2',e.title);$('article').replaceChildren(el('div',H.title+' · '+e.group),title);$('entry-label').textContent=e.title;$('toc-title').textContent='עניני '+H.title;$('toc').setAttribute('aria-label','עניני '+H.title);document.querySelectorAll('[data-subject]').forEach(b=>{if(b.dataset.subject===H.id)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current');});
const note=el('p','הסבר ערוך על פי המקורות; לשון המחברים נפתחת בכל סעיף.');note.className='entry-note';$('article').append(note);
for(const b of e.blocks){const d=el('details');d.className='chapter';d.id=e.id+'--'+b.id;d.open=true;d.append(el('summary',b.title));for(const p of b.paragraphs)d.append(el('p',p));if(b.items.length){const list=el('dl');list.className='fact-list';for(const i of b.items){list.append(el('dt',i.label),el('dd',i.text));}d.append(list);}if(b.by!=='ביאור ערוך על פי הרמב״ם'){const by=el('div',b.by);by.className='by';d.append(by);}d.append(refControls(b.refs));if(b.links.length){const related=el('nav');related.className='related';related.setAttribute('aria-label','ענינים קשורים');for(const id of b.links){const next=H.entries.find(x=>x.id===id);related.append(btn(next.title,()=>navigate(id)));}d.append(related);}$('article').append(d);}
const n=H.entries.indexOf(e),pager=el('nav');pager.className='pager';pager.setAttribute('aria-label','מעבר בין הענינים');if(n>0)pager.append(btn('הקודם: '+H.entries[n-1].title,()=>navigate(H.entries[n-1].id)));if(n<H.entries.length-1)pager.append(btn('הבא: '+H.entries[n+1].title,()=>navigate(H.entries[n+1].id)));$('article').append(pager);
$('toc').replaceChildren();let group='';for(const other of H.entries){if(other.group!==group){group=other.group;const h=el('h3',group);$('toc').append(h);}const a=el('a',other.title);a.href='#'+other.id;if(other.id===e.id)a.setAttribute('aria-current','page');a.onclick=event=>{event.preventDefault();navigate(other.id);};$('toc').append(a);}
if(blockId){const b=$(e.id+'--'+blockId);if(b){b.open=true;requestAnimationFrame(()=>b.scrollIntoView({block:'start'}));}}
}
function navigate(id,blockId){$('search').value='';search();render(id,blockId);const hash=current+(blockId?'--'+blockId:'');if(location.hash.slice(1)!==hash)history.pushState(null,'','#'+hash);if(!blockId)$('reading').scrollIntoView({block:'start'});$('reading').focus({preventScroll:true});}
function route(){const [id,block]=location.hash.slice(1).split('--');render(id||'olah',block);}
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

$('about').onclick=()=>{resetNative();$('source-title').textContent='על ההסברים והמקורות';$('source-note').textContent=H.method;$('source-edition').textContent='עריכה: DanTheMan · גרסה '+D.version;$('source-segments').replaceChildren(el('h3','היקף ההסברים'),el('p',H.limits),el('h3','דרך העריכה'),el('p',D.editorialPolicy.principle),el('p',D.editorialPolicy.style));$('whole-source').hidden=true;$('source-dialog').showModal();};
route();
})();
