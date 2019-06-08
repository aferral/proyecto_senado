import requests
from bs4 import BeautifulSoup
from utils import get_using_cache

# carga un pagina cualquiera para listar legislaturasi

url_diarios = 'http://www.senado.cl/appsenado/index.php?mo=sesionessala&ac=listado&listado=1&legi={0}'
legis_base = 490

contenido = get_using_cache(url_diarios.format(legis_base))
soup = BeautifulSoup(contenido)

# Ir a listado de sessiones por legislatura
legislaturas=soup.find_all('select',attrs={'name' : 'legislaturas'})[0]

datos_legis=[]
for elem in legislaturas.find_all('option'):
    t1,t2=elem.text.split()[0],"".join(elem.text.split()[1:])
    n=int(t1.strip())
    id_legis = int(elem.get('value'))
    datos_legis.append((n,id_legis))

print(datos_legis)

# Abrir cada legislatura y listar todas las sessiones con diarios

datos_diarios=[]

for n_legislatura, id_legis in datos_legis:
    url = url_diarios.format(n_legislatura)
    contenido = get_using_cache(url)
    
    soup  = BeautifulSoup(contenido) 
    s2=soup.find_all('section',attrs={"class":"seccion2"})[0]

    sessions_table = s2.next.next

    rows = sessions_table.find_all('tr')[1:] # se salta header
    for elem in rows:
        tds = elem.find_all('td')
        session_n = tds[0].text.strip()
        session_tipo = tds[1].text.strip()
        diario_text = tds[6].text.strip()

        # Se saltan los que no tengan numero de session (ej cuentas publicas)
        if session_n == '':
            print("Sin numero de session se salta {0}".format(session_tipo))
            continue

        # salta si no tiene diario (las muy recientes aun no tienen diario)
        if diario_text == '':
            print('Sin diario se salta sn: {0} legis: {1}'.format(session_n,n_legislatura))
            continue
        diario_url = tds[6].next.get('href') 
        
        t= (diario_url,int(session_n), int(n_legislatura))
        datos_diarios.append(t)

print(datos_diarios)
base_url = "http://www.senado.cl"

tuplas_salida = []


# Abre todos los diarios
for url_d, session_n, legis_n in datos_diarios:
    url_completa = base_url + url_d

    contenido = get_using_cache(url_completa) 
    soup  = BeautifulSoup(contenido)

    # Abre los oradores y su orden
    listas_oradores= soup.find_all('div',attrs={'style' : "overflow: hidden; visibility: visible; height: 0px;"})

    # TODO para cada uno anotar nombre completo y su #intervencionX
    # TODO colocar en diccionario {intervencionX : nombre_completo}

    # Abre todas las intervenciones en los parrafos
    import re
    lista_intervenciones = soup.find_all('a',attrs={'name' : re.compile("Intervencion(\d)*")})
    
    """
    Aca se pone dificil. Pues solo entrega
    <a name="Intervencion1"> lo cual indica el inicio de un interveccion para hacer de navegacion rapida.
    Para detectar el fin de un intervencion es neceario encontrar donde deja de hablar.

    Lo que se me ocurre es usar el .- ejemplo:
    
    El señor CANTERO (Vicepresidente).- (Aca habla)

    El problema es que muchas veces meten titulos de cambios de secciones, simbolos extranos y citas a boletines. Habria que determinar todos los posibles formas de terminar una seccion
    """
    # TODO recordar aca colocar el orden de forma incremental
    
    # TODO despues de determinar texto a cortar conseguir 
    # TODO nombre completo,texto_completo, n_session,n_legis,orden y agregar a tuplas_salida


# TODO pasar tuplas salida a csv
