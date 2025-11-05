from equipos import menu_equipos
from jugadores import menu_jugadores
from calendario import menu_calendario
from ranking import menu_ranking
from utiles import leer_int

def main():
    activo = 1
    while activo == 1:
        print("\n=== Liga Deportiva Amateur ===")
        print("1. Gestión de equipos")
        print("2. Gestión de jugadores")
        print("3. Calendario de partidos")
        print("4. Resultados y clasificación")
        print("5. Salir")

        opcion = leer_int("Opción: ", 1, 5)

        if opcion == 1:
            menu_equipos()
        elif opcion == 2:
            menu_jugadores()
        elif opcion == 3:
            menu_calendario()
        elif opcion == 4:
            menu_ranking()
        elif opcion == 5:
            activo = 0
    print("Programa finalizado.")

if __name__ == "__main__":
    main()
