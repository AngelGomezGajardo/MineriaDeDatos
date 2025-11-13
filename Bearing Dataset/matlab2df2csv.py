#install pip install scipy
import pandas as pd
from scipy.io import loadmat
import numpy as np

data=loadmat("100.mat")

#revisamos que hay en el archivo,
#print(data.keys())
#print(data.values())

#con shape mostramos la forma
#en general cuando hacemos .algo <- sin parentesis, es para mostrar tu forma, un atributo
# cuando hacemos .algo() <- estamos llamando a una funcion que actua sobre lo que esta antes del punto.
print(data["X100_DE_time"].shape)     # OK
print(data["X100_FE_time"].shape)     # OK
print(data["X100RPM"].shape)

#convertimos ahora a flat para trabajar con dataframes
# al ser archivos que vienen de matlab, necesitamos nosotros generar la tabla de datos con columnas y filas
# por eso es que se convierte a flatten y despues armamos el datafame, #pandas no tiene lectura nativa de matlab
DE = data["X100_DE_time"].flatten()
FE = data["X100_FE_time"].flatten()
RPM = data["X100RPM"].flatten()
print(RPM)
#conocemos el largo de DE
n=len(DE)

#generamos el dataframe df
#lo que sigue es pandas: lo que hace es tomar el vector y ponerlo como columna, para el valor unitario RPM hace un
# broadcasting, replica lo mismo en todas las columnas
df = pd.DataFrame({
    "sample": np.arange(n),
    "vib_DE": DE,
    "vib_FE": FE,
    "RPM"   : RPM[0],
})
print(df)
df.to_csv('Data.csv')

