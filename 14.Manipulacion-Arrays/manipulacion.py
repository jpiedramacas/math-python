# Importar el módulo array para trabajar con arrays de forma más eficiente
import array as arr

# Creación de arrays
# Crear un array de enteros
array_enteros = arr.array('i', [1, 2, 3, 4, 5])
print("Array de enteros:", array_enteros)

# Crear un array de floats
array_floats = arr.array('f', [1.5, 2.5, 3.5, 4.5])
print("Array de floats:", array_floats)

# Acceso a elementos de un array
print("\nAcceso a elementos:")
print("Primer elemento de array_enteros:", array_enteros[0])
print("Último elemento de array_floats:", array_floats[-1])

# Modificación de elementos de un array
array_enteros[1] = 20
print("\nArray de enteros después de la modificación:", array_enteros)

# Recorrido de un array
print("\nRecorrido de array_enteros:")
for elemento in array_enteros:
    print(elemento, end=" ")
print()

# Añadir elementos a un array
array_enteros.append(6)
print("\nArray de enteros después de añadir un elemento:", array_enteros)

# Eliminar elementos de un array
array_enteros.remove(20)
print("\nArray de enteros después de eliminar un elemento:", array_enteros)

# Obtener la longitud de un array
print("\nLongitud de array_enteros:", len(array_enteros))

# Slicing de un array (obtener una sub-sección)
sub_array = array_enteros[1:3]
print("\nSub-array de array_enteros:", sub_array)

# Concatenación de arrays
array_concatenado = array_enteros + arr.array('i', [7, 8, 9])
print("\nArray concatenado:", array_concatenado)

# Inversión de un array
array_invertido = array_concatenado[::-1]
print("\nArray invertido:", array_invertido)

# Búsqueda de elementos en un array
indice_elemento = array_concatenado.index(4)
print("\nÍndice del elemento '4' en array_concatenado:", indice_elemento)

