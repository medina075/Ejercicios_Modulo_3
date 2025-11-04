import importlib, pytest
Ej = importlib.import_module("Ejercicio15")
def test_guardar_cargar(tmp_path):
    Ej.ARCHIVO = str(tmp_path/'biblio.json')
    datos = [{'libro_id':'1','titulo':'Libro A','prestado_a':None}]
    Ej.guardar_biblioteca(datos)
    carg = Ej.cargar_biblioteca()
    assert carg[0]['titulo'] == 'Libro A'
