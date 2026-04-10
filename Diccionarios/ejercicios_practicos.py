# Ejercicio 1
vuelo = {'aerolinea': 'Avianca', 'vuelo': 'AV123', 'origen': 'BOG', 'destino': 'MDE'}   

# Ejercicio 2
ciudad_llegada = vuelo['destino']
print(ciudad_llegada)

# Ejercicio 3
vuelo['destino'] = 'CLO'
print(vuelo["destino"])

# Ejercicio 4
vuelo['estado'] = 'En el aire'
print(vuelo["estado"])    

# Ejercicio 5   
nombre_piloto = vuelo.get('piloto', 'Piloto no asignado')
print(nombre_piloto)    

# Ejercicio 6   
del vuelo["vuelo"]  
print(vuelo)