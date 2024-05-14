import math  # Olvidamos importar esta librería


def calcular_promedio(valores):
    suma = 0
    for valor in valores:
        suma += valor
    promedio = suma / len(valores)
    return promedio


numeros = [10, 20, 30, 40, 50]

print(max(numeros))
print(math.cos(20))
resultado = calcular_promedio(numeros)
print("El promedio es:", resultado)
