# Proyecto Senado

Queremos realizar una página interactiva con los datos de la página de Senado Chile, para mayor visualización de los datos.

## Introducción

Para realizar nuestro se tendrá que hacer los siguientes pasos, webscraping de la página de senado, crear una base de datos sql, montar una página Django y generar datos interactivos y visualización.

## Objetivos o algo así.

Los objetivos de participar a este repositorio es aprender:
- Webscraping
- Sql
- Django
- La utilización de Javascript con modulos de highchart


## Descripción de la base de datos

La base de datos se puede ver directamente en estructura.sql, 
En que en resumen son 7 tablas:

1. Senador
   - Id_s: Id del Senador.
   - Nombre:  Nombre de cada Senador
   - Partido: Partido político al que pertenece cada Senador.
   - Region: Region a la que representa cada senador.
 
2. Vigencia Legislatura:
   - id_legislatura: Es el id de cada legislatura. 
   - id_senador: Id del senador
   - asistencia_total: Asistencia de cada senador en legislatura
   
3. Legislatura:
   - id: Es Id de cada legislatura.
   - fecha_inicial: Fecha en que inicia cada legislatura.
   - fecha_final: Fecha en que finaliza cada legislatura.
   
 4. Sessiones:
    - id: Id de cada session (es el id impuesto por cada pagina html).
    - numero de session: Numero de session (Existen sessiones distintas en cada legislatura).
    - id_legislatura: Es el Id de cada legislatura.
    
5. Tema:
   - id : Id de cada tema.
   - descripcion: Descripción de cada session.
   - id_sesion: Id de la session en cual se discutio el tema.
   - fecha_epoch: Fecha en que se discutio tema (Contiene Año/mes/dia Hora y minutos)
 
6. Intervenciones:
   - id_senador: Id de cada senador.
   - id_sesion: Id de la session en que se interviene.
   - id_cargo: Pueden intervenir Senadores, presidentes o ministros. (Comentario: Parece que hicimos un filtro de solo Senadores)
   - texto: Intervención que realizo id_senador en id_sesion.
   - n_orden: es el orden en que se realizo cada intervencion. 
   
 7. Votos_temas:
    - id_tema: Id del tema.
    - id_senador: id Senador.
    - voto: Voto que realizo id_senador en id_tema.  Voto= [1:Aprobar, 2:Desarpobar, 3:Abstinencia, 4:Pareo], se puede ver que no cuenta la inasistencia del senador, pues se puede ver cruzando las otras tablas de Vigencia Legislatura y Legislatura.
    
  
  
## Cualquier duda al telegram. 

### Seguiré agregando el readme segun vayamos avanzando
