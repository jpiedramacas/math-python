Enunciado:
Desarrolla pruebas unitarias en Python utilizando la biblioteca `unittest` para verificar el correcto funcionamiento de las funciones y procedimientos desarrollados en ejercicios anteriores.

Explicación:
Las pruebas unitarias son una parte fundamental del desarrollo de software. Permiten verificar que cada componente de un programa funcione correctamente de manera aislada, lo que facilita la detección y corrección de errores.

La biblioteca estándar de Python incluye un módulo llamado `unittest` que proporciona un marco de trabajo para escribir y ejecutar pruebas unitarias de manera estructurada.

Para desarrollar pruebas unitarias con `unittest`, primero debes identificar las funciones y procedimientos que deseas probar. Luego, escribe casos de prueba para cada uno de estos componentes.

Un caso de prueba típico consta de tres partes:
1. **Preparación (Setup):** Crea el entorno necesario para ejecutar la prueba, como configurar variables, objetos o cualquier otro estado inicial.
2. **Ejecución (Execution):** Llama a la función o procedimiento que estás probando con los argumentos necesarios.
3. **Verificación (Assertion):** Verifica que el resultado de la función o procedimiento sea el esperado utilizando métodos de aserción proporcionados por `unittest`.

Una vez que hayas escrito tus casos de prueba, puedes ejecutarlos para comprobar si la funcionalidad de tu código es la esperada. Si alguna prueba falla, indica que hay un problema en el código que debe ser corregido.

Las pruebas unitarias no solo garantizan que tu código funcione correctamente, sino que también sirven como documentación viva que describe cómo se supone que debe comportarse cada parte de tu programa. Esto facilita la colaboración entre miembros del equipo y la realización de cambios en el código sin introducir errores inadvertidos.
