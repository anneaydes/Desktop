import pandas as pd
import matplotlib.pyplot as plt

# lista donde guardaremos los datos
semanas = []
pesos = []

def registrar_peso():
    semana = int(input("Ingrese número de semana: "))
    peso = float(input("Ingrese su peso en libras: "))

    semanas.append(semana)
    pesos.append(peso)

    print("Peso registrado correctamente")

def mostrar_datos():
    if len(semanas) == 0:
        print("No hay datos registrados")
        return

    datos = pd.DataFrame({
        "Semana": semanas,
        "Peso": pesos
    })

    print("\nRegistro de progreso")
    print(datos)

def estadisticas():
    if len(pesos) == 0:
        print("No hay datos para analizar")
        return

    datos = pd.DataFrame({
        "Semana": semanas,
        "Peso": pesos
    })

    peso_promedio = datos["Peso"].mean()
    peso_max = datos["Peso"].max()
    peso_min = datos["Peso"].min()

    print("\nEstadísticas del progreso")
    print("Peso promedio:", peso_promedio)
    print("Peso máximo:", peso_max)
    print("Peso mínimo:", peso_min)

def graficar_progreso():
    if len(semanas) == 0:
        print("No hay datos para graficar")
        return

    plt.plot(semanas, pesos, marker='o')
    plt.title("Progreso de Peso por Semana")
    plt.xlabel("Semanas")
    plt.ylabel("Peso")
    plt.show()


while True:

    print("\n---- MENÚ PRINCIPAL ----")
    print("1 Registrar peso")
    print("2 Mostrar datos")
    print("3 Ver estadísticas")
    print("4 Ver gráfica")
    print("5 Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_peso()

    elif opcion == "2":
        mostrar_datos()

    elif opcion == "3":
        estadisticas()

    elif opcion == "4":
        graficar_progreso()

    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida")