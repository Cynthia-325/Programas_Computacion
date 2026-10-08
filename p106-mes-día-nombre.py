# p106-mes-dia-nombre.py
# Mostrar el nombre y los días de un mes

print('\033[H\033[J')
print("Días de los meses del año\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

nombres = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    mes = int(input("Introduzca un número de mes (1-12): "))

    if mes < 1 or mes > 12:
        print("Error: El mes debe estar entre 1 y 12.")
    else:
        print("\n--- Resultados ---")
        print(f"Mes: {nombres[mes - 1]}")
        print(f"Días: {dias[mes - 1]}")

except ValueError:
    print("Error: Debe introducir un número entero.")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")