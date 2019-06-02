# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:41:39 2019

@author: darkh
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

link_principal="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=asistenciaSenadores&camara=S&legiini=361&legiid=361" #"http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=asistenciaSenadores&camara=S&legiini=361&legiid=381"  
requests_link = requests.get(link_principal)
soup_html = BeautifulSoup(requests_link.text, 'html.parser')

link_redireccionar="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=asistenciaSenadores&camara=S&legiini=361&legiid=" #"http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=asistenciaSenadores&camara=S&legiini=361&legiid=381"  


tables = soup_html.find_all("table", attrs={"class":'clase_tabla'})
Tabla_iterator=tables[0].find_all("option")


Empty_class = {'Legislatura': [],
        'Senador': [],
        'Asistencia': []}
#vigencia_legislatura = pd.DataFrame(Empty_class,columns= ['Legislatura', 'Senador','Asistencia'])


for i in range(len(Tabla_iterator)):
    Legislatura=Tabla_iterator[i].get_text().strip().split()[0]
    link_redireccionar="http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=asistenciaSenadores&camara=S&legiini=361&legiid=" #"http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=asistenciaSenadores&camara=S&legiini=361&legiid=381"  
    requests_link = requests.get(link_redireccionar+str(Tabla_iterator[i].get("value")))
    soup_html = BeautifulSoup(requests_link.text, 'html.parser')
    tables = soup_html.find_all("table", attrs={"class":'clase_tabla'})

    list_tables_senadores=table[1].find_all("tr", attrs={"align":'left'} )
    list_tables_senadores=list_tables_senadores[1:]
    for i in range(len(list_tables_senadores)):
        senador= list_tables_senadores[i].find_all("td", attrs={"class":'clase_td'})[0].get_text()
#        print(senador)
        asistencia= list_tables_senadores[i].find_all("td", attrs={"class":'clase_td_center'})[0].get_text().strip()
#        print(asistencia)
        Empty_class["Legislatura"].append(Legislatura)
        Empty_class["Senador"].append(senador)
        Empty_class["Asistencia"].append(asistencia)
      #  new_senador = pd.DataFrame({'Legislatura':[Legislatura] , 'Senador':[senador],'Asistencia':[asistencia]})
       # vigencia_legislatura = vigencia_legislatura.append(new_senador)
        

vigencia_legislatura = pd.DataFrame(Empty_class ) #, columns= ['Legislatura', 'Senador','Asistencia'])



vigencia_legislatura.to_csv("vigencia_legislatura.csv",encoding='utf-8-sig', index=False)
#print (vigencia_legislatura)



