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
        datos.origen_match,         # 1 si coincide ciudad origen
        datos.destino_match,        # 1 si coincide ciudad destino
        datos.dias_diferencia       # días de diferencia entre fechaEncomienda y fechaViaje
    ]