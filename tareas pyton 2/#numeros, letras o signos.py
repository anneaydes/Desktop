#numeros, letras o signos
texto = input("Digite un texto: ")

tiene_letras = False
tiene_numeros = False
tiene_signos = False

for caracter in texto:
    if caracter.isalpha():
        tiene_letras = True
    elif caracter.isdigit():
        tiene_numeros = True
    else:
        if caracter != " ":
            tiene_signos = True

if tiene_letras:
    print("El texto contiene LETRAS")
if tiene_numeros:
    print("El texto contiene NÚMEROS")
if tiene_signos:
    print("El texto contiene SIGNOS")
