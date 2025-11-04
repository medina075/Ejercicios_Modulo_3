# ejercicio9.py
from functools import reduce
from typing import List

def sumar_lista(numeros: List[int]) -> int:
    """
    Suma los números de una lista usando functools.reduce.
    """
    # Usamos 0 como valor inicial para evitar errores con listas vacías.
    return reduce(lambda a, b: a + b, numeros, 0)


def unir_texto(partes: List[str]) -> str:
    """
    Une los textos de una lista usando functools.reduce.
    Devuelve cadena vacía si la lista está vacía.
    """
    # Convertimos cada elemento a str por seguridad y usamos "" como inicializador.
    return reduce(lambda a, b: a + str(b), partes, "")


def main() -> None:
    """
    Prueba rápida del ejercicio 9.
    """
    print(f"Sumar [1,2,3] ->", sumar_lista([1,2,3]))
    print(f"Unir ['Hola',' ','SENA'] ->", unir_texto(["Hola", " ", "SENA"]))


if __name__ == "__main__":
    main()
