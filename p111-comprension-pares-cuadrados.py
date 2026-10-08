# p111-comprension-pares-cuadrados.py
# Calcular los cuadrados de los números pares

print('\033[H\033[J')
print("Cuadrados de números pares\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

try:
    n = int(input("Introduzca el límite n: "))

    if n < 1:
        print("Error: El límite debe ser mayor que cero.")
    else:
        numeros = list(range(1, n + 1))

        cuadrados = [numero ** 2 for numero in numeros if numero % 2 == 0]

        suma = sum(cuadrados)

        print("\n--- Resultados ---")
        print(f"Lista original (1 a {n}): {numeros}")
        print(f"Cuadrados de números pares: {cuadrados}")
        print(f"Suma de cuadrados: {suma}")

except ValueError:
    print("Error: Debe introducir un número entero.")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")