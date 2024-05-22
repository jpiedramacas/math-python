### Enunciado:

Crea un programa en Python que maneje excepciones utilizando bloques `try`, `except`, y `finally`. Incluye ejemplos de lanzamiento y captura de excepciones para demostrar cómo se pueden manejar errores comunes y cómo lanzar excepciones personalizadas.

### Explicación:

En Python, el manejo de errores y excepciones es crucial para crear programas robustos y confiables. Los bloques `try`, `except`, y `finally` se utilizan para capturar y manejar excepciones, permitiendo que el programa responda adecuadamente a situaciones inesperadas sin fallar abruptamente. Además, podemos lanzar nuestras propias excepciones personalizadas usando la instrucción `raise`. 

El programa a continuación muestra ejemplos prácticos de cómo manejar y lanzar excepciones en Python.

### Descripción del Código:

1. **Función `dividir`**:
   - **try**: En este bloque, intentamos realizar la división. Si la operación tiene éxito, pasa al bloque `else`.
   - **except ZeroDivisionError**: Este bloque captura la excepción cuando se intenta dividir por cero. Se imprime un mensaje de error y se asigna `None` al resultado.
   - **except TypeError**: Este bloque captura la excepción cuando los tipos de datos proporcionados no son compatibles para la división (por ejemplo, un número y una cadena). Se imprime un mensaje de error y se asigna `None` al resultado.
   - **else**: Este bloque se ejecuta solo si no se produce ninguna excepción en el bloque `try`, indicando que la división fue exitosa.
   - **finally**: Este bloque se ejecuta siempre, independientemente de si hubo o no una excepción, y se utiliza aquí para indicar que la operación de división ha finalizado.

2. **Función `lanzar_excepcion_personalizada`**:
   - Esta función lanza una excepción `ValueError` si el valor proporcionado es negativo. Esto se hace utilizando la instrucción `raise`.

3. **Ejemplos de uso**:
   - **Ejemplo 1**: Se realiza una división sin errores (`10 / 2`).
   - **Ejemplo 2**: Se intenta dividir por cero (`10 / 0`), capturando la excepción de división por cero.
   - **Ejemplo 3**: Se intenta dividir por una cadena (`10 / "a"`), capturando la excepción de tipo de dato incorrecto.
   - **Ejemplo 4**: Se usa un valor negativo en `lanzar_excepcion_personalizada`, capturando la excepción `ValueError`.
   - **Ejemplo 5**: Se usa un valor positivo en `lanzar_excepcion_personalizada`, que no lanza ninguna excepción.

Este programa muestra cómo manejar excepciones comunes y lanzar excepciones personalizadas, permitiendo que el flujo del programa continúe de manera controlada y segura, incluso cuando se producen errores.
