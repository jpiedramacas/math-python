# Definición de una función que suma dos números
def suma(a, b):
    return a + b

# Definición de un procedimiento que imprime un mensaje
def imprimir_mensaje():
    print("¡Hola desde el procedimiento!")

# Definición de una función que modifica una lista
def modificar_lista(lista):
    lista.append(4)

# Definición de una función que duplica una lista
def duplicar_lista(lista):
    return lista * 2

# Definición de una función que intercambia los valores de dos variables
def intercambiar_valores(a, b):
    return b, a

# Ejemplo de parámetros por valor
x = 10
y = 20
print("Suma:", suma(x, y))  # Salida: 30

# Ejemplo de parámetros por referencia
mi_lista = [1, 2, 3]
print("Lista original:", mi_lista)  # Salida: [1, 2, 3]
modificar_lista(mi_lista)
print("Lista modificada:", mi_lista)  # Salida: [1, 2, 3, 4]

# Ejemplo de retorno de una lista duplicada
mi_lista_duplicada = duplicar_lista(mi_lista)
print("Lista duplicada:", mi_lista_duplicada)  # Salida: [1, 2, 3, 4, 1, 2, 3, 4]

# Ejemplo de intercambio de valores
a = 5
b = 10
print("Valores originales:", a, b)  # Salida: 5 10
a, b = intercambiar_valores(a, b)
print("Valores intercambiados:", a, b)  # Salida: 10 5

