Enunciado:
Desarrolla un programa en Python que calcule el factorial de un número de forma recursiva

Explicación:
El programa consiste en una función llamada `factorial` que utiliza la recursividad para calcular el factorial de un número entero no negativo. El factorial de un número entero `n`, denotado como `n!`, es el producto de todos los enteros positivos menores o iguales a `n`. Por ejemplo, el factorial de 5 (`5!`) es igual a 5 x 4 x 3 x 2 x 1 = 120.

La función `factorial` toma un parámetro `n`, que representa el número del cual se desea calcular el factorial. Si `n` es igual a 0, la función devuelve 1 (ya que el factorial de 0 es 1). De lo contrario, la función devuelve `n` multiplicado por el factorial de `n - 1`. Este proceso continúa hasta que `n` es igual a 0, momento en el cual se alcanza el caso base de la recursión.

Luego, se utiliza un ejemplo de uso de la función `factorial` para calcular y mostrar el factorial de un número específico (en este caso, el número 5).
