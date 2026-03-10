"""
Proyecto: Sistema de Rutina, Dieta y Progreso Fitness

El programa registra personas con su peso en libras y estatura en pies.
Calcula su IMC, recomienda rutina, dieta y estrategia calórica.

También:
- Estima progreso mensual
- Guarda los datos
- Muestra una tabla de usuarios
- Genera una gráfica del peso
"""

import pandas as pd
import matplotlib.pyplot as plt


nombres = []
sexos = []
pesos_lb = []
estaturas_ft = []
imc_lista = []


def convertir_peso(peso_lb):
    """Convierte libras a kilogramos"""
    return peso_lb * 0.453592


def convertir_estatura(estatura_ft):
    """Convierte pies a metros"""
    return estatura_ft * 0.3048


def calcular_imc(peso_lb, estatura_ft):
    """Calcula el IMC usando conversiones"""

    peso_kg = convertir_peso(peso_lb)
    estatura_m = convertir_estatura(estatura_ft)

    imc = peso_kg / (estatura_m ** 2)

    return imc


def recomendar_rutina(imc):
    """Recomienda rutina de gimnasio"""

    print("\n--- Rutina semanal ---")

    if imc < 18.5:

        print("Objetivo: Subir masa muscular")
        print("Lunes: Piernas")
        print("Martes: Pecho")
        print("Miércoles: Descanso")
        print("Jueves: Espalda")
        print("Viernes: Hombros y brazos")

    elif imc < 25:

        print("Objetivo: Mantener condición física")
        print("Lunes: Pecho y tríceps")
        print("Martes: Piernas")
        print("Miércoles: Cardio")
        print("Jueves: Espalda")
        print("Viernes: Hombros")

    else:

        print("Objetivo: Bajar peso")
        print("Lunes: Cardio + Piernas")
        print("Martes: Cardio")
        print("Miércoles: Pecho")
        print("Jueves: Cardio")
        print("Viernes: Espalda")


def recomendar_dieta(imc):
    """Recomienda dieta básica"""

    print("\n--- Dieta recomendada ---")

    if imc < 18.5:

        print("Aumentar calorías saludables")
        print("Avena, huevos, arroz, pollo, aguacate")

    elif imc < 25:

        print("Dieta balanceada")
        print("Proteína, arroz integral, vegetales")

    else:

        print("Reducir calorías")
        print("Más vegetales, proteínas magras")


def recomendacion_calorica(imc):
    """Determina déficit o superávit"""

    if imc < 18.5:

        print("\nDebe hacer SUPERÁVIT CALÓRICO")

        return "superavit"

    elif imc < 25:

        print("\nDebe MANTENER CALORÍAS")

        return "mantener"

    else:

        print("\nDebe hacer DÉFICIT CALÓRICO")

        return "deficit"


def progreso_mensual(peso, tipo):
    """Simula progreso mensual"""

    print("\n--- Progreso estimado en 1 mes ---")

    if tipo == "deficit":

        nuevo_peso = peso - 4
        print("Si sigues la rutina podrías bajar hasta:", nuevo_peso, "lb")

    elif tipo == "superavit":

        nuevo_peso = peso + 3
        print("Si sigues la rutina podrías subir hasta:", nuevo_peso, "lb")

    else:

        print("Tu peso probablemente se mantenga en:", peso, "lb")


def registrar_persona():
    """Registra persona"""

    nombre = input("Ingrese su nombre: ")

    sexo = input("Sexo (M/F): ")

    peso = float(input("Peso en libras: "))

    estatura = float(input("Estatura en pies: "))

    imc = calcular_imc(peso, estatura)

    nombres.append(nombre)
    sexos.append(sexo)
    pesos_lb.append(peso)
    estaturas_ft.append(estatura)
    imc_lista.append(imc)

    print("\nIMC:", round(imc, 2))

    recomendar_rutina(imc)

    recomendar_dieta(imc)

    tipo = recomendacion_calorica(imc)

    progreso_mensual(peso, tipo)


def mostrar_datos():
    """Muestra datos en tabla"""

    if len(nombres) == 0:

        print("No hay datos")

        return

    datos = pd.DataFrame({

        "Nombre": nombres,
        "Sexo": sexos,
        "Peso (lb)": pesos_lb,
        "Estatura (ft)": estaturas_ft,
        "IMC": imc_lista

    })

    print("\nDatos registrados")

    print(datos)


def grafica_peso():
    """Gráfica de peso con color según sexo"""

    if len(nombres) == 0:

        print("No hay datos")

        return

    colores = []

    for sexo in sexos:

        if sexo.upper() == "F":

            colores.append("pink")

        else:

            colores.append("blue")

    plt.bar(nombres, pesos_lb, color=colores)

    plt.title("Peso de los usuarios")

    plt.xlabel("Personas")

    plt.ylabel("Peso en libras")

    plt.show()


while True:

    print("\n----- MENÚ -----")
    print("1 Registrar persona")
    print("2 Mostrar datos")
    print("3 Ver gráfica")
    print("4 Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":

        registrar_persona()

    elif opcion == "2":

        mostrar_datos()

    elif opcion == "3":

        grafica_peso()

    elif opcion == "4":

        print("Programa finalizado")

        break

    else:

        print("Opción incorrecta")