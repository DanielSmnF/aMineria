import numpy as np
from scipy import stats

tabla = np.array([
    [40,20],
    [30,30]
])

chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)

print(f"Chi-cuadrado = {chi2:.4f}")
print(f"P_values = {p_value:.4f}")
print(f"Grados de libertad = {gl}")
print("Frecuencias esperadas: ")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("Hay evidencia sufienciente para determinar que hacer ejercicio depende del genero")
else:
    print("No hay evidencia sufienciente para determinar que hacer ejercicio depende del genero")

#Ejercicio 1

tabla = np.array([
    [85, 65],
    [50, 100]
])

chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)

print(f"Chi-cuadrado = {chi2:.4f}")
print(f"P_value = {p_value:.4f}")
print(f"Grados de libertad = {gl}")
print("Frecuencias esperadas:")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("Hay evidencia suficiente para afirmar que la preferencia de transporte depende de la ciudad")
else:
    print("No hay evidencia suficiente para afirmar que la preferencia de transporte depende de la ciudad")

#Ejercicio 2

tabla = np.array([
    [40, 20],
    [35, 45],
    [15, 45]
])

chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)

print(f"Chi-cuadrado = {chi2:.4f}")
print(f"P_value = {p_value:.4f}")
print(f"Grados de libertad = {gl}")
print("Frecuencias esperadas:")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("Hay evidencia suficiente para afirmar que fumar depende del nivel educativo")
else:
    print("No hay evidencia suficiente para afirmar que fumar depende del nivel educativo")

#Ejercicio 3

tabla = np.array([
    [10, 50],
    [30, 40],
    [45, 5]
])

chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)

print(f"Chi-cuadrado = {chi2:.4f}")
print(f"P_values = {p_value:.4f}")
print(f"Grados de libertad = {gl}")
print("Frecuencias esperadas: ")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("Hay evidencia sufienciente para determinar que hacer ejercicio depende del genero")
else:
    print("No hay evidencia sufienciente para determinar que hacer ejercicio depende del genero")









