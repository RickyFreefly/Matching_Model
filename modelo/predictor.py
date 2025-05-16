import joblib
import os
from modelo.features import preparar_features

# Cargar el modelo
modelo_path = os.path.join(os.path.dirname(__file__), "modelo_entrenado.pkl")
modelo = joblib.load(modelo_path)

# Función para predecir match a partir de datos
def predecir_match(datos):
    features = preparar_features(datos)
    pred = modelo.predict([features])[0]
    return pred
