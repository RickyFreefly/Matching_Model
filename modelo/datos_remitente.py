# app/modelo/datos_remitente.py

class DatosRemitenteViaje:
    def __init__(self, encomienda, viaje):
        self.origen_match = int(encomienda["ciudadOrigen"].lower() == viaje["ciudadOrigen"].lower())
        self.destino_match = int(encomienda["ciudadDestino"].lower() == viaje["ciudadDestino"].lower())

        self.valor_encomienda = encomienda["valorEncomienda"]
        self.peso_encomienda = encomienda["pesoEncomienda"]

        self.capacidad_disponible = viaje["capacidadDisponible"]
        self.reputacion_viajero = viaje["reputacion"]

        self.dias_diferencia = self._calcular_dias_diferencia(encomienda["fechaEncomienda"], viaje["fechaViaje"])

    def _calcular_dias_diferencia(self, fecha_encomienda_str, fecha_viaje_str):
        from datetime import datetime
        fecha_encomienda = datetime.strptime(fecha_encomienda_str, "%Y-%m-%d")
        fecha_viaje = datetime.strptime(fecha_viaje_str, "%Y-%m-%dT%H:%M:%SZ")
        return abs((fecha_viaje - fecha_encomienda).days)
