from random import randint

meses= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
lista= []

for i in range(12):
    dato = randint(20, 80)
    lista.append(dato)

print (lista)

mayor = max(lista)
veces = lista.count(mayor)
mes = lista.index(mayor)

if veces > 1:
    lista_meses= []
    for i in range(len(lista)):
        if lista[i] == mayor:
            lista_meses.append(i)
    print ("Ventas mayores en: ")
    for mes in lista_meses:
        print (f"Mayor venta en: {meses[mes]}")
