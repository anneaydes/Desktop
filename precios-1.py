#
precio1 = float (input("ingrese el precio:"))
precio2 = float (input("ingrese el precio:"))
precio3 = float (input("ingrese el precio:"))
precio4 = float (input("ingrese el precio:"))
precio5 = float (input("ingrese el precio:"))


#Total

total = precio1 + precio2 + precio3 + precio4 + precio5

#porcentaje
porcentaje = float(input("ingrese el porcentaje:"))

#Monto a pagar

monto_a_pagar = total * (porcentaje / 100)
resto = total - monto_a_pagar

print ("el total es:", total)
print ("el porcentaje es:", porcentaje)
print ("el monto a pagar es:", monto_a_pagar)

print ("Gracias por preferirnos")


