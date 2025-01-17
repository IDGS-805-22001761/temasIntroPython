lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["lunes","martes","miercoles"]
lista4=["Juan",45,1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0])

suma=0
x=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1

print("La suma es: {} ".format(suma))
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

lista5=[]

for x in range(5):
    valor=int(input("Ingresa un valor: "))
    lista5.append(valor)

print(lista5)

#eliminar elementos de una lista

print(lista1)
lista1.pop()
print(lista1)

#programa que pide la cantidad de n numeros y almacenarlos en un arreglo la salida debera ser la siguiente
#lista completa: xxxx
#numeros pares: xxx
#numeros impares: xxx

lista6=[]
listaPares=[]
listaImpares=[]
tamanio=0

tamanio=int(input("Cuantos numeros deseas ingresar: "))
for x in range(tamanio):
    valor=int(input("Ingresa un valor: "))
    lista6.append(valor)
    if valor%2==0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)



print("Lista completa: {}".format(lista6))
print("Numeros pares: {}".format(listaPares))
print("Numeros impares: {}".format(listaImpares))
