### Enunciado:

Desarrolla un programa en Python que trabaje con arrays, realizando operaciones como creación, acceso a elementos, modificación y recorrido. Además, incluye ejemplos de cómo añadir y eliminar elementos, obtener la longitud de un array, realizar slicing, concatenar arrays, invertir un array y buscar elementos específicos.

### Explicación:

En Python, los arrays (o arreglos) son estructuras de datos que permiten almacenar múltiples elementos del mismo tipo. Aunque las listas de Python son más flexibles y comunes, el módulo `array` proporciona una implementación de arrays más eficiente en términos de memoria y rendimiento para datos homogéneos.

A continuación, se presenta un programa que demuestra diversas operaciones con arrays:

1. **Importar el Módulo `array`**:
   - `import array as arr` se utiliza para trabajar con arrays más eficientes que las listas estándar de Python, especialmente cuando se manejan grandes cantidades de datos homogéneos.

2. **Creación de Arrays**:
   - `array_enteros` se crea como un array de enteros usando el tipo `'i'`.
   - `array_floats` se crea como un array de flotantes usando el tipo `'f'`.

3. **Acceso a Elementos**:
   - Se accede a elementos específicos del array usando índices. Por ejemplo, `array_enteros[0]` para el primer elemento y `array_floats[-1]` para el último elemento.

4. **Modificación de Elementos**:
   - Los elementos de un array se pueden modificar directamente usando sus índices. Por ejemplo, `array_enteros[1] = 20` cambia el segundo elemento a 20.

5. **Recorrido de un Array**:
   - Se pueden recorrer y procesar todos los elementos de un array usando un bucle `for`.

6. **Añadir Elementos**:
   - Se pueden añadir nuevos elementos al final de un array usando el método `append`.

7. **Eliminar Elementos**:
   - Se pueden eliminar elementos específicos de un array usando el método `remove`.

8. **Obtener la Longitud de un Array**:
   - La longitud de un array, es decir, el número de elementos que contiene, se puede obtener con la función `len`.

9. **Slicing de un Array**:
   - Se pueden obtener sub-arrays (sub-secciones) usando slicing, por ejemplo, `array_enteros[1:3]`.

10. **Concatenación de Arrays**:
    - Dos arrays se pueden concatenar usando el operador `+`.

11. **Inversión de un Array**:
    - Un array se puede invertir usando slicing, por ejemplo, `array_concatenado[::-1]`.

12. **Búsqueda de Elementos**:
    - Se puede buscar el índice de un elemento específico en un array usando el método `index`.

Este programa cubre la creación de arrays, acceso y modificación de elementos, recorrido, adición y eliminación de elementos, obtención de longitud, slicing, concatenación, inversión y búsqueda de elementos. Estos ejemplos muestran cómo trabajar con arrays en Python de manera eficiente utilizando el módulo `array`.
