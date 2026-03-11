import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def calcular_imc(peso_lb, estatura_ft):
    peso_kg = peso_lb * 0.453592
    estatura_m = estatura_ft * 0.3048
    imc = peso_kg / (estatura_m ** 2)
    return imc


def recomendacion_calorica(imc):
    if imc < 18.5:
        return "Superávit calórico"
    elif imc < 25:
        return "Mantenimiento calórico"
    else:
        return "Déficit calórico"


def rutina(imc):
    if imc < 18.5:
        return "Entrenamiento de fuerza 4 días por semana."
    elif imc < 25:
        return "Rutina mixta de fuerza y cardio."
    else:
        return "Cardio 4 días y fuerza 2 días."


def dieta(imc):
    if imc < 18.5:
        return "Dieta alta en proteínas y calorías."
    elif imc < 25:
        return "Dieta balanceada."
    else:
        return "Dieta con déficit calórico."


st.title("💪 Analizador Fitness")

nombre = st.text_input("Nombre")
edad = st.number_input("Edad", 10, 80)

sexo = st.selectbox(
    "Sexo",
    ["Mujer", "Hombre"]
)

peso = st.number_input("Peso en libras")
estatura = st.number_input("Estatura en pies")

if st.button("Analizar"):

    imc = calcular_imc(peso, estatura)

    st.write(f"Hola {nombre}")
    st.write(f"Edad: {edad}")
    st.write(f"Tu IMC es: {imc:.2f}")

    st.write("Plan calórico:")
    st.write(recomendacion_calorica(imc))

    st.write("Rutina recomendada:")
    st.write(rutina(imc))

    st.write("Dieta recomendada:")
    st.write(dieta(imc))

    pesos = [peso, peso-2, peso-4, peso-6, peso-8, peso-10]

    meses = ["Mes 1","Mes 2","Mes 3","Mes 4","Mes 5","Mes 6"]

    df = pd.DataFrame({
        "Mes": meses,
        "Peso": pesos
    })

    color = "pink"

    if sexo == "Hombre":
        color = "blue"

    fig, ax = plt.subplots()

    ax.plot(df["Mes"], df["Peso"], marker="o", color=color)

    ax.set_title("Progreso estimado")

    ax.set_xlabel("Mes")

    ax.set_ylabel("Peso")

    st.pyplot(fig)