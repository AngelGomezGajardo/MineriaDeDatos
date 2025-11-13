import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

#lo siguiente es para mostrar la tabla completa y Pandas no se limite por ancho de consola a mostrar

pd.set_option("display.max_columns", None)   # muestra todas las columnas
pd.set_option("display.width", None)         # evita cortes por ancho de consola

df=pd.read_csv("sensor_maintenance_data.csv")
#print(f"encabezado 5 primeras lineas: \n{df.head()}")## Mostrar las primeras 5 filas
#print(f"\ninformacion general: \n{df.info()}")## Información general, el df.info() se imprime solo, no necesita
# estar dentro de un print, además python lee primero lo que esta dentro del {} antes de imprimir, para tener los
# datos por consiguiente, primero se imprime .info y luego imprime lo siguiente. lo correcto para imprimir y luego mostrar
# el resultado es lo siguiente:
#################################################
#print("\ninformacion general:\n")
#df.info()
##################################################


# Recuento de valores nulos por columna
#print("\n--- Valores nulos ---")
#print(df.isnull().sum())

# Filas duplicadas
duplicados = df.duplicated().sum()
#print(f"\nFilas duplicadas: {duplicados}")

# Estadísticas generales
#print("\n--- Estadísticas ---")
#print(df.describe(include='all'))

#resultado resumen
# [5 rows x 27 columns]
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 500 entries, 0 to 499
# Data columns (total 27 columns):

# hay 300 filas failure type como nulos, esto significa que hay 300 registros donde no hubieron fallas


## la idea ahora es trabajar con los otros 200 registros
## creo que aqui lo pense mal, hay algun motivo que haya provocado que no se registre la falla? por ejemplo que
## desactivado algun elemento de las columnas que genere que se guarde el tipo de falla?
# Filtrar las filas SIN tipo de falla
df_no_fail = df[df["Failure Type"].isna()]#isna filtra por columnas null o faltantes
#print(f"Total filas sin registro de falla: {len(df_no_fail)}\n") #contamos cuantas filas nulas existen
#print(df_no_fail.head(10))  # puedes aumentar el número si quieres ver más
#esto imprime el resumen y no las columnas completas, puedo hacer que filtre de acuerdo a las columnas de interes con
#lo siguiente:

cols_interes=[
    "Sensor_ID","Timestamp", "Voltage (V)", "Current (A)",
    "Temperature (°C)", "Vibration (m/s²)",
    "Operational Status", "Fault Status", "Predictive Maintenance Trigger"
]
#print("\n############################## \n  Datos con falta: null\n##############################\n",)
Nan_Filtro=df[df["Failure Type"].isna()]
#print(Nan_Filtro)
#print("\n############################## \n  Datos con falta \"Failure Type\"\n##############################\n",)
notna_Filtro=df[df["Failure Type"].notna()]
#print(notna_Filtro)

#vamos a comprobar si los no registrados fueron por algun motivo
# Comparar registros con y sin falla por estado operativo
print("-----------------------------------------------------------------------------")
print("--------registro con y sin falla por estado operativo------------------------")
print("-----------------------------------------------------------------------------")
print(df.groupby(df["Failure Type"].isna())["Operational Status"].value_counts())
print("-----------------------------------------------------------------------------")

# Revisar si hay 'Fault Detected' activado sin tipo de falla
#print("-----------------------------------------------------------------------------")
#print("-------------Revisar si hay 'Fault Detected' activado sin tipo de falla------")
#print("-----------------------------------------------------------------------------")
#print(df[(df["Failure Type"].isna()) & (df["Fault Detected"] == 1)].head())
#print("-----------------------------------------------------------------------------")
tmp = (df
       .assign(FailureTypeIsNa=df["Failure Type"].isna())
       .groupby(["FailureTypeIsNa", "Operational Status"])
       .size()
       .reset_index(name="count"))
print(tmp)
#print("-----------------------------------------------------------------------------")
#print("----Revisar si hay disparos de mantenimiento predictivo sin tipo de falla----")
## Revisar si hay disparos de mantenimiento predictivo sin tipo de falla
#print(df[(df["Failure Type"].isna()) & (df["Predictive Maintenance Trigger"] == 1)].head())

#creamos una columna will fail
# 1 → si hubo falla real (“Failure Type” tiene valor)
# 0 → si NO hubo falla (“Failure Type” es NaN)

df["Will_Fail"] = df["Failure Type"].notna().astype(int)
#print(df["Will_Fail"].value_counts())

#verificamos como se ve la etiqueta

#print(df[["Failure Type", "Will_Fail"]].head(10))

##########################################

# ANALISIS EXPLORATORIO EDA #

###########################################
# aqui empezamos con la mineria de datos

# “¿Qué variables se comportan distinto cuando hay falla vs cuando no?”
# # Para eso haremos:
# # # Distribución de temperatura en ambos casos (Ver cómo se comporta la temperatura cuando el equipo falla vs cuando no falla.)
# # # Distribución de vibración (Mismos análisis que la temperatura pero sobre vibración.)
# # # Comparación de medias (“Si las medias son muy distintas, esa variable es un predictor excelente.”, compara falladas y no fallas )
# # # Boxplots (Un gráfico que muestra: minimo, maximo mediana cuartiles, outliers, ender la dispersion y detectar valores atipicos)
# # # Correlaciones (Medir qué variables están relacionadas entre sí, y ver si alguna se relaciona con Will_Fail.)
# # # Exploración de estados operativos asociados a falla (Ver si las fallas ocurren más en: operacion, mantencion, idle, fault, etc, Ayuda a identificar contexto operacional de la falla.)
# # # Esto te da el mapa de qué señales son predictoras reales.

matplotlib.use("Qt5Agg")
# distribucion de temperatura (will_fail=0 vs 1)
#sns.histplot(data=df, x="Temperature (°C)", hue="Will_Fail", kde=True)
#plt.title("Distribución de Temperatura según Falla")
#plt.show()

print(df.groupby("Will_Fail")["Vibration (m/s²)"].value_counts())