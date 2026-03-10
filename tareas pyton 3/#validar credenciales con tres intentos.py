#validar credenciales con tres intentos
usuario_correcto = "admin"
clave_correcta = "1234"

intentos = 3

while intentos > 0:
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido ✅")
        break
    else:
        intentos -= 1
        print(f"Credenciales incorrectas ❌. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Cuenta bloqueada 🚫")
