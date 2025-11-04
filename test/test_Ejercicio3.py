import importlib, pytest
Ej = importlib.import_module("Ejercicio3")
def test_crear_contador_independiente():
    crear = getattr(Ej, "crear_contador", None)
    assert crear is not None
    c1 = crear(); c2 = crear()
    assert c1() == 1
    assert c1() == 2
    assert c2() == 1
