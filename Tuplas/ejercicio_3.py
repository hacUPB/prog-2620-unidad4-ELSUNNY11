def analizar_perfil_ala(datos_tunel):
    """
    Analiza datos de pruebas de túnel de viento para diferentes perfiles de ala.

    Args:
        datos_tunel: Lista de tuplas con formato:
            (nombre_perfil, coef_sustentacion, coef_resistencia, angulo_ataque)

    Returns:
        Diccionario con análisis de los perfiles
    """
    perfiles = {}

    # Agrupar datos por perfil
    for nombre, cl, cd, angulo in datos_tunel:
        if nombre not in perfiles:
            perfiles[nombre] = {
                "datos": [],
                "suma_cl": 0,
                "suma_cd": 0,
                "suma_eficiencia": 0
            }

        eficiencia = cl / cd

        perfiles[nombre]["datos"].append((cl, cd, angulo, eficiencia))
        perfiles[nombre]["suma_cl"] += cl
        perfiles[nombre]["suma_cd"] += cd
        perfiles[nombre]["suma_eficiencia"] += eficiencia

    analisis = {}
    mejor_perfil = None
    mejor_eficiencia = 0

    # Analizar cada perfil
    for nombre, info in perfiles.items():
        cantidad = len(info["datos"])

        promedio_cl = info["suma_cl"] / cantidad
        promedio_cd = info["suma_cd"] / cantidad
        promedio_eficiencia = info["suma_eficiencia"] / cantidad

        # Buscar el mejor ángulo de ataque según mayor eficiencia
        mejor_dato = info["datos"][0]
        for dato in info["datos"]:
            if dato[3] > mejor_dato[3]:
                mejor_dato = dato

        mejor_angulo = mejor_dato[2]

        analisis[nombre] = {
            "promedio_cl": round(promedio_cl, 3),
            "promedio_cd": round(promedio_cd, 3),
            "eficiencia_promedio": round(promedio_eficiencia, 3),
            "mejor_angulo_ataque": mejor_angulo
        }

        if promedio_eficiencia > mejor_eficiencia:
            mejor_eficiencia = promedio_eficiencia
            mejor_perfil = nombre

    analisis["mejor_perfil"] = mejor_perfil

    return analisis


# Datos de prueba
datos_prueba = [
    ("NACA2412", 0.25, 0.021, 0),
    ("NACA2412", 0.45, 0.028, 2),
    ("NACA2412", 0.85, 0.036, 5),
    ("NACA4415", 0.32, 0.022, 0),
    ("NACA4415", 0.52, 0.029, 2),
    ("NACA4415", 0.95, 0.041, 5),
    ("NACA6412", 0.36, 0.028, 0),
    ("NACA6412", 0.62, 0.039, 2),
    ("NACA6412", 1.05, 0.065, 5)
]

analisis = analizar_perfil_ala(datos_prueba)
print(analisis)
