# Conversión de moneda
tasa = float(input("Digite la tasa del dólar actual: "))

opcion = int(input("1. Peso a Dólar\n2. Dólar a Peso\nElija una opción: "))

if opcion == 1:
    pesos = float(input("Digite la cantidad en pesos: "))
    dolares = pesos / tasa
    print("Equivale a:", dolares, "dólares")

elif opcion == 2:
    dolares = float(input("Digite la cantidad en dólares: "))
    pesos = dolares * tasa
    print("Equivale a:", pesos, "pesos")

else:
    print("Opción no válida")
