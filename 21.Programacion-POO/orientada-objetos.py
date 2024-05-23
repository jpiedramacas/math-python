class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear objetos de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Llamar al método saludar de cada objeto
persona1.saludar()
persona2.saludar()

