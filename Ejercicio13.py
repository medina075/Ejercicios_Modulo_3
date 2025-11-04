import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table

console = Console()
ARCHIVO = "inventario.json"

def cargar_inventario() -> List[Dict]:
    """Carga el inventario desde el archivo JSON."""
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_inventario(inventario: List[Dict]) -> None:
    """Guarda el inventario en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=2, ensure_ascii=False)

def agregar_producto() -> None:
    """Agrega un nuevo producto al inventario."""
    inv = cargar_inventario()
    producto = {
        "id": input("ID del producto: "),
        "nombre": input("Nombre del producto: "),
        "cantidad": int(input("Cantidad: ")),
        "precio": float(input("Precio: "))
    }
    inv.append(producto)
    guardar_inventario(inv)
    console.print("[green]Producto agregado correctamente.[/green]")

def vender_producto() -> None:
    """Resta unidades a un producto según la venta realizada."""
    inv = cargar_inventario()
    codigo = input("ID del producto a vender: ")
    cantidad = int(input("Cantidad vendida: "))
    encontrado = False

    for p in inv:
        if p["id"] == codigo:
            encontrado = True
            if p["cantidad"] >= cantidad:
                p["cantidad"] -= cantidad
                guardar_inventario(inv)
                console.print("[green]Venta realizada con éxito.[/green]")
            else:
                console.print("[red]No hay suficiente stock.[/red]")
            break

    if not encontrado:
        console.print("[red]Producto no encontrado.[/red]")

def mostrar_inventario() -> None:
    """Muestra todos los productos usando rich."""
    inv = cargar_inventario()
    if not inv:
        console.print("[yellow]No hay productos registrados.[/yellow]")
        return

    tabla = Table(title="Inventario Actual")
    tabla.add_column("ID", justify="right")
    tabla.add_column("Nombre")
    tabla.add_column("Cantidad", justify="right")
    tabla.add_column("Precio", justify="right")

    for p in inv:
        tabla.add_row(p["id"], p["nombre"], str(p["cantidad"]), f"${p['precio']:.2f}")
    console.print(tabla)

if __name__ == "__main__":
    while True:
        console.print("\n[bold cyan]GESTOR DE INVENTARIO[/bold cyan]")
        print("1. Agregar producto\n2. Ver inventario\n3. Vender producto\n4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            break
        else:
            console.print("[red]Opción no válida[/red]")
