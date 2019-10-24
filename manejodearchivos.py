archivo = open("Don Quijote.txt")
quijote={}
indice=1
línea=archivo.readline()
while línea != '':

    quijote[indice]=línea
    línea=archivo.readline()
    indice=indice+1
print(quijote)
print(indice)
