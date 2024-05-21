def main():
    # Estructuras condicionales
    x = 10

    # if
    if x > 0:
        print("x es positivo")

    # if-else
    if x % 2 == 0:
        print("x es par")
    else:
        print("x es impar")

    # if-elif-else
    if x > 0:
        print("x es positivo")
    elif x < 0:
        print("x es negativo")
    else:
        print("x es cero")

    # Bucles
    # Bucle for
    for i in range(5):
        print(i)

    # Bucle while
    i = 0
    while i < 5:
        print(i)
        i += 1

if __name__ == "__main__":
    main()

