import importlib
import pytest

Ej = importlib.import_module("Ejercicio6")

def test_lista_precios_descuento():
    """
    Prueba unitaria para la función lista_precios.
    Verifica que se apliquen correctamente los descuentos del 10% y que los datos
    devueltos mantengan el formato esperado.
    """
    fn = getattr(Ej, "lista_precios", None)
    assert fn is not None, "No se encontró la función lista_precios"

    # Arrange
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Chaqueta", "precio": 100000},
    ]

    # Act
    resultado = fn(productos)

    # Assert
    assert isinstance(resultado, list)
    assert all(isinstance(p, dict) for p in resultado)
    assert all("precio" in p and "nombre" in p for p in resultado)
    # Cada producto debe tener un 10% menos que el precio original
    for i, p in enumerate(resultado):
        esperado = round(productos[i]["precio"] * 0.9, 2)
        assert p["precio"] == esperado
