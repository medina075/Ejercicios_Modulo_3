import importlib, pytest
Ej = importlib.import_module("Ejercicio13")
def test_cargar_guardar(tmp_path):
    Ej.ARCHIVO = str(tmp_path/'inv.json')
    data = [{'id':'1','nombre':'Lapiz','cantidad':5,'precio':1000}]
    Ej.guardar_inventario(data)
    carg = Ej.cargar_inventario()
    assert isinstance(carg, list)
