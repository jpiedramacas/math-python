# Conversiones de Tipos en Python

# Convertir de entero a flotante
entero = 10
flotante = float(entero)
print(f'Convertir entero a flotante: {entero} -> {flotante}')

# Convertir de flotante a entero
flotante = 10.75
entero = int(flotante)
print(f'Convertir flotante a entero: {flotante} -> {entero}')

# Convertir de cadena a entero
cadena = "123"
entero = int(cadena)
print(f'Convertir cadena a entero: "{cadena}" -> {entero}')

# Convertir de cadena a flotante
cadena = "123.45"
flotante = float(cadena)
print(f'Convertir cadena a flotante: "{cadena}" -> {flotante}')

# Convertir de entero a cadena
entero = 456
cadena = str(entero)
print(f'Convertir entero a cadena: {entero} -> "{cadena}"')

# Convertir de flotante a cadena
flotante = 789.01
cadena = str(flotante)
print(f'Convertir flotante a cadena: {flotante} -> "{cadena}"')

# Convertir de booleano a entero
booleano = True
entero = int(booleano)
print(f'Convertir booleano a entero: {booleano} -> {entero}')

# Convertir de entero a booleano
entero = 0
booleano = bool(entero)
print(f'Convertir entero a booleano: {entero} -> {booleano}')

# Convertir de lista a cadena (usando join)
lista = ['a', 'b', 'c']
cadena = ''.join(lista)
print(f'Convertir lista a cadena: {lista} -> "{cadena}"')

# Convertir de cadena a lista
cadena = "abc"
lista = list(cadena)
print(f'Convertir cadena a lista: "{cadena}" -> {lista}')

# Convertir de tupla a lista
tupla = (1, 2, 3)
lista = list(tupla)
print(f'Convertir tupla a lista: {tupla} -> {lista}')

# Convertir de lista a tupla
lista = [4, 5, 6]
tupla = tuple(lista)
print(f'Convertir lista a tupla: {lista} -> {tupla}')

