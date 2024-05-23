# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        print(f"{self.marca} {self.modelo} está en movimiento.")

# Definición de la subclase Carro, que hereda de Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def conducir(self):
        print(f"{self.color} {self.marca} {self.modelo} está en movimiento.")

# Definición de la subclase Avion, que hereda de Vehiculo
class Avion(Vehiculo):
    def __init__(self, marca, modelo, altura_maxima):
        super().__init__(marca, modelo)
        self.altura_maxima = altura_maxima

    def volar(self):
        print(f"{self.marca} {self.modelo} está volando a una altura de {self.altura_maxima} metros.")

# Crear objetos de las clases Carro y Avion
mi_carro = Carro("Toyota", "Corolla", "Rojo")
mi_avion = Avion("Boeing", "747", 10000)

# Llamar al método conducir() de los objetos
mi_carro.conducir()
mi_avion.conducir()  # Aquí se muestra el polimorfismo, ya que la implementación del método depende del tipo de objeto.
mi_avion.volar()     # Este método solo está disponible para objetos de la clase Avion.

