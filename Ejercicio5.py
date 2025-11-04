TASA_IVA = 0.19

def calculo_iva(precio_base):
    valor1 = precio_base * TASA_IVA
    valor2 = precio_base - valor1
    return valor1 , valor2

def actualizar_tasa(nueva_tasa):
    global TASA_IVA
    TASA_IVA = nueva_tasa

def main():
    while True:
        precio_base = float(input("Ingresa el valor actual: "))
        if precio_base < 0:
            print("Como va a ser un valor negativo te falla el ..🧠🧠")
        elif precio_base == " " or precio_base == None:
            print("Como va a ser un precio sin ningun valor, IDIOTA")
        else:
            break
    valor1, valor2 = calculo_iva(precio_base)
    print(f"El precio del valor de iva es: {valor1:.2f}")
    print(f"El valor total con iva es: {valor2:.2f}")

    while True:
        nueva_tasa = float(input("Ingresa el valor de tasa actual: "))
        if nueva_tasa < 0:
            print("De nuevo?... estas mal del 🥥🥥")
        elif nueva_tasa == " " or nueva_tasa == None:
            print("No puedo creer lo pendejo, digita un valor REAL")
        else:
            actualizar_tasa(nueva_tasa)
            break
    valor3, valor4 = calculo_iva(precio_base)
    print ("Calculo con la nueva tasa")
    print(f"El precio del valor de iva es: {valor3:.2f}")
    print(f"El valor total con iva es: {valor4:.2f}")

if __name__ == "__main__":
    main()
