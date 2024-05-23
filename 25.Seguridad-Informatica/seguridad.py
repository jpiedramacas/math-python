import hashlib
from cryptography.fernet import Fernet

# Función para generar una clave de cifrado
def generar_clave():
    return Fernet.generate_key()

# Función para cifrar un mensaje
def cifrar_mensaje(clave, mensaje):
    f = Fernet(clave)
    mensaje_cifrado = f.encrypt(mensaje.encode())
    return mensaje_cifrado

# Función para descifrar un mensaje
def descifrar_mensaje(clave, mensaje_cifrado):
    f = Fernet(clave)
    mensaje_descifrado = f.decrypt(mensaje_cifrado).decode()
    return mensaje_descifrado

# Función para calcular el hash de una contraseña
def calcular_hash(contrasena):
    hash_object = hashlib.sha256(contrasena.encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password

# Ejemplo de uso
if __name__ == "__main__":
    # Generar una clave de cifrado
    clave = generar_clave()
    print("Clave de cifrado generada:", clave)

    # Cifrar y descifrar un mensaje
    mensaje = "Hola, mundo!"
    mensaje_cifrado = cifrar_mensaje(clave, mensaje)
    print("Mensaje cifrado:", mensaje_cifrado)
    mensaje_descifrado = descifrar_mensaje(clave, mensaje_cifrado)
    print("Mensaje descifrado:", mensaje_descifrado)

    # Calcular el hash de una contraseña
    contrasena = "secreta123"
    hashed_password = calcular_hash(contrasena)
    print("Contraseña hasheada:", hashed_password)

