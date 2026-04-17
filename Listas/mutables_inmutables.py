frase = "unuiversidad"
 
print(frase.upper)  ## upper es para que sea mayuscula
 
lista = [5,65,8,2,3,4,78,41,55]  ## la lista es mutable
print (lista)
lista.sort   ## sort organiza la lista
print(lista)
 
 
print(frase[0])   ## con el 0 muestra la primer caracter de la palbra universidad
print(lista[0])  ## con el 0 muestra el primer elemento de la lista
 
lista[0] = 999  ## cambia el primer objeto de la lista por el 999, porque la lista es mutable, por eso se puede cmabiar
 
 
## pero no puede cambiar los caracteres de la palabra unversidad porque es inmutable
 
 
# con ejemplos inmutables (strings) se le puede agregar mas texto con el mas (+)
modelo = "boeing 747"
modelo = modelo + "-800"
print(modelo)
print(id(modelo))   ## el id sirve para saber donde se guardo en la memoria ram
 
listas_2 = [hola 1,hola 2, hola 3]
listas_2.append("hola4")  ## la funcion append sirve para agregar objetos a la lista
 
 