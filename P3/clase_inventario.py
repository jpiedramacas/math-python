class Inventario:
    def __init__(self):
        self.libros = []
        self.total_ventas = 0

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado al inventario.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print("Libro encontrado:")
                print(libro)
                return libro
        print(f"El libro '{titulo}' no está en el inventario.")
        return None

    def registrar_venta(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            self.total_ventas += libro.precio
            print(f"Libro '{titulo}' vendido por ${libro.precio:.2f}.")
            print(f"Total de ventas: ${self.total_ventas:.2f}")
        else:
            print(f"No se puede registrar la venta. El libro '{titulo}' no está en el inventario.")
