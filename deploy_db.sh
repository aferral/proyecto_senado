#!/bin/sh
rm proyecto_senadores.db # borra base de datos antigua 
python start_db.py 
python csv_to_db.py 

