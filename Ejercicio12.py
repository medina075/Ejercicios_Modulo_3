import csv
from typing import Dict
from rich.console import Console
from rich.table import Table

console = Console()

def crear_csv(nombre_archivo: str, cantidad: int) -> None:
    """Crea o sobreescribe un CSV con los datos de los estudiantes ingresados."""
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre", "edad", "calificacion"])
        for i in range(cantidad):
            print(f"\nEstudiante {i+1}:")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            calificacion = input("Calificación: ")
            escritor.writerow([nombre, edad, calificacion])
    console.print("[green]Datos guardados correctamente.[/green]")


def analizar_csv(nombre_archivo: str, columna: str) -> Dict[str, float]:
    """Lee un CSV y calcula promedio, máximo y mínimo de una columna numérica."""
    valores = []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            try:
                valores.append(float(fila[columna]))
            except (ValueError, KeyError):
                pass

    if not valores:
        return {"promedio": 0.0, "max": 0.0, "min": 0.0}

    return {
        "promedio": sum(valores) / len(valores),
        "max": max(valores),
        "min": min(valores)
    }


def mostrar_resultados(datos: Dict[str, float]) -> None:
    """Muestra los resultados en una tabla usando rich."""
    tabla = Table(title="Resultados del Análisis")
    tabla.add_column("Métrica")
    tabla.add_column("Valor", justify="right")
    for k, v in datos.items():
        tabla.add_row(k.capitalize(), f"{v:.2f}")
    console.print(tabla)


if __name__ == "__main__":
    archivo = "estudiantes.csv"
    try:
        cantidad = int(input("¿Cuántos estudiantes deseas ingresar? "))
        crear_csv(archivo, cantidad)
        resultados = analizar_csv(archivo, "calificacion")
        mostrar_resultados(resultados)
    except ValueError:
        console.print("[red]Debes ingresar un número válido.[/red]")
