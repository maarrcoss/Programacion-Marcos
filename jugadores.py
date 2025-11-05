from utiles import generar_id, leer_texto, leer_int, imprimir_tabla
from equipos import equipos

jugadores = []

def menu_jugadores():
    seguir = 1
    while seguir == 1:
        print("\n--- Gestión de Jugadores ---")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Buscar jugador")
        print("4. Actualizar jugador")
        print("5. Eliminar jugador")
        print("6. Volver al menú principal")

        opcion = leer_int("Opción: ", 1, 6)

        if opcion == 1:
            crear_jugador()
        elif opcion == 2:
            listar_jugadores()
        elif opcion == 3:
            buscar_jugador()
        elif opcion == 4:
            actualizar_jugador()
        elif opcion == 5:
            eliminar_jugador()
        elif opcion == 6:
            seguir = 0

def crear_jugador():
    nombre = leer_texto("Nombre del jugador: ")
    posicion = leer_texto("Posición: ")
    equipo_id = leer_int("ID del equipo: ")

    equipo_valido = 0
    for e in equipos:
        if e["id"] == equipo_id and e["activo"] == 1:
            equipo_valido = 1
    if equipo_valido == 0:
        print("Equipo no válido o inactivo.")
    else:
        jugador = {"id": generar_id(jugadores), "nombre": nombre, "posicion": posicion, "equipo_id": equipo_id, "activo": 1}
        jugadores.append(jugador)
        print("Jugador creado correctamente.")

def listar_jugadores():
    filas = []
    for j in jugadores:
        if j["activo"] == 1:
            nombre_equipo = "Sin equipo"
            for e in equipos:
                if e["id"] == j["equipo_id"]:
                    nombre_equipo = e["nombre"]
            filas.append([j["id"], j["nombre"], j["posicion"], nombre_equipo])
    imprimir_tabla(filas, ["ID", "Nombre", "Posición", "Equipo"])

def buscar_jugador():
    id_j = leer_int("ID del jugador: ")
    encontrado = None
    for j in jugadores:
        if j["id"] == id_j and j["activo"] == 1:
            encontrado = j
    if encontrado is not None:
        nombre_equipo = "Sin equipo"
        for e in equipos:
            if e["id"] == encontrado["equipo_id"]:
                nombre_equipo = e["nombre"]
        imprimir_tabla([[encontrado["id"], encontrado["nombre"], encontrado["posicion"], nombre_equipo]],
                       ["ID", "Nombre", "Posición", "Equipo"])
    else:
        print("Jugador no encontrado.")

def actualizar_jugador():
    id_j = leer_int("ID del jugador: ")
    actualizado = 0
    for j in jugadores:
        if j["id"] == id_j and j["activo"] == 1:
            nuevo_nombre = leer_texto("Nuevo nombre (actual: " + j["nombre"] + "): ")
            nueva_pos = leer_texto("Nueva posición (actual: " + j["posicion"] + "): ")
            nuevo_equipo = leer_int("Nuevo ID de equipo (actual: " + str(j["equipo_id"]) + "): ")
            equipo_valido = 0
            for e in equipos:
                if e["id"] == nuevo_equipo and e["activo"] == 1:
                    equipo_valido = 1
            if equipo_valido == 1:
                j["nombre"] = nuevo_nombre
                j["posicion"] = nueva_pos
                j["equipo_id"] = nuevo_equipo
                actualizado = 1
    if actualizado == 1:
        print("Jugador actualizado.")
    else:
        print("Jugador no encontrado o equipo no válido.")

def eliminar_jugador():
    id_j = leer_int("ID del jugador: ")
    eliminado = 0
    for j in jugadores:
        if j["id"] == id_j and j["activo"] == 1:
            j["activo"] = 0
            eliminado = 1
    if eliminado == 1:
        print("Jugador eliminado (inactivo).")
    else:
        print("Jugador no encontrado.")
