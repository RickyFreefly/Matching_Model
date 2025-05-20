from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import joblib

from modelo.predictor import predecir_match
from modelo.predictor_remitente import predecir_match_remitente

app = FastAPI()

# 🧾 Entrada para predict individual (viajero → encomienda)
class DatosEntrada(BaseModel):
    origen_match: int
    destino_match: int
    dias_diferencia: int
    valor_encomienda: float
    reputacion_viajero: float

# 🧾 Modelo de viaje (para emparejamiento remitente → viajes)
class Viaje(BaseModel):
    _id: str
    uid: str
    ciudadOrigen: str
    ciudadDestino: str
    fechaViaje: str
    capacidadDisponible: float
    reputacion: float

# 🧾 Entrada para predict-remitente (encomienda → viajes)
class InputRemitente(BaseModel):
    ciudadOrigen: str
    ciudadDestino: str
    fechaEncomienda: str
    valorEncomienda: float
    viajes: List[Viaje]

# 🔘 Bienvenida
@app.get("/")
def root():
    return {"mensaje": "¡Bienvenido al motor de emparejamiento Lapticon!"}

# 🧠 Modelo predict tradicional (viajero → encomienda)
modelo = joblib.load("modelo/modelo_entrenado.pkl")

@app.post("/predict")
def predict(datos: DatosEntrada):
    resultado = predecir_match(datos)
    return {"match": int(resultado)}

# 🤖 Modelo predict-remitente (encomienda → viajes)
@app.post("/predict-remitente")
def predict_remitente_endpoint(data: InputRemitente):
    if not data.viajes:
        raise HTTPException(status_code=422, detail="La lista de viajes está vacía.")

    encomienda = {
        "ciudadOrigen": data.ciudadOrigen,
        "ciudadDestino": data.ciudadDestino,
        "fechaEncomienda": data.fechaEncomienda,
        "valorEncomienda": data.valorEncomienda,
    }

    viajes_dict = [v.dict() for v in data.viajes]
    return predecir_match_remitente(encomienda, viajes_dict)
