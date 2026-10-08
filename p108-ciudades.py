# p108-ciudades.py
# Registrar y ordenar ciudades

print('\033[H\033[J')
print("Lista de ciudades\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

ciudades = []

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")

    if ciudad == "$":
        break

    ciudades.append(ciudad)

ordenadas = sorted(ciudades, reverse=True)

consonantes = []
vocales = "aeiouáéíóúü"

for ciudad in ciudades:
    primera = ciudad[0].lower()

    if primera.isalpha() and primera not in vocales:
        consonantes.append(ciudad)

print("\n--- Resultados ---")
print(f"Total de ciudades introducidas: {len(ciudades)}")
print(f"Lista original: {ciudades}")
print(f"Lista ordenada descendente: {ordenadas}")
print(f"Ciudades que inician con consonante: {len(consonantes)}")
print(f"Lista de ciudades con consonante inicial: {consonantes}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")