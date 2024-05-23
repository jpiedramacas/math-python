Enunciado:
Desarrolla un programa modular en Python que utilice módulos y paquetes para organizar el código de manera más eficiente y reutilizable. El programa debe calcular y mostrar el área y el perímetro de diferentes formas geométricas, como rectángulos y círculos. Cada forma geométrica debe ser manejada por un módulo separado dentro del paquete `formas_geometricas`.

Explicación:
El enunciado te pide crear un programa modular en Python que calcule y muestre el área y el perímetro de diferentes formas geométricas, como rectángulos y círculos. Para organizar este código de manera eficiente y reutilizable, debes utilizar módulos y paquetes.

1. **Creación de módulos:**
   Crea un módulo para cada forma geométrica que desees manejar en tu programa. Por ejemplo, puedes crear un módulo `rectangulo.py` para manejar rectángulos y un módulo `circulo.py` para manejar círculos. En cada módulo, define funciones para calcular el área y el perímetro de la forma geométrica correspondiente.

2. **Organización en paquetes:**
   Organiza estos módulos en un paquete llamado `formas_geometricas`. Para hacer esto, coloca todos los archivos de módulo en un directorio llamado `formas_geometricas`. Asegúrate de incluir un archivo `__init__.py` vacío en este directorio para que Python reconozca el directorio como un paquete.

3. **Uso en el programa principal:**
   En el programa principal (por ejemplo, `main_formas.py`), importa los módulos necesarios desde el paquete `formas_geometricas`. Utiliza las funciones definidas en estos módulos para calcular y mostrar el área y el perímetro de las formas geométricas según sea necesario.

Siguiendo este enfoque, tendrás un programa modular que utiliza módulos y paquetes para organizar el código de manera eficiente y reutilizable. Cada módulo manejará una forma geométrica específica, lo que facilitará la extensibilidad y el mantenimiento del programa.
