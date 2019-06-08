import requests
import base64
import os 
import io

cache_folder='htmls_descargados'
os.makedirs(cache_folder,exist_ok=True)

def get_using_cache(url):
    name = base64.b64encode(url.encode()).decode('utf-8') # consigue el nombre en un formato unico (evita problemas con espacios y signos)
    f_name = "{0}.html".format(name)
    path_html = os.path.join(cache_folder,f_name)
    
    if os.path.exists(path_html): # Si estaba abrir el archivo simplemente
    
        print("Reutilizando {0}".format(url))
        with open(path_html,'r') as f:
            out=f.read()
        return out
    else:           # Si no estaba conseguir y escribir a disco
        print("Url: {0} no encontrada realizando GET".format(url))
        contenido = requests.get(url).text
        with open(path_html,'w') as f:
            f.write(contenido)

        return contenido
