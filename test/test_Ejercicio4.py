import importlib, pytest
Ej = importlib.import_module("Ejercicio4")

def test_aplicar_validador_numeros():
    aplicar = getattr(Ej, "aplicar_validador", None)
    assert aplicar is not None
    val = lambda x: x > 10
    datos = [5, 12, 20]
    res = aplicar(datos, val)
    assert isinstance(res, list)
    assert all(x > 10 for x in res)
