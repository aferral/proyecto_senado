# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:41:37 2019

@author: darkh
"""

from bs4 import BeautifulSoup
import pandas as pd
from utils import get_using_cache
##
Empty_class = {'Nombre': [],
        'Partido': [],
        'Region': []}
###


Link_Principal="http://www.senado.cl/appsenado/index.php?mo=senadores&ac=fichasenador&id="

for i in range(2500):
    url = Link_Principal+str(i+1)
    request_text = get_using_cache(url)
    soup_html = BeautifulSoup(request_text, 'html.parser')
    
    personal_info = soup_html.find("div", attrs={"class":'info sans'})
    
    if personal_info.find("h1", attrs={"class":'serif'}).get_text() =="":
        continue

    Nombre=personal_info.find("h1", attrs={"class":'serif'}).get_text().strip()
    Partido=personal_info.find("li").get_text().strip().split()[1]
    Region=personal_info.find_all("h2")[1].get_text().strip()
    
    Empty_class["Nombre"].append(Nombre)
    Empty_class["Partido"].append(Partido)
    Empty_class["Region"].append(Region)
    
senador = pd.DataFrame(Empty_class ) 

senador.to_csv("senador.csv",encoding='utf-8-sig', index=False)
