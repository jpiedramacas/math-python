# Variable global
global_var = 10

# Función que utiliza una variable global y una variable local
def test_function():
    # Variable local dentro de la función
    local_var = 5
    print("Dentro de la función:")
    print("Variable global:", global_var)
    print("Variable local:", local_var)

# Llamada a la función
test_function()

# Intentar acceder a la variable local fuera de su ámbito causará un error
# print("Fuera de la función:")
# print("Variable local:", local_var)

