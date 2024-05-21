# Importamos las funciones de operaciones.py
from operaciones import sumar, restar, multiplicar, dividir

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Solicitamos la operación al usuario
    operacion = input("¿Qué operación desea realizar? (+ para suma, - para resta, * para multiplicación, / para división): ")

    # Realizamos la operación correspondiente según la entrada del usuario
    if operacion == '+':
        resultado = sumar(num1, num2)
        print("La suma de", num1, "y", num2, "es:", resultado)
    elif operacion == '-':
        resultado = restar(num1, num2)
        print("La resta de", num2, "a", num1, "es:", resultado)
    elif operacion == '*':
        resultado = multiplicar(num1, num2)
        print("El producto de", num1, "y", num2, "es:", resultado)
    elif operacion == '/':
        resultado = dividir(num1, num2)
        print("La división de", num1, "entre", num2, "es:", resultado)
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()
