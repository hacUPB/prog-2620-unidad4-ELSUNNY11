import math
from itertools import permutations

def distancia(coord1, coord2):
    """
    Calcula una distancia aproximada entre dos puntos usando
    la fórmula de Haversine.
    """
    lat1, lon1 = math.radians(coord1[1]), math.radians(coord1[2])
    lat2, lon2 = math.radians(coord2[1]), math.radians(coord2[2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    radio_tierra = 6371  # km
    return radio_tierra * c


def costo_ruta(ruta, condiciones_clima, peso_clima=100):
    """
    Calcula el costo total de una ruta.
    costo = distancia total + penalización por clima
    """
    costo_total = 0

    for i in range(len(ruta) - 1):
        costo_total += distancia(ruta[i], ruta[i + 1])

    for punto in ruta[1:-1]:  # solo waypoints intermedios
        nombre = punto[0]
        riesgo = condiciones_clima.get(nombre, 0)
        costo_total += riesgo * peso_clima

    return costo_total


def optimizar_ruta(origen, destino, waypoints, condiciones_clima):
    """
    Determina la mejor ruta considerando distancia y clima.

    Args:
        origen: Tupla (nombre, latitud, longitud)
        destino: Tupla (nombre, latitud, longitud)
        waypoints: Lista de tuplas (nombre, latitud, longitud)
        condiciones_clima: Diccionario con claves = nombres de waypoints
                          valores = índice de riesgo climático (0-10)

    Returns:
        Lista de tuplas con la ruta óptima incluyendo origen y destino
    """
    mejor_ruta = None
    mejor_costo = float("inf")

    for orden in permutations(waypoints):
        ruta_actual = [origen] + list(orden) + [destino]
        costo_actual = costo_ruta(ruta_actual, condiciones_clima)

        if costo_actual < mejor_costo:
            mejor_costo = costo_actual
            mejor_ruta = ruta_actual

    return mejor_ruta


# Datos de prueba
origen = ("KLAX", 33.9425, -118.4081)  # Los Angeles
destino = ("KJFK", 40.6413, -73.7781)  # New York JFK
puntos_intermedios = [
    ("KDEN", 39.8561, -104.6737),  # Denver
    ("KORD", 41.9742, -87.9073),   # Chicago
    ("KCLE", 41.4075, -81.8511),   # Cleveland
    ("KBNA", 36.1245, -86.6782)    # Nashville
]
clima = {"KDEN": 2, "KORD": 8, "KCLE": 5, "KBNA": 3}

mejor_ruta = optimizar_ruta(origen, destino, puntos_intermedios, clima)

print("Ruta óptima:")
for punto in mejor_ruta:
    print(f"  {punto[0]} ({punto[1]}, {punto[2]})")
