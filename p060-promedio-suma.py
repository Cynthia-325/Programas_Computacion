#Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la
#suma y el promedio de la serie.

while True:
    print('\033[H\033[J')
    print("Ingresar 0 para terminar")
    print("-" * 40)

    
    numero = 1
    while numero != 0:
        numero = int(input("Introduce un número: "))
        suma += numero

    print()
    print(f"La suma de los numeros es: {suma}")
    print("-" * 40)

    res = input("\n¿Desea continuar (S/N)? ").upper()

    if res == 'N':
        break

print("\nFin del programa.")