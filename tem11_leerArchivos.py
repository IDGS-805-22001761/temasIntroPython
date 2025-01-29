from io import open


#read lee todo el archivo, readlines lee todas las lineas de una por una y readline solo lee una linea
fichero = open('archivo.txt', 'r')
texto=fichero.readlines()
print(texto)
print(type(texto))
fichero.close()
for i in texto:
    print(i)
