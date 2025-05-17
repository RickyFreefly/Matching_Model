# 🤖 Motor de Emparejamiento Inteligente - Lapticon

Este microservicio implementa un motor de emparejamiento con inteligencia artificial para conectar **remitentes con viajeros** y viceversa. Está desarrollado con **FastAPI** y utiliza un modelo de Machine Learning entrenado con `scikit-learn`.

---

## 🚀 Funcionalidades

- `/predict`: Emparejamiento tradicional (viajero → encomienda)
- `/predict-remitente`: Emparejamiento inverso (remitente → viajes)
- Modelo basado en criterios como ciudad origen/destino, reputación, fechas y pesos
- Preparado para consumo por servicios backend en Node.js o apps Flutter

---

## 🛠 Requisitos

- Python 3.8 o superior
- pip

Instala las dependencias:

```bash
pip install -r requirements.txt
