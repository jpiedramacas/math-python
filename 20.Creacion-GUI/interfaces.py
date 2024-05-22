import tkinter as tk
from tkinter import messagebox

# Función para manejar el evento del botón
def saludar():
    nombre = entrada_nombre.get()
    if nombre:
        mensaje = "¡Hola, " + nombre + "!"
        messagebox.showinfo("Saludo", mensaje)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Saludo")

# Etiqueta
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.pack()

# Campo de entrada
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Botón
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()

