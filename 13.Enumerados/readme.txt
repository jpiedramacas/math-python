### Enunciado:

Implementa un programa en Python que utilice enumerados (enums) para representar conjuntos de constantes con nombres asociados. Como ejemplo, define un enumerado para los días de la semana y utiliza este enumerado en una función para mostrar información específica sobre cada día.

### Explicación:

En Python, las enumeraciones (enums) permiten definir un conjunto de constantes con nombres significativos, lo que mejora la legibilidad y el mantenimiento del código. El módulo `enum` proporciona la clase `Enum` para crear enumeraciones. A continuación, se muestra un ejemplo de cómo definir y utilizar un enumerado para representar los días de la semana.

### Explicación del Código:

1. **Importar el Módulo `enum`**:
   - `from enum import Enum, auto` se utiliza para importar las clases necesarias para crear enumeraciones.

2. **Definir el Enumerado `DiaDeLaSemana`**:
   - Se define una clase `DiaDeLaSemana` que hereda de `Enum`. Cada miembro del enumerado representa un día de la semana.
   - `auto()` se usa para asignar automáticamente valores a cada miembro del enumerado, simplificando la asignación de valores y mejorando la legibilidad del código.

3. **Función `mostrar_info_dia`**:
   - Esta función toma un miembro del enumerado `DiaDeLaSemana` y muestra un mensaje específico para cada día.
   - Utiliza una serie de condicionales `if-elif` para verificar cuál es el día y mostrar el mensaje correspondiente.

4. **Función `main`**:
   - Establece `dia_actual` a `DiaDeLaSemana.MIERCOLES` y llama a `mostrar_info_dia` para mostrar información sobre ese día.
   - Itera sobre todos los miembros del enumerado `DiaDeLaSemana` y los imprime, mostrando tanto el nombre como el valor de cada día.

5. **Condicional `if __name__ == "__main__":`**:
   - Esta línea asegura que la función `main` se ejecute solo si el script se está ejecutando directamente, no si se está importando como un módulo.

### Ejecución del Programa:

Al ejecutar este programa, se muestra información específica para el día `MIERCOLES` y luego se listan todos los días de la semana con sus nombres y valores asignados automáticamente. Esto demuestra cómo usar enumeraciones en Python para representar conjuntos de constantes con nombres asociados, mejorando la claridad y la organización del código.
