import importlib, pytest
Ej = importlib.import_module("Ejercicio7")
def test_estudiantes_aprovados():
    fn = getattr(Ej, "estudiantes_aprovados", None)
    if not fn: pytest.skip("No se encontró estudiantes_aprovados")
    est = [("Ana",4.5),("Juan",2.8),("Maria",3.9)]
    res = fn(est)
    assert isinstance(res, list)
    assert all(t[1]>=3 for t in res)
