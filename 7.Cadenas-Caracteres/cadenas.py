def main():
    # Ejemplo de manipulación de cadenas de caracteres en Python
    
    # Definir una cadena de caracteres
    cadena = "Hola, mundo!"
    
    # Imprimir la cadena original
    print("Cadena original:", cadena)
    
    # Longitud de la cadena
    print("Longitud de la cadena:", len(cadena))
    
    # Acceso a elementos de la cadena por índice
    print("Primer carácter de la cadena:", cadena[0])
    print("Último carácter de la cadena:", cadena[-1])
    
    # Subcadena (slice) de la cadena
    print("Subcadena desde el tercer carácter:", cadena[2:])
    print("Subcadena hasta el séptimo carácter:", cadena[:7])
    print("Subcadena desde el tercer al séptimo carácter:", cadena[2:7])
    
    # Concatenación de cadenas
    nueva_cadena = cadena + " ¿Cómo estás?"
    print("Nueva cadena concatenada:", nueva_cadena)
    
    # Repetición de cadenas
    cadena_repetida = cadena * 3
    print("Cadena repetida tres veces:", cadena_repetida)
    
    # Conversión a mayúsculas y minúsculas
    print("Cadena en mayúsculas:", cadena.upper())
    print("Cadena en minúsculas:", cadena.lower())
    
    # Buscar subcadena
    subcadena = "mundo"
    if subcadena in cadena:
        print("La subcadena '{}' está en la cadena original.".format(subcadena))
    else:
        print("La subcadena '{}' no está en la cadena original.".format(subcadena))
    
    # Reemplazar caracteres
    cadena_reemplazada = cadena.replace("Hola", "Hello")
    print("Cadena con reemplazo:", cadena_reemplazada)
    
    # Separar cadena en palabras
    palabras = cadena.split(",")
    print("Palabras separadas:", palabras)
    
    # Unir lista de palabras en una sola cadena
    nueva_cadena = " ".join(palabras)
    print("Nueva cadena uniendo palabras:", nueva_cadena)

if __name__ == "__main__":
    main()

