def encontrar_maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Ejemplo de uso
num1 = 10
num2 = 20
num3 = 15

maximo = encontrar_maximo(num1, num2, num3)
print("El máximo de los tres números es:", maximo)

