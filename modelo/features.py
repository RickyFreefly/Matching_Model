def preparar_features(datos):
    return [
        datos.origen_match,
        datos.destino_match,
        datos.dias_diferencia,
        datos.valor_encomienda,
        datos.reputacion_viajero,
     #   datos.peso_encomienda
    ]

def preparar_features_remitente(datos):
    return [
        datos.origen_match,
        datos.destino_match,
        datos.dias_diferencia,
        datos.valor_encomienda,
        datos.peso_encomienda,
        datos.capacidad_disponible,
        datos.reputacion_viajero
    ]