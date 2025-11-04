import importlib, pytest, json
Ej = importlib.import_module("Ejercicio14")
def test_generar_reporte(tmp_path):
    est = tmp_path/'est.csv'
    cur = tmp_path/'cursos.json'
    rep = tmp_path/'reporte.txt'
    est.write_text('id,nombre,edad\n1,Ana,20\n')
    cur.write_text(json.dumps([{'id_estudiante':'1','curso':'Python'}]))
    ests = Ej.leer_csv(str(est))
    cursos = Ej.leer_json(str(cur))
    Ej.generar_reporte(ests,cursos,str(rep))
    assert rep.exists()
