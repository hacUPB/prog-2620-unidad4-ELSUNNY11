def planificar_mantenimiento(aviones_mantenimiento, tecnicos_habilidades):
    """
    Asigna técnicos a tareas de mantenimiento de aeronaves basado en habilidades.

    Args:
        aviones_mantenimiento: Dict con claves = aeronaves, valores = sets de tareas
        tecnicos_habilidades: Dict con claves = técnicos, valores = sets de habilidades

    Returns:
        Dict con la asignación óptima de técnicos a aeronaves
    """
    asignacion = {}

    for avion, tareas in aviones_mantenimiento.items():
        mejor_tecnico = None
        mejor_coincidencia = set()

        for tecnico, habilidades in tecnicos_habilidades.items():
            tareas_que_puede_hacer = tareas.intersection(habilidades)

            if len(tareas_que_puede_hacer) > len(mejor_coincidencia):
                mejor_coincidencia = tareas_que_puede_hacer
                mejor_tecnico = tecnico

        asignacion[avion] = {
            "tecnico_asignado": mejor_tecnico,
            "tareas_cubiertas": mejor_coincidencia,
            "tareas_pendientes": tareas - mejor_coincidencia
        }

    return asignacion


# Datos de prueba
mantenimiento_requerido = {
    "N12345": {"inspeccion-motor", "revision-hidraulica", "calibracion-instrumentos"},
    "N67890": {"revision-electrica", "inspeccion-combustible", "prueba-presion"},
    "N54321": {"inspeccion-motor", "revision-tren", "calibracion-instrumentos"},
    "N09876": {"revision-electrica", "revision-oxigeno", "actualizacion-software"}
}

habilidades_tecnicas = {
    "Técnico 1": {"inspeccion-motor", "revision-hidraulica", "revision-tren"},
    "Técnico 2": {"revision-electrica", "calibracion-instrumentos", "actualizacion-software"},
    "Técnico 3": {"inspeccion-combustible", "prueba-presion", "revision-oxigeno"},
    "Técnico 4": {"calibracion-instrumentos", "actualizacion-software", "inspeccion-motor"}
}

plan = planificar_mantenimiento(mantenimiento_requerido, habilidades_tecnicas)

for avion, info in plan.items():
    print("\nAeronave:", avion)
    print("Técnico asignado:", info["tecnico_asignado"])
    print("Tareas cubiertas:", info["tareas_cubiertas"])
    print("Tareas pendientes:", info["tareas_pendientes"])
