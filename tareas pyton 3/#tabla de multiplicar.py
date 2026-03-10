#tabla de multiplicar
numero = int(input("Ingresa el número para ver su tabla de multiplicación: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
