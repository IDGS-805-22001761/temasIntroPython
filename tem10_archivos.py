from io import open

texto = "Una línea con texto\nOtra línea con texto"

fichero=open('archivo.txt','w')
fichero.write(texto)

cadena = "\nEsto es una nueva línea de texto"
fichero.write(cadena)
fichero.close()