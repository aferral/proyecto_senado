from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt 
import sqlite3
from proceso_texto.stop_words import stops
from sklearn.decomposition import PCA,TruncatedSVD

db=sqlite3.connect('proyecto_senadores.db')
c=db.cursor()

vectorizer = TfidfVectorizer()

query_ids_senadores= 'select id_s,nombre from senador'
query_texts_senador = 'select texto from intervenciones where id_senador = {0}'

# consigue todos los senadores
c.execute(query_ids_senadores)
ids_senadores, nombres = zip(*c.fetchall())

def iterador_senadores(cursor,ids_senadores):
    # itera todos los senadores consiguiendo todas las intervenciones
    for id_s in ids_senadores:
        print(id_s)
        query = query_texts_senador.format(id_s)
        cursor.execute(query)
        res=cursor.fetchall()
        full_text = ' '.join([x[0] for x in res])
        yield full_text # entrega id_senador, textos_unidos de un senador en cada iteracion

# aplicar tf idf
X = vectorizer.fit_transform(iterador_senadores(c,ids_senadores))

# cierra coneccion a db
c.close()
db.close()


# reduce dimensionalidad
pca=TruncatedSVD(2)

x_2d = pca.fit_transform(X)

to_show = 30
x_plot = x_2d[:to_show]
names_plot = nombres[:to_show]

# Realizar plot 2d de senadores
fig, ax = plt.subplots()
ax.scatter(x_plot[:,0],x_plot[:,1])
for i in range(to_show):
    ax.annotate(names_plot[i], (x_plot[i,0], x_plot[i,1]))

plt.legend()
plt.show()

