#Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos
#números se introdujeron y la suma final.

while True:
    print('\033[H\033[J')
    print("Suma de números hasta alcanzar 200")
    print("-" * 50)

    suma = 0
    contador = 0

    while suma < 200:
        print(f"Suma actual: {suma}.", end=" ")
        numero = int(input("Introduce un número: "))

        suma += numero
        contador += 1

    print("\nMeta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de números introducidos: {contador}")
    print("-" * 50)

    res = input("\n¿Desea continuar (S/N)? ").upper()

    if res == 'N':
        break

print("\nFin del programa.")