#Ejercicio 1

suma = 0
N = int(input("Ingresa un número: "))

for i in range(1, N + 1):
    suma += i

print("La suma de los primeros", N, "números es:", suma)

#Ejercicio 2

numero = 5
factorial = 1

for i in range (1,numero + 1):
    factorial = factorial * i
print(factorial)

#Ejercicio 3

numero = int(input("Ingresa un número para la tabla de multiplicar: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)


#Ejercicio 4

suma_notas = 0
contador_notas = int(input("ingrese el numero de notas a capturar: "))

for i in range (contador_notas):
    calif = int(input(f"Calificacion numero {i + 1} Ingrese la calificacion: "))
    suma_notas += calif
    promedio = suma_notas / contador_notas
print ("El promedio final es de: ", promedio)

#Ejercicio 5

resultado = 1

numero_base = int(input("Ingrese un numero para sacar la potencia: "))
exponente = int(input("Ahora escriba el exponente para el numero: "))

for i in range (exponente):
    resultado *= numero_base
print("La potencia es: ", resultado)

#Ejercicio 6

a = int(input("Ingresa el valor A: "))
b = int(input("Ingresa el valor B: "))

suma = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        suma += i

print("La suma de los números pares es:", suma)
