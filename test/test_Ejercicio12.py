import importlib, pytest
Ej = importlib.import_module("Ejercicio12")
def test_analizar_csv(tmp_path):
    arch = tmp_path/'est.csv'
    arch.write_text('nombre,edad,calificacion\nAna,20,4.5\nJuan,19,3.5\n')
    res = Ej.analizar_csv(str(arch), 'calificacion')
    assert isinstance(res, dict)
    assert 'promedio' in res
