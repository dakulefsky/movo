from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
out=root/'dist';out.mkdir(exist_ok=True)
with zipfile.ZipFile(out/'Mevoot-Shas-0.11.0.otzplugin','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted((root/'plugin').rglob('*')):
  if f.is_file():z.write(f,f.relative_to(root/'plugin'))
print(out/'Mevoot-Shas-0.11.0.otzplugin')
