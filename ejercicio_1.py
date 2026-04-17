def analizar_rutas(aerolineas_rutas):
    """
    Analiza las rutas de diferentes aerolíneas para identificar
    posibles alianzas estratégicas.

    Args:
        aerolineas_rutas: Diccionario donde las claves son nombres de aerolíneas
                         y los valores son sets de rutas (origen-destino)

    Returns:
        Diccionario con análisis de superposición de rutas y recomendaciones
    """
    resultado = {}
    nombres = list(aerolineas_rutas.keys())

    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            aerolinea1 = nombres[i]
            aerolinea2 = nombres[j]

            rutas1 = aerolineas_rutas[aerolinea1]
            rutas2 = aerolineas_rutas[aerolinea2]

            comunes = rutas1.intersection(rutas2)
            total_unico = rutas1.union(rutas2)

            porcentaje_superposicion = (len(comunes) / len(total_unico)) * 100

            if porcentaje_superposicion >= 40:
                recomendacion = "Alta posibilidad de alianza"
            elif porcentaje_superposicion >= 20:
                recomendacion = "Posible alianza moderada"
            else:
                recomendacion = "Baja posibilidad de alianza"

            clave = aerolinea1 + " - " + aerolinea2
            resultado[clave] = {
                "rutas_comunes": comunes,
                "cantidad_rutas_comunes": len(comunes),
                "porcentaje_superposicion": round(porcentaje_superposicion, 2),
                "recomendacion": recomendacion
            }

    return resultado


# Datos de prueba
rutas = {
    "Aerolínea A": {"LAX-JFK", "LAX-ORD", "ORD-JFK", "JFK-LHR", "LAX-NRT", "JFK-CDG"},
    "Aerolínea B": {"LAX-ORD", "ORD-JFK", "JFK-FRA", "FRA-CDG", "LAX-SYD", "SYD-NRT"},
    "Aerolínea C": {"MEX-LAX", "MEX-JFK", "MEX-BOG", "BOG-GRU", "MEX-MAD", "MAD-CDG"}
}

analisis = analizar_rutas(rutas)

for par, info in analisis.items():
    print("\nComparación:", par)
    print("Rutas comunes:", info["rutas_comunes"])
    print("Cantidad de rutas comunes:", info["cantidad_rutas_comunes"])
    print("Porcentaje de superposición:", info["porcentaje_superposicion"], "%")
    print("Recomendación:", info["recomendacion"])
