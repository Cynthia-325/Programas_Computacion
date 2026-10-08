# p104-procesar-notas.py
# Programa para procesar calificaciones usando listas

print('\033[H\033[J')
print("Procesar calificaciones\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

notas = []

while True:
    try:
        nota = float(input("Introduzca nota (0 para detener): "))

        if nota == 0:
            break

        if nota < 0 or nota > 100:
            print("Error: La nota debe estar entre 0 y 100.")
            continue

        notas.append(nota)

    except ValueError:
        print("Error: Debe introducir un número.")

print("\n--- Resultados ---")

if len(notas) == 0:
    print("No se introdujeron notas.")
else:
    suma = sum(notas)
    promedio = suma / len(notas)
    maxima = max(notas)
    minima = min(notas)

    menores = []

    for nota in notas:
        if nota < promedio:
            menores.append(nota)

    print(f"Total de notas introducidas: {len(notas)}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma}")
    print(f"Promedio de notas: {promedio}")
    print(f"Nota máxima: {maxima}")
    print(f"Nota mínima: {minima}")
    print(f"Notas menores al promedio ({promedio}): {len(menores)}")
    print(f"Lista de notas menores al promedio: {menores}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")