#El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión
#a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.


while True:
    print('\033[H\033[J')
    print("Conversión de Celsius a Fahrenheit")
    print("-" * 40)

    temperatura_inicial = int(input("Introduce la temperatura inicial: "))
    temperatura_final = int(input("Introduce la temperatura final: "))

    print("-" * 30)

    temperatura = temperatura_inicial

    while temperatura <= temperatura_final:
        fahrenheit = (temperatura * 9 / 5) + 32

        print(f"{temperatura}°C = {fahrenheit:.1f}°F")

        temperatura += 1

    res = input("¿Desea continuar (S/N)? ").upper()

    if res == 'N':
        break

print("\nFin del programa.")