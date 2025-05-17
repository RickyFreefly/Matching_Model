from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

from modelo.predictor import predecir_match
from modelo.predictor_remitente import predecir_match_remitente

app = FastAPI()

# Entrada simple para predict individual
class DatosEntrada(BaseModel):
    origen_match: int
    destino_match: int
    dias_diferencia: int
    valor_encomienda: float
    reputacion_viajero: float

# Entrada para predict-remitente (emparejamiento múltiple)
class Viaje(BaseModel):
    _id: str
    uid: str
    ciudadOrigen: str
    ciudadDestino: str
    fechaViaje: str
    capacidadDisponible: float
    reputacion: float

class InputRemitente(BaseModel):
    ciudadOrigen: str
    ciudadDestino: str
    fechaEncomienda: str
    valorEncomienda: float
    pesoEncomienda: float
    viajes: List[Viaje]

# Endpoint raíz
@app.get("/")
def root():
    return {"mensaje": "¡Bienvenido al motor de emparejamiento Lapticon!"}

# Carga del modelo
modelo = joblib.load("modelo/modelo_entrenado.pkl")

@app.post("/predict")
def predict(datos: DatosEntrada):
    resultado = predecir_match(datos)
    return {"match": int(resultado)}

@app.post("/predict-remitente")
def predict_remitente_endpoint(data: InputRemitente):
    encomienda = {
        "ciudadOrigen": data.ciudadOrigen,
        "ciudadDestino": data.ciudadDestino,
        "fechaEncomienda": data.fechaEncomienda,
        "valorEncomienda": data.valorEncomienda,
        "pesoEncomienda": data.pesoEncomienda
    }
    viajes_dict = [v.dict() for v in data.viajes]
    return predecir_match_remitente(encomienda, viajes_dict)
