import importlib, pytest

Ej = importlib.import_module("Ejercicio5")

def test_calculo_iva_y_actualizacion():
    """
    Prueba unitaria para validar el cálculo del IVA y la actualización de la tasa.
    Se valida que las funciones devuelvan tipos correctos y resultados esperados.
    """
    calcular = getattr(Ej, "calculo_iva", None)
    actualizar = getattr(Ej, "actualizar_tasa", None)

    assert calcular is not None, "No se encontró la función 'calculo_iva'"
    assert actualizar is not None, "No se encontró la función 'actualizar_tasa'"

    # Prueba de cálculo normal
    iva, total = calcular(100.0)
    assert isinstance(iva, float)
    assert isinstance(total, float)
    assert iva > 0
    assert total < 100.0  # tu código resta el IVA

    # Prueba de actualización de tasa
    tasa_original = Ej.TASA_IVA
    actualizar(0.10)
    assert Ej.TASA_IVA == 0.10
    iva_nuevo, total_nuevo = calcular(100.0)
    assert iva_nuevo != iva  # debe cambiar
    # Restaurar tasa original
    actualizar(tasa_original)
