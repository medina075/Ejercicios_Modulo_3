def aplicar_validador(datos, validador):
    return [dato for dato in datos if validador(dato)]


def email_validado(email: str) -> bool:
    return "@" in email and "." in email


def numero_valido(numero: str) -> bool:
    try:
        return int(numero) > 10
    except ValueError:
        return False


def main():
    emails = ["kaliuchis@space.com", "maluma@flow.com", "tamal_de_perro.com"]
    numeros = ["15", "10", "03", "69", "0", "9"]

    email_validos = aplicar_validador(emails, email_validado)
    print("Emails validados", email_validos)

    numero_validos = aplicar_validador(numeros, numero_valido)
    print("Numeros validos", numero_validos)


if __name__ == "__main__":
    main()
