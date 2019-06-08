import pandas as pd
import sqlite3

db = sqlite3.connect('proyecto_senadores.db')

"""
Este script lee todos los csv descargados por los scraper y agrega a la base de datos.
Solo debe ejecutarse una vez ya que de lo contrario duplicara los valores.
"""

# funciones utiles
        
def calza_acronimo(ape2_acronimo, full_nombre_cand):
    full_nombre_cand = full_nombre_cand.replace(' De ',' De-').replace(' San ',' San-') # truco para evitar apellidos de mas trozos que 3
    assert(len(ape2_acronimo) == 1), "El acronimo es solo una letra"
    nombre_cand,ape1_cand,ape2_cand = full_nombre_cand.split()
    return ape2_cand[0] == ape2_acronimo


def match_nombre(x):
    partes=x.replace(',','').replace('"','').split() ;
    if len(partes) < 3:
        return None 

    if partes[1][1:] == '.': # nombre con acronimo: Moreno R., Rafael
        n,ap1,ap2 = partes[2].strip(),partes[0].strip(),partes[1].strip().replace('.','')
        
        c1=set(senadores_nombres[n]) if n in senadores_nombres else set()  # consigue todos los con nombre X
        c2=set(senadores_1_ape[ap1]) if ap1 in senadores_1_ape else set() # consigue todos los con apellido X
        posibles = c1.intersection(c2)

        cumplen_condiciones = list(filter(lambda t : calza_acronimo(ap2,t[0]), posibles))
        if len(cumplen_condiciones) > 1:
            print("Nombre ambiguo {0} varios candidatos {1}".format(x, cumplen_condiciones))
        
        if len(cumplen_condiciones) > 0:
            return cumplen_condiciones[0][1]
        else:
            return None


    else: # nombre completo solo hay que re ordenar
        reorden = " ".join([partes[2],partes[0],partes[1]]) ; 
        valor_r = senadores_ids[reorden] if reorden in senadores_ids else None
        return valor_r



# senador (id, nombre ,partido, region)
df=pd.read_csv('./senador.csv')
# quita repetidos por nombre (se queda con el primero) 
df = df.drop_duplicates(subset='Nombre')
print("senadores agregados : {0}".format(len(df)))
df.to_sql('senador', con=db,if_exists='append',index=False)

c=db.cursor()
c.execute("select id_s,nombre from senador")
todos_los_senadores = c.fetchall()
senadores_ids = {name : id_s for id_s,name in todos_los_senadores }

# indexa senadores por nombres y apellidos
senadores_nombres = {}
senadores_1_ape = {}
for id_s,name in todos_los_senadores:
    p=name.split()
    n,ape1 = p[0].strip(),p[1].strip()
    senadores_nombres.setdefault(n,[]).append((name,id_s))
    senadores_1_ape.setdefault(ape1,[]).append((name,id_s))

# vigencia_legislatura (id_legistaltura, id_senador, asistencia_total )
df = pd.read_csv('./vigencia_legislatura.csv')
df['id_s'] = df['Senador'].apply(match_nombre)

n_b = len(df)
df = df.dropna()
n_a = len(df)
print("Se borraron {0} elementos que no fueron encontrados en nombre de senadores".format(n_b-n_a))

df_to_db = df[['Legislatura','id_s','Asistencia']]
df_to_db = df_to_db.rename(columns={'Legislatura': 'id_legislatura', 'id_s': 'id_senador', 'Asistencia' : 'asistencia_total'})
print("vigencia_legislatura agregadas : {0}".format(len(df_to_db)))
df_to_db.to_sql('vigencia_legislatura', con=db, if_exists='append',index=False)



    
# legislatura (id, fecha_inicial, fecha_final)
df = pd.read_csv('./legislaturas.csv',header=0,names=['id','fecha_inicial','fecha_final']) # numero,inicio,fin
df['id'] = df.id.apply(int)
df = df.set_index('id')
print("legislaturas agregadas : {0}".format(len(df)))
df.to_sql('legislatura',con=db,if_exists='append',index=True)


df = pd.read_csv('./tema.csv') # id_tema, descripcion, numero_session, id_legislatura, id_session,fecha_epoch 
df_sessiones = df[['numero_session','id_legislatura','id_session']]

# sessiones (id, numero_sesion, id_legislatura)
df_sessiones = df_sessiones.rename(columns={'id_session' : 'id'})
df_sessiones = df_sessiones.drop_duplicates()
print("sessiones agregadas : {0}".format(len(df_sessiones)))
df_sessiones.to_sql('sessiones',con=db,if_exists='append',index=False)

df_temas = df[['id_tema','descripcion','id_session','fecha_epoch']]
df_temas = df_temas.rename(columns={'id_tema': 'id' , 'id_session' : 'id_sesion'})
# tema (id, descripcion, id_sesion, fecha_epoch)
print("df_temas agregados : {0}".format(len(df_temas)))
df_temas.to_sql('tema',con=db,if_exists='append',index=False)


#id_senador,id_sesion,id_cargo,texto,n_orden
df_inter = pd.read_csv("./intervenciones.csv") # id_senador,id_sesion,id_cargo,intervencion,n_orden

df_inter['id_senador'] = df_inter['id_senador'].apply(match_nombre)

n_b = len(df_inter)
df_inter = df_inter.dropna()
n_a = len(df_inter)
print("Se borraron {0} elementos que no fueron encontrados en nombre de senadores".format(n_b-n_a))
df_inter = df_inter.rename(columns={'intervencion' : 'texto'})
print("intervenciones agregadas {0}".format(len(df_inter)))
df_inter.to_sql('intervenciones',con=db,if_exists='append',index=False)


# votos_temas (id_tema, id_senador, voto)
df_votos = pd.read_csv('./votos_temas.csv') # id,id_senador,voto
df_votos['id_senador'] = df_votos['id_senador'].apply(match_nombre)
n_b = len(df_votos)
df_votos= df_votos.dropna()
n_a = len(df_votos)
print("Se borraron {0} elementos que no fueron encontrados en nombre de senadores".format(n_b-n_a))

df_votos=df_votos.rename(columns={'id' : 'id_tema'})
print("votos_temas agregados {0}".format(len(df_votos)))
df_votos.to_sql('votos_temas',con=db,if_exists='append',index=False)




c.close()
db.commit()
