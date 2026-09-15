print('\033[H\033[J')
print('Imprime una piramide de caracteres')
altura = int(input("Introduce la altura de la pirámide: "))
car = input("Introduce el carácter para la pirámide: ")

print("\n--- Pirámide Generada ---")
print("\n   🐱‍👤🐱‍👤🐱‍👤")

for i in range(1, altura + 1):
    espacios = altura - i
    caracteres = 2 * i - 1

    for j in range(espacios):
        print(" ", end="")
    for k in range(caracteres):
        print(car, end="")
    print()