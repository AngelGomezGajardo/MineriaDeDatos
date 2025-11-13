#   el pipeline es el siguiente:
#   recoleccion y limpieza de datos
#   analisis exploratorio (EDA)
#   preperacion de datos
#   modelo (machine learning)
#   evaluacion del modelo
#   optimizacion y validación
#   despliegue o interpretacion de resultados

import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Dataset público incluido en Seaborn
df = sns.load_dataset('titanic')
print(df.head())

# Eliminar columnas irrelevantes
df = df.drop(['deck', 'embark_town', 'alive', 'class', 'who', 'adult_male'], axis=1)

# Eliminar filas con datos nulos
df = df.dropna()

# Convertir variables categóricas a numéricas
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['embarked'] = df['embarked'].map({'C': 0, 'Q': 1, 'S': 2})

print(df.head())

#separamos variables y objetivo
X = df.drop('survived', axis=1)
y = df['survived']

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, y_pred))
print('\nReporte de Clasificación:\n', classification_report(y_test, y_pred))

importances = pd.Series(model.feature_importances_, index=X.columns)
