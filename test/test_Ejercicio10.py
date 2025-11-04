import importlib, pytest
Ej = importlib.import_module("Ejercicio10")
def test_explorar_estructura(capsys):
    fn = getattr(Ej, "explorar_estructura", None)
    assert fn
    fn([1,[2,3],{"a":4}])
    salida = capsys.readouterr().out
    assert "Valor" in salida
