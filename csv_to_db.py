import pandas as pd
import sqlite3

db = sqlite3.connect('proyecto_senadores.db')

"""
Este script lee todos los csv descargados por los scraper y agrega a la base de datos.
Solo debe ejecutarse una vez ya que de lo contrario duplicara los valores.
"""

# id, nombre ,partido, region
df=pd.read_csv('./senador.csv')
# quita repetidos por nombre (se queda con el primero) 
df = df.drop_duplicates(subset='Nombre')
df.to_sql('senador', con=db,if_exists='append',index=False)

c=db.cursor()
c.execute("select id_s,nombre from senador")
senadores_ids = {name : id_s for id_s,name in c.fetchall() }


# id_legistaltura, id_senador, asistencia_total
df = pd.read_csv('./vigencia_legislatura.csv')
df['id_s'] = df['Senador'].apply(lambda x : senadores_ids[x])
df_to_db = df[['Legislatura','id_s','Asistencia']]
df_to_db.to_sql('vigencia_legislatura', con=db, if_exists='append',index=False)


# convierte los valores 
