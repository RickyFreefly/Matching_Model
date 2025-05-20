import joblib
import os
from datetime import datetime
from modelo.features import preparar_features_remitente
from modelo.datos_remitente import DatosRemitenteViaje

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

modelo = joblib.load(os.path.join(BASE_DIR, "modelo_remitente.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler_remitente.pkl"))

def predecir_match_remitente(encomienda, viajes):
    X = []
    ids = []

    print("✅ Encomienda recibida:", encomienda)
    print("📦 Número de viajes recibidos:", len(viajes))

    for i, viaje in enumerate(viajes):
        try:
            print(f"🔹 Procesando viaje {i + 1}: {viaje}")
            datos = DatosRemitenteViaje(encomienda, viaje)
            features = preparar_features_remitente(datos)
            X.append(features)
            ids.append(viaje.get("_id", f"viaje_{i}"))
        except Exception as e:
            print(f"❌ Error al procesar viaje {i + 1}: {e}")
            continue  # salta viajes inválidos sin detener todo

    if not X:
        raise ValueError("❌ No se pudo procesar ningún viaje válido.")

    try:
        X_scaled = scaler.transform(X)
        predicciones = modelo.predict(X_scaled)
    except Exception as e:
        print("❌ Error durante escalado o predicción:", e)
        raise

    resultados = []
    for i, score in enumerate(predicciones):
        resultados.append({
            "viajeId": ids[i],
            "afinidad": round(float(score), 3),
            "ciudadOrigen": viajes[i]["ciudadOrigen"],
            "ciudadDestino": viajes[i]["ciudadDestino"],
            "fechaViaje": viajes[i]["fechaViaje"]
        })

    print("✅ Predicciones generadas:", resultados)
    return sorted(resultados, key=lambda x: -x["afinidad"])
