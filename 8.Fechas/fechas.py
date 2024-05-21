import datetime

def main():
    # Obtener la fecha y hora actual
    ahora = datetime.datetime.now()
    print("Fecha y hora actual:", ahora)

    # Acceder a componentes individuales de la fecha y hora
    año_actual = ahora.year
    mes_actual = ahora.month
    dia_actual = ahora.day
    hora_actual = ahora.hour
    minuto_actual = ahora.minute
    segundo_actual = ahora.second

    print("Año:", año_actual)
    print("Mes:", mes_actual)
    print("Día:", dia_actual)
    print("Hora:", hora_actual)
    print("Minuto:", minuto_actual)
    print("Segundo:", segundo_actual)

if __name__ == "__main__":
    main()

