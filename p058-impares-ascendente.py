#Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el
#usuario.

while True:
    print('\033[H\033[J')
    print("Números impares ascendentes y suma")
    print("-" * 40)

    limite = int(input("Introduce un número límite: "))

    numero = 1
    suma = 0

    print("Números impares:")

    while numero <= limite:
        if numero % 2 != 0:
            print(numero)
            suma += numero

        numero += 1

    print()
    print(f"La suma de los impares es: {suma}")
    print("-" * 40)

    res = input("\n¿Desea continuar (S/N)? ").upper()

    if res == 'N':
        break

print("\nFin del programa.")