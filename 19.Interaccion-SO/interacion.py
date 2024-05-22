import os

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print("Directorio de trabajo actual:", directorio_actual)

# Listar los archivos y directorios en el directorio actual
archivos_en_directorio = os.listdir()
print("Archivos en el directorio actual:", archivos_en_directorio)

# Crear un nuevo directorio
nuevo_directorio = "nuevo_directorio"
os.makedirs(nuevo_directorio)
print("Nuevo directorio creado:", nuevo_directorio)

# Cambiar al nuevo directorio
os.chdir(nuevo_directorio)
print("Cambiado al directorio:", os.getcwd())

# Crear un nuevo archivo y escribir en él
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es el contenido del archivo.")

# Leer el contenido del archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)

# Regresar al directorio anterior
os.chdir(directorio_actual)
print("Regresado al directorio:", os.getcwd())

# Eliminar el directorio y su contenido
os.rmdir(nuevo_directorio)
print("Directorio eliminado:", nuevo_directorio)

