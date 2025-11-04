import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table

console = Console()
ARCHIVO = "biblioteca.json"

# ---------------- Funciones de persistencia ----------------

def guardar_biblioteca(libros: List[Dict]) -> None:
    """Guarda la lista de libros en biblioteca.json."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=2, ensure_ascii=False)

def cargar_biblioteca() -> List[Dict]:
    """Carga la biblioteca o devuelve lista vacía si no existe."""
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ---------------- Funciones principales ----------------

def registrar_libros() -> List[Dict]:
    """Permite ingresar manualmente los libros iniciales."""
    libros = []
    try:
        cantidad = int(input("¿Cuántos libros deseas registrar? "))
    except ValueError:
        console.print("[red]Número inválido.[/red]")
        return libros

    for i in range(cantidad):
        print(f"\nLibro {i+1}:")
        libro_id = input("ID del libro: ").strip()
        titulo = input("Título del libro: ").strip()
        libros.append({"libro_id": libro_id, "titulo": titulo, "prestado_a": None})

    guardar_biblioteca(libros)
    console.print(f"[green]{cantidad} libros registrados correctamente.[/green]")
    return libros

def prestar_libro(libro_id: str, nombre_aprendiz: str) -> None:
    """Marca un libro como prestado."""
    libros = cargar_biblioteca()
    for l in libros:
        if l["libro_id"] == libro_id:
            if l["prestado_a"]:
                console.print(f"[red]El libro '{l['titulo']}' ya está prestado a {l['prestado_a']}.[/red]")
                return
            l["prestado_a"] = nombre_aprendiz
            guardar_biblioteca(libros)
            console.print(f"[green]Libro '{l['titulo']}' prestado a {nombre_aprendiz}.[/green]")
            return
    console.print("[red]Libro no encontrado.[/red]")

def devolver_libro(libro_id: str) -> None:
    """Marca un libro como devuelto."""
    libros = cargar_biblioteca()
    for l in libros:
        if l["libro_id"] == libro_id:
            if not l["prestado_a"]:
                console.print("[yellow]Ese libro ya está disponible.[/yellow]")
                return
            l["prestado_a"] = None
            guardar_biblioteca(libros)
            console.print(f"[green]Libro '{l['titulo']}' devuelto correctamente.[/green]")
            return
    console.print("[red]Libro no encontrado.[/red]")

def buscar_libro(query: str) -> None:
    """Busca libros por título y los muestra en una tabla."""
    libros = cargar_biblioteca()
    resultados = [l for l in libros if query.lower() in l["titulo"].lower()]
    tabla = Table(title=f"Resultados para '{query}'")
    tabla.add_column("ID", justify="right")
    tabla.add_column("Título")
    tabla.add_column("Prestado a")

    if resultados:
        for l in resultados:
            tabla.add_row(l["libro_id"], l["titulo"], l["prestado_a"] or "Disponible")
    else:
        tabla.add_row("-", "Sin resultados", "-")
    console.print(tabla)

def ver_libros_prestados() -> None:
    """Muestra todos los libros actualmente prestados."""
    libros = cargar_biblioteca()
    prestados = [l for l in libros if l["prestado_a"]]
    tabla = Table(title="Libros Prestados")
    tabla.add_column("ID", justify="right")
    tabla.add_column("Título")
    tabla.add_column("Prestado a")

    if prestados:
        for l in prestados:
            tabla.add_row(l["libro_id"], l["titulo"], l["prestado_a"])
    else:
        tabla.add_row("-", "Ninguno", "-")
    console.print(tabla)

# ---------------- Menú principal ----------------

def main() -> None:
    """Ejecuta el sistema interactivo de biblioteca."""
    libros = cargar_biblioteca()
    if not libros:
        registrar_libros()

    while True:
        console.print("\n[bold cyan]SISTEMA DE BIBLIOTECA[/bold cyan]")
        print("1. Ver libros prestados")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Agregar libro nuevo")
        print("6. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            ver_libros_prestados()
        elif opcion == "2":
            buscar_libro(input("Título a buscar: "))
        elif opcion == "3":
            prestar_libro(input("ID del libro: "), input("Nombre del aprendiz: "))
        elif opcion == "4":
            devolver_libro(input("ID del libro: "))
        elif opcion == "5":
            registrar_libros()
        elif opcion == "6":
            break
        else:
            console.print("[red]Opción no válida.[/red]")

if __name__ == "__main__":
    main()
