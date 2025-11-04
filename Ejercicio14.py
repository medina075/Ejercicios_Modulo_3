import csv
import json
from typing import List, Dict
from rich.console import Console
from rich.panel import Panel

console = Console()

def ingresar_estudiantes(nombre_archivo: str) -> List[Dict]:
    """Permite ingresar datos de estudiantes y los guarda en un CSV."""
    estudiantes = []
    try:
        cantidad = int(input("¿Cuántos estudiantes deseas ingresar? "))
    except ValueError:
        console.print("[red]Número inválido.[/red]")
        return estudiantes

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["id", "nombre", "edad"])
        for i in range(cantidad):
            print(f"\nEstudiante {i+1}:")
            id_est = input("ID: ").strip()
            nombre = input("Nombre: ").strip()
            edad = input("Edad: ").strip()
            estudiantes.append({"id": id_est, "nombre": nombre, "edad": edad})
            escritor.writerow([id_est, nombre, edad])
    console.print(f"[green]Archivo {nombre_archivo} creado correctamente.[/green]")
    return estudiantes

def ingresar_cursos(nombre_archivo: str) -> List[Dict]:
    """Permite ingresar datos de cursos y los guarda en un JSON."""
    cursos = []
    try:
        cantidad = int(input("\n¿Cuántos cursos deseas registrar? "))
    except ValueError:
        console.print("[red]Número inválido.[/red]")
        return cursos

    for i in range(cantidad):
        print(f"\nCurso {i+1}:")
        id_estudiante = input("ID del estudiante: ").strip()
        curso = input("Nombre del curso: ").strip()
        cursos.append({"id_estudiante": id_estudiante, "curso": curso})

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(cursos, f, indent=2, ensure_ascii=False)
    console.print(f"[green]Archivo {nombre_archivo} creado correctamente.[/green]")
    return cursos

def leer_csv(nombre_archivo: str) -> List[Dict]:
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        console.print(f"[red]No se encontró el archivo {nombre_archivo}[/red]")
        return []

def leer_json(nombre_archivo: str) -> List[Dict]:
    """Lee un archivo JSON y devuelve su contenido."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[red]No se encontró el archivo {nombre_archivo}[/red]")
        return []

def generar_reporte(estudiantes: List[Dict], cursos: List[Dict], nombre_salida: str = "reporte.txt") -> None:
    """Genera y muestra un reporte combinando estudiantes y cursos."""
    lineas = []
    for est in estudiantes:
        nombre = est.get("nombre", "Desconocido")
        cursos_tomados = [c["curso"] for c in cursos if c.get("id_estudiante") == est.get("id")]
        if cursos_tomados:
            linea = f"{nombre} ha tomado los cursos: {', '.join(cursos_tomados)}"
        else:
            linea = f"{nombre} no tiene cursos registrados."
        lineas.append(linea)

    texto_reporte = "\n".join(lineas)

    # Mostrar con rich
    console.print(Panel(texto_reporte, title="Reporte de Estudiantes y Cursos", expand=False))

    # Guardar en archivo
    with open(nombre_salida, "w", encoding="utf-8") as f:
        f.write(texto_reporte)
    console.print(f"[green]Reporte guardado en {nombre_salida}[/green]")

def main() -> None:
    """Ejecuta todo el flujo del programa."""
    console.print("[bold cyan]GENERADOR DE REPORTES[/bold cyan]")

    estudiantes = ingresar_estudiantes("estudiantes.csv")
    cursos = ingresar_cursos("cursos.json")

    if estudiantes and cursos:
        generar_reporte(estudiantes, cursos)
    else:
        console.print("[red]No se pudo generar el reporte por falta de datos.[/red]")

if __name__ == "__main__":
    main()
