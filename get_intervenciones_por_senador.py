from utils import get_using_cache

min_y = 1990
max_y = 2019

# ir a http://www.senado.cl/appsenado/index.php?mo=senadores&ac=periodos&tipo=2

# ir a http://www.senado.cl/appsenado/index.php?mo=senadores&ac=periodos&tipo=1

# anotar todas las ids de senadores existente


url_base_intervenciones = "http://www.senado.cl/appsenado/index.php?mo=senadores&ac=intervenciones_senador&parlamentario={0}&ano={1}" 

lista_urls_intervenciones = []

for senador_id in lista_senadores:

    for y_st in range(min_y, max_y):

        url = url_base_intervenciones.format(senador_id,y_st)
        
        html_lista_intervenciones = get_using_cache(url)

        # TODO use bs4 para conseguir todos los link a intervencciones 


        (senador_id,y_st,url_extraidas)
        lista_urls_intervenciones.append(   )




for senador_id,y_st, url_interv in lista_urls_intervenciones:

    # TODO DETECTAR N_SESSION, N_LEGISLATURA

    # TODO detectar cuantas intervencinoes hay dentro (a veces hay mas de una)
    # TODO cortar en tantos trozoso como corresponde
    # TODO el orden es imposible de sacar, pero colocar orden de la intervenciones del mismo senador
    

    # TODO agregar cada trozo (id_senador, session, legisltaura,texto, orden)


# listas de valores a csv 

