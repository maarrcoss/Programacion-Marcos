import random

# Lista de monstruos y sus niveles de dificultad (1 = fácil, 5 = difícil)
monstruos = {
    'vampiro': 3,
    'momia': 2,
    'bruja': 4,
    'esqueleto': 1,
    'fantasma': 5
}

# Lista de objetos disponibles para capturar
objetos = ['estaca', 'poción mágica', 'hechizo']


def seleccionar_monstruo():
    monstruo = random.choice(list(monstruos.keys()))
    dificultad = monstruos[monstruo]
    return monstruo, dificultad


def calcular_probabilidad(dificultad, objeto):
    bonus = {
        'estaca': 0.3,
        'poción mágica': 0.5,
        'hechizo': 0.4
    }
    base = random.random() 
    probabilidad = base + bonus.get(objeto, 0) - (dificultad * 0.1)
    if probabilidad >= 0.5:
        return True
    else:
        return False


def jugar():
    print("¡Bienvenido a la caza de monstruos de Halloween!")
    monstruo, dificultad = seleccionar_monstruo()
    print(f"Un {monstruo} ha aparecido con dificultad {dificultad}.\n")

    intentos = 3
    capturado = False

    while intentos > 0 and capturado == False:
        print(f"Tienes {intentos} intento(s) restante(s).")
        print("Objetos disponibles:", ", ".join(objetos))
        objeto = input("Elige un objeto para intentar capturarlo: ").lower()

        if objeto in objetos:
            exito = calcular_probabilidad(dificultad, objeto)
            if exito:
                print(f"¡Has capturado al {monstruo} con un/a {objeto}! \n")
                capturado = True
            else:
                print(f"Fallaste al intentar capturar al {monstruo} con un/a {objeto}. \n")
                intentos = intentos - 1
        else:
            print("Objeto no válido. Pierdes un intento.\n")
            intentos = intentos - 1

    if capturado == False:
        print(f"El {monstruo} ha escapado... ¡Mejor suerte la próxima vez!\n")


if __name__ == "__main__":
    jugar()
