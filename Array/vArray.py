import numpy as np

array1 = np.random.randint(0, 101, 10)
print("Array con 10 enteros: ", array1)

array2 = np.random.rand(5)
print("Array con 5 decimales:", array2)

array3 = np.random.randint(0, 100, 5)

array4 = np.random.randint(0, 100, 5)
concatenado = np.concatenate((array3, array4))
print("Primer Array: ", array3)
print("Segundo Array: ", array4)
print("Concatenado: ", concatenado)

array5 = np.random.randint(0, 100, 10)
parte1, parte2 = np.split(array5, 2)
print("Array principal: ", array5)
print("Primera parte: ", parte1)
print("Segunda parte: ", parte2)

matriz = np.random.rand(3,3)
print("Matriz de 3x3: ")
print(matriz)

array6 = np.random.randint(0, 100, 10)
seleccion = np.random.choice(array6, 3)
print("Array: ", array6)
print("3 elementos al azar: ", seleccion)

array7 = np.random.randint(0, 101, 10)
media = np.mean(array7)
print("Array: ", array7)
print("Media: ", media)
