stops = ['un',
 'una','alvaro','seria','quiero','seria','mis','saludarles','posible','pilar','despide','atentamente',
 'unas','yunny','wrote','enviado','iPhone','desde',
 'unos','iphone','senor','hay','cuales','importancia','otros'
 'uno',
 'sobre',
 'todo',
 'tambien',
 'tras',
 'otro',
 'algo',
 'alguno',
 'alguna',
 'algunos',
 'algunas',
 'ser',
 'es',
 'soy',
 'eres',
 'somos',
 'sois',
 'estoy',
 'esta',
 'estamos',
 'estais',
 'estan',
 'como','gustaria',
 'en','necesito',
 'para',
 'atras',
 'porque',
 'por',
 'que',
 'estado',
 'estaba',
 'ante',
 'antes',
 'siendo',
 'ambos',
 'pero',
 'por',
 'poder',
 'puede',
 'puedo',
 'podemos',
 'podeis',
 'pueden',
 'fui',
 'fue',
 'fuimos',
 'fueron',
 'hacer',
 'hago',
 'hace',
 'hacemos',
 'haceis',
 'hacen',
 'cada',
 'fin',
 'incluso',
 'primero',
 'desde',
 'conseguir',
 'consigo',
 'consigue',
 'consigues',
 'conseguimos',
 'consiguen',
 'ir',
 'voy',
 'va',
 'vamos',
 'vais',
 'van',
 'vaya',
 'gueno',
 'ha',
 'tener',
 'tengo',
 'tiene',
 'tenemos',
 'teneis',
 'tienen',
 'el','de',
 'la',
 'lo',
 'las',
 'los',
 'su',
 'saludos','salu2','atte','gracias','listo','favor','porfavor','estimado','estimada','browser','the',
 'aqui','www','https','incluya','to','you','mozilla','cl','http','00','990','30','10','537','ip','estimados',
 'mio','hola','del','mi','me','se','ya','del','este','facebook','this','message',
 'tuyo',
 'ellos',
 'ellas',
 'nos',
 'nosotros',
 'vosotros',
 'vosotras',
 'si',
 'dentro',
 'solo',
 'solamente',
 'saber',
 'sabes',
 'sabe',
 'sabemos',
 'sabeis',
 'saben',
 'ultimo',
 'largo',
 'bastante',
 'haces',
 'muchos',
 'aquellos',
 'aquellas',
 'sus',
 'entonces',
 'tiempo',
 'verdad',
 'verdadero',
 'verdadera',
 'cierto','hotmail','fri','nov','date','subject',
 'ciertos','attached','please','lt','gt','tbody','quot','style','px',
 'cierta','margin','background','left','padding','follow','em','font','th','float',
 'ciertas','width','class','border','color',
 'intentar',
 'intento','javier','jose', 'maria', 'jose', 'maria' , 'contreras' , 'aguila','ingrid','alfredo','manuel',
 'intenta','td','tr','src','img','felipe', 'cristian','recabal' , 'gypsy' , 'pedro', 'vargas',
 'intentas',
 'intentamos',
 'intentais','lunes','martes','miercoles','jueves','viernes','sabado','domingo',
 'intentan','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre',
 'dos','octubre','noviembre','diciembre','uchile','chile','al','universidad',
 'bajo',
 'arriba',
 'encima',
 'usar',
 'uso',
 'usas',
 'usa',
 'usamos',
 'usais',
 'usan','gmail','com','tu','te',
 'emplear',
 'empleo',
 'empleas',
 'emplean',
 'ampleamos',
 'empleais',
 'valor',
 'muy',
 'era',
 'eras',
 'eramos',
 'eran',
 'modo',
 'bien',
 'cual',
 'cuando',
 'donde',
 'mientras',
 'quien',
 'con',
 'entre',
 'sin',
 'trabajo',
 'trabajar',
 'trabajas',
 'trabaja',
 'trabajamos',
 'trabajais',
 'trabajan',
 'podria',
 'podrias',
 'podriamos',
 'podrian',
 'podriais','strong',
 'yo',
 'aquel','presidenta','congreso','aca','abigeato','cariola','absolutamente']


with open('./proceso_texto/stop_words_extras.txt') as f:
    for l in f.readlines():
        stops.append(l.strip())
