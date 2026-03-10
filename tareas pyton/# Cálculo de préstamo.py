# Cálculo de préstamo
prestamo = float(input("Digite el valor del préstamo: "))
tiempo = float(input("Digite el tiempo (en años): "))
interes = float(input("Digite el interés anual (%): "))

total_interes = prestamo * (interes / 100) * tiempo
total_pagar = prestamo + total_interes

print("El total a pagar es:", total_pagar)
