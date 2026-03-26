#Ejemplo 1 - Un investigador quiere saber si el puntuaje promedio de los estudiantes en un examen
#es de 70 puntos

import numpy as np
from scipy import stats

scores = np.array([
    72, 68, 75, 70, 66, 74, 71, 69, 73, 67,
    70, 72, 65, 76, 68, 71, 69, 74, 70, 66,
    73, 67, 72, 68, 75, 69, 71, 70, 74, 66
])

mu0 = 70

res = stats.ttest_1samp(scores, mu0)

t_stats = res.statistic
p_value = res.pvalue

alpha = 0.05

print("t =", t_stats)
print("p-value: ", p_value)

if p_value < alpha:
    print("Rechazo H0")
else: 
    print("No rechazo H0")

#T-STUDENT 
#Actividad 1

tiempos = np.array([
    47, 44, 46, 45, 43,
    48, 46, 44, 47, 45,
    46, 43, 44, 48, 47,
    45, 46, 44, 43, 47,
    46, 45, 44, 48, 47
])

mu0 = 45

res = stats.ttest_1samp(tiempos, mu0)

alpha = 0.05

print("t =", res.statistic)
print("p-value =", res.pvalue)

if res.pvalue < alpha:
    print("Rechazo H0")
else:
    print("No rechazo H0")

#Ejercicio 2

antes = np.array([220, 210, 230, 215, 225, 240, 235, 228, 222, 219,
                  231, 226, 234, 229, 223, 227, 232, 236, 221, 224])

despues = np.array([200, 195, 210, 205, 208, 220, 215, 210, 205, 202,
                    212, 207, 215, 209, 204, 206, 211, 218, 203, 205])

res = stats.ttest_rel(antes, despues)

t_stat = res.statistic
p_value = res.pvalue

p_value_one_tailed = p_value / 2

alpha = 0.05

print("t =", t_stat)
print("p-value (una cola) =", p_value_one_tailed)

if p_value_one_tailed < alpha and t_stat > 0:
    print("Rechazo H0: hubo reducción significativa")
else:
    print("No hay evidencia suficiente de reducción")

#Ejercicio 3

cafe = np.array([495, 498, 502, 490, 497, 499, 501, 493, 496, 498, 492, 495, 500, 494, 496])

mu0 = 500

res = stats.ttest_1samp(cafe, mu0)

t_stat = res.statistic
p_value = res.pvalue

alpha = 0.05

print("t =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Se rechaza H0")
else:
    print("No se rechaza H0")