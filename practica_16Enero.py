#programa que te permite calcular la distancia entre dos puntos
import math
punto1=[]
punto2=[]

for x in range(2):
    valor=int(input("Ingresa el valor del punto 1: "))
    punto1.append(valor)

for x in range(2):
    valor=int(input("Ingresa el valor del punto 2: "))
    punto2.append(valor)

distancia= math.sqrt((punto1[0] - punto1[1])**2 + (punto2[0] - punto2[1])**2)

print("La distancia entre los puntos es: {}".format(distancia))
