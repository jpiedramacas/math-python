Enunciado:
Elaborar un programa que utilice programación concurrente o paralela en Python utilizando las bibliotecas `threading` o `multiprocessing`, respectivamente.

Explicación:
La programación concurrente y paralela son técnicas utilizadas para realizar múltiples tareas simultáneamente, lo que puede mejorar el rendimiento de una aplicación al aprovechar los recursos del sistema de manera más eficiente.

En Python, las bibliotecas estándar `threading` y `multiprocessing` proporcionan herramientas para implementar programación concurrente y paralela, respectivamente.

- **Programación Concurrente con `threading`:** La biblioteca `threading` permite crear hilos (threads) que ejecutan funciones de manera concurrente en un mismo proceso. Los hilos comparten recursos y espacio de memoria, lo que los hace adecuados para tareas que involucran operaciones de entrada/salida (E/S) bloqueantes, como la lectura/escritura de archivos o la realización de solicitudes de red.

- **Programación Paralela con `multiprocessing`:** La biblioteca `multiprocessing` permite crear procesos independientes que se ejecutan en paralelo, cada uno con su propio espacio de memoria. Los procesos son útiles para tareas que requieren cálculos intensivos en CPU y pueden aprovechar múltiples núcleos de CPU.

El enunciado te pide elaborar un programa que utilice una de estas técnicas para realizar tareas simultáneas y demostrar cómo puede mejorar el rendimiento de una aplicación.

Por ejemplo, en el caso de `multiprocessing`, dividir tareas en procesos independientes puede reducir el tiempo total de ejecución al distribuir la carga de trabajo entre múltiples núcleos de CPU. En el caso de `threading`, ejecutar tareas concurrentemente puede evitar bloqueos y mantener la capacidad de respuesta de la aplicación mientras se realizan operaciones de E/S.

Al utilizar programación concurrente o paralela de manera adecuada, puedes mejorar la eficiencia y la escalabilidad de tu aplicación, permitiendo que realice más trabajo en menos tiempo y responda mejor a las demandas del usuario.
