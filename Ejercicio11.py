from typing import List
from rich.console import Console
from rich.table import Table

console = Console()

def agregar_tarea(tarea: str) -> None:
    """Agrega una tarea al archivo."""
    with open("tareas.txt", "a", encoding="utf-8") as f:
        f.write(tarea + "\n")

def ver_tareas() -> List[str]:
    """Devuelve la lista de tareas guardadas."""
    try:
        with open("tareas.txt", "r", encoding="utf-8") as f:
            return [t.strip() for t in f if t.strip()]
    except FileNotFoundError:
        return []

def mostrar_tareas() -> None:
    """Muestra las tareas usando rich."""
    tareas = ver_tareas()
    tabla = Table(title="Tareas")
    tabla.add_column("N°", justify="right")
    tabla.add_column("Tarea")
    for i, t in enumerate(tareas, 1):
        tabla.add_row(str(i), t)
    console.print(tabla)

if __name__ == "__main__":
    while True:
        print("\n1. Agregar tarea\n2. Ver tareas\n3. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            agregar_tarea(input("Nueva tarea: "))
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
