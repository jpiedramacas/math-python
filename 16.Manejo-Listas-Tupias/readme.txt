Enunciado:

Escribe un programa en Python que trabaje con listas y tuplas, destacando la diferencia entre estos dos tipos de datos y demostrando cómo se pueden utilizar en distintos contextos.

Explicación:

En Python, las listas y las tuplas son tipos de datos que se utilizan para almacenar colecciones ordenadas de elementos. La diferencia principal entre ellas radica en su mutabilidad: las listas son mutables (sus elementos pueden ser modificados después de la creación), mientras que las tuplas son inmutables (una vez creadas, no se pueden modificar sus elementos). A continuación, se explica cómo trabajar con listas y tuplas:

1. **Definición de Listas y Tuplas**:
   - Se definen mediante corchetes `[]` para las listas y paréntesis `()` para las tuplas. Por ejemplo:
     ```python
     lista_frutas = ["manzana", "banana", "cereza", "naranja"]
     tupla_colores = ("rojo", "verde", "azul")
     ```

2. **Acceso a Elementos**:
   - Se accede a los elementos individuales de una lista o tupla mediante su índice. Por ejemplo:
     ```python
     primer_fruta = lista_frutas[0]
     segundo_color = tupla_colores[1]
     ```

3. **Modificación** (Solo en Listas):
   - Solo las listas pueden ser modificadas después de su creación. Por ejemplo:
     ```python
     lista_frutas[0] = "pera"
     ```

4. **Longitud**:
   - Se puede obtener la cantidad de elementos en una lista o tupla usando la función `len()`. Por ejemplo:
     ```python
     longitud_frutas = len(lista_frutas)
     longitud_colores = len(tupla_colores)
     ```

5. **Iteración**:
   - Se puede iterar sobre los elementos de una lista o tupla usando un bucle `for`. Por ejemplo:
     ```python
     for fruta in lista_frutas:
         print(fruta)
     ```

6. **Concatenación** (Solo en Listas):
   - Solo las listas pueden ser concatenadas mediante el método `extend()` o el operador `+`. Por ejemplo:
     ```python
     otra_lista_frutas = ["uva", "sandía"]
     lista_frutas.extend(otra_lista_frutas)
     ```

7. **Inversión** (Solo en Listas):
   - Solo las listas pueden ser invertidas mediante el método `reverse()`. Por ejemplo:
     ```python
     lista_frutas.reverse()
     ```

8. **Añadir Elementos** (Solo en Listas):
   - Solo las listas permiten añadir nuevos elementos mediante el método `append()`. Por ejemplo:
     ```python
     tupla_colores = tupla_colores + ("amarillo",)
     ```

Este programa muestra cómo trabajar con listas y tuplas en Python, resaltando sus diferencias y las operaciones que se pueden realizar con cada una. Las listas son más versátiles y se utilizan cuando se necesita una colección de elementos que pueda cambiar, mientras que las tuplas se usan para datos que no deben ser modificados después de su creación.
