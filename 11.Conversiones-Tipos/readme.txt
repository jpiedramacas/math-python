### Enunciado:

En los programas a veces es necesario convertir algún valor de un tipo a otro. Por ejemplo, si estás usando un valor numérico decimal y deseas solo su parte entera, puedes realizar una conversión. Escribe un programa en Python que demuestre varios ejemplos de conversiones de tipos comunes, tales como de entero a flotante, de flotante a entero, de cadena a entero, entre otros.

### Explicación:

En Python, es común tener que convertir valores entre diferentes tipos de datos para realizar ciertas operaciones o para satisfacer los requisitos de la entrada/salida de datos. Aquí se presentan varios ejemplos de cómo se pueden hacer estas conversiones usando funciones integradas de Python.

1. **Entero a flotante**:
   - Usamos la función `float()` para convertir un valor entero a un número de punto flotante.
   - Ejemplo: `float(10)` convierte el entero `10` al flotante `10.0`.

2. **Flotante a entero**:
   - Usamos la función `int()` para convertir un número de punto flotante a un entero. Esta conversión trunca la parte decimal.
   - Ejemplo: `int(10.75)` convierte el flotante `10.75` al entero `10`.

3. **Cadena a entero**:
   - Usamos la función `int()` para convertir una cadena que contiene un número entero a un tipo entero.
   - Ejemplo: `int("123")` convierte la cadena `"123"` al entero `123`.

4. **Cadena a flotante**:
   - Usamos la función `float()` para convertir una cadena que contiene un número de punto flotante a un tipo flotante.
   - Ejemplo: `float("123.45")` convierte la cadena `"123.45"` al flotante `123.45`.

5. **Entero a cadena**:
   - Usamos la función `str()` para convertir un entero a una cadena.
   - Ejemplo: `str(456)` convierte el entero `456` a la cadena `"456"`.

6. **Flotante a cadena**:
   - Usamos la función `str()` para convertir un número de punto flotante a una cadena.
   - Ejemplo: `str(789.01)` convierte el flotante `789.01` a la cadena `"789.01"`.

7. **Booleano a entero**:
   - Usamos la función `int()` para convertir un valor booleano a un entero (`True` se convierte en `1`, `False` se convierte en `0`).
   - Ejemplo: `int(True)` convierte el booleano `True` al entero `1`.

8. **Entero a booleano**:
   - Usamos la función `bool()` para convertir un entero a un valor booleano (`0` se convierte en `False`, cualquier otro entero se convierte en `True`).
   - Ejemplo: `bool(0)` convierte el entero `0` al booleano `False`.

9. **Lista a cadena**:
   - Usamos el método `''.join()` para convertir una lista de caracteres a una cadena.
   - Ejemplo: `''.join(['a', 'b', 'c'])` convierte la lista `['a', 'b', 'c']` a la cadena `"abc"`.

10. **Cadena a lista**:
    - Usamos la función `list()` para convertir una cadena a una lista de caracteres.
    - Ejemplo: `list("abc")` convierte la cadena `"abc"` a la lista `['a', 'b', 'c']`.

11. **Tupla a lista**:
    - Usamos la función `list()` para convertir una tupla a una lista.
    - Ejemplo: `list((1, 2, 3))` convierte la tupla `(1, 2, 3)` a la lista `[1, 2, 3]`.

12. **Lista a tupla**:
    - Usamos la función `tuple()` para convertir una lista a una tupla.
    - Ejemplo: `tuple([4, 5, 6])` convierte la lista `[4, 5, 6]` a la tupla `(4, 5, 6)`.

Estas conversiones son útiles en una variedad de contextos, como la manipulación de datos, el procesamiento de entradas de usuarios y la interoperabilidad entre diferentes componentes de un programa.
