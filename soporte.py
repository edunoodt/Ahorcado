import sqlite3
import random as ra
import dibujo
def bajar(lineas):
    for i in range (lineas): print()
def sql_connection():
    con = sqlite3.connect('basePalabras.db')
    return con
def bienvenida():
    bajar(20)
    print('Bienvenido al juego del Ahorcado')
    print('Podés elegie entre el modo "TEMATICO" donde se indican las letras de la palabra mediante guiones y ademas ')
    print('se indica el "TEMA o AREA DEL CONOCIMIENTO" al que pertenece la palabra')
    print('O podes elegie "EXTREMOS" donde el juego te informa la primera y última letra de la palabra')
    print('tendrás seis chances o vidas para adivinar las letras de la palabra oculta')
    print('si te equivocas ya sea de letra o de palabra, perdés una vida')

    print('en cualquier momento podrás ingresar o una letra o la palabra oculta.')
    bajar(6)
    print('___________________________________________________________________________________________________________')
    print('Ingresa tu nombre')
    nombre=input('==> ')
    return nombre.upper()
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

def juego(jugador,modo,parElegido):
    adivinadas = []
    vidas = 6
    for i in range(len(parElegido[0])): adivinadas.append(False)
    if modo == 2:
        adivinadas[0] = True
        adivinadas[len(parElegido[0]) - 1] = True
    gano = False
    if modo == 1:
        inf = 0
        sup = len(parElegido[0])
    else:
        inf = 1
        sup = len((parElegido[0])) - 1
    while gano == False and vidas > 0:
        dibujo.horca(6 - vidas, jugador)
        print(' ', end='   ')
        mostrarPalabraOculta(parElegido[0], adivinadas)
        bajar(2)
        if modo == 1: print('Categoría====>> ', parElegido[1])
        bajar(2)
        respuesta = input('Ingrese letra o palabra ==> ')
        respuesta = respuesta.upper()
        encontroLetra = False
        if len(respuesta) == 1:
            todoslosguiones = True
            for i in range(inf, sup):
                if respuesta == parElegido[0][i]:
                    adivinadas[i] = True
                    encontroLetra = True
                todoslosguiones = todoslosguiones and adivinadas[i]
        else:
            if respuesta == parElegido[0]:
                gano = True
        if todoslosguiones:
            gano = True
        if not encontroLetra:
            vidas = vidas - 1
    return [gano,vidas]
def final(jugador,resultadoJuego,con):
    if resultadoJuego[0]:
        cursorObj = con.cursor()
        cursorObj.execute('SELECT PUNTAJE FROM JUGADORES WHERE NOMBRE="{}";'.format(jugador.upper()))
        puntaje = cursorObj.fetchall()
        print(jugador.upper())
        puntos = puntaje[0][0] + 10
        cursorObj.execute('UPDATE JUGADORES SET PUNTAJE=("{}") WHERE JUGADORES.NOMBRE=("{}");'.format(puntos, jugador))
        con.commit()
        print('GANO!!')
        print('felicitaciones!')
        print('Usted tiene ahora ', puntos, ' puntos')

    else:
        dibujo.horca(6 - resultadoJuego[1], jugador)
        print(jugador.upper())
        print('PERDIO!')
        print('Que pena!')
