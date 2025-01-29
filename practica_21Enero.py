#cinepolisPy
from io import open

class Main:
    # declaracion de las propiedades
    numBoletos = 0
    boletos_maximos = 0
    numPersonas = 0
    nombre = ""
    total=0.0
    totalfinal=0.0
    descuento=0
    descuento2=0
    opcion=0
    opcion2=0
    tarjeta = False
    x=0

    def mostrar_menu(self):
        print("\nBienvenido a Cinepolis")
        print("1.- Comprar Boletos")
        print("2.- Salir")
        return int(input("Seleccione una opcion: "))
    
    def comprar_boletos(self):
        self.numPersonas = int(input("Cuantas personas van a comprarar: "))
        self.numBoletos = self.obtener_num_boletos(self.numPersonas)
        total = self.calcular_total(self.numBoletos, self.numPersonas)
        texto = "\nEl total a pagar es: " + str(self.totalfinal) + "\n" + str(self.nombre) + " Gracias por su compra\n"
        print(texto)
        fichero=open('archivo.txt','a')
        fichero.write(texto)
        fichero.close()
        
    
    def calcular_total(self, numBoletos, numPersonas):
        total = numBoletos * 12
        if numBoletos > 5:
            descuento = total * 0.15
            total -= descuento
        elif numBoletos >= 3:
            descuento = total * 0.10
            total -= descuento
        return total

    def obtener_num_boletos(self, numPersonas):
        self.nombre = input("Ingrese el nombre de la persona: ")
        boletos_maximos = numPersonas * 7
        self.numBoletos = int(input(f"¿Cuántos boletos desea comprar (máximo {boletos_maximos})? "))

        # Validación de boletos
        while self.numBoletos > boletos_maximos or self.numBoletos <= 0:
            print(f"Lo siento, el límite es de {boletos_maximos} boletos para {numPersonas} persona(s).")
            print("¿Qué desea hacer?")
            print("1.- Agregar otra persona")
            print("2.- Cambiar el número de boletos")
            print("3.- Salir")
            self.opcion2 = int(input("Seleccione una opción: "))

            if self.opcion2 == 1:
                numPersonas += 1
                self.numPersonas = numPersonas
                boletos_maximos = numPersonas * 7  
                self.numBoletos = int(input(f"¿Cuántos boletos desea comprar (máximo {boletos_maximos})? "))
            elif self.opcion2 == 2:
                self.numBoletos = int(input(f"Ingrese nuevamente la cantidad de boletos (máximo {boletos_maximos}): "))
            elif self.opcion2 == 3:
                print("Gracias por su visita.")
                return 0  # Salida del flujo si elige salir
            else:
                print("Opción no válida. Intente de nuevo.")

        # Calcular el total
        total = self.numBoletos * 12
        if self.numBoletos > 5:
            descuento = total * 0.15
            self.totalfinal = total - descuento
            print(f"El total con un descuento del 15% es: {self.totalfinal:.2f}")
        elif self.numBoletos >= 3:
            descuento = total * 0.10
            self.totalfinal = total - descuento
            print(f"El total con un descuento del 10% es: {self.totalfinal:.2f}")
        else:
            self.totalfinal = total
            print(f"El total a pagar es: {self.totalfinal:.2f}")

        # Elección del método de pago
        print("Elija el método de pago:")
        print("1.- CINECO")
        print("2.- Efectivo")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            self.descuento2 = self.totalfinal * 0.10
            self.totalfinal -= self.descuento2
            print(f"El total con el descuento adicional del 10% por pagar con CINECO es: {self.totalfinal:.2f}")
        else:
            print(f"El total a pagar es: {self.totalfinal:.2f}")

        return self.totalfinal


    
    def main(self):
        while True:
            opcion = self.mostrar_menu()
            if opcion == 2:
                print("Gracias por su visita")
                fichero = open('archivo.txt', 'r')
                texto=fichero.read()
                print(texto)
                fichero.close()
                break
            elif opcion == 1:
                self.comprar_boletos()
            else:
                print("Opcion no valida")
                break


if __name__ == "__main__":
    Main().main()

