# Función recursiva para calcular el número de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Función que implementa memoización para la función fibonacci
def fibonacci_con_memoizacion(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        resultado = fibonacci_con_memoizacion(n-1, memo) + fibonacci_con_memoizacion(n-2, memo)
        memo[n] = resultado
        return resultado

# Ejemplo de uso de las dos versiones de la función fibonacci
if __name__ == "__main__":
    n = 30

    # Sin memoización
    print("Calculando Fibonacci sin memoización para n =", n)
    resultado = fibonacci(n)
    print("Resultado:", resultado)

    # Con memoización
    print("\nCalculando Fibonacci con memoización para n =", n)
    resultado_memoizado = fibonacci_con_memoizacion(n)
    print("Resultado:", resultado_memoizado)

