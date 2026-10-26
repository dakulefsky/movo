const {packageRuntime,isRemoteRequest}=require('./test_runtime.cjs');
// Uses the actual injected JavaScript SDK from a pinned external Otzaria checkout.
// Flutter RPC boundary is a test double: this is not an installed-app E2E test.
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),{execFileSync}=require('node:child_process');
let pw;try{pw=require('playwright')}catch{pw=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/playwright')}
const root=__dirname,host=process.env.OTZARIA_HOST_SOURCE||'/workspace/otzaria-audit-host';
const commit=execFileSync('git',['rev-parse','HEAD'],{cwd:host,encoding:'utf8'}).trim();
assert.equal(commit,'9f11690b80bf37703a3d1477a32c677c889dab7b','Use the reviewed SDK revision; review before changing the pin');
const dart=fs.readFileSync(path.join(host,'lib/plugins/view/plugin_sdk_scripts.dart'),'utf8');
const stub=dart.split("const String _sdkStubCore = r'''")[1].split("''';")[0];
const boot=dart.split('String buildPluginBootScript')[1].split("'''")[1]
 .replace("${fontFaceJson == null ? '' : _fontFaceJs(fontFaceJson)}",'')
 .replaceAll('$nonceJson','"mevoot-contract-test"').replaceAll('$payloadJson',JSON.stringify({theme:{mode:'light',colorScheme:{primary:'#345678',onPrimary:'#ffffff',surface:'#fdfdfd',onSurface:'#101010',onSurfaceVariant:'#505050',surfaceContainerLow:'#eeeeee',outline:'#999999',scrim:'#000000'},typography:{fontFamily:'serif',uiFontFamily:'sans-serif',fontSize:24}}}));
(async()=>{
 fs.mkdirSync(path.join(root,'work'),{recursive:true});
 const unpacked=fs.mkdtempSync(path.join(root,'work/host-package-'));
 execFileSync('python3',['-c',`import zipfile; zipfile.ZipFile(${JSON.stringify(path.join(root,'dist/Mevoot-Shas-0.13.15.otzplugin'))}).extractall(${JSON.stringify(unpacked)})`]);
 const runtime=await packageRuntime(unpacked);
 const packagedManifest=JSON.parse(fs.readFileSync(path.join(unpacked,'manifest.json')));assert.equal(packagedManifest.version,'0.13.15');
 const browser=await pw.chromium.launch({headless:true,executablePath:process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE,args:['--no-sandbox']});
 try{
  const page=await browser.newPage(),errors=[],remote=[];
  page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(isRemoteRequest(r.url(),runtime.url))remote.push(r.url())});
  await page.addInitScript(stub);await page.goto(runtime.url+'#olah');
  await page.evaluate(()=>{
   window.rpcCalls=[];window.hostCase='success';window.openOK=true;
   window.flutter_inappwebview={callHandler:async(name,request)=>{
    window.rpcCalls.push({name,...request});assertNonce(request.nonce);
    const p=request.payload;
    if(request.method==='reader.openBook')return {success:true,data:window.openOK};
    if(request.method==='search.query'){
     if(p.__cancelStreamId){window.cancelled=true;window.resolvePending?.({success:true,data:{completed:false,cancelled:true}});return {success:true,data:true};}
     if(window.hostCase==='error')return {success:false,error:{code:'error.permission_denied',message:'permission denied'}};
     if(window.hostCase==='pending')return new Promise(resolve=>window.resolvePending=resolve);
     const emit=(sequence,results)=>window.dispatchEvent(new CustomEvent('__otzaria.search.query.chunk',{detail:{streamId:p.__streamId,chunk:{sequence,results}}}));
     if(window.hostCase!=='empty'){
      emit(0,[{id:22,type:'text',source:'library',book:'פירוש המשנה לרמב״ם',index:17,text:'wrong text',textStatus:'ok'}]);
      emit(1,[{id:73,type:'text',source:'user',book:'פירוש המשנה לרמב״ם — זבחים',reference:'ה, ד',index:201,text:p.query.split(' ').map(w=>'<b>'+w+'</b>').join(' '),textStatus:'ok'},
       {id:73,type:'text',source:'library',book:'עותק נוסף של פירוש המשנה',reference:'ה, ד',index:201,text:p.query,textStatus:'ok'},
       {id:74,type:'text',index:202,text:p.query,textStatus:'stale'}]);
     }
     return {success:true,data:{completed:true}};
    }
    return {success:false,error:{code:'error.not_found',message:'unsupported test method'}};
   }};
   function assertNonce(n){if(n!=='mevoot-contract-test')throw Error('bad nonce');}
  });
  assert.equal(await page.evaluate(()=>getComputedStyle(document.body).visibility),'hidden');
  const permissionsSource=fs.readFileSync(path.join(host,'lib/plugins/models/plugin_valid_permissions.dart'),'utf8');assert.match(permissionsSource.split('pluginBaselinePermissions')[1].split('};')[0],/events.subscribe:theme.changed/);
  await page.evaluate(boot);
  await page.waitForFunction(()=>getComputedStyle(document.body).visibility==='visible');
  assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--color-primary')),'#345678');
  assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--reader-size')),'24px');
  await page.locator('#olah--service>summary').click();await page.locator('#olah--service .refs summary').click();await page.locator('#olah--service .refs button').first().click();
  const trigger=()=>page.locator('.source-segment button').first().click();
  await trigger();await page.locator('#native-results button').first().waitFor();assert.equal(await page.locator('#native-results button').count(),2);
  assert.equal((await page.locator('#native-results').innerText()).includes('<b>'),false);
  await page.locator('#native-results button').first().click();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('נפתח'));
  let call=await page.evaluate(()=>window.rpcCalls.findLast(x=>x.method==='reader.openBook'));
  assert.equal(call.payload.id,73);assert.equal(call.payload.source,'user');assert.equal(call.payload.index,201);assert.equal(call.payload.navigateToPositionIfReused,true);
  await page.evaluate(()=>window.openOK=false);await page.locator('#native-results button').first().click();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('לא ניתן לפתוח'));
  await page.evaluate(()=>window.hostCase='empty');await trigger();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('לא נמצאה'));
  await page.evaluate(()=>window.hostCase='error');await trigger();await page.waitForFunction(()=>document.getElementById('native-status').textContent.includes('לא הצליח'));
  await page.evaluate(()=>window.hostCase='pending');await trigger();await page.waitForFunction(()=>window.rpcCalls.some(c=>c.method==='search.query'&&c.payload.__streamId));await page.click('#close-source');await page.waitForFunction(()=>window.cancelled===true);
  await page.evaluate(()=>window.dispatchEvent(new CustomEvent('theme.changed',{detail:{mode:'dark',colorScheme:{primary:'#abcdef',surface:'#121212',onSurface:'#fefefe'}}})));
  assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--color-primary')),'#abcdef');
  assert.equal(await page.evaluate(()=>document.documentElement.style.colorScheme),'dark');
  // Reopening must apply the previous host palette before any content becomes visible.
  await page.reload();
  assert.equal(await page.evaluate(()=>document.documentElement.style.colorScheme),'dark');
  assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--color-primary')),'#abcdef');
  assert.equal(await page.evaluate(()=>getComputedStyle(document.body).visibility),'hidden');
  await page.evaluate(boot);await page.waitForFunction(()=>getComputedStyle(document.body).visibility==='visible');
  assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--color-primary')),'#345678');
  assert.deepEqual(errors,[]);assert.deepEqual(remote,[]);
  console.log('PASS actual Otzaria SDK '+commit+': streamed chunks, highlighted text, envelope true/false, source identity, no-match, permission failure, cancellation, boot/change theme. Flutter RPC remains a double; no screenshots.');
 }finally{await browser.close();await runtime.close();fs.rmSync(unpacked,{recursive:true,force:true})}
})().catch(e=>{console.error(e);process.exit(1)});
