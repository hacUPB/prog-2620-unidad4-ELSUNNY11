def analizar_rendimiento(datos_vuelo, especificaciones):
    """
    Analiza el rendimiento de una aeronave comparando datos de vuelo
    con especificaciones del fabricante.

    Args:
        datos_vuelo: Dict con registros reales de operación
        especificaciones: Dict con valores óptimos según fabricante

    Returns:
        Dict con análisis y recomendaciones
    """
    analisis = {
        "consumo": {},
        "velocidades": {}
    }

    # Analizar consumo
    for fase in especificaciones["consumo_optimo"]:
        analisis["consumo"][fase] = {}

        for nivel in especificaciones["consumo_optimo"][fase]:
            consumo_optimo = especificaciones["consumo_optimo"][fase][nivel]
            consumo_real = datos_vuelo["consumo"][fase][nivel]

            diferencia = consumo_real - consumo_optimo
            porcentaje = (diferencia / consumo_optimo) * 100

            if consumo_real > consumo_optimo:
                recomendacion = "Reducir consumo en esta condición"
            elif consumo_real < consumo_optimo:
                recomendacion = "Consumo por debajo del óptimo"
            else:
                recomendacion = "Consumo dentro del valor óptimo"

            analisis["consumo"][fase][nivel] = {
                "optimo": consumo_optimo,
                "real": consumo_real,
                "diferencia": diferencia,
                "porcentaje_diferencia": round(porcentaje, 2),
                "recomendacion": recomendacion
            }

    # Analizar velocidades
    for fase in especificaciones["velocidades_optimas"]:
        analisis["velocidades"][fase] = {}

        for nivel in especificaciones["velocidades_optimas"][fase]:
            velocidad_optima = especificaciones["velocidades_optimas"][fase][nivel]
            velocidad_real = datos_vuelo["velocidades"][fase][nivel]

            diferencia = velocidad_real - velocidad_optima
            porcentaje = (diferencia / velocidad_optima) * 100

            if velocidad_real > velocidad_optima:
                recomendacion = "Reducir velocidad"
            elif velocidad_real < velocidad_optima:
                recomendacion = "Aumentar velocidad"
            else:
                recomendacion = "Velocidad óptima"

            analisis["velocidades"][fase][nivel] = {
                "optima": velocidad_optima,
                "real": velocidad_real,
                "diferencia": diferencia,
                "porcentaje_diferencia": round(porcentaje, 2),
                "recomendacion": recomendacion
            }

    return analisis


# Datos de prueba
especificaciones_b737 = {
    "consumo_optimo": {
        "crucero": {"FL290": 2200, "FL330": 2100, "FL370": 2050},
        "ascenso": {"inicial": 3100, "medio": 2800, "final": 2500},
        "descenso": {"inicial": 1800, "medio": 1500, "final": 1200}
    },
    "velocidades_optimas": {
        "crucero": {"FL290": 450, "FL330": 460, "FL370": 470},
        "ascenso": {"inicial": 290, "medio": 280, "final": 270},
        "descenso": {"inicial": 280, "medio": 270, "final": 250}
    }
}

datos_operacionales = {
    "vuelo_123": {
        "consumo": {
            "crucero": {"FL290": 2350, "FL330": 2150, "FL370": 2080},
            "ascenso": {"inicial": 3300, "medio": 2950, "final": 2600},
            "descenso": {"inicial": 1850, "medio": 1600, "final": 1300}
        },
        "velocidades": {
            "crucero": {"FL290": 440, "FL330": 455, "FL370": 465},
            "ascenso": {"inicial": 280, "medio": 270, "final": 260},
            "descenso": {"inicial": 290, "medio": 280, "final": 260}
        }
    }
}

analisis = analizar_rendimiento(datos_operacionales["vuelo_123"], especificaciones_b737)

print("\nAnálisis de rendimiento:")
for categoria, datos in analisis.items():
    print(f"\n{categoria.upper()}:")
    for subcategoria, valores in datos.items():
        print(f"\n{subcategoria.upper()}:")
        for nivel, resultado in valores.items():
            print(f"  {nivel}: {resultado}")
