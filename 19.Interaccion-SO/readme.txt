Enunciado:

Desarrolla un programa en Python que interactúe con el sistema operativo, realizando operaciones como lectura y escritura de archivos, navegación por directorios y ejecución de comandos.

Explicación:

Para interactuar con el sistema operativo en Python, utilizamos el módulo `os`, que proporciona funciones para realizar operaciones relacionadas con el sistema operativo subyacente. Aquí está la explicación de cómo se utiliza en el programa propuesto:

1. **Obtener el Directorio de Trabajo Actual**:
   - La función `os.getcwd()` se utiliza para obtener el directorio de trabajo actual del programa.

2. **Listar Archivos y Directorios**:
   - La función `os.listdir()` se utiliza para listar los archivos y directorios en el directorio actual.

3. **Crear un Nuevo Directorio**:
   - La función `os.makedirs(nombre_directorio)` se utiliza para crear un nuevo directorio con el nombre especificado.

4. **Cambiar de Directorio**:
   - La función `os.chdir(nombre_directorio)` se utiliza para cambiar al directorio especificado.

5. **Crear y Escribir en un Archivo**:
   - Se utiliza la operación `open(nombre_archivo, modo)` junto con un bloque `with` para abrir un archivo en modo escritura (`"w"`) y escribir contenido en él.

6. **Leer el Contenido de un Archivo**:
   - Se utiliza la misma operación `open(nombre_archivo, modo)` junto con un bloque `with` para abrir un archivo en modo lectura (`"r"`) y leer su contenido.

7. **Regresar al Directorio Anterior**:
   - Se utiliza `os.chdir()` para regresar al directorio de trabajo original después de completar las operaciones en el nuevo directorio.

8. **Eliminar un Directorio y su Contenido**:
   - La función `os.rmdir(nombre_directorio)` se utiliza para eliminar el directorio especificado.

En resumen, el programa interactúa con el sistema operativo utilizando funciones del módulo `os` para realizar varias operaciones, lo que demuestra cómo interactuar con el sistema desde un programa Python.
