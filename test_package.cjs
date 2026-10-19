const assert=require('node:assert/strict'),path=require('node:path'),fs=require('node:fs'),{execFileSync}=require('node:child_process');
let pw;try{pw=require('playwright')}catch{pw=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/playwright')}
(async()=>{
const root=__dirname,unpacked=path.join(root,'test-unpacked');fs.rmSync(unpacked,{recursive:true,force:true});fs.mkdirSync(unpacked);
execFileSync('python',['-c',`import zipfile;zipfile.ZipFile(${JSON.stringify(path.join(root,'dist/Mevoot-Shas-0.13.3.otzplugin'))}).extractall(${JSON.stringify(unpacked)})`]);
const manifest=JSON.parse(fs.readFileSync(path.join(unpacked,'manifest.json')));assert.equal(manifest.author,'DanTheMan');assert.equal(manifest.version,'0.13.3');assert.equal(manifest.network.enabled,false);
const browser=await pw.chromium.launch({headless:true,...(process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE?{executablePath:process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE}:{}),args:['--no-sandbox']}),page=await browser.newPage();const errors=[],remote=[];
try{
page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(/^https?:/.test(r.url()))remote.push(r.url())});
await page.goto('file://'+path.join(unpacked,'index.html'));
const chooseSubject=async id=>{await page.selectOption('#subject-switch',id);assert.equal(await page.locator('#directory-view').isVisible(),true);assert.equal(await page.locator('#entry-view').isVisible(),false);};
const chooseEntry=async (id,expand=true)=>{if(await page.locator('#entry-view').isVisible())await page.click('#directory-toggle');await page.click('#toc a[href="#'+id+'"]');if(expand)await readingOption('expand');};
const expandSection=async id=>{const section=page.locator('#'+id);if(await section.getAttribute('open')===null)await section.locator(':scope > summary').click();};
const readingOption=async id=>{if(await page.locator('.reading-options').getAttribute('open')===null)await page.locator('.reading-options>summary').click();await page.click('#'+id);await page.locator('.reading-options>summary').click();};
const searchFor=async value=>{if(await page.locator('#search-panel').isHidden())await page.click('#search-toggle');await page.fill('#search',value);};
assert.equal(await page.locator('#home-view').isVisible(),true);assert.equal(await page.locator('#article h2').count(),0);assert.equal(await page.locator('#subjects button').count(),6);assert.equal(await page.locator('aside').count(),0);
assert.equal(await page.locator('#continue-panel').isVisible(),false);assert.match(await page.locator('#subjects .card-count').first().innerText(),/מבואות/);await page.click('#home-search');assert.equal(await page.locator('#search-panel').isVisible(),true);await page.click('#search-toggle');assert.equal(await page.locator('#search-panel').isVisible(),false);
await page.evaluate(async()=>{await document.fonts.load('400 24px MevootText');await document.fonts.load('500 16px MevootUI');await document.fonts.ready;});assert.equal(await page.evaluate(()=>document.fonts.check('400 24px MevootText')),true);assert.equal(await page.evaluate(()=>document.fonts.check('500 16px MevootUI')),true);
await chooseSubject('kodashim');assert.equal(await page.locator('#article h2').count(),0);await chooseEntry('olah',false);assert.equal(await page.locator('.chapter[open]').count(),1);
assert.equal(await page.locator('html').getAttribute('dir'),'rtl');assert.equal(await page.locator('#article h2').innerText(),'עולה');assert.equal(await page.locator('#toc a').count(),28);assert.equal(await page.locator('#subjects button:disabled').count(),0);assert.equal(await page.locator('.chapter').count(),7);
await page.click('#read-all');assert.equal(await page.locator('.chapter[open]').count(),7);
await page.click('#home-button');assert.equal(await page.locator('#home-view').isVisible(),true);assert.equal(await page.locator('#continue-panel').isVisible(),true);assert.match(await page.locator('#continue-button').innerText(),/עולה/);await page.click('#continue-button');assert.equal(await page.locator('#article h2').innerText(),'עולה');
await readingOption('collapse');assert.equal(await page.locator('.chapter[open]').count(),0);await readingOption('expand');assert.equal(await page.locator('.chapter[open]').count(),7);
await chooseEntry('asham');assert.equal(await page.locator('#article h2').innerText(),'אשם');assert.equal(await page.locator('.fact-list dt').count(),6);assert.match(await page.locator('#asham--types').innerText(),/אשם נזיר/);assert.equal(await page.locator('#toc a[aria-current]').innerText(),'אשם');
await page.reload();assert.equal(await page.locator('#article h2').innerText(),'אשם');await page.locator('.pager button').first().click();assert.equal(await page.locator('#article h2').innerText(),'חטאות הפנימיות');await page.goBack();assert.equal(await page.locator('#article h2').innerText(),'אשם');
await searchFor('עוֹלַת הָעוֹף');assert.ok((await page.locator('#results button').count())>0);await page.locator('#results button').filter({hasText:'עולה · עולת העוף'}).first().click();assert.equal(await page.locator('#article h2').innerText(),'עולה');assert.match(page.url(),/olah--bird/);assert.equal(await page.locator('#olah--bird').getAttribute('open'),'');
await searchFor('אשם מעילות');assert.ok((await page.locator('#results button').count())>0);await page.locator('#results button').filter({hasText:'אשם · ששת מיני האשם'}).first().click();assert.equal(await page.locator('#article h2').innerText(),'אשם');
await searchFor('abcdefghzz');assert.match(await page.locator('#search-status').innerText(),/לא נמצאו/);await page.click('#clear');assert.equal(await page.locator('#results').isVisible(),false);
await expandSection('asham--service');await page.locator('#asham--service .refs summary').click();await expandSection('asham--service');await page.locator('#asham--service .refs button').first().click();assert.equal(await page.locator('#source-dialog').isVisible(),true);assert.match(await page.locator('#source-title').innerText(),/זבחים/);assert.ok((await page.locator('.source-segment p').first().innerText()).length>100);
await page.locator('.source-segment button').first().click();assert.match(await page.locator('#native-status').innerText(),/בתוך אוצריא/);
await page.evaluate(()=>{window.__calls=[];window.Otzaria={call(method,payload){window.__calls.push({method,payload});if(method==='search.query')return(async function*(){yield{results:[]}})();return Promise.resolve(false)}}});await page.locator('.source-segment button').first().click();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('לא נמצאה'));assert.equal(await page.locator('#native-results button').count(),0);
await page.evaluate(()=>{window.Otzaria.call=(method,payload)=>{window.__calls.push({method,payload});if(method==='search.query')return(async function*(){yield{results:[{id:81,type:'text',book:'פירוש המשנה לרמב״ם — זבחים',index:314,reference:'פרק ה משנה ה',text:payload.query,textStatus:'ok'},{id:82,index:7,text:payload.query,textStatus:'stale'},{id:83,index:8,text:'unrelated',textStatus:'ok'}]}})();return Promise.resolve(true)}});await page.locator('.source-segment button').first().click();await page.locator('#native-results button').waitFor();assert.equal(await page.locator('#native-results button').count(),1);await page.locator('#native-results button').click();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('נפתח'));const call=await page.evaluate(()=>window.__calls.at(-1));assert.equal(call.method,'reader.openBook');assert.equal(call.payload.id,81);assert.equal(call.payload.index,314);
await page.evaluate(()=>{const orig=window.Otzaria.call;window.Otzaria.call=(m,p)=>m==='reader.openBook'?Promise.resolve(false):orig(m,p)});await page.locator('#native-results button').click();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('לא ניתן לפתוח'));
await page.evaluate(()=>{window.Otzaria.call=()=>{throw Error('permission denied')}});await page.locator('.source-segment button').first().click();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('לא הצליח'));
await page.click('#close-source');await page.click('#all-sources');assert.equal(await page.locator('#source-segments>button').count(),215);await page.locator('#source-segments>button').first().click();assert.equal(await page.locator('.source-segment').count(),55);assert.match(await page.locator('#source-note').innerText(),/המעתיק/);await page.click('#close-source');
await chooseEntry('todah');await expandSection('todah--bread');await page.locator('#todah--bread .refs summary').click();await expandSection('todah--bread');await page.locator('#todah--bread .refs button').click();assert.match(await page.locator('#source-title').innerText(),/מנחות/);assert.match(await page.locator('#source-segments').innerText(),/מנין החלות/);await page.click('#close-source');
// Cross-area navigation, search and exact source locations.
await chooseSubject('tahorot');assert.equal(await page.locator('#toc a').count(),15);await chooseEntry('t-met');assert.equal(await page.locator('#article h2').innerText(),'טומאת מת');
await chooseEntry('t-kelim');await expandSection('t-kelim--cheres');await page.locator('#t-kelim--cheres .refs summary').click();await expandSection('t-kelim--cheres');await page.locator('#t-kelim--cheres .refs button').first().click();assert.match(await page.locator('#source-title').innerText(),/כלים/);assert.match(await page.locator('#source-segments').innerText(),/באויר/);await page.click('#close-source');
await chooseSubject('ishut');assert.equal(await page.locator('#toc a').count(),11);await chooseEntry('i-kiddushin');assert.equal(await page.locator('#article h2').innerText(),'קידושין');await chooseEntry('i-chalitzah');await expandSection('i-chalitzah--seder');await page.locator('#i-chalitzah--seder .refs summary').click();await expandSection('i-chalitzah--seder');await page.locator('#i-chalitzah--seder .refs button').first().click();assert.match(await page.locator('#source-title').innerText(),/יבמות/);assert.match(await page.locator('#source-segments').innerText(),/רֹק הַנִּרְאֶה/);await page.click('#close-source');
await chooseSubject('zeraim');assert.equal(await page.locator('#toc a').count(),17);await chooseEntry('z-maaser-sheni');await expandSection('z-maaser-sheni--fifth');await page.locator('#z-maaser-sheni--fifth .refs summary').click();await expandSection('z-maaser-sheni--fifth');await page.locator('#z-maaser-sheni--fifth .refs button').click();assert.match(await page.locator('#source-title').innerText(),/מעשר שני/);assert.match(await page.locator('#source-segments').innerText(),/רביע עיקר הממון/);await page.click('#close-source');
await searchFor('הכשר אוכלין');await page.locator('#results button').filter({hasText:'טהרות · הכשר אוכלין ומשקין · הכנת האוכל לקבלת טומאה'}).first().click();assert.equal(await page.locator('[data-subject="tahorot"]').getAttribute('aria-current'),'page');assert.match(page.url(),/t-hechsher--meaning/);await page.reload();assert.equal(await page.locator('#article h2').innerText(),'הכשר אוכלין ומשקין');
await chooseSubject('mammon');assert.equal(await page.locator('#toc a').count(),19);await chooseEntry('d-shomrim');await expandSection('d-shomrim--ones');await page.locator('#d-shomrim--ones .refs summary').click();await expandSection('d-shomrim--ones');await page.locator('#d-shomrim--ones .refs button').last().click();assert.match(await page.locator('#source-title').innerText(),/בבא מציעא/);assert.match(await page.locator('#source-segments').innerText(),/בשעת שאלה/);await page.click('#close-source');
await searchFor('כסף, שטר וחזקה');await page.locator('#results button').filter({hasText:'קנין קרקע · כסף, שטר וחזקה'}).first().click();assert.equal(await page.locator('[data-subject="mammon"]').getAttribute('aria-current'),'page');assert.match(page.url(),/d-karka--ways/);
await chooseSubject('issur');assert.equal(await page.locator('#toc a').count(),8);await chooseEntry('a-basar-chalav');await expandSection('a-basar-chalav--meaning');await page.locator('#a-basar-chalav--meaning .refs summary').click();await expandSection('a-basar-chalav--meaning');await page.locator('#a-basar-chalav--meaning .refs button').first().click();assert.match(await page.locator('#source-title').innerText(),/חולין/);assert.match(await page.locator('#source-segments').innerText(),/והלכה כר/);await page.click('#close-source');
await searchFor('פרוזבול');assert.ok(await page.locator('#results button').count());assert.equal(await page.locator('#results button').filter({hasText:'מקור:'}).count(),0);await page.selectOption('#search-scope','sources');assert.ok(await page.locator('#results button').filter({hasText:'מקור:'}).count());await page.selectOption('#search-scope','introductions');await page.click('#clear');
await chooseSubject('mammon');await chooseEntry('d-geneivah');await expandSection('d-geneivah--meaning');await page.locator('#d-geneivah--meaning .refs summary').click();await expandSection('d-geneivah--meaning');await page.locator('#d-geneivah--meaning .refs button').click();assert.match(await page.locator('#source-title').innerText(),/מאירי.*בבא קמא/);assert.match(await page.locator('#source-segments').innerText(),/ואפילו ראוהו/);await page.click('#close-source');await expandSection('d-geneivah--distinction');await page.locator('#d-geneivah--distinction .related button').click();assert.equal(await page.locator('#article h2').innerText(),'השבת גזלה ושינוי');
await searchFor('יוצאי ירכו');await page.locator('#results button').filter({hasText:'סדר נחלות · קדימה ויוצאי ירך'}).click();assert.match(page.url(),/d-yerushah--meaning/);
await chooseSubject('mammon');await chooseEntry('d-chovel');await expandSection('d-chovel--distinction');await page.locator('#d-chovel--distinction .refs summary').click();await expandSection('d-chovel--distinction');await page.locator('#d-chovel--distinction .refs button').first().click();assert.match(await page.locator('#source-segments').innerText(),/עבר.*דברי הרופא|יעבור.*דברי הרופא/);assert.match(await page.locator('#source-note').innerText(),/לא הוחלף/);await page.click('#close-source');
await chooseEntry('d-edut');await expandSection('d-edut--distinction');await page.locator('#d-edut--distinction .refs summary').click();await expandSection('d-edut--distinction');await page.locator('#d-edut--distinction .refs button').click();assert.match(await page.locator('#source-segments').innerText(),/דרך הודאה ומסירת עדות/);await page.click('#close-source');
await chooseSubject('zeraim');await chooseEntry('z-biur');await expandSection('z-biur--distinction');await page.locator('#z-biur--distinction .refs summary').click();await expandSection('z-biur--distinction');await page.locator('#z-biur--distinction .refs button').last().click();assert.match(await page.locator('#source-title').innerText(),/רמב.*ויקרא/);assert.match(await page.locator('#source-segments').innerText(),/וּלְהַפְקִירָם/);await page.click('#close-source');
await chooseSubject('tahorot');await chooseEntry('t-ohel');await expandSection('t-ohel--distinction');await page.locator('#t-ohel--distinction .refs summary').click();await expandSection('t-ohel--distinction');await page.locator('#t-ohel--distinction .refs button').first().click();assert.match(await page.locator('#source-segments').innerText(),/חור שחררוהו מים/);await page.click('#close-source');await chooseEntry('t-niddah');await expandSection('t-niddah--distinction');await page.locator('#t-niddah--distinction .refs summary').click();await expandSection('t-niddah--distinction');await page.locator('#t-niddah--distinction .refs button').click();assert.match(await page.locator('#source-note').innerText(),/הסוגריים/);await page.click('#close-source');
const corpus=await page.evaluate(()=>window.MEVOOT);assert.ok(!corpus.handbooks.some(h=>h.id==='berakhot'));assert.ok(!corpus.handbooks.flatMap(h=>h.entries).some(e=>e.id.startsWith('b-')));assert.ok(!Object.keys(corpus.sources).some(id=>id.startsWith('v-Berakhot-')));assert.equal(corpus.handbooks.length,6);assert.ok(!corpus.subjects.some(s=>s.id==='moed'));assert.ok(!corpus.handbooks.some(h=>h.id==='moed'));for(const id of ['s-melachot','s-hotzaah','s-eruv','s-techum','s-shvut','s-muktzeh'])assert.ok(!corpus.handbooks.flatMap(h=>h.entries).some(e=>e.id===id));assert.equal(corpus.handbooks.flatMap(h=>h.entries).length,98);assert.equal(corpus.handbooks.flatMap(h=>h.entries).reduce((n,e)=>n+e.blocks.length,0),317);
for(const h of corpus.handbooks){await chooseSubject(''+h.id+'');for(const e of h.entries){await chooseEntry(''+e.id+'');assert.equal(await page.locator('#article h2').innerText(),e.title);assert.equal(await page.locator('.chapter').count(),e.blocks.length);assert.equal(await page.locator('.chapter>.refs').count(),e.blocks.length);}}
// Cross-handbook related links are supported, not just cross-handbook search results.
await chooseSubject('ishut');await chooseEntry('i-kiddushin');
await expandSection('i-kiddushin--way-of-act');
assert.equal(await page.locator('#i-kiddushin--way-of-act .related button').count(),1);
await page.locator('#i-kiddushin--way-of-act .related button').click();
const land=corpus.handbooks.find(h=>h.id==='mammon').entries.find(e=>e.id==='d-karka');
assert.equal(await page.locator('#article h2').innerText(),land.title);
assert.equal(await page.locator('#subject-switch').inputValue(),'mammon');
assert.match(page.url(),/#d-karka$/);
// Invalid future links must never blank an otherwise valid reading page.
await page.evaluate(()=>window.MEVOOT.handbooks.find(h=>h.id==='ishut').entries.find(e=>e.id==='i-kiddushin').blocks.find(b=>b.id==='way-of-act').links.push('invalid-target-from-audit'));
await chooseSubject('ishut');await chooseEntry('i-kiddushin');
assert.equal(await page.locator('#article h2').innerText(),'קידושין');
assert.equal(await page.locator('#i-kiddushin--way-of-act .related button').count(),1);
await page.click('#home-button');assert.equal(await page.locator('#home-view').isVisible(),true);await page.reload();assert.equal(await page.locator('#home-view').isVisible(),true);await chooseSubject('kodashim');await page.reload();assert.equal(await page.locator('#directory-view').isVisible(),true);
await chooseEntry('av-zerikah');assert.equal(await page.locator('#article h2').innerText(),'זריקה ומתנות הדם');assert.equal(await page.locator('#av-zerikah--outer dt').count(),3);await expandSection('av-zerikah--meakev');await page.locator('#av-zerikah--meakev .refs summary').click();await expandSection('av-zerikah--meakev');await page.locator('#av-zerikah--meakev .refs button').first().click();assert.match(await page.locator('#source-title').innerText(),/זבחים/);assert.match(await page.locator('#source-segments').innerText(),/מַתָּנָה אַחַת/);await page.click('#close-source');
await chooseEntry('av-tenufah');await expandSection('av-tenufah--when');await page.locator('#av-tenufah--when .refs summary').click();await expandSection('av-tenufah--when');await page.locator('#av-tenufah--when .refs button').first().click();assert.match(await page.locator('#source-title').innerText(),/מנחות/);assert.match(await page.locator('#source-segments').innerText(),/תְּנוּפָה חַיִּים/);await page.click('#close-source');
await chooseEntry('olah');await expandSection('olah--service');await page.locator('#olah--service .related button').filter({hasText:'זריקה ומתנות הדם'}).click();assert.equal(await page.locator('#article h2').innerText(),'זריקה ומתנות הדם');await expandSection('av-zerikah--shirayim');await page.locator('#av-zerikah--shirayim .related button').filter({hasText:'חטאת'}).click();assert.equal(await page.locator('#article h2').innerText(),'חטאת');await chooseEntry('olah');
await page.click('#about');assert.match(await page.locator('#source-note').innerText(),/אינם ציטוט/);assert.match(await page.locator('#source-segments').innerText(),/זמני ההקטרה/);await page.click('#close-source');
for(const width of [390,1280]){await page.setViewportSize({width,height:900});for(const id of ['asham','chattat','minchah']){await chooseEntry(''+id+'');assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false)}}
await page.click('#larger');await page.reload();assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--reader-size')),'25px');
const d=await page.evaluate(()=>window.MEVOOT);assert.equal(d.editorialPolicy.format,'subject-handbook');assert.equal(d.handbooks.flatMap(h=>h.entries).reduce((n,e)=>n+e.blocks.length,0),317);for(const e of d.handbooks.flatMap(h=>h.entries)){for(const b of e.blocks){assert.ok(b.refs.length);for(const r of b.refs){assert.ok(d.sources[r.source]);assert.ok(r.segments.every(n=>n>=1&&n<=d.sources[r.source].segments.length))}}}
const approvedSubjects=d.subjects.map(x=>x.id);assert.deepEqual(approvedSubjects,['kodashim','tahorot','ishut','zeraim','mammon','issur']);
const entry=(entryId,blockId)=>d.handbooks.flatMap(h=>h.entries).find(e=>e.id===entryId)?.blocks.find(b=>b.id===blockId);
assert.match(entry('olah','purpose').paragraphs.join(' '),/בקרבן עולה הבשר מוקטר כולו/);
assert.match(entry('z-peah','meaning').paragraphs.join(' '),/מתנות העניים/);
assert.match(entry('t-met','source').paragraphs.join(' '),/חלקים ממנו/);
assert.match(entry('i-kiddushin','meaning').paragraphs.join(' '),/אין הקידושין חלים אלא מרצונה/);
assert.match(entry('d-nezikin','avot').paragraphs.join(' '),/ארבעה אבות נזיקין/);
assert.match(entry('a-neder','meaning').paragraphs.join(' '),/בנדרי איסור/);
assert.match(entry('av-shechitah','person').paragraphs.join(' '),/בסכין ארוכה/,'Source-audit long knife must remain visible');
assert.match(entry('av-shechitah','person').paragraphs.join(' '),/שלא ישחוט לכתחילה/,'Do not claim an unrestricted lechatchila exception');
assert.match(entry('t-met','scope').paragraphs.join(' '),/אתם קרוין אדם/);
assert.doesNotMatch(entry('t-met','scope').paragraphs.join(' '),/אין זו דעה המוסכמת/);
assert.match(entry('olah','bird').paragraphs.join(' '),/סופגים אותו במלח/);
assert.match(entry('chattat','shem').paragraphs.join(' '),/שנעשתה סתם כשרה ועולה לבעלים/);
for(const [entryId,blockId,sourceId] of [['av-shechitah','person','z3-1'],['t-met','scope','t-intro'],['olah','bird','z6-5'],['chattat','shem','z1-1']]) {
 assert.ok(entry(entryId,blockId).refs.some(r=>r.source===sourceId),'Gemini-audit correction lost original reference: '+entryId+'/'+blockId);
}

// Source-led editorial regression: cited source identity and a short actual-source
// quotation must still support the named, still-visible explanatory sentence.
// This establishes traceability only, not scholarly/halachic correctness.
const evidence=JSON.parse(fs.readFileSync(path.join(root,'SOURCE-REVIEW-0.12.3.json'),'utf8'));
const normalizeSource=s=>String(s).normalize('NFKD').replace(/<[^>]*>/g,' ').replace(/\p{M}/gu,'').replace(/[^\p{L}\p{N}]+/gu,' ').replace(/\s+/g,' ').trim();
const checkedEntries=new Set();
for(const check of evidence.checks){
 const [entryId,blockId]=check.key.split('/'),block=entry(entryId,blockId);
 assert.ok(block,'Source review block missing: '+check.key);
 assert.ok(block.refs.some(r=>r.source===check.sourceId&&r.segments.includes(check.segment)),'Primary-source citation missing: '+check.key+' '+check.sourceId);
 const src=d.sources[check.sourceId];assert.ok(src,'Bundled source missing: '+check.sourceId);
 assert.equal(src.filename,check.filename,'Source filename changed: '+check.sourceId);
 const passage=src.segments[check.segment-1]?.text;
 assert.ok(passage&&normalizeSource(passage).includes(normalizeSource(check.sourceTextAnchor)),'Source quotation drift: '+check.key+' '+check.sourceId);
 assert.ok(normalizeSource(block.paragraphs.join(' ')).includes(normalizeSource(check.expectedInExplanation)),'Reviewed wording drift: '+check.key);
 checkedEntries.add(check.key);
}
assert.equal(evidence.checks.length,19);assert.equal(checkedEntries.size,16);
// 0.13.1 coverage regression: distinct major sugyas and new explanatory depth.
const expansion=JSON.parse(fs.readFileSync(path.join(root,'coverage_013_entries.json'),'utf8'));
const detailA=JSON.parse(fs.readFileSync(path.join(root,'coverage_013_details_a.json'),'utf8'));
const detailB=JSON.parse(fs.readFileSync(path.join(root,'coverage_013_details_b.json'),'utf8'));
assert.equal(expansion.entries.length,9);
assert.equal(detailA.additions.length+detailB.additions.length,39);
for(const e of expansion.entries){
 const found=d.handbooks.find(h=>h.id===e.handbook)?.entries.find(x=>x.id===e.id);
 assert.ok(found,'New central-sugya entry not present: '+e.id);
 assert.equal(found.blocks.length,3);
 for(const b of found.blocks){assert.ok(b.paragraphs.join(' ').split(/\s+/).length>=32,'New introduction too thin: '+e.id+'/'+b.id);}
}
for(const item of [...detailA.additions,...detailB.additions]){assert.ok(entry(item.entry,item.block.id),'New explanatory block not present: '+item.entry+'/'+item.block.id);}
const extendedCounts=Object.fromEntries(d.handbooks.map(h=>[h.id,h.entries.length]));
assert.deepEqual(extendedCounts,{kodashim:28,tahorot:15,ishut:11,zeraim:17,mammon:19,issur:8});
// Gemini audit follow-up: these wording and source anchors were independently reviewed.
const geminiReview=JSON.parse(fs.readFileSync(path.join(root,'GEMINI-AUDIT-FOLLOWUP-0.13.0.json'),'utf8'));
assert.equal(geminiReview.checkRows.length,7);
for(const check of geminiReview.checkRows){
 const [entryId,blockId]=check.block.split('/'),block=entry(entryId,blockId);
 assert.ok(block,'Gemini-reviewed block missing: '+check.block);
 assert.ok(block.refs.some(ref=>ref.source===check.source&&ref.segments.includes(check.segment)),
   'Gemini-reviewed block lost exact citation: '+check.block+' → '+check.source);
 assert.ok(normalizeSource(d.sources[check.source].segments[check.segment-1].text).includes(normalizeSource(check.sourceAnchor)),
   'Gemini-reviewed source quotation mismatch: '+check.block+' → '+check.source);
 assert.ok(normalizeSource(block.paragraphs.join(' ')).includes(normalizeSource(check.explanationAnchor)),
   'Gemini-reviewed explanatory correction missing: '+check.block);
}
// Independent audit #2: enforce the actual cited segment and editorial correction.
// These checks ensure evidence traceability, not formal halachic validation.
const audit2=JSON.parse(fs.readFileSync(path.join(root,'SOURCE-REVIEW-0.13.1.json'),'utf8'));
assert.equal(audit2.edition,'0.13.1');
assert.equal(audit2.checks.length,13);
const audit2Blocks=new Set();
for(const record of audit2.checks){
 const [entryId,blockId]=record.blockId.split('/');
 const block=entry(entryId,blockId);
 assert.ok(block,'Second audit lost block '+record.blockId);
 assert.ok(block.refs.some(r=>r.source===record.sourceId && r.segments.includes(record.segment)),
   'Second audit citation detached '+record.blockId+' '+record.sourceId);
 const src=d.sources[record.sourceId];
 assert.ok(src,'Second audit source absent: '+record.sourceId);
 assert.equal(src.filename,record.filename,'Second audit source identity drift '+record.blockId);
 assert.ok(normalizeSource(src.segments[record.segment-1]?.text||'').includes(normalizeSource(record.sourceAnchor)),
   'Second audit source quotation drift '+record.blockId+' '+record.sourceId);
 assert.ok(normalizeSource(block.paragraphs.join(' ')).includes(normalizeSource(record.explanationAnchor)),
   'Second audit explanation omission returned '+record.blockId);
 audit2Blocks.add(record.blockId);
}
assert.equal(audit2Blocks.size,8);
assert.match(entry('z-challah','dough').paragraphs[0],/אין ההפרשה הראשונה עושה את הקמח לחלה גמורה/);
assert.match(entry('d-shomrim','four').paragraphs[0],/בכפוף לפטוריו/);
// Source-audited 0.13.2 corrections with a separately bundled Mishneh Torah text.
const audit3=JSON.parse(fs.readFileSync(path.join(root,'SOURCE-REVIEW-0.13.2.json'),'utf8'));
assert.equal(audit3.version,'0.13.2');assert.equal(audit3.checks.length,9);
for(const record of audit3.checks){
 const [entryId,blockId]=record.blockId.split('/');const block=entry(entryId,blockId);
 assert.ok(block,'0.13.2 block missing '+record.blockId);
 assert.ok(block.refs.some(ref=>ref.source===record.sourceId&&ref.segments.includes(record.segment)),
   '0.13.2 source missing from block '+record.blockId+'/'+record.sourceId);
 const src=d.sources[record.sourceId];assert.ok(src,'Source ID not bundled: '+record.sourceId);
 assert.equal(src.filename,record.filename);
 assert.ok(normalizeSource(src.segments[record.segment-1]?.text||'').includes(normalizeSource(record.sourceQuote)),
   '0.13.2 source anchor mismatched: '+record.blockId+'/'+record.sourceId);
 assert.ok(normalizeSource(block.paragraphs.join(' ')).includes(normalizeSource(record.explanationQuote)),
   '0.13.2 reviewed wording missing: '+record.blockId);
}
assert.ok(d.sources['mt-sanhedrin-authority']);
const newRelated=entry('i-kiddushin','way-of-act').links;
assert.ok(newRelated.includes('d-karka'));
assert.deepEqual(errors,[]);assert.deepEqual(remote,[]);console.log('PASS: actual unpacked 0.13.3 package; home search, voluntary resume, continuous reading; all 98 entries and 317 block controls in six areas; new avodot source dialogs and reciprocal offering links; cross-area deep-link search and exact source dialogs; Hebrew search, back/reload/pager, SDK success and failure paths, mobile+desktop no overflow, font persistence. No network requests, JS errors or screenshots.');
}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
