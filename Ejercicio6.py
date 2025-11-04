def lista_precios(productos):
    precios_desc = list(map(lambda p: {"nombre": p["nombre"], "precio":round(p["precio"]*0.9,2)}, productos))
    return precios_desc
def main():
    productos = [
        {"nombre":"camisa","precio":50000},
        {"nombre":"pantalon","precio":120000},
        {"nombre":"chaqueta","precio":80000},
    ]
    product_desc = lista_precios(productos)
    print("Lista con 10% de descuento:")
    for p in product_desc:
        print(f"{p['nombre']}: ${p['precio']:.2f}")
if __name__ == "__main__":
    main()