import joblib
import os
from sklearn.preprocessing import MinMaxScaler
from modelo.features import preparar_features_remitente
from modelo.datos_remitente import DatosRemitenteViaje

# Cargar modelo entrenado (puede ser el mismo que usas para el viajero)
modelo_path = os.path.join(os.path.dirname(__file__), "modelo_remitente.pkl")
modelo_remitente = joblib.load(modelo_path)

# Función para predecir afinidad de una encomienda respecto a múltiples viajes
def predecir_match_remitente(encomienda, viajes):
    X = []
    ids = []

    for viaje in viajes:
        datos = DatosRemitenteViaje(encomienda, viaje)
        features = preparar_features_remitente(datos)
        X.append(features)
        ids.append(viaje.get("_id", ""))

    # Escalado normalizado
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Predicción de afinidad
    predicciones = modelo_remitente.predict(X_scaled)

    # Ensamblar resultados
    resultados = []
    for i, score in enumerate(predicciones):
        resultados.append({
            "viajeId": ids[i],
            "afinidad": round(float(score), 3),
            "ciudadOrigen": viajes[i]["ciudadOrigen"],
            "ciudadDestino": viajes[i]["ciudadDestino"],
            "fechaViaje": viajes[i]["fechaViaje"],
            "reputacion": viajes[i]["reputacion"]
        })

    # Ordenar por mayor afinidad
    return sorted(resultados, key=lambda x: -x["afinidad"])
