
CREATE TABLE IF NOT EXISTS senador
	(
     id_s integer primary key, 
     nombre varchar(20) NOT NULL UNIQUE, 
     partido varchar(30),
     region varchar(30)
    );
    
    
CREATE TABLE IF NOT EXISTS vigencia_legislatura
	(
     id_legislatura integer  NOT NULL, 
     id_senador integer NOT NULL, 
     asistencia_total integer
    );

CREATE TABLE IF NOT EXISTS legislatura
	(
     id integer  primary key,
     fecha_inicial TEXT NOT NULL, 
     fecha_final TEXT NOT NULL
    );


CREATE TABLE IF NOT EXISTS sessiones
(
id integer primary key,
numero_session integer NOT NULL,
id_legislatura integer NOT NULL
);

CREATE TABLE IF NOT EXISTS tema
	(
     id integer  primary key,
     descripcion varchar(30) NOT NULL, 
     id_sesion integer NOT NULL,
     fecha_epoch integer NOT NULL
    );

CREATE TABLE IF NOT EXISTS intervenciones
	(
     id_senador integer NOT NULL,
     id_sesion integer NOT NULL,
     id_cargo integer,
     texto varchar(30) NOT NULL,
     n_orden integer NOT NULL
    );

CREATE TABLE IF NOT EXISTS votos_temas
	(
     id_tema integer NOT NULL,
     id_senador integer NOT NULL,
     voto integer NOT NULL
    );



    
