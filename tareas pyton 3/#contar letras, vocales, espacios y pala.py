#contar letras, vocales, espacios y palabras
oracion = input("Escribe una oración: ")

letras = 0
vocales = 0
espacios = 0

for caracter in oracion:
    if caracter.isalpha():
        letras += 1
        if caracter.lower() in "aeiou":
            vocales += 1
    elif caracter == " ":
        espacios += 1

palabras = len(oracion.split())

print("Cantidad de letras:", letras)
print("Cantidad de vocales:", vocales)
print("Cantidad de espacios:", espacios)
print("Cantidad de palabras:", palabras)
