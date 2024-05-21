from flask import Flask, request, render_template
from libros.clase_libro import Libro
from libros.clase_inventario import Inventario

app = Flask(__name__)
inventario = Inventario()

@app.route('/')
def index():
    return render_template('index.html', libros=inventario.libros)

@app.route('/agregar', methods=['POST'])
def agregar_libro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    try:
        precio = float(request.form['precio'])
        nuevo_libro = Libro(titulo, autor, precio)
        inventario.agregar_libro(nuevo_libro)
    except ValueError:
        pass  # Manejo de errores de entrada aquí
    return render_template('index.html', libros=inventario.libros)

@app.route('/buscar', methods=['POST'])
def buscar_libro():
    titulo = request.form['titulo']
    libro = inventario.buscar_libro(titulo)
    return render_template('index.html', libros=inventario.libros, libro=libro)

@app.route('/vender', methods=['POST'])
def vender_libro():
    titulo = request.form['titulo']
    inventario.registrar_venta(titulo)
    return render_template('index.html', libros=inventario.libros)

if __name__ == '__main__':
    app.run(debug=True)
