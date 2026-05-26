"""Problema 5: Una matriz registra las horas trabajadas por un equipo durante la semana: [Nombre del Recurso, Lunes, Martes, ..., Viernes]. Necesitas calcular el total de horas semanales por persona y señalar si alguien excedió las horas estándar.
Requisitos de Desarrollo
-
Matriz: Crear una matriz con 4 recursos y horas trabajadas por día (valores numéricos).
-
Módulos: Se requiere un módulo (función) para calcular la suma total de horas semanales por recurso y clasificar su jornada.
-
Lógica de Negocio:
✓
Calcular la suma de horas para cada recurso.
✓
Clasificar la jornada como "Sobretiempo" si el total de horas es mayor al umbral de 40 horas.
✓
Clasificar como "Horario Estándar" o inferior si no excede el umbral.
-
Salida: Imprimir el nombre de cada recurso, su total de horas semanales y la clasificación de su jornada."""
# -----------------------------------------
# PROBLEMA 5 - EVALUACIÓN FINAL POA
# -----------------------------------------

# Matriz con nombre y horas trabajadas
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 7, 8, 7],
    ["Luis", 9, 9, 10, 9, 8],
    ["Marta", 6, 7, 6, 7, 6]
]

# Función para calcular horas y clasificar jornada
def calcular_horas(datos_recurso):

    nombre = datos_recurso[0]

    # Suma de horas de lunes a viernes
    total_horas = sum(datos_recurso[1:])

    # Clasificación
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# Mostrar resultados
print("REPORTE DE HORAS SEMANALES\n")

for recurso in recursos:

    nombre, total, estado = calcular_horas(recurso)

    print("Recurso:", nombre)
    print("Total Horas:", total)
    print("Clasificación:", estado)
    print("-----------------------------")
    print("-----------------------------")
