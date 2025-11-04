import pytest, importlib
Ej = importlib.import_module("Ejercicio1")

def test_calcular_imc_valores():
    calcular = getattr(Ej, "calcular_imc", None)
    assert calcular is not None
    imc = calcular(70.0, 1.75)
    assert isinstance(imc, float)
    assert 20.0 <= imc <= 24.0

def test_interpretar_imc_categorias():
    interpretar = getattr(Ej, "interpretar_imc", None)
    if interpretar is None:
        pytest.skip("No se encontró la función interpretar_imc")

    texto_bajo = interpretar(16.0).lower()
    assert any(pal in texto_bajo for pal in ["bajo", "peso", "flaco", "delgado", "desnutrido", "re flaco"])

    texto_normal = interpretar(22.0).lower()
    # Acepta tu expresión "re chimba" y otras posibles
    assert any(pal in texto_normal for pal in ["chimba", "normal", "bien", "adecuado", "salud"])

    texto_sobre = interpretar(28.0).lower()
    assert any(pal in texto_sobre for pal in ["sobre", "alto", "peso", "gordo", "exceso", "ojo", "baje"])
