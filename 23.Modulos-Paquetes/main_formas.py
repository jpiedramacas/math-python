import rectangulo
import circulo

# Rectángulo
base_rectangulo = 5
altura_rectangulo = 3
print("Rectángulo:")
print("Área:", rectangulo.calcular_area(base_rectangulo, altura_rectangulo))
print("Perímetro:", rectangulo.calcular_perimetro(base_rectangulo, altura_rectangulo))

# Círculo
radio_circulo = 4
print("\nCírculo:")
print("Área:", circulo.calcular_area(radio_circulo))
print("Perímetro:", circulo.calcular_perimetro(radio_circulo))

