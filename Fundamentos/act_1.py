# Creamos un objeto (en este caso, un número)
altitud = 10000  # metros

# 'altitud' es una etiqueta que apunta al objeto entero 10000
# Creamos otra variable que apunta al mismo valor
elevacion = altitud

# Cambiamos el valor de 'elevacion'
elevacion = 9500

# Mostramos los valores
print("Altitud:", altitud)
print("Elevación:", elevacion)

# Conclusión
print("\nConclusión:")
print("Al cambiar 'elevacion', la variable 'altitud' no cambia.")
print("Esto demuestra que reasignar una variable no modifica la otra.") 
"""altitud y elevacion inicialmente tienen el mismo valor.
Cuando elevacion cambia a 9500, altitud sigue en 10000.
Esto pasa porque en Python una variable puede reasignarse sin afectar a la otra."""