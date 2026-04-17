componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

print(componentes [0:5])

#lista vacía con 10 datos iguales
lista1 = []

for i in range (1, 11):
    lista1.append("Hola")

print (lista1)

#Llenar lista con 3 datos diferentes ingresados por el teclado 
lista2 = []

for i in range (1, 4):
    dato = input("Ingrese un dato ")
    lista2.append(dato)

print(lista2)



# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

#Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T={t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")

#