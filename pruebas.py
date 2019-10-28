import sqlite3
import random as ra
con = sqlite3.connect('basePalabras.db')
jugador='EDU'
cursorObj = con.cursor()
cursorObj.execute('SELECT PUNTAJE FROM JUGADORES WHERE NOMBRE="{}";'.format(jugador))
puntaje=cursorObj.fetchall()
print(puntaje)
puntos = puntaje[0][0]+10
cursorObj.execute('UPDATE JUGADORES SET PUNTAJE=("{}") WHERE JUGADORES.NOMBRE=("{}");'.format(puntos, jugador))
con.commit()