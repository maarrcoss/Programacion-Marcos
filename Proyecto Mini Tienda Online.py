#Definimos las variables
articulos = []    
usuarios = []     
carrito_actual = [] 
usuario_activo = None
ventas = []       

#Definimos las funciones
def generar_id(lista):
    maximo=0
    for item in lista:
        if item["id"]>maximo:
            maximo=item["id"]
    return maximo+1

def leer_texto(mensaje):
    texto=""
    while texto=="":
        texto=input(mensaje).strip()
        if texto=="": print("No puede estar vacío.")
    return texto

def leer_entero(mensaje,minimo):
    while True:
        entrada=input(mensaje).strip()
        if entrada.isdigit():
            valor=int(entrada)
            if valor>=minimo: return valor
            else: print("Debe ser >= ",minimo)
        else: print("Número no válido.")

def leer_numero(mensaje,minimo):
    while True:
        entrada=input(mensaje).strip()
        partes=entrada.split(".")
        if len(partes)<=2 and all(p.isdigit() for p in partes if p!=""):
            valor=float(entrada)
            if valor>=minimo: return valor
            else: print("Debe ser >= ",minimo)
        else: print("Número no válido.")

def mostrar_item(item, tipo="general"):
    estado="Activo" if item["activo"]==1 else "Inactivo"
    if tipo=="articulo":
        print(f"ID:{item['id']} | {item['nombre']} | {item['precio']}€ | Stock:{item['stock']} | {estado}")
    elif tipo=="usuario":
        print(f"ID:{item['id']} | {item['nombre']} | {item['email']} | {estado}")

def listar_items(lista, solo_activos=None, tipo="general"):
    for item in lista:
        if solo_activos is None or item["activo"]==solo_activos:
            mostrar_item(item,tipo)

def buscar_por_id(lista,id_buscar):
    for item in lista:
        if item["id"]==id_buscar: return item
    return None

def alternar_activo(lista,id_buscar):
    item=buscar_por_id(lista,id_buscar)
    if item is None: print("No encontrado.")
    else:
        item["activo"]=0 if item["activo"]==1 else 1
        print("Estado cambiado a:", "Activo" if item["activo"]==1 else "Inactivo")

def eliminar_item(lista,id_buscar):
    i=0
    while i<len(lista):
        if lista[i]["id"]==id_buscar:
            lista.pop(i)
            print("Eliminado.")
            i=len(lista)
        else: i+=1

#FUNCIONES ARTICULOS
def art_crear():
    nombre=leer_texto("Nombre del artículo: ")
    precio=leer_numero("Precio (>0): ",0.01)
    stock=leer_entero("Stock (>=0): ",0)
    articulos.append({"id":generar_id(articulos),"nombre":nombre,"precio":round(precio,2),"stock":stock,"activo":1})
    print("Artículo creado.")

def art_listar():
    print("\n1. Todos\n2. Solo activos\n3. Solo inactivos")
    opc=input("Elige: ").strip()
    if opc=="2": listar_items(articulos,1,"articulo")
    elif opc=="3": listar_items(articulos,0,"articulo")
    else: listar_items(articulos,None,"articulo")

def art_buscar():
    idb=leer_entero("ID a buscar: ",1)
    art=buscar_por_id(articulos,idb)
    if art: mostrar_item(art,"articulo")
    else: print("No encontrado.")

def art_actualizar():
    idb=leer_entero("ID a actualizar: ",1)
    art=buscar_por_id(articulos,idb)
    if art is None: print("No encontrado."); return
    n=input(f"Nombre ({art['nombre']}): ").strip()
    if n!="": art["nombre"]=n
    p=input(f"Precio ({art['precio']}): ").strip()
    if p.replace(".","",1).isdigit(): art["precio"]=round(float(p),2)
    s=input(f"Stock ({art['stock']}): ").strip()
    if s.isdigit(): art["stock"]=int(s)
    print("Actualizado.")

def menu_articulos():
    ejecutando=1
    while ejecutando==1:
        print("\n--- ARTÍCULOS ---")
        print("1. Crear artículo")
        print("2. Listar artículos")
        print("3. Buscar artículo por id")
        print("4. Actualizar artículo")
        print("5. Eliminar artículo")
        print("6. Alternar activo/inactivo")
        print("7. Volver")
        op=input("Opción: ").strip()
        if op=="1": art_crear()
        elif op=="2": art_listar()
        elif op=="3": art_buscar()
        elif op=="4": art_actualizar()
        elif op=="5":
            idb=leer_entero("ID a eliminar: ",1)
            eliminar_item(articulos,idb)
        elif op=="6":
            idb=leer_entero("ID a alternar: ",1)
            alternar_activo(articulos,idb)
        elif op=="7": ejecutando=0
        else: print("Opción no válida.")

#FUNCIONES USUARIOS
def usr_crear():
    nombre=leer_texto("Nombre del usuario: ")
    while True:
        email=input("Email: ").strip()
        if "@" in email and "." in email: break
        print("Email inválido.")
    usuarios.append({"id":generar_id(usuarios),"nombre":nombre,"email":email,"activo":1})
    print("Usuario creado.")

def usr_listar():
    print("\n1. Todos\n2. Solo activos\n3. Solo inactivos")
    opc=input("Elige: ").strip()
    if opc=="2": listar_items(usuarios,1,"usuario")
    elif opc=="3": listar_items(usuarios,0,"usuario")
    else: listar_items(usuarios,None,"usuario")

def usr_buscar():
    idb=leer_entero("ID a buscar: ",1)
    usr=buscar_por_id(usuarios,idb)
    if usr: mostrar_item(usr,"usuario")
    else: print("No encontrado.")

def usr_actualizar():
    idb=leer_entero("ID a actualizar: ",1)
    usr=buscar_por_id(usuarios,idb)
    if usr is None: print("No encontrado."); return
    n=input(f"Nombre ({usr['nombre']}): ").strip()
    if n!="": usr["nombre"]=n
    e=input(f"Email ({usr['email']}): ").strip()
    if e!="" and "@" in e and "." in e: usr["email"]=e
    print("Actualizado.")

def menu_usuarios():
    ejecutando=1
    while ejecutando==1:
        print("\n--- USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por id")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Alternar activo/inactivo")
        print("7. Volver")
        op=input("Opción: ").strip()
        if op=="1": usr_crear()
        elif op=="2": usr_listar()
        elif op=="3": usr_buscar()
        elif op=="4": usr_actualizar()
        elif op=="5":
            idb=leer_entero("ID a eliminar: ",1)
            eliminar_item(usuarios,idb)
        elif op=="6":
            idb=leer_entero("ID a alternar: ",1)
            alternar_activo(usuarios,idb)
        elif op=="7": ejecutando=0
        else: print("Opción no válida.")

#FUNCIONES VENTAS / CARRITO
def seleccionar_usuario_activo():
    global usuario_activo
    idb=leer_entero("ID de usuario: ",1)
    usr=buscar_por_id(usuarios,idb)
    if usr and usr["activo"]==1:
        usuario_activo=idb
        print(f"Usuario activo: {usr['nombre']}")
    else: print("Usuario no válido o inactivo.")

def anadir_al_carrito():
    if usuario_activo is None: print("Primero selecciona usuario."); return
    idb=leer_entero("ID artículo: ",1)
    art=buscar_por_id(articulos,idb)
    if art is None or art["activo"]==0: print("Artículo no válido."); return
    cant=leer_entero("Cantidad: ",1)
    if cant>art["stock"]: print("Stock insuficiente."); return
    for i in range(len(carrito_actual)):
        if carrito_actual[i][0]==idb:
            carrito_actual[i]=(idb,carrito_actual[i][1]+cant)
            print("Cantidad sumada al carrito."); return
    carrito_actual.append((idb,cant))
    print("Añadido al carrito.")

def quitar_del_carrito():
    if not carrito_actual: print("Carrito vacío."); return
    idb=leer_entero("ID artículo a quitar: ",1)
    i=0
    encontrado=False
    while i<len(carrito_actual):
        if carrito_actual[i][0]==idb:
            carrito_actual.pop(i)
            print("Artículo eliminado del carrito.")
            encontrado=True
            i=len(carrito_actual)
        else: i+=1
    if not encontrado: print("No estaba en el carrito.")

def ver_carrito():
    if not carrito_actual: print("Carrito vacío."); return
    total=0
    print("\nCarrito actual:")
    for art_id,cant in carrito_actual:
        art=buscar_por_id(articulos,art_id)
        if art:
            subtotal=art["precio"]*cant
            total+=subtotal
            print(f"{art['nombre']} x{cant} = {subtotal}€")
    print("TOTAL:",round(total,2))

def confirmar_compra():
    global carrito_actual
    if usuario_activo is None: print("Selecciona usuario primero."); return
    if not carrito_actual: print("Carrito vacío."); return
    total=0
    items=[]
    for art_id,cant in carrito_actual:
        art=buscar_por_id(articulos,art_id)
        if art is None or art["activo"]==0 or cant>art["stock"]:
            print("Error con el artículo",art_id); return
        subtotal=art["precio"]*cant
        total+=subtotal
        items.append((art_id,cant,art["precio"]))
    for art_id,cant,_ in items:
        art=buscar_por_id(articulos,art_id)
        art["stock"]-=cant
    ventas.append({"id_venta":generar_id(ventas),"usuario_id":usuario_activo,"items":items,"total":round(total,2)})
    carrito_actual=[]
    print("Compra confirmada. Total:",round(total,2))

def historial_ventas():
    if usuario_activo is None: print("Selecciona usuario primero."); return
    print(f"\nHistorial usuario ID {usuario_activo}:")
    for v in ventas:
        if v["usuario_id"]==usuario_activo:
            print(f"Venta {v['id_venta']} | Total: {v['total']}€")
            for art_id,cant,precio in v["items"]:
                art=buscar_por_id(articulos,art_id)
                if art: print(f"  {art['nombre']} x{cant} @ {precio}€")

def vaciar_carrito():
    global carrito_actual
    carrito_actual=[]
    print("Carrito vaciado.")

def menu_ventas():
    ejecutando=1
    while ejecutando==1:
        print("\n--- VENTAS / CARRITO ---")
        print("1. Seleccionar usuario activo")
        print("2. Añadir artículo al carrito")
        print("3. Quitar artículo del carrito")
        print("4. Ver carrito")
        print("5. Confirmar compra")
        print("6. Historial de ventas por usuario")
        print("7. Vaciar carrito")
        print("8. Volver")
        op=input("Opción: ").strip()
        if op=="1": seleccionar_usuario_activo()
        elif op=="2": anadir_al_carrito()
        elif op=="3": quitar_del_carrito()
        elif op=="4": ver_carrito()
        elif op=="5": confirmar_compra()
        elif op=="6": historial_ventas()
        elif op=="7": vaciar_carrito()
        elif op=="8": ejecutando=0
        else: print("Opción no válida.")

#Definimos la lógica del programa
def menu_principal():
    ejecutando=1
    while ejecutando==1:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Artículos")
        print("2. Gestión de Usuarios")
        print("3. Ventas / Carrito")
        print("4. Salir")
        op=input("Elige opción: ").strip()
        if op=="1": menu_articulos()
        elif op=="2": menu_usuarios()
        elif op=="3": menu_ventas()
        elif op=="4": ejecutando=0
        else: print("Opción no válida.")

if __name__=="__main__":
    menu_principal()
