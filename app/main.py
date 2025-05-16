from fastapi import FastAPI
from pydantic import BaseModel
from modelo.predictor import predecir_match
import joblib

app = FastAPI()

class DatosEntrada(BaseModel):
    origen_match: int
    destino_match: int
    dias_diferencia: int
    valor_encomienda: float
    reputacion_viajero: float
 #   peso_encomienda: float

@app.get("/")
def root():
    return {"mensaje": "¡Bienvenido al motor de emparejamiento Lapticon!"}

modelo = joblib.load("modelo/modelo_entrenado.pkl")

@app.post("/predict")
def predict(datos: DatosEntrada):
    resultado = predecir_match(datos)
    return {"match": int(resultado)}

