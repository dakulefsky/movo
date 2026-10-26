from pathlib import Path
import zipfile,json
root=Path(__file__).resolve().parent
out=root/'dist';out.mkdir(exist_ok=True)
version=json.loads((root/'plugin/manifest.json').read_text())['version']
filename=f'Mevoot-Shas-{version}.otzplugin'
with zipfile.ZipFile(out/filename,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted((root/'plugin').rglob('*')):
  if f.is_file():z.write(f,f.relative_to(root/'plugin'))
print(out/filename)
