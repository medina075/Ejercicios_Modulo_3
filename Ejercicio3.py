def crear_contador():
    conteo = 0

    def incrementar():
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def limite_conteo(valor: int, limite=4) -> bool:
    return valor == limite


def main():
    contador1 = crear_contador()
    print("Iniciar contador hasta el limite ")
    while True:
        valor_actual = contador1()
        print(f"El contador actual es: {valor_actual}")
        if limite_conteo(valor_actual, limite=4):
            print("Limite actual alcanzado 🥵🥵")
            break


if __name__ == "__main__":
    main()
