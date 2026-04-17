def analizar_compatibilidad(componentes_por_modelo):
    """
    Analiza la compatibilidad de componentes entre modelos de aeronaves.

    Args:
        componentes_por_modelo: Diccionario donde las claves son modelos
                              y los valores son sets de componentes

    Returns:
        Diccionario con información de compatibilidad entre modelos
    """
    resultado = {}
    modelos = list(componentes_por_modelo.keys())

    for i in range(len(modelos)):
        for j in range(i + 1, len(modelos)):
            modelo1 = modelos[i]
            modelo2 = modelos[j]

            comp1 = componentes_por_modelo[modelo1]
            comp2 = componentes_por_modelo[modelo2]

            comunes = comp1.intersection(comp2)
            total = comp1.union(comp2)

            porcentaje = (len(comunes) / len(total)) * 100

            if porcentaje >= 70:
                conclusion = "Alta compatibilidad"
            elif porcentaje >= 40:
                conclusion = "Compatibilidad media"
            else:
                conclusion = "Baja compatibilidad"

            clave = modelo1 + " - " + modelo2
            resultado[clave] = {
                "componentes_comunes": comunes,
                "cantidad_comunes": len(comunes),
                "porcentaje_compatibilidad": round(porcentaje, 2),
                "conclusion": conclusion
            }

    return resultado


# Datos de prueba
componentes = {
    "B737-800": {"motor-CFM56", "apu-131-9B", "radar-WXR-2100", "fms-Pegasus", "transponder-Mode-S"},
    "B737-MAX": {"motor-LEAP-1B", "apu-131-9B", "radar-WXR-2100", "fms-Pegasus", "transponder-Mode-S"},
    "A320": {"motor-CFM56", "apu-APS3200", "radar-RDR-4000", "fms-Thales", "transponder-Mode-S"},
    "A320neo": {"motor-PW1100G", "apu-APS3200", "radar-RDR-4000", "fms-Thales", "transponder-Mode-S"}
}

compatibilidad = analizar_compatibilidad(componentes)

for par, info in compatibilidad.items():
    print("\nComparación:", par)
    print("Componentes comunes:", info["componentes_comunes"])
    print("Cantidad comunes:", info["cantidad_comunes"])
    print("Porcentaje de compatibilidad:", info["porcentaje_compatibilidad"], "%")
    print("Conclusión:", info["conclusion"])
