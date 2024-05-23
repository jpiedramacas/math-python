# Escribir en un archivo
def escribir_archivo():
    # Abrir el archivo en modo escritura ('w')
    with open('archivo.txt', 'w') as archivo:
        # Escribir en el archivo
        archivo.write("Hola, este es un ejemplo de escritura en un archivo.\n")
        archivo.write("Esta es otra línea de texto.\n")

# Leer un archivo
def leer_archivo():
    # Abrir el archivo en modo lectura ('r')
    with open('archivo.txt', 'r') as archivo:
        # Leer todo el contenido del archivo
        contenido = archivo.read()
        print("Contenido del archivo:\n", contenido)

# Recorrido secuencial de un archivo utilizando feof
def recorrer_archivo():
    # Abrir el archivo en modo lectura ('r')
    with open('archivo.txt', 'r') as archivo:
        # Leer la primera línea
        linea = archivo.readline()
        # Iterar hasta que se llegue al final del archivo
        while linea:
            # Imprimir la línea actual
            print(linea, end='')
            # Leer la siguiente línea
            linea = archivo.readline()

if __name__ == "__main__":
    # Escribir en el archivo
    escribir_archivo()
    # Leer el archivo
    leer_archivo()
    # Recorrer el archivo secuencialmente
    recorrer_archivo()

