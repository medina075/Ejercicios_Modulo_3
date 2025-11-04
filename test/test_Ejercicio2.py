import importlib, pytest
Ej = importlib.import_module("Ejercicio2")

def test_crear_perfil_basico():
    crear = getattr(Ej, "crear_perfil", None)
    assert crear is not None
    perfil = crear("Carlos", 25, "futbol", "leer")
    assert isinstance(perfil, str)
    assert any(nombre in perfil.lower() for nombre in ["carlos", "25", "futbol", "leer"])
