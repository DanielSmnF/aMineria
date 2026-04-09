import numpy as np
from scipy import stats

#Frecuencias observadas
observadas = np.array([90,70,40])

#Proporciones historicas esperadas
p = np.array([0.50, 0.30, 0.20])

#Total de personas encuestadas
n = observadas.sum()

#Frecuencias esperadas
esperadas = n * p

#Calculo estadistico del chi cuadrado
res = stats.chisquare(f_obs=observadas, f_exp=esperadas)

#Extraer Resultados
chi2 = res.statistic
p_value = res.pvalue
gl = len(observadas) - 1 

#Mostrar los resultados
print(f"Frecuencias observadas: {observadas}")
print(f"Frecuencias esperadas: {esperadas}")
print(f"Chi cuadrado: {chi2:.4f}")
print(f"Grados de libertas: {gl}")
print(f"Valor P: {p_value:.4f}")

#Interpretacion
alpha = 0.05
if p_value < alpha:
    print("Se rechaza Hipotesis nula")
else:
    print("No se rechaza hipotesis nula")

#EJERCICIO 1 
print("\nEjercicio 1 - Agua: ")

agua = np.array([498, 501, 499, 502, 500, 497, 503, 499, 501, 500])

res = stats.ttest_1samp(agua, popmean=500)

#Resultados
t = res.statistic
p_value = res.pvalue

print(f"t: {t:.4f}")
print(f"p-value: {p_value:.4f}")

#Interpretacion
alpha = 0.05
if p_value < alpha:
    print("Se rechaza la hipotesis nula")
else:
    print("No se rechaza la hipotesis nula")

#EJERCICIO 2
print("\nEjercicio 2 - Musica: ")

musica = np.array([65, 70, 68, 72, 66, 69, 71, 67, 70, 68])
silencio = np.array([85, 88, 90, 87, 92, 86, 89, 91, 88, 90])

res = stats.ttest_ind(musica, silencio, equal_var=False)

#Resultados
t = res.statistic
p_value = res.pvalue

print(f"t: {t:.4f}")
print(f"p-value: {p_value:.4f}")

alpha = 0.01
if p_value < alpha:
    print("Se rechaza la hipótesis nula")
else:
    print("No se rechaza la hipótesis nula")

#EJERCICIO 3
print("\nEjercicio 3 - Carreras: ")

observadas = np.array([200, 120, 80])

p = np.array([0.40, 0.35, 0.25])
n = observadas.sum()
esperadas = n * p

res = stats.chisquare(f_obs=observadas, f_exp=esperadas)

chi2 = res.statistic
p_value = res.pvalue
gl = len(observadas) - 1

print(f"Observadas: {observadas}")
print(f"Esperadas: {esperadas}")
print(f"Chi2: {chi2:.4f}")
print(f"Grados de libertad: {gl}")
print(f"p-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Se rechaza la hipótesis nula")
else:
    print("No se rechaza la hipótesis nula")


