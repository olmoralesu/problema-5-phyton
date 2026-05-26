# Programa para calcular horas semanales de trabajo
# y clasificar la jornada laboral

# Función para calcular total y clasificación
def calcular_horas(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Matriz de recursos
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 8, 7, 8],
    ["Luis", 9, 9, 10, 9, 9],
    ["Marta", 8, 8, 8, 8, 8]
]

# Mostrar resultados
print("CONTROL DE HORAS SEMANALES\n")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_horas(horas)

    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------")
