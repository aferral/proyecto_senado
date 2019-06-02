-- this version is using your browser's built-in SQLite
CREATE TABLE senador
	(
     id integer primary key, 
     nombre varchar(20) NOT NULL, 
     partido varchar(30),
     region varchar(30)
    );
    
    
CREATE TABLE vigencia_legislatura
	(
     id_legislatura integer  NOT NULL, 
     id_senador integer NOT NULL, 
     asistencia_total integer
    );

CREATE TABLE legislatura
	(
     id integer  primary key,
     fecha_inicial TEXT NOT NULL, 
     fecha_final TEXT NOT NULL
    );


CREATE TABLE tema
	(
     id integer  primary key,
     descripcion varchar(30) NOT NULL, 
     numero_session integer NOT NULL,
     id_legislatura integer NOT NULL
     fecha_epoch integer NOT NULL
    );

CREATE TABLE intervenciones
	(
     id_senador integer NOT NULL,
     id_tema integer NOT NULL, 
     texto varchar(30) NOT NULL,
     n_orden integer NOT NULL
    );

CREATE TABLE votos_temas
	(
     id_tema integer NOT NULL,
     id_senador integer NOT NULL,
     voto integer NOT NULL
    );



    
