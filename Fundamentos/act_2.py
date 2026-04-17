"""**Implicaciones en el paso de argumentos**

La mutabilidad afecta cómo se comportan los objetos cuando se pasan como argumentos a funciones.

> Realiza el siguiente ejercicio y explica (en tu bitácora) tu respuesta a la pregunta:
> 

❓**¿Cómo afecta la mutabilidad a los objetos que se usan como argumentos de una función?**"""


def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada

"""En este ejercicio se observa que la lista combustible_actual es un objeto mutable. Al pasarla como argumento a la función agregar_combustible, la función trabaja sobre la misma lista original y le agrega un nuevo valor con append(). Por esta razón, al imprimir la lista fuera de la función, aparece también modificada. 
Esto demuestra que la mutabilidad permite que los cambios hechos dentro de una función afecten directamente al objeto original que se pasó como argumento."""