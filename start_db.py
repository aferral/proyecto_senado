 	
import sqlite3 	

db = sqlite3.connect('proyecto_senadores.db')

cursor = db.cursor()
with open("./estructura.sql",'r') as f:
    create_tables_query = f.read()

print(create_tables_query)
for elem in create_tables_query.split(';'):
    cursor.execute(elem)

db.commit()


