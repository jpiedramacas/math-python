import random

# Generación de un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
print("Número aleatorio generado:", numero_aleatorio)

# Simulación de un lanzamiento de moneda (cara o cruz)
resultado_moneda = random.choice(["cara", "cruz"])
print("Resultado del lanzamiento de la moneda:", resultado_moneda)

# Simulación de un dado de seis caras
resultado_dado = random.randint(1, 6)
print("Resultado del lanzamiento del dado:", resultado_dado)

# Simulación de una decisión aleatoria entre dos opciones
opcion_1 = "Ir al cine"
opcion_2 = "Quedarse en casa"
decision = random.choice([opcion_1, opcion_2])
print("Decisión aleatoria:", decision)

