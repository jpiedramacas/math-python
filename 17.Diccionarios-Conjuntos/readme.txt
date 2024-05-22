### Enunciado:

Desarrolla un programa en Python que haga uso de diccionarios y conjuntos para almacenar y manipular datos de manera eficiente.

### Explicación:

En Python, los diccionarios y los conjuntos son estructuras de datos muy útiles para almacenar y manipular datos de manera eficiente. Aquí está la explicación de cómo se utilizan en el programa propuesto:

1. **Diccionarios**:
   - Un diccionario es una colección de pares clave-valor, donde cada clave está asociada a un valor. En este programa, el diccionario se utiliza para almacenar los nombres de los estudiantes como claves y sus calificaciones como valores. Por ejemplo:
     ```python
     estudiantes = {
         "Juan": 85,
         "María": 90,
         "Pedro": 75,
         "Ana": 95,
         "Luis": 80
     }
     ```
   - Los diccionarios son eficientes para realizar búsquedas rápidas de valores utilizando claves, lo que los hace ideales para situaciones donde necesitas asociar datos relacionados.

2. **Conjuntos**:
   - Un conjunto es una colección desordenada de elementos únicos. En este programa, se crea un conjunto de calificaciones únicas a partir de los valores del diccionario de estudiantes. Por ejemplo:
     ```python
     calificaciones = set(estudiantes.values())
     ```
   - Los conjuntos son útiles para eliminar duplicados y realizar operaciones de conjunto eficientes, como unión, intersección y diferencia.

En resumen, el programa utiliza un diccionario para almacenar datos asociados y un conjunto para manejar datos únicos, mostrando cómo estas estructuras de datos pueden ser utilizadas de manera eficiente en Python.
