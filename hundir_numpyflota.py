import random
import numpy as np

MAXIMOTABLERO = 19  # tablero 20x20 (0-19)

def colocarBarco(barco, posiciones):
    colocado = False

    while not colocado:

        # elegir fila válida
        fila_valida = False
        while not fila_valida:
            fila_inicio = random.randint(0, MAXIMOTABLERO)
            fila_fin = fila_inicio + barco - 1
            if fila_fin <= MAXIMOTABLERO:
                fila_valida = True

        columna = random.randint(0, MAXIMOTABLERO)
        inicio = (fila_inicio, columna)
        fin = (fila_fin, columna)

        # comprobar colisiones
        hay_colision = False
        for (ini_ex, fin_ex) in posiciones:
            fi_ex, ci_ex = ini_ex
            ff_ex, cf_ex = fin_ex

            if ci_ex == columna:
                for f_new in range(fila_inicio, fila_fin + 1):
                    for f_old in range(fi_ex, ff_ex + 1):
                        if f_new == f_old:
                            hay_colision = True

        # si no hay colisión, colocamos el barco
        if not hay_colision:
            posiciones.append((inicio, fin))
            colocado = True

    return posiciones


def generar_tablero():
    tablero = np.zeros((20, 20), dtype=int)
    tamanos = [4, 3, 2]
    posiciones = []

    for tam in tamanos:
        posiciones = colocarBarco(tam, posiciones)

    # marcar los barcos en el tablero
    for (inicio, fin) in posiciones:
        fi, ci = inicio
        ff, cf = fin
        for fila in range(fi, ff + 1):
            tablero[fila][ci] = 1

    return tablero


def jugar():
    tablero = generar_tablero()
    disparos = np.zeros((20, 20), dtype=int)

    total_barcos = int(np.sum(tablero == 1))
    jugando = True

    print("Bienvenido a Hundir la Flota")
    print("Introduce coordenadas como: fila,columna (ejemplo: 5,7)\n")

    while jugando:

        print("\nTABLERO DE DISPAROS (0 = sin disparar, 1 = agua, 2 = tocado):")
        print(disparos)

        coord = input("\nIntroduce una coordenada: ")

        # validar formato
        partes = coord.split(",")
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            fila = int(partes[0])
            col = int(partes[1])

            # validar rango
            if 0 <= fila <= MAXIMOTABLERO and 0 <= col <= MAXIMOTABLERO:

                # comprobar si ya disparó ahí
                if disparos[fila][col] == 0:

                    if tablero[fila][col] == 1:
                        print("TOCADO")
                        disparos[fila][col] = 2
                    else:
                        print("AGUA")
                        disparos[fila][col] = 1

                    aciertos = int(np.sum((tablero == 1) & (disparos == 2)))

                    if aciertos == total_barcos:
                        print("\n ¡HAS HUNDIDO TODOS LOS BARCOS!")
                        jugando = False

                else:
                    print("Ya habías disparado en esa posición.")

            else:
                print("Coordenadas fuera del rango 0-19.")
        else:
            print("Formato incorrecto. Usa: fila,columna")


# Ejecutar el juego
jugar()
