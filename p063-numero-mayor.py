#Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el
#número más grande de todos los introducidos.
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