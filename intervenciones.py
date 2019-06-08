# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 03:24:03 2019

@author: darkh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 01:08:43 2019

@author: darkh
"""

from bs4 import BeautifulSoup
import pandas as pd
from utils import get_using_cache


Empty_class = {'id_senador': [],
        'id_sesion': [],
        'id_cargo': [],
        'intervencion': [],
        'n_orden': []}


Link_origen="http://www.senado.cl"
Link_Principal="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=votacionSala&legiid=490&sesiid=8234"
Link_redireccionar="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=votacionSala&legiid="

requests_sesion="http://www.senado.cl/wspublico/diariosesion.php?idsesion="
url=Link_Principal
request_text = get_using_cache(url)
soup_html = BeautifulSoup(request_text, 'html.parser')

Tabla_legislaturas=soup_html.find("select").find_all("option")
Tabla_legislaturas=Tabla_legislaturas[::-1]

for i in range(len(Tabla_legislaturas)):
    url = Link_redireccionar+str(Tabla_legislaturas[i].get("value"))
    request_text = get_using_cache(url)
    soup_html = BeautifulSoup(request_text, 'html.parser')
    
    Legislatura=Tabla_legislaturas[i].get_text().strip().split()[0]
    
    #print(i)
    Tabla_sesiones=soup_html.find_all("select")[1].find_all("option")
    print("Legislatura:"+ str(Legislatura))
    Tabla_sesiones=Tabla_sesiones[::-1]
    for j in range(len(Tabla_sesiones)-1):
        url = Link_redireccionar+str(Tabla_legislaturas[i].get("value"))+"&sesiid="+str(Tabla_sesiones[j].get("value"))
        request_text = get_using_cache(url)
        soup_html = BeautifulSoup(request_text, 'html.parser')
        requests_sesion="http://www.senado.cl/wspublico/diariosesion.php?idsesion="
        sesion_real=int(Tabla_sesiones[j].get_text()[2:5])
        print("Session:"+str(sesion_real)) 
        
        id_session=Tabla_sesiones[j].get("value")
        url = requests_sesion+str(id_session)
        request_text = get_using_cache(url)
        soup_html = BeautifulSoup(request_text, 'lxml')
        tabla_intervenciones=soup_html.find_all("intervencion", attrs={"janusmarca":"0"}    )
        if tabla_intervenciones==[]:
            continue
        for posicion,intervencion in enumerate(tabla_intervenciones):
            intervencion_text=intervencion.text.strip().replace("\n", " ").replace("\t", " ").replace("  "," ")
            intervencion_text=intervencion_text[intervencion_text.find(".-")+2:].strip().replace("  "," ")
            el_cargo=intervencion.get("tipo")
            nombre_senador=intervencion.get("nombre")
            Empty_class['id_senador'].append(nombre_senador)
            Empty_class['id_sesion'].append(int(id_session))
            Empty_class['id_cargo'].append(el_cargo)
            Empty_class['intervencion'].append(intervencion_text)
            Empty_class['n_orden'].append(posicion)
            
            
intervenciones= pd.DataFrame(Empty_class) 
intervenciones.to_csv("intervenciones.csv",encoding='utf-8-sig', index=False)
