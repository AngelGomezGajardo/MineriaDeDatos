import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Data.csv")
print(df.head())

#############################################
# ANALISIS BASICO
#############################################
print("\n info: ")
df.info()

#Revisar estructuras basicas
print("Shape:", df.shape) #info de columnas y filas
print("\nColumnas:", df.columns.tolist()) #muestra encabezados como filas en una lista

print("describe:")
print(df.describe())

#############################################
# GRAFICO EDA (analisis exploratorio de datos)
#############################################
subset = df.iloc[:2000]
plt.figure()
plt.title("mostrando de 0 a 2000 registros")
plt.xlabel("sample")
plt.ylabel("vibración DE")
plt.plot(subset["sample"],subset["vib_DE"]) #aqui se indican los datos a graficar
plt.tight_layout()
plt.show(block=False)

subset = df.iloc[:2000]
plt.figure()
plt.title("mostrando de 0 a 2000 registros")
plt.xlabel("sample")
plt.ylabel("vibración DE")
plt.plot(subset["sample"],subset["vib_FE"]) #aqui se indican los datos a graficar, plot es el tip de grafico que mostrara
plt.tight_layout()
plt.show(block=False)

subset = df.iloc[:2000]
plt.figure()
plt.title("mostrando de 0 a 2000 registros")
plt.xlabel("sample")
plt.ylabel("vibración DE")
plt.plot(subset["sample"],subset["RPM"]) #aqui se indican los datos a graficar
plt.tight_layout()#ajusta el grafico para que calce mas bonito
plt.show(block=True)