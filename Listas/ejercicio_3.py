import random

lista=[]
indice = 201

for i in range (10):
    x = (random.randint(100,200))
    lista.append(x)
    if indice > x:
        indice = x


print (lista)
print(f"el número menor de la lista es {indice}")