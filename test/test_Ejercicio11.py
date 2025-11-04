import importlib, pytest
Ej = importlib.import_module("Ejercicio11")
def test_ver_tareas(tmp_path):
    fn = getattr(Ej, "ver_tareas", None)
    if not fn: pytest.skip("No se encontró ver_tareas")
    res = fn()
    assert isinstance(res, list)
