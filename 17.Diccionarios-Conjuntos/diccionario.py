# Definición de un diccionario de estudiantes y sus calificaciones
estudiantes = {
    "Juan": 85,
    "María": 90,
    "Pedro": 75,
    "Ana": 95,
    "Luis": 80
}

# Mostrar el diccionario de estudiantes
print("Diccionario de Estudiantes:", estudiantes)

# Acceso a elementos del diccionario
print("Calificación de María:", estudiantes["María"])

# Modificación de elementos del diccionario
estudiantes["Pedro"] = 80

# Añadir un nuevo estudiante al diccionario
estudiantes["Lucía"] = 88

# Eliminar un estudiante del diccionario
del estudiantes["Luis"]

# Mostrar el diccionario actualizado
print("Diccionario de Estudiantes Actualizado:", estudiantes)

# Crear un conjunto de calificaciones únicas
calificaciones = set(estudiantes.values())

# Mostrar el conjunto de calificaciones únicas
print("Conjunto de Calificaciones Únicas:", calificaciones)

