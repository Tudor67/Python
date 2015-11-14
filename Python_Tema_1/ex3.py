import re
import json
from datetime import datetime

def email(sir):
    expr_re = re.compile('\S{1,}@\S{1,}')
    return None if not expr_re.search(sir) else expr_re.findall(sir)[0]

fi = open("input.json","r")
fo = open("output.json","w")

suma_varste = 0
ani_de_nastere = []
ob = json.loads(fi.read())
for pers in ob:
    today = datetime.today()
    birthday = datetime.strptime(pers['birthday'],'%d.%m.%Y')
    
    an = birthday.strftime("%Y")
    if an not in ani_de_nastere:
        ani_de_nastere += [an]
     
    diff = (today - birthday).days/365.25
    suma_varste += int(diff)

print "Varsta medie :", suma_varste/len(ob),"ani" #Varsta medie : 30 ani
print "Lista cu toti anii de nastere:"
for an in ani_de_nastere: #Lista cu toti anii de nastere
    print an

dictionar = {}
for pers in ob:
    s = email(pers['about'])
    if s:
        dictionar[pers['name']] = s

ob = json.dumps(dictionar)
fo.write(ob)

fi.close()
fo.close()
