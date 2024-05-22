# Manejo de Errores (Excepciones) en Python

def dividir(a, b):
    try:
        # Intentar realizar la división
        resultado = a / b
    except ZeroDivisionError as e:
        # Capturar y manejar la excepción de división por cero
        print(f"Error: No se puede dividir por cero. Detalles: {e}")
        resultado = None
    except TypeError as e:
        # Capturar y manejar la excepción de tipo de dato incorrecto
        print(f"Error: Tipo de dato incorrecto. Detalles: {e}")
        resultado = None
    else:
        # Si no hubo ninguna excepción, se ejecuta este bloque
        print("La división se realizó correctamente.")
    finally:
        # Este bloque se ejecuta siempre, ocurra o no una excepción
        print("Operación de división completada.")
    return resultado

def lanzar_excepcion_personalizada(valor):
    if valor < 0:
        raise ValueError("El valor no puede ser negativo.")
    return valor

# Ejemplo de uso de la función dividir
print("Ejemplo 1:")
resultado = dividir(10, 2)
print(f"Resultado: {resultado}\n")

print("Ejemplo 2:")
resultado = dividir(10, 0)
print(f"Resultado: {resultado}\n")

print("Ejemplo 3:")
resultado = dividir(10, "a")
print(f"Resultado: {resultado}\n")

# Ejemplo de lanzamiento y captura de una excepción personalizada
print("Ejemplo 4:")
try:
    valor = lanzar_excepcion_personalizada(-5)
    print(f"Valor: {valor}")
except ValueError as e:
    print(f"Excepción capturada: {e}")
finally:
    print("Operación con valor completada.")

print("\nEjemplo 5:")
try:
    valor = lanzar_excepcion_personalizada(5)
    print(f"Valor: {valor}")
except ValueError as e:
    print(f"Excepción capturada: {e}")
finally:
    print("Operación con valor completada.")

