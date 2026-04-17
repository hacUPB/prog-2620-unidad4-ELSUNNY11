# 📝 Plantilla de Autoevaluación: Gestión de Mantenimiento de Flota Aeronáutica ✈️

**Instrucciones para los estudiantes:**
1. Hagan una copia de este archivo y guárdenlo en la raíz de su repositorio con el nombre `AUTOEVALUACION.md`.
2. Lean cuidadosamente cada criterio de la rúbrica.
3. En el apartado **Nota Esperada**, asignen una calificación numérica (de 0.0 a 5.0) que consideren justa para su trabajo en ese criterio.
4. En el apartado **Justificación**, expliquen con sus propias palabras por qué merecen esa nota. Sean críticos y honestos.
5. En el apartado **Evidencia**, inserten pantallazos de la ejecución de la consola, imágenes de su diagrama o bloques de código (usando la sintaxis de Markdown con \`\`\`) que respalden su justificación.
6. Al final, calculen su nota definitiva esperada según los porcentajes.

---

## 👥 1. Información del Equipo

* **Miembro 1:** Santiago Marin Betancur - 557188
* **Miembro 2:** Nicolás Moreno Blandon - 270965

---

## 📊 2. Evaluación por Criterios

### Criterio 1: Diagrama y Lógica (Valor: 20%)
*Evalúa si el diagrama es claro, lógico y representa fielmente la estructura de datos utilizada (listas/diccionarios) y el flujo del programa.*

* **Nota Esperada (0.0 - 5.0):** 5
* **Justificación:** 
  > *[Consideramos que nuestro codigo si sigue fielmente el diagrama y la estructura, no hay nada que cambiamos]*
* **Evidencia:**
  *Inserta aquí la imagen de tu diagrama ![Diagrama de Flujo](/RETO/Diagrama%20bloques.jpeg) el codigo se conecta a partir de bucles while y for.*

### Criterio 2: Uso de Estructuras (Listas y Diccionarios) (Valor: 30%)
*Se utilizaron 2 listas y dentro de ellas diccionarios, todo bien estructurado y sin codigo de más*

* **Nota Esperada (0.0 - 5.0):** [4]
* **Justificación:**
  > *[Usamos una lista pricipal llamada "Flota" el cual dentro de ella hay un diccionario para cada avión, luego dentro de cada diccionario de avión creamos una lista llamada "componentes" ahí despues se crea un diccionario por componente]*
* **Evidencia:**
  *Pega aquí el fragmento de código exacto donde inicializas y llenas estas estructuras. Usa el formato de código de Markdown:*
  ```python
  # Reemplaza esto con tu fragmento de código real
  flota = {}
  # ... código de inserción de datos ...

### Criterio 3: Cumplimiento de Restricciones Técnicas (Valor: 20%)
*Evalúa el respeto total a las reglas: uso de ciclos clásicos (for/while), cero uso de list comprehensions, y ninguna librería/función avanzada no vista en clase.*

* **Nota Esperada (0.0 - 5.0):** [3.5]
* **Justificación:**
    > *En nuestro código solo utilizamos estructuras vistas en clase, como listas, diccionarios, condicionales, ciclos for y while, entradas con input() y conversiones básicas de datos. No usamos librerías externas, funciones avanzadas ni list comprehensions. Por eso consideramos que cumplimos completamente con las restricciones técnicas establecidas. 
* **Evidencia:** for _ in range(n_aeronaves):
    matricula = input("Matricula: ")
    modelo = input("Modelo: ")
    horas_vuelo = float(input("Horas de vuelo: "))

    componentes = []
    n_componentes = int(input("Numero de componentes: "))

    for _ in range(n_componentes):
        nombre = input("Componente: ")
        horas_uso = float(input("Horas de uso: "))
        limite = float(input("Limite de horas: "))*

### Criterio 4: Funcionalidad del Código (Valor: 15%)
*Evalúa si el programa pide datos correctamente, no se "crashea" y genera el reporte final de mantenimiento esperado.*

* **Nota Esperada (0.0 - 5.0):** [3.8]
* **Justificación:**
    > *El programa funciona correctamente porque solicita los datos de las aeronaves y de sus componentes sin cerrarse inesperadamente. Además, valida que se ingresen mínimo 3 aeronaves y genera un reporte final en el que se muestran únicamente los componentes que alcanzaron o superaron su límite de horas de uso.*
* **Evidencia:** *Inserta aquí 1 o 2 pantallazos (![Ejecución](/RETO/Captura%20de%20pantalla%202026-04-17%20001309.png)) mostrando la terminal donde se vea:*
*El ingreso manual de datos.*
*El reporte final impreso en pantalla con las piezas que requieren mantenimiento.*

### Criterio 5: Preparación para Sustentación (Valor: 15%)
*Aunque esta nota la dará el profesor en la entrevista oral, autoevalúen su nivel de preparación y comprensión del código que entregaron.*

* **Nivel de Confianza (Bajo / Medio / Alto):** [medio]
* **Justificación:**
    > *Tenemos una idea general de cómo funciona el código y sí entendemos varias partes, como el uso de listas, diccionarios, ciclos y el reporte final. Pero todavía hay partes que tendríamos que repasar un poco más para poder explicarlas con total seguridad en la sustentación.*
* **Evidencia de preparación: Revisamos el código entre los dos y fuimos mirando qué hacía cada parte para entenderlo mejor.**

### 📈 3. Cálculo de Nota Definitiva Esperada
Multipliquen la nota asignada en cada criterio por su porcentaje respectivo y sumen los resultados para obtener su nota final esperada.

|Criterio	|Nota |Asignada	|Peso	|Subtotal |(Nota * Peso) |
|---|---|---|---|---|---|
|1. Diagrama y Lógica	|5|20% |(0.2)	|1|
|2. Uso de Estructuras	|4|30% |(0.3)	|1.2|
|3. Cumplimiento Restricciones|3.5|20% |(0.2)	|0.7|
|4. Funcionalidad	|3.8|15% |(0.15)	|0.57|
|5. Sustentación (Estimado)|3|	15%| (0.15)|0.45|

NOTA FINAL ESPERADA		100%	[3.92]

✨ ""La educación es para el carácter, no solo para la mente"." ✨
