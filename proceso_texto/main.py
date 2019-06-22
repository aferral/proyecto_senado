from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt 
import numpy as np 
import sqlite3
from proceso_texto.stop_words import stops
from sklearn.decomposition import PCA,TruncatedSVD
import pickle


db=sqlite3.connect('proyecto_senadores.db')
c=db.cursor()


params_tf_idf= {
        'norm' : 'l2',
        'strip_accents':'ascii',
        'stop_words':stops}

vectorizer = TfidfVectorizer(**params_tf_idf)

senadores_con_intervenciones = "select DISTINCT(id_senador) from intervenciones"
query_ids_senadores= 'select id_s,nombre,partido from senador where id_s in ({0})'.format(senadores_con_intervenciones)
query_texts_senador = 'select texto from intervenciones where id_senador = {0}'

# consigue todos los senadores
c.execute(query_ids_senadores)
ids_senadores, nombres,partidos = zip(*c.fetchall())

def iterador_senadores(cursor,ids_senadores):
    # itera todos los senadores consiguiendo todas las intervenciones
    for name,id_s in zip(nombres,ids_senadores):
        print("Procesando: {0} ".format(name))
        query = query_texts_senador.format(id_s)
        cursor.execute(query)
        res=cursor.fetchall()
        full_text = ' '.join([x[0] for x in res])
        if len(full_text) == 0:
            raise Exception("Senador: {0} no tiene intervenciones ".format(name))
        yield full_text # entrega id_senador, textos_unidos de un senador en cada iteracion

# aplicar tf idf
X = vectorizer.fit_transform(iterador_senadores(c,ids_senadores))

# cierra coneccion a db
c.close()
db.close()

# pasa vectores a archivo para posterior analisis
with open('intervenciones_tfidf.pkl','wb') as f:
    pickle.dump((X,vectorizer),f)


ind_to_word = {ind : word for word,ind in vectorizer.vocabulary_.items()}


# reduce dimensionalidad
svd=TruncatedSVD(2)

x_2d = svd.fit_transform(X)

# De los primeros componentes muestra las X palabras mas presentes
x_presentes = 10
for i in range(2):
    comp = svd.components_[i]
    inds_repr=comp.argsort()[::-1][0:x_presentes]
    palabras_repr = [ind_to_word[x] for x in inds_repr]
    print("Comp {0} Top {2} dimensiones: {1}".format(i,palabras_repr,x_presentes))

to_show = x_2d.shape[0]
x_plot = x_2d[:to_show]
names_plot = nombres[:to_show]
partidos_plot = np.array(partidos[:to_show])


# Realizar plot 2d de senadores
fig, ax = plt.subplots()
for partido_str in set(partidos_plot):
    sel_partido = (partidos_plot == partido_str)
    x,y = x_plot[sel_partido,0] , x_plot[sel_partido, 1]
    ax.scatter(x,y,label=partido_str)

for i in range(to_show):
    ax.annotate(names_plot[i], (x_plot[i,0], x_plot[i,1]))

plt.legend()
plt.show()

