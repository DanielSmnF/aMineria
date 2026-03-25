import numpy as np
import pandas as pd
from scipy import stats

#Datos de los 3 problemas
datos = {
    "Problema": ["Uno", "Dos", "Tres"],
    "mu": [10, 20, 1000],
    "n": [49, 30, 40],
    "x_bar": [9.7, 18.5, 990],
    "desv": [0.5, 2.5, 12],
    "alpha": [0.01, 0.05, 0.02]
}

df = pd.DataFrame(datos)

#Calculo estadistico 
df["z_calculado"] = (df["x_bar"] - df["mu"]) / (df["desv"] / np.sqrt(df["n"]))

#Valor critico
df["z_critico"] = df["alpha"].apply(lambda a: stats.norm.ppf(a))

#Hipotesis
df["Decision"] = df.apply(
    lambda row: "Rechazar Hipotesis" if row["z_calculado"] < row["z_critico"] else "No rechazar Hipotesis",
    axis=1
)

df["z_calculado"] = df["z_calculado"].round(4)
df["z_critico"] = df["z_critico"].round(4)

print(df)
