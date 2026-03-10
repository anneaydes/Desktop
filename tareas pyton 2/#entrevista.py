#entrevista
print("Entrevista para obtener nacionalidad dominicana")

nacio_rd = input("¿Nació en República Dominicana? (si/no): ").lower()
padres_rd = input("¿Sus padres son dominicanos? (si/no): ").lower()
residencia = int(input("¿Cuántos años ha vivido en RD?: "))

if nacio_rd == "si":
    print("Felicidades, usted es dominicano por nacimiento 🇩🇴")
elif padres_rd == "si":
    print("Usted puede optar por nacionalidad dominicana 🇩🇴")
elif residencia >= 10:
    print("Puede solicitar nacionalidad por naturalización 🇩🇴")
else:
    print("No cumple los requisitos para nacionalidad dominicana.")
