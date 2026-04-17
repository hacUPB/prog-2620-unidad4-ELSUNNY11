def simular_costos(rutas, aeronaves, precios_combustible, tarifas_aeroportuarias):
    """
    Simula los costos operativos de diferentes combinaciones de rutas y aeronaves.

    Args:
        rutas: Dict con información de rutas (distancia, tiempo estimado, origen, destino)
        aeronaves: Dict con especificaciones de aeronaves
        precios_combustible: Dict con precios de combustible por aeropuerto
        tarifas_aeroportuarias: Dict con tarifas por aeropuerto

    Returns:
        Dict con análisis de costos por combinación ruta-aeronave
    """
    resultados = {}

    for nombre_ruta, info_ruta in rutas.items():
        origen = info_ruta["origen"]
        destino = info_ruta["destino"]
        tiempo = info_ruta["tiempo_estimado"]

        for nombre_aeronave, info_aeronave in aeronaves.items():
            capacidad = info_aeronave["capacidad_pax"]
            consumo = info_aeronave["consumo"]  # litros/hora
            costo_tripulacion = info_aeronave["costos_tripulacion"]

            # Precio combustible: aquí se toma el del aeropuerto de origen
            precio_comb = precios_combustible[origen]

            costo_combustible = consumo * tiempo * precio_comb
            costo_aeropuertos = tarifas_aeroportuarias[origen] + tarifas_aeroportuarias[destino]
            costo_total = costo_combustible + costo_tripulacion + costo_aeropuertos
            costo_por_pasajero = costo_total / capacidad

            clave = nombre_ruta + " - " + nombre_aeronave
            resultados[clave] = {
                "ruta": nombre_ruta,
                "aeronave": nombre_aeronave,
                "costo_combustible": round(costo_combustible, 2),
                "costo_tripulacion": round(costo_tripulacion, 2),
                "costo_aeropuertos": round(costo_aeropuertos, 2),
                "costo_total": round(costo_total, 2),
                "costo_por_pasajero": round(costo_por_pasajero, 2)
            }

    return resultados
