import concurrent.futures,json,pathlib,urllib.request
p=pathlib.Path(__file__).parent/'sources'
refs=['Rambam_on_Mishnah_Zevachim.3.1','Rambam_on_Mishnah_Zevachim.5.3','Rambam_on_Mishnah_Zevachim.5.4','Rambam_on_Mishnah_Zevachim.5.5','Rambam_on_Mishnah_Zevachim.5.7','Rambam_on_Mishnah_Zevachim.5.8']
def get(r):
 b=urllib.request.urlopen('https://www.sefaria.org/api/texts/'+r+'?context=0&commentary=0',timeout=35).read();d=json.loads(b);assert d.get('he');(p/(r+'.json')).write_bytes(b);return r,len(b)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for x in ex.map(get,refs):print(x)
