def palabras_mayusculas(texto: str) -> list[str]:
    """
    Devuelve todas las palabras con más de 5 letras en mayúsculas.
    """
    return [p.upper() for p in texto.split() if len(p) > 5]


def longitudes(palabras: list[str]) -> dict[str, int]:
    """
    Devuelve un diccionario con cada palabra y su longitud.
    """
    return {p: len(p) for p in palabras}


def main() -> None:
    """
    Prueba rápida del ejercicio 8.
    """
    texto = "Voy a pone' una tiendecita pa' vender cerveza Para yo tomarme una de vez en cuando"
    lista = palabras_mayusculas(texto)
    print("Palabras seleccionadas:", lista)
    print("Longitudes:", longitudes(lista))


if __name__ == "__main__":
    main()
