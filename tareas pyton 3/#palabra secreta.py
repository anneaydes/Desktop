#palabra secreta
palabra_secreta = "love"

intento = input("Adivina la palabra secreta: ")

if intento.lower() == palabra_secreta:
    print("¡Correcto! 🎉 Adivinaste la palabra.")
else:
    print("Incorrecto 😢 Intenta nuevamente.")
