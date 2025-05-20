from datetime import datetime

class DatosRemitenteViaje:
    def __init__(self, encomienda, viaje):
        self.encomienda = encomienda
        self.viaje = viaje

        self.origen_match = int(encomienda["ciudadOrigen"] == viaje["ciudadOrigen"])
        self.destino_match = int(encomienda["ciudadDestino"] == viaje["ciudadDestino"])

        fecha_encomienda = datetime.fromisoformat(encomienda["fechaEncomienda"].replace("Z", ""))
        fecha_viaje = datetime.fromisoformat(viaje["fechaViaje"].replace("Z", ""))
        self.dias_diferencia = abs((fecha_viaje - fecha_encomienda).days)
