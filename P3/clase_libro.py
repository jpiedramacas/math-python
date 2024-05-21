class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio:.2f}"
