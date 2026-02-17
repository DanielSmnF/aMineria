from ePoo import Coche, CuentaBancaria, Rectangulo

# Coche
coche = Coche("Nissan", "Tsuru", "Azul")
coche.acelerar(80)
coche.frenar(30)
coche.mostrar_info()

# Cuenta bancaria
print("\n")
cuenta = CuentaBancaria("Daniel")
cuenta.depositar(2000)
cuenta.retirar(500)
cuenta.mostrar_saldo()

# Rectangulo
print("\n")
rectangulo = Rectangulo(10, 5)
rectangulo.mostrar_info()

