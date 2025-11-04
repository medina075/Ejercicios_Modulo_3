import importlib, pytest
Ej = importlib.import_module("Ejercicio8")
def test_palabras_mayusculas_y_longitudes():
    fn = getattr(Ej, "palabras_mayusculas", None)
    long = getattr(Ej, "longitudes", None)
    assert fn and long
    texto = "Hola ejemplo EXCEPCIONAL corto palabras"
    resultado = fn(texto)
    assert isinstance(resultado, list)
    mapa = long(["EXCEPCIONAL", "PALABRAS"])
    assert mapa["EXCEPCIONAL"] == 11
