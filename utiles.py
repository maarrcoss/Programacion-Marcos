from tabulate import tabulate

def generar_id(lista):
    mayor = 0
    for item in lista:
        if item["id"] > mayor:
            mayor = item["id"]
    return mayor + 1

def leer_texto(mensaje):
    texto = ""
    while texto == "":
        texto = input(mensaje).strip()
        if texto == "":
            print("No puede estar vacío.")
    return texto

def leer_int(mensaje, minimo=None, maximo=None):
    while True:
        valor_str = input(mensaje)
        if valor_str.isdigit():
            valor = int(valor_str)
            if minimo is not None and valor < minimo:
                print("Valor menor que el mínimo.")
            elif maximo is not None and valor > maximo:
                print("Valor mayor que el máximo.")
            else:
                return valor
        else:
            print("Debe ser un número entero.")

def imprimir_tabla(filas, columnas):
    if len(filas) > 0:
        print(tabulate(filas, headers=columnas, tablefmt="grid"))
    else:
        print("No hay datos para mostrar.")
