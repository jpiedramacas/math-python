# Definición de una lista
lista_frutas = ["manzana", "banana", "cereza", "naranja"]

# Definición de una tupla
tupla_colores = ("rojo", "verde", "azul")

# Acceso a elementos
print("Primer elemento de la lista de frutas:", lista_frutas[0])
print("Segundo elemento de la tupla de colores:", tupla_colores[1])

# Modificación (Solo en listas)
lista_frutas[0] = "pera"
print("Lista de frutas después de modificar el primer elemento:", lista_frutas)

# Longitud
print("Cantidad de elementos en la lista de frutas:", len(lista_frutas))
print("Cantidad de elementos en la tupla de colores:", len(tupla_colores))

# Iteración
print("Elementos de la lista de frutas:")
for fruta in lista_frutas:
    print(fruta)

print("Elementos de la tupla de colores:")
for color in tupla_colores:
    print(color)

# Concatenación (Solo en listas)
otra_lista_frutas = ["uva", "sandía"]
lista_frutas.extend(otra_lista_frutas)
print("Lista de frutas después de concatenar:", lista_frutas)

# Inversión (Solo en listas)
lista_frutas.reverse()
print("Lista de frutas después de invertir:", lista_frutas)

# Añadir elementos (Solo en listas)
tupla_colores = tupla_colores + ("amarillo",)
print("Tupla de colores después de añadir un nuevo color:", tupla_colores)

