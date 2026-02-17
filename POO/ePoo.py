#Clase Coche y metodos implementados
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, velocidad):
        self.velocidad += velocidad

    def frenar(self, velocidad):
        self.velocidad -= velocidad
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Velocidad:", self.velocidad, "km/h")
        
#Clase CuentaBancaria y metodos implementados
class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print("Titular:", self.titular)
        print("Saldo actual: $", self.saldo)

#Clase Rectangulo y metodos implementados
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        print("Ancho:", self.ancho)
        print("Alto:", self.alto)
        print("Area:", self.calcular_area())
        print("Perimetro:", self.calcular_perimetro())


