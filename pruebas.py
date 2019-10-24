import sqlite3
import random as ra

con = sqlite3.connect('basePalabras.db')
cursor=con.cursor()

#arma una lista con todas las palabras de la base
cursor.execute('SELECT PALABRA FROM PALABRAS')
palabra=cursor.fetchall()

#Selecciona aleatoriamente una palabra y la almacena en palabra
palabra=ra.choice(palabra)[0]

print(palabra)
#Busca la categoría a la que pertenece la palabra
cursor.execute('SELECT CATEGORIAS.CATEGORIA FROM CATEGORIAS WHERE CATEGORIAS.ID =(SELECT PALABRAS.CATEGORIA_ID FROM PALABRAS WHERE PALABRAS.PALABRA = "{}");'.format(palabra))
categoriaElegida=cursor.fetchall()[0][0]
print(categoriaElegida)

largo=len(palabra)
vector2=[]
adivinadas=[]
for i in range (largo): adivinadas.append(False)
adivinadas[0]=True
adivinadas[largo-1]=True
for i in range (largo): vector2.append(palabra[i])



for i in range(largo):
    if adivinadas[i]:
        print (vector2[i],end=' ')
    else:
        print('_',end=' ')
