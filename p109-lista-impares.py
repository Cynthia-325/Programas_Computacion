# p109-lista-impares.py
# Generar y analizar números impares

print('\033[H\033[J')
print("Lista de números impares\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

try:
    n = int(input("Introduzca la cantidad de números impares (n): "))

    if n <= 0:
        print("Error: La cantidad debe ser mayor que cero.")
    else:
        impares = []

        for i in range(n):
            numero = 2 * i + 1
            impares.append(numero)

        suma = sum(impares)
        promedio = suma / len(impares)

        divisibles = []

        for numero in impares:
            if numero % 3 == 0:
                divisibles.append(numero)

        suma_divisibles = sum(divisibles)

        print("\n--- Generación de Lista ---")
        print(f"Lista de los primeros {n} números impares: {impares}")

        print("\n--- Cálculos ---")
        print(f"Suma de los números: {suma}")
        print(f"Promedio de los números: {promedio}")

        print("\n--- Divisibles entre 3 ---")
        print(f"Números divisibles entre 3: {divisibles}")
        print(f"Suma de los números divisibles entre 3: {suma_divisibles}")

        print("\n--- Búsqueda ---")
        buscar = int(input("Introduzca elemento a buscar: "))

        if buscar in impares:
            posicion = impares.index(buscar)
            print(f"El elemento {buscar} está en la lista en la posición (índice) {posicion}.")
        else:
            print(f"El elemento {buscar} no está en la lista.")

except ValueError:
    print("Error: Debe introducir un número entero.")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")