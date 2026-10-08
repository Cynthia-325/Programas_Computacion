# p105-listas-multiplica.py
# Multiplicar los elementos de dos listas

print('\033[H\033[J')
print("Multiplicación de listas\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

listaA = []
listaB = []
listaC = []

print("Introduzca 5 números para la Lista A:")

for i in range(5):
    numero = float(input(f"Número {i + 1}: "))
    listaA.append(numero)

print("\nIntroduzca 5 números para la Lista B:")

for i in range(5):
    numero = float(input(f"Número {i + 1}: "))
    listaB.append(numero)

for i in range(5):
    resultado = listaA[i] * listaB[i]
    listaC.append(resultado)

print("\n--- Resultados ---")
print(f"Lista A: {listaA}")
print(f"Lista B: {listaB}")
print(f"Lista C (A * B): {listaC}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")