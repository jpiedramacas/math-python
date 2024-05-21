from clase_libro import Libro
from clase_inventario import Inventario

def main():
    inventario = Inventario()
    
    while True:
        print("\n--- Menú de la Tienda de Libros ---")
        print("1. Agregar un nuevo libro al inventario")
        print("2. Buscar un libro por título")
        print("3. Registrar una venta de un libro")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            libro = Libro(titulo, autor, precio)
            inventario.agregar_libro(libro)
        
        elif opcion == "2":
            titulo = input("Ingrese el título del libro que busca: ")
            inventario.buscar_libro(titulo)
        
        elif opcion == "3":
            titulo = input("Ingrese el título del libro vendido: ")
            inventario.registrar_venta(titulo)
        
        elif opcion == "4":
            print("Saliendo del sistema. ¡Gracias por usar la tienda de libros en línea!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
