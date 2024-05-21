class Inventario:
    def __init__(self):
        self.libros = []
        self.total_ventas = 0

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def registrar_venta(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            self.total_ventas += libro.precio
            return True
        return False
