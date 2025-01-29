x=0

print("Por favor dame un numero: ")
num=input("Numero:")

print("Su tabla de multiplicar es:")
while int(x)<=10:
    multiplicacion=int(num)*x
    print("{} X {} = {}".format(num,x,multiplicacion) )
    x=x+1
    