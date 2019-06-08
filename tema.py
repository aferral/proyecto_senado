# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 01:08:43 2019

@author: darkh
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd



Empty_class = {'id_tema': [],
        'descripcion': [],
        'numero_session': [],
        'id_legislatura': [],
        'id_session': [],
        'fecha_epoch': []}


Link_origen="http://www.senado.cl"
Link_Principal="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=votacionSala&legiid=490&sesiid=8234"
Link_redireccionar="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=votacionSala&legiid="
requests_link = requests.get(Link_Principal)
soup_html = BeautifulSoup(requests_link.text, 'html.parser')

Tabla_legislaturas=soup_html.find("select").find_all("option")

Tabla_legislaturas=Tabla_legislaturas[::-1]

for i in range(len(Tabla_legislaturas)):
    requests_link = requests.get(Link_redireccionar+str(Tabla_legislaturas[i].get("value")))
    soup_html = BeautifulSoup(requests_link.text, 'html.parser')
    
    Legislatura=Tabla_legislaturas[i].get_text().strip().split()[0]
    
    #print(i)
    Tabla_sesiones=soup_html.find_all("select")[1].find_all("option")
    print("Legislatura:"+ str(Legislatura))
    Tabla_sesiones=Tabla_sesiones[::-1]
    for j in range(len(Tabla_sesiones)-1):
        requests_link = requests.get(Link_redireccionar+str(Tabla_legislaturas[i].get("value"))+"&sesiid="+str(Tabla_sesiones[j].get("value")))
        soup_html = BeautifulSoup(requests_link.text, 'html.parser')
        id_session=Tabla_sesiones[j].get("value")
        sesion_real=int(Tabla_sesiones[j].get_text()[2:5])
        print("Session:"+str(sesion_real)) 
        tabla_temas=soup_html.find("table", attrs={"class":'clase_tabla'})
        tabla_temas_tr=tabla_temas.find_all("tr")
        temas=[]
        fechas=[]
        href_list=[]
        for k in range(len(tabla_temas_tr)):
            if '#3333FF">TEMA:' in str(tabla_temas_tr[k]).split():
                temas.append(tabla_temas_tr[k])
                fechas.append(tabla_temas_tr[k+2])
        
        if temas!=[]: 
            href=tabla_temas.find_all("a")
            for k in range(len(href)):
                href_list.append(href[k].get("href")[href[k].get("href").find("votaid=")+7:])
        
        for k in range(len(temas)):
            hasta_quorum=temas[k].get_text().strip().find("QUORUM:")
            tema_real=temas[k].get_text().strip()[5:hasta_quorum]
            quorum=temas[k].get_text().strip()[hasta_quorum+7:]
            fecha_real= fechas[k].get_text().strip()[:16]
            tema_real=tema_real.replace("\n", " ")
            
            Empty_class['id_tema'].append(href_list[k])
            Empty_class['descripcion'].append(tema_real)
            Empty_class['numero_session'].append(int(sesion_real))
            Empty_class['id_session'].append(int(id_session))
            Empty_class['id_legislatura'].append(int(Legislatura))
            Empty_class['fecha_epoch'].append(fecha_real)
        
        
        #print(j)
        #print(temas)
        
    #print(Legislatura)
    

tema = pd.DataFrame(Empty_class) 

tema.to_csv("tema.csv",encoding='utf-8-sig', index=False)