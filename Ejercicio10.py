from typing import Any

def explorar_estructura(elemento: Any, nivel: int = 1) -> None:
    """
    Muestra los valores no iterables de una estructura junto con su profundidad.
    """
    if isinstance(elemento, dict):
        for v in elemento.values():
            explorar_estructura(v, nivel + 1)
    elif isinstance(elemento, (list, tuple, set)):
        for i in elemento:
            explorar_estructura(i, nivel + 1)
    else:
        print(f"Valor: {elemento}, Profundidad: {nivel}")


if __name__ == "__main__":
    datos = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
    explorar_estructura(datos)
