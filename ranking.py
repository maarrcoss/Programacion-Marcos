from utiles import leer_int, imprimir_tabla
from equipos import equipos
from calendario import partidos

def menu_ranking():
    seguir = 1
    while seguir == 1:
        print("\n--- Resultados y Clasificación ---")
        print("1. Registrar resultado")
        print("2. Ver clasificación")
        print("3. Estadísticas por equipo")
        print("4. Volver al menú principal")

        opcion = leer_int("Opción: ", 1, 4)

        if opcion == 1:
            registrar_resultado()
        elif opcion == 2:
            mostrar_clasificacion()
        elif opcion == 3:
            estadisticas_equipo()
        elif opcion == 4:
            seguir = 0

def registrar_resultado():
    id_p = leer_int("ID del partido a registrar: ")
    registrado = 0
    for p in partidos:
        if p["id"] == id_p and p["jugado"] == 0:
            g_local = leer_int("Goles equipo local: ", 0)
            g_visitante = leer_int("Goles equipo visitante: ", 0)
            p["resultado"] = (g_local, g_visitante)
            p["jugado"] = 1
            registrado = 1
    if registrado == 1:
        print("Resultado registrado.")
    else:
        print("Partido no encontrado o ya registrado.")

def mostrar_clasificacion():
    tabla = []
    for e in equipos:
        if e["activo"] == 1:
            pj = g = e_ = p = gf = gc = dg = pts = 0
            for p_part in partidos:
                if p_part["jugado"] == 1:
                    if p_part["local_id"] == e["id"]:
                        pj += 1
                        gf += p_part["resultado"][0]
                        gc += p_part["resultado"][1]
                        if p_part["resultado"][0] > p_part["resultado"][1]:
                            g += 1
                            pts += 3
                        elif p_part["resultado"][0] == p_part["resultado"][1]:
                            e_ += 1
                            pts += 1
                        else:
                            p += 1
                    elif p_part["visitante_id"] == e["id"]:
                        pj += 1
                        gf += p_part["resultado"][1]
                        gc += p_part["resultado"][0]
                        if p_part["resultado"][1] > p_part["resultado"][0]:
                            g += 1
                            pts += 3
                        elif p_part["resultado"][1] == p_part["resultado"][0]:
                            e_ += 1
                            pts += 1
                        else:
                            p += 1
            dg = gf - gc
            tabla.append([e["nombre"], pj, g, e_, p, gf, gc, dg, pts])
    tabla.sort(key=lambda x: x[8], reverse=True)
    imprimir_tabla(tabla, ["Equipo","PJ","G","E","P","GF","GC","DG","PTS"])

def estadisticas_equipo():
    id_e = leer_int("ID del equipo: ")
    encontrado = None
    for e in equipos:
        if e["id"] == id_e and e["activo"] == 1:
            encontrado = e
    if encontrado is None:
        print("Equipo no encontrado o inactivo.")
        return
    pj = g = e_ = p = gf = gc = dg = pts = 0
    for p_part in partidos:
        if p_part["jugado"] == 1:
            if p_part["local_id"] == id_e:
                pj += 1
                gf += p_part["resultado"][0]
                gc += p_part["resultado"][1]
                if p_part["resultado"][0] > p_part["resultado"][1]:
                    g += 1
                    pts += 3
                elif p_part["resultado"][0] == p_part["resultado"][1]:
                    e_ += 1
                    pts += 1
                else:
                    p += 1
            elif p_part["visitante_id"] == id_e:
                pj += 1
                gf += p_part["resultado"][1]
                gc += p_part["resultado"][0]
                if p_part["resultado"][1] > p_part["resultado"][0]:
                    g += 1
                    pts += 3
                elif p_part["resultado"][1] == p_part["resultado"][0]:
                    e_ += 1
                    pts += 1
                else:
                    p += 1
    dg = gf - gc
    imprimir_tabla([[encontrado["nombre"], pj, g, e_, p, gf, gc, dg, pts]], ["Equipo","PJ","G","E","P","GF","GC","DG","PTS"])
