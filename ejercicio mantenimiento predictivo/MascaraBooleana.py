# Estructura general de una máscara booleana
# # Siempre hay dos elementos clave:
# # # 1. Un conjunto de datos base (por ejemplo, una columna de un DataFrame).
# # # 2. Una condición o comparación aplicada sobre ese conjunto.
# # El resultado de esa comparación es una serie booleana del mismo largo,
# donde cada valor indica si la condición se cumple (True) o no (False).

# Pandas soporta todas las comparaciones lógicas típicas:
#
# Operador	Significado	        Ejemplo
#   ==	    igual a	            df["Estado"] == "On"
#   !=	    distinto de	        df["Estado"] != "Off"
#   >	        mayor que	    df["Voltaje"] > 220
#   <	        menor que	    df["Temperatura"] < 30
#   >=	    mayor o igual	    df["Humedad"] >= 60
#   <=	    menor o igual	    df["Potencia"] <= 100
#
# Y además funciones lógicas:
# #     .isna() → True si es nulo
# #     .notna() → True si tiene valor
# #     .str.contains("error") → True si contiene cierta palabra
# #     .between(10, 20) → True si el valor está en el rango 10–20

#Ejemplos
import pandas as pd

# ejemplo 1-sin pandas #

Fila_Data=["peras","manzanas","guindas","peras","peras","bananas"]
MascaraBooleana=[True, False, False, True, True,False]

resultado = [f for f, m in zip(Fila_Data, MascaraBooleana) if m]
print(resultado)


# aplicando Pandas, debe haber un encabezado, por lo que el dataframe es distinto#

df = pd.DataFrame({
    "Fruta": ["peras","manzanas","guindas","peras","peras","bananas"]
})

mascara = df[df["Fruta"] == "peras"] #Comparacion vectorizada
print(mascara)

# En Python puro, tú fabricas la lista mascara = [True, False, True...].
# En pandas, la máscara se genera sola al hacer una comparación vectorizada:
