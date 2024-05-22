### Enunciado:

Desarrolla un programa en Python que cree una interfaz gráfica de usuario (GUI) utilizando bibliotecas como Tkinter o PyQt.

La interfaz debe incluir al menos algunos elementos básicos como botones, etiquetas y campos de entrada.

### Explicación:

En este programa, utilizamos la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI) en Python. Aquí está la explicación de cómo se crea la interfaz:

1. **Importar Tkinter**:
   - Importamos la biblioteca `tkinter` de Python para trabajar con GUI.

2. **Definir Funcionalidades**:
   - Definimos una función `saludar()` que se ejecutará cuando se haga clic en el botón. Esta función obtiene el nombre ingresado en el campo de entrada y muestra un mensaje de saludo.

3. **Crear la Ventana**:
   - Creamos una ventana principal utilizando `tk.Tk()` y le asignamos un título con `ventana.title()`.

4. **Agregar Elementos a la Interfaz**:
   - Creamos y empaquetamos una etiqueta (con `tk.Label()`), un campo de entrada (con `tk.Entry()`) y un botón (con `tk.Button()`). Los elementos se "empaquetan" en la ventana utilizando el método `pack()`.

5. **Ejecutar el Bucle Principal**:
   - Llamamos al método `mainloop()` en la ventana para iniciar el bucle principal de la interfaz gráfica, lo que permite que la ventana sea interactiva y responda a eventos como clics de botón.

Al ejecutar este programa, se abrirá una ventana con una etiqueta, un campo de entrada y un botón. Cuando se ingresa un nombre y se hace clic en el botón, se muestra un mensaje de saludo. Si no se ingresa ningún nombre y se hace clic en el botón, se muestra un mensaje de advertencia.

Este ejemplo muestra cómo crear una interfaz gráfica básica en Python utilizando Tkinter. Si prefieres utilizar PyQt en lugar de Tkinter, el proceso es similar, pero requerirá una instalación adicional de la biblioteca PyQt.
