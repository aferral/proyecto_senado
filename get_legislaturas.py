import requests
from bs4 import BeautifulSoup

"""
Consigue las legislaturas mediante ir a una session en particular y revisar el select de todas las legislaturas

Crear un csv legislaturas.csv que contiene n_legislatura,fecha inicio, fecha fin 

"""

r=requests.get("http://www.senado.cl/appsenado/index.php?mo=sesionessala&listado=1&ac=listado&legi=490")
soup=BeautifulSoup(r.content)

legislaturas=soup.find_all('select',attrs={'name' : 'legislaturas'})[0]

out_string=""
for elem in legislaturas.find_all('option'):
    t1,t2=elem.text.split()[0],"".join(elem.text.split()[1:])
    n=t1.strip()
    st,en = list(map(lambda x : x.replace('(','').replace(")",'') , t2.split('-') ))
    out_string += "{0},{1},{2}\n".format(n,st,en)

with open("legislaturas.csv",'w') as f:
    f.write("numero,inicio,fin\n")
    f.write(out_string)
