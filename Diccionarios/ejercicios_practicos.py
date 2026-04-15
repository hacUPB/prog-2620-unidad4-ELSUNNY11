# Ejercicio 1
vuelo = {'aerolinea': 'Avianca', 'vuelo': 'AV123', 'origen': 'BOG', 'destino': 'MDE'}   

# Ejercicio 2
ciudad_llegada = vuelo['destino']
print(ciudad_llegada)

# Modiicación de un valor existente
vuelo['destino'] = 'CLO'
print(vuelo["destino"])

# Agregar un nuevo par clave-valor
vuelo['estado'] = 'En el aire'
print(vuelo["estado"])    

# Uso metodo .get   
nombre_piloto = vuelo.get('piloto', 'Piloto no asignado')
print(nombre_piloto)    

# Eliminar un dato   
del vuelo["vuelo"]  
print(vuelo)