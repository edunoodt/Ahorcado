import sqlite3
import soporte as sop
import random as ra
import dibujo

con = sop.sql_connection()
jugador=sop.bienvenida()
sop.busquedaNombre(jugador,con)
modo=sop.seleccion(jugador)
parElegido=sop.buscaPalabra(con)
adivinadas=[]

vidas=8
for i in range (len(parElegido[0])):adivinadas.append(False)
if modo==2:
    adivinadas[0]=True
    adivinadas[len(parElegido[0])-1]=True
gano=False
if modo==1:
    inf=0
    sup=len(parElegido[0])
else:
    inf=1
    sup=len((parElegido[0]))-1
while gano==False and vidas>0:
    dibujo.horca(8-vidas,jugador)
    print(' ',end='   ')
    sop.mostrarPalabraOculta(parElegido[0],adivinadas)
    sop.bajar(2)
    if modo==1: print('Categoría====>> ',parElegido[1])
    sop.bajar(2)
    respuesta=input('Ingrese letra o palabra ==> ')
    respuesta=respuesta.upper()
    encontroLetra = False
    if len(respuesta)==1:
        todoslosguiones=True
        for i in range(inf,sup):
            if respuesta==parElegido[0][i]:
                adivinadas[i]=True
                encontroLetra=True
            todoslosguiones=todoslosguiones and adivinadas[i]
    else:
        if respuesta==parElegido[0]:
            gano=True
    if todoslosguiones:
        gano=True
    if not encontroLetra:
        vidas=vidas-1
if gano:
    print ('felicitaciones!')
else:
    print('Que pena!')

