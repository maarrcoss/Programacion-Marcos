from utiles import generar_id, leer_int, leer_texto, imprimir_tabla
from equipos import equipos
from datetime import datetime

partidos = []

def menu_calendario():
    seguir = 1
    while seguir == 1:
        print("\n--- Calendario de Partidos ---")
        print("1. Crear partido")
        print("2. Listar partidos")
        print("3. Reprogramar partido")
        print("4. Eliminar partido")
        print("5. Volver al menú principal")

        opcion = leer_int("Opción: ", 1, 5)

        if opcion == 1:
            crear_partido()
        elif opcion == 2:
            listar_partidos()
        elif opcion == 3:
            reprogramar_partido()
        elif opcion == 4:
            eliminar_partido()
        elif opcion == 5:
            seguir = 0

def crear_partido():
    jornada = leer_int("Número de jornada (>=1): ", 1)
    local = leer_int("ID equipo local: ")
    visitante = leer_int("ID equipo visitante: ")
    fecha = leer_texto("Fecha (YYYY-MM-DD): ")
    hora = leer_texto("Hora (HH:MM): ")

    if local == visitante:
        print("No puede jugar contra sí mismo.")
        return

    local_ok = 0
    vis_ok = 0
    for e in equipos:
        if e["id"] == local and e["activo"] == 1:
            local_ok = 1
        if e["id"] == visitante and e["activo"] == 1:
            vis_ok = 1
    if local_ok == 1 and vis_ok == 1:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            partido = {"id": generar_id(partidos), "jornada": jornada, "local_id": local, "visitante_id": visitante,
                       "fecha": fecha, "hora": hora, "jugado": 0, "resultado": None}
            partidos.append(partido)
            print("Partido creado.")
        except:
            print("Formato de fecha u hora incorrecto.")
    else:
        print("Equipos no válidos o inactivos.")

def listar_partidos():
    filas = []
    for p in partidos:
        nombre_local = "?"
        nombre_vis = "?"
        for e in equipos:
            if e["id"] == p["local_id"]:
                nombre_local = e["nombre"]
            if e["id"] == p["visitante_id"]:
                nombre_vis = e["nombre"]
        estado = "Jugado" if p["jugado"] == 1 else "Pendiente"
        resultado = ""
        if p["resultado"] is not None:
            resultado = str(p["resultado"][0]) + " - " + str(p["resultado"][1])
        filas.append([p["id"], p["jornada"], nombre_local, nombre_vis, p["fecha"], p["hora"], estado, resultado])
    imprimir_tabla(filas, ["ID", "Jornada", "Local", "Visitante", "Fecha", "Hora", "Estado", "Resultado"])

def reprogramar_partido():
    id_p = leer_int("ID del partido: ")
    modificado = 0
    for p in partidos:
        if p["id"] == id_p and p["jugado"] == 0:
            nueva_fecha = leer_texto("Nueva fecha (YYYY-MM-DD): ")
            nueva_hora = leer_texto("Nueva hora (HH:MM): ")
            try:
                datetime.strptime(nueva_fecha, "%Y-%m-%d")
                datetime.strptime(nueva_hora, "%H:%M")
                p["fecha"] = nueva_fecha
                p["hora"] = nueva_hora
                modificado = 1
            except:
                print("Formato incorrecto.")
    if modificado == 1:
        print("Partido reprogramado.")
    else:
        print("Partido no encontrado o ya jugado.")

def eliminar_partido():
    id_p = leer_int("ID del partido: ")
    eliminado = 0
    for p in partidos:
        if p["id"] == id_p and p["jugado"] == 0:
            partidos.remove(p)
            eliminado = 1
    if eliminado == 1:
        print("Partido eliminado.")
    else:
        print("Partido no encontrado o ya jugado.")
