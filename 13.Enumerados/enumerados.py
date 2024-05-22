from enum import Enum, auto

# Definir un enumerado para los días de la semana
class DiaDeLaSemana(Enum):
    LUNES = auto()
    MARTES = auto()
    MIERCOLES = auto()
    JUEVES = auto()
    VIERNES = auto()
    SABADO = auto()
    DOMINGO = auto()

# Función para mostrar información sobre el día
def mostrar_info_dia(dia):
    if dia == DiaDeLaSemana.LUNES:
        print("Hoy es Lunes, inicio de la semana.")
    elif dia == DiaDeLaSemana.MARTES:
        print("Hoy es Martes, segundo día de la semana.")
    elif dia == DiaDeLaSemana.MIERCOLES:
        print("Hoy es Miércoles, mitad de semana.")
    elif dia == DiaDeLaSemana.JUEVES:
        print("Hoy es Jueves, casi terminamos la semana.")
    elif dia == DiaDeLaSemana.VIERNES:
        print("Hoy es Viernes, último día laborable para muchos.")
    elif dia == DiaDeLaSemana.SABADO:
        print("Hoy es Sábado, día de descanso.")
    elif dia == DiaDeLaSemana.DOMINGO:
        print("Hoy es Domingo, fin de semana.")

# Ejemplo de uso del enumerado
def main():
    # Mostrar información sobre un día específico
    dia_actual = DiaDeLaSemana.MIERCOLES
    mostrar_info_dia(dia_actual)

    # Listar todos los días de la semana
    print("\nDías de la semana:")
    for dia in DiaDeLaSemana:
        print(f"{dia.name} = {dia.value}")

if __name__ == "__main__":
    main()

