def preparar_features(datos):
    return [
        datos.origen_match,
        datos.destino_match,
        datos.dias_diferencia,
        datos.valor_encomienda,
        datos.reputacion_viajero,
     #   datos.peso_encomienda
    ]
