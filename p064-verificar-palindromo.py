#Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se
#lee igual de izquierda a derecha que de derecha a izquierda

while True:
    print('\033[H\033[J')
    print("Verificar si un número es palíndromo")
    print("-" * 40)

    numero = input("Introduce un número para verificar si es palíndromo: ")

    original = numero
    invertido = ""
    posicion = len(numero) - 1

    while posicion >= 0:
        invertido += numero[posicion]
        posicion -= 1

    if original == invertido:
        print(f"El número {original} es un palíndromo.")
    else:
        print(f"El número {original} no es un palíndromo.")

    res = input("¿Desea continuar (S/N)? ").upper()

    if res == 'N':
        break

print("\nFin del programa.")