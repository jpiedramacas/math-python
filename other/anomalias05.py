# Inconsistencias en el tipo de parámetros:
def multiplicar(a, b): 
    return a * b 

# Convertimos la cadena "4" en un número entero antes de llamar a la función
resultado = multiplicar(3, int("4"))
print(resultado)
