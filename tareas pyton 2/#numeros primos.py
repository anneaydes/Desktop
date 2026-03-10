#numeros primos
numero = int(input("Digite un número: "))

if numero <= 1:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print("El número es PRIMO")
    else:
        print("El número NO es primo")
