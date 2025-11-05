from utiles import generar_id, leer_texto, leer_int, imprimir_tabla

equipos = []

def menu_equipos():
    seguir = 1
    while seguir == 1:
        print("\n--- Gestión de Equipos ---")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar por ID")
        print("4. Actualizar equipo")
        print("5. Eliminar equipo")
        print("6. Volver al menú principal")

        opcion = leer_int("Opción: ", 1, 6)

        if opcion == 1:
            crear_equipo()
        elif opcion == 2:
            listar_equipos()
        elif opcion == 3:
            buscar_equipo()
        elif opcion == 4:
            actualizar_equipo()
        elif opcion == 5:
            eliminar_equipo()
        elif opcion == 6:
            seguir = 0

def crear_equipo():
    nombre = leer_texto("Nombre del equipo: ")
    ciudad = leer_texto("Ciudad: ")
    equipo = {"id": generar_id(equipos), "nombre": nombre, "ciudad": ciudad, "activo": 1}
    equipos.append(equipo)
    print("Equipo creado correctamente.")

def listar_equipos():
    filas = []
    for e in equipos:
        if e["activo"] == 1:
            filas.append([e["id"], e["nombre"], e["ciudad"]])
    imprimir_tabla(filas, ["ID", "Nombre", "Ciudad"])

def buscar_equipo():
    id_equipo = leer_int("ID del equipo: ")
    encontrado = None
    for e in equipos:
        if e["id"] == id_equipo and e["activo"] == 1:
            encontrado = e
    if encontrado is not None:
        imprimir_tabla([[encontrado["id"], encontrado["nombre"], encontrado["ciudad"]]], ["ID", "Nombre", "Ciudad"])
    else:
        print("Equipo no encontrado o inactivo.")

def actualizar_equipo():
    id_equipo = leer_int("ID del equipo: ")
    actualizado = 0
    for e in equipos:
        if e["id"] == id_equipo and e["activo"] == 1:
            nuevo_nombre = leer_texto("Nuevo nombre (actual: " + e["nombre"] + "): ")
            nueva_ciudad = leer_texto("Nueva ciudad (actual: " + e["ciudad"] + "): ")
            e["nombre"] = nuevo_nombre
            e["ciudad"] = nueva_ciudad
            actualizado = 1
    if actualizado == 1:
        print("Equipo actualizado.")
    else:
        print("Equipo no encontrado o inactivo.")

def eliminar_equipo():
    id_equipo = leer_int("ID del equipo: ")
    eliminado = 0
    for e in equipos:
        if e["id"] == id_equipo and e["activo"] == 1:
            e["activo"] = 0
            eliminado = 1
    if eliminado == 1:
        print("Equipo eliminado (inactivo).")
    else:
        print("Equipo no encontrado o ya inactivo.")
