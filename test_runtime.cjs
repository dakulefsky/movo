// Optional loopback HTTP transport for environments that authorize HTTP previews.
// Default remains file:// for the native plugin transport; no policy is changed.
const http=require('node:http'),fs=require('node:fs'),path=require('node:path');
exports.packageRuntime=async function(directory){
 if(process.env.MOVO_TEST_TRANSPORT!=='http')return {url:'file://'+path.join(directory,'index.html'),close:async()=>{}};
 const root=path.resolve(directory),types={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.css':'text/css; charset=utf-8','.woff2':'font/woff2'};
 const server=http.createServer((req,res)=>{
  let file;try{file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));}catch{res.writeHead(400);res.end();return;}
  if(!file.startsWith(root+path.sep)){res.writeHead(403);res.end();return;}
  fs.readFile(file,(err,data)=>{if(err){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');res.end(data);});
 });
 await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve)});
 return {url:`http://127.0.0.1:${server.address().port}/index.html`,close:()=>new Promise(resolve=>server.close(resolve))};
};
exports.isRemoteRequest=(url,base)=>/^https?:/.test(url)&&new URL(url).origin!==new URL(base).origin;
