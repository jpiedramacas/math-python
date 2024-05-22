# Uso de Operadores Bit a Bit en Python

# Definir dos números enteros
a = 60  # 60 en binario es 0011 1100
b = 13  # 13 en binario es 0000 1101

# Operador AND bit a bit
resultado_and = a & b  # 0000 1100
print(f"{a} & {b} = {resultado_and}")

# Operador OR bit a bit
resultado_or = a | b  # 0011 1101
print(f"{a} | {b} = {resultado_or}")

# Operador XOR bit a bit
resultado_xor = a ^ b  # 0011 0001
print(f"{a} ^ {b} = {resultado_xor}")

# Operador NOT bit a bit
resultado_not = ~a  # 1100 0011 (complemento a dos)
print(f"~{a} = {resultado_not}")

# Desplazamiento a la izquierda
resultado_left_shift = a << 2  # 1111 0000
print(f"{a} << 2 = {resultado_left_shift}")

# Desplazamiento a la derecha
resultado_right_shift = a >> 2  # 0000 1111
print(f"{a} >> 2 = {resultado_right_shift}")

