import multiprocessing
import time

# Función para calcular el cuadrado de un número
def calcular_cuadrado(numero):
    time.sleep(1)  # Simula una tarea que toma tiempo
    resultado = numero * numero
    print(f"El cuadrado de {numero} es {resultado}")

if __name__ == "__main__":
    # Lista de números
    numeros = [1, 2, 3, 4, 5]

    # Crear un proceso para cada número
    procesos = []
    for num in numeros:
        proceso = multiprocessing.Process(target=calcular_cuadrado, args=(num,))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    print("Todas las tareas han sido completadas.")

