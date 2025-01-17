from io import open

fichero = open('archivo.txt', 'r')
texto=fichero.readlines()
print(texto)
print(type(texto))
fichero.close()
for i in texto:
    print(i)
