import sqlite3
import random as ra
def bajar(lineas):
    for i in range (lineas): print()
def sql_connection():
    con = sqlite3.connect('basePalabras.db')
    return con
def bienvenida():
    bajar(10)
    print('Bienvenido al juego del Ahorcado')
    print('tendrás seis chances para adivinar las letras de la palabra oculta')
    print('en cualquier momento podrás adivinar la palabra oculta. Si no la adivinas pierdes una chance')
    bajar(4)
    print('Ingresa tu nombre')
    nombre=input('==> ')
    return nombre
def busquedaNombre(nombre,con):
    nombre=nombre.upper()
    cursorObj=con.cursor()
    cursorObj.execute('SELECT NOMBRE FROM JUGADORES;')
    participantes = cursorObj.fetchall()
    listaparticipantes = []
    for i in (participantes): listaparticipantes.append(i[0])
    if nombre not in listaparticipantes:
        cursorObj.execute('INSERT INTO JUGADORES (NOMBRE) VALUES("{}");'.format(nombre))
        print(nombre,'Usted ha sido incluido en la lista de jugadores. Comienza con "0" puntos')
        puntos=0
        con.commit()
    else:
        cursorObj.execute('SELECT PUNTAJE FROM JUGADORES WHERE NOMBRE="{}";'.format(nombre))
        puntos=cursorObj.fetchall()
        print(nombre,': Usted tiene '+str(puntos[0][0])+' puntos')
    input('pulse enter para continuar')
    return puntos
def seleccion (nombre):
    bajar(5)
    print(nombre,'podés elegir entre dos opciones de juego, "TEMATICO" o "EXTREMOS"')
    print(' "TEMATICO" te muestra la cantidad de letras de la palabra sin mostrate ninguna letra, pero te indica a '
          'que tema pertenece la palabra: Artes, Ciencia, Deportes, Entretenimiento, Geografía e Historia)')
    print('"EXTREMOS" te muestra una palabra de uno de los temas antes mencionados, pero no te indica el tema.  '
          'En cambio te muestra la primera y la última letra de la misma')
    print('Ingrese la opción deseada')
    opcion=0
    while opcion!=1 and opcion!=2:
        print('      1.- TEMATICO')
        print('      2.- EXTREMOS')
        opcion=int(input('==> '))
    return opcion
def buscaPalabra(con):
    cursor=con.cursor()
    parElegido=[]
    cursor.execute('SELECT PALABRA FROM PALABRAS;')
    listaPalabras=cursor.fetchall()
    palabraElegida=ra.choice(listaPalabras)
    parElegido.append(palabraElegida[0])
    cursor.execute('SELECT CATEGORIAS.CATEGORIA FROM CATEGORIAS WHERE CATEGORIAS.ID =(SELECT PALABRAS.CATEGORIA_ID FROM PALABRAS WHERE PALABRAS.PALABRA = "{}");'.format(palabraElegida[0]))
    categoriaElegida=cursor.fetchall()
    parElegido.append(categoriaElegida[0][0])
    return parElegido
def mostrarPalabraOculta(vector2,adivinadas):
    for i in range(len(vector2)):
        if adivinadas[i]:
            print(vector2[i], end=' ')
        else:
            print('_', end=' ')


