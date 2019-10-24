import sqlite3
import soporte as sop

def listaJugadores(c):
    cursorObj = c.cursor()
    cursorObj.execute('SELECT NOMBRE FROM JUGADORES')
    respuesta=cursorObj.fetchall()
    print(respuesta)
    input('pulse enter para continuar')

def sql_tabla(c):
    clave=input('ingrese password ==> ')
    if clave=='Epica':
        cursorObj = c.cursor()
        cursorObj.execute(
            "CREATE TABLE CATEGORIAS(id integer PRIMARY KEY AUTOINCREMENT, CATEGORIA text);")
        cursorObj.execute(
            "CREATE TABLE PALABRAS( ID INTEGER PRIMARY KEY AUTOINCREMENT,PALABRA TEXT,"
            "CATEGORIA_ID INTEGER,FOREIGN KEY(CATEGORIA_ID) REFERENCES CATEGORIAS(id));")
        cursorObj.execute(
            "CREATE TABLE JUGADORES( ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE TEXT,PUNTAJE INTEGER DEFAULT 0);")
        c.commit()

def categorias(c):
    cursorObj = c.cursor()
    sop.bajar(10)
    nombre=input('Ingrese nombre de la categoría > ')
    while nombre !='*':
        cursorObj.execute('INSERT INTO CATEGORIAS (CATEGORIA) VALUES("{}");'.format(nombre))
        nombre = input('Ingrese nombre de la categoría > ')
    con.commit()

def cargaPalabras (con):
    cursorObj = con.cursor()
    categoria= ''
    while categoria != '*':
        cursorObj.execute('SELECT * FROM CATEGORIAS;')
        sop.bajar(15)
        respuesta = cursorObj.fetchall()
        for i in (respuesta):
            print(i)
        print('Seleccione el número de la categoria de la/las palabras a ingresar:')
        print('o presione "*" para salir')
        categoria = input('===> ')
        if categoria!='*':
            cursorObj.execute('SELECT PALABRA FROM PALABRAS WHERE CATEGORIA_ID=' + categoria)
            palabrasenbase = cursorObj.fetchall()
            listapalabrasenbase=[]
            for i in (palabrasenbase):listapalabrasenbase.append(i[0])
            print(listapalabrasenbase)
            nuevaPalabra = input('Ingrese Palabra (o "*" para terminar) > ')
            while nuevaPalabra != '*':
                nuevaPalabraMayuscula = nuevaPalabra.upper()
                if nuevaPalabraMayuscula not in listapalabrasenbase:
                    cursorObj.execute('INSERT INTO PALABRAS (PALABRA,CATEGORIA_ID) VALUES("{}","{}");'.format(nuevaPalabraMayuscula, categoria))
                    listapalabrasenbase.append(nuevaPalabraMayuscula)
                else:
                    sop.bajar(3)
                    print('Esa palabra ya está en la base')
                nuevaPalabra = input('Ingrese Palabra (o "*" para terminar)> ')
    con.commit()
    return

def listaPalabras(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT CATEGORIAS.CATEGORIA,PALABRAS.PALABRA FROM CATEGORIAS,PALABRAS WHERE PALABRAS.CATEGORIA_ID=CATEGORIAS.ID;')
    respuesta = cursorObj.fetchall()
    for i in (respuesta):
        print(i)
    input('pulse enter para continuar')

con = sop.sql_connection()
listaopciones=[listaJugadores,cargaPalabras,listaPalabras,categorias,sql_tabla]
respuesta=0
while respuesta != '*':
    sop.bajar(15)
    print('1.- Lista los jugadores')
    print('2.- Agrega palabras a la base')
    print('3.- Lista todas las palabras de la base')
    print('4.- Agrega categorías')
    print('5.- Crea base de datos')
    respuesta=input('Ingrese opción ("*" PARA SALIR) ==>  ')
    if respuesta!='*':
        try:
            respuestaEntero=int(respuesta)
            listaopciones[respuestaEntero-1](con)
        except IndexError:
            print('no ingreso una opción correcta')
        except ValueError:
            print('no ingreso una opción correcta')