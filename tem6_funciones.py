import os


def funcion1():
    os.system('cls')
    print("Dame dos numeros")
    num1=int(input("Primer numero: "))
    num2=int(input("Segundo numero: "))

    res=num1+num2
    print("La suma de {} + {} es {}".format(num1,num2,res))

def funcion2():
    print("Hola soy la funcion 2")

def run():
    os.system('cls')
    print("Menu de opciones")
    print("1. Suma de dos numeros")
    print("2. Otra opcion")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion"))
    if opcion==1:
       funcion1()
    if opcion ==2:
       funcion2()

if __name__=="__main__":
    run
    