def crear_perfil(nombre: str, edad: int, hobbies: str, redes: str):
    """
    Esta funcion muestra un perfil con nombre, edad, hobbies y redes
    Arg:

    return:
        perfil(str): perfil con nombre, edad, hobbies, redes
    """
    return f"Creando el perfil en la base de datos\n nombre={nombre}\n edad={edad}\n hobbies={hobbies}\n redes={redes}"


def main():
    """
    Esta funcion ingresa los datos para la creacion del perfil
    Arg:
        nombre (str): nombre del perfil
        edad (int): edad del perfil
        hobbies (str): hobbies del perfil
        redes (str): redes del perfil
    :return:
    """
    while True:
        nombre = str(input("Ingresa el nombre del usuario: "))
        if nombre == " " or nombre is None:
            print("el campo tiene que etar lleno baboso")
        else:
            break
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("como va a estar una edad en negativo? te falla 🧠🧠🧠🧠?")
            elif edad > 110:
                print("Como va a tener mas de 110, usted es un mentiroso")
            else:
                break
        except ValueError:
            print("el campo tiene que etar lleno baboso")

    hobbies = []
    redes = []
    hobbies = str(input("Hobbies: ")).strip()
    redes = str(input("Redes: ")).strip()
    perfil = crear_perfil(nombre, edad, hobbies, redes)
    print(perfil)


if __name__ == "__main__":
    main()
