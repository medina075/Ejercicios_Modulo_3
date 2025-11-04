import importlib, pytest
Ej = importlib.import_module("Ejercicio9")
def test_sumar_lista():
    sumar = getattr(Ej, "sumar_lista", None)
    assert sumar([1,2,3]) == 6
    assert sumar([]) == 0
def test_unir_texto():
    unir = getattr(Ej, "unir_texto", None)
    assert unir(["Hola"," ","SENA"]) == "Hola SENA"
