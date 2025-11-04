def estudiantes_aprovados(estudiantes):
    notas_aprovadas = list(filter(lambda n: n[1] >= 3.0, estudiantes))
    return notas_aprovadas

def main():
    estudiantes = [("Mariana", 2.5),("Vannesa",2.8),("Angie",4.0),("Sara",3.0),("Valentina",2.9),("Laura",5.0)]
    aprovados = estudiantes_aprovados(estudiantes)
    print("Estudiantes aprovadas")
    for estudiante in aprovados:
        print(estudiante)
if __name__ == "__main__":
    main()


