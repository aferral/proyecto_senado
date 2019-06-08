# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 01:08:43 2019

@author: darkh
"""

from bs4 import BeautifulSoup
import pandas as pd
from utils import get_using_cache

#CREATE TABLE IF NOT EXISTS votos_temas	(
#     id_tema integer NOT NULL,
#     id_senador integer NOT NULL,
#     voto integer NOT NULL    );
  
# Voto= [1:Aprobar, 2:Desarpobar, 3:Abstinencia, 4:Pareo]

Empty_class = {'id': [],
        'id_senador': [],
        'voto': []}


Link_origen="http://www.senado.cl"
Link_Principal="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=votacionSala&legiid=490&sesiid=8234"
Link_redireccionar="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=votacionSala&legiid="

Link_votos="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=detalleVotacion&votaid="
texto_request = get_using_cache(Link_Principal)
soup_html = BeautifulSoup(texto_request, 'html.parser')

Tabla_legislaturas=soup_html.find("select").find_all("option")

Tabla_legislaturas=Tabla_legislaturas[::-1]

for i in range(len(Tabla_legislaturas)):
    url = Link_redireccionar+str(Tabla_legislaturas[i].get("value"))
    texto_request = get_using_cache(url)
    soup_html = BeautifulSoup(texto_request, 'html.parser')
    Tabla_sesiones=soup_html.find_all("select")[1].find_all("option")
    
    Tabla_sesiones=Tabla_sesiones[::-1]
    for j in range(len(Tabla_sesiones)-1):
        url = Link_redireccionar+str(Tabla_legislaturas[i].get("value"))+"&sesiid="+str(Tabla_sesiones[j].get("value"))
        texto_request = get_using_cache(url)
        soup_html = BeautifulSoup(texto_request, 'html.parser')
        
        sesion_real=int(Tabla_sesiones[j].get_text()[2:5])
        print("Session:"+str(sesion_real)) 
        
        tabla_temas=soup_html.find("table", attrs={"class":'clase_tabla'})
        tabla_temas_tr=tabla_temas.find_all("tr")
        temas=[]
        fechas = []
        for k in range(len(tabla_temas_tr)):
            if '#3333FF">TEMA:' in str(tabla_temas_tr[k]).split():
                temas.append(tabla_temas_tr[k])
                fechas.append(tabla_temas_tr[k+2])
        href_list = [] 
        if temas!=[]: 
            href=tabla_temas.find_all("a")
            for k in range(len(href)):
                href_list.append(href[k].get("href")[href[k].get("href").find("votaid=")+7:])
        
        for l in range(len(href_list)):
            print(href_list[l])
            url = Link_votos+str(href_list[l])
            texto_request = get_using_cache(url)
            soup_html = BeautifulSoup(texto_request, 'html.parser')
            Tabla_Diputados=soup_html.find_all("tr",attrs={"align":'left'})
            Tabla_Diputados=Tabla_Diputados[1:]
            for m in range(len(Tabla_Diputados)):
                Diputado=Tabla_Diputados[m]
                
                Diputado=Diputado.find_all("td")
                Diputado_nombre=Diputado[0].get_text()
                Diputado=Diputado[1:]
                voto_diputado=0
                for n in range(len(Diputado)):
                    if Diputado[n].get_text()!=" ":
                        voto_diputado=n+1
                        
                Empty_class['id'].append(href_list[l])
                Empty_class['id_senador'].append(Diputado_nombre)
                Empty_class['voto'].append(voto_diputado)
            
        
        #print(j)
        #print(temas)
        
    #print(Legislatura)
    

votos_temas = pd.DataFrame(Empty_class) 

votos_temas.to_csv("votos_temas.csv",encoding='utf-8-sig', index=False)
