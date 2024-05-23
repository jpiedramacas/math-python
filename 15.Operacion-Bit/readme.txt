Enunciado:

Escribe un programa en Python que haga uso de operadores bit a bit para realizar operaciones a nivel de bits. Incluye ejemplos de operaciones como AND, OR, XOR, NOT, desplazamiento a la izquierda y desplazamiento a la derecha.

Explicación:

En Python, los operadores bit a bit permiten realizar operaciones a nivel de bits en enteros. Estos operadores son útiles cuando se necesita trabajar con datos a un nivel más bajo que las operaciones aritméticas estándar. Aquí está el desglose de los operadores utilizados en el programa:

1. **Operador AND Bit a Bit (`&`)**:
   - Realiza una operación AND lógica entre los bits de dos números. Cada bit del resultado es 1 si ambos bits correspondientes en los números de entrada son 1.

2. **Operador OR Bit a Bit (`|`)**:
   - Realiza una operación OR lógica entre los bits de dos números. Cada bit del resultado es 1 si al menos uno de los bits correspondientes en los números de entrada es 1.

3. **Operador XOR Bit a Bit (`^`)**:
   - Realiza una operación XOR lógica entre los bits de dos números. Cada bit del resultado es 1 si los bits correspondientes en los números de entrada son diferentes, y 0 si son iguales.

4. **Operador NOT Bit a Bit (`~`)**:
   - Realiza una operación NOT lógica en los bits de un número. Cambia cada bit de 0 a 1 y de 1 a 0.

5. **Desplazamiento a la Izquierda (`<<`)**:
   - Desplaza todos los bits de un número hacia la izquierda una cierta cantidad de veces. Esto equivale a multiplicar el número por 2 elevado a la potencia del número de posiciones desplazadas.

6. **Desplazamiento a la Derecha (`>>`)**:
   - Desplaza todos los bits de un número hacia la derecha una cierta cantidad de veces. Esto equivale a dividir el número por 2 elevado a la potencia del número de posiciones desplazadas.

El programa demuestra cada uno de estos operadores en acción utilizando ejemplos simples y proporciona la salida correspondiente para cada operación. Esto ayuda a comprender cómo funcionan estos operadores y cómo se pueden utilizar en aplicaciones prácticas.
