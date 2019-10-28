import sqlite3
import soporte as sop
import random as ra
import dibujo

con = sop.sql_connection()
jugador=sop.bienvenida()
sop.busquedaNombre(jugador,con)
modo=sop.seleccion(jugador)
parElegido=sop.buscaPalabra(con)

resultadoJuego=sop.juego(jugador,modo,parElegido)

sop.final(jugador,resultadoJuego,con)
