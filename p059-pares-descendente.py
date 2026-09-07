#Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el
#usuario..

while True:
    print('\033[H\033[J')
    print("Números pares descendentes y suma")
    print("-" * 40)

    limite = int(input("Introduce un número minimo: "))

    numero = 100
    suma = 0

    print("Números pares:")

    while numero >= limite:
        if numero % 2 == 0:
            print(numero)
            suma += numero

        numero -= 1

    print()
    print(f"La suma de los pares es: {suma}")
    print("-" * 40)

    res = input("\n¿Desea continuar (S/N)? ").upper()

    if res == 'N':
        break

print("\nFin del programa.")