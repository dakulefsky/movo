/* Runs synchronously in <head>, before the stylesheet or first content paint. */
(()=>{'use strict';
 const root=document.documentElement,key='mevoot-theme-v1';let previous=null;
 function apply(theme){
  if(!theme||!theme.colorScheme)return false;
  const cs={...(previous?.colorScheme||{}),...theme.colorScheme};previous={mode:theme.mode||previous?.mode,colorScheme:cs};
  for(const role of ['primary','onPrimary','surface','onSurface','onSurfaceVariant','surfaceContainerLow','surfaceContainerHigh','surfaceContainerHighest','secondaryContainer','onSecondaryContainer','outline','outlineVariant','scrim']){
   const value=cs[role];if(typeof value==='string'&&CSS.supports('color',value))root.style.setProperty('--color-'+role.replace(/[A-Z]/g,c=>'-'+c.toLowerCase()),value);
  }
  root.style.colorScheme=previous.mode==='dark'?'dark':'light';
  if(typeof cs.surface==='string'&&CSS.supports('color',cs.surface))root.style.backgroundColor=cs.surface;
  try{localStorage.setItem(key,JSON.stringify(previous));}catch{}
  return true;
 }
 try{apply(JSON.parse(localStorage.getItem(key)||'null'));}catch{}
 // The host supplies its SDK stub at document start. Standalone reading stays usable.
 if(window.Otzaria){root.dataset.themeWait='true';setTimeout(()=>{delete root.dataset.themeWait;},3000);}
 window.MevootTheme={apply,ready(){delete root.dataset.themeWait;}};
})();
