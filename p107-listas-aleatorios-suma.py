# p107-listas-aleatorios-suma.py
# Sumar elementos cuando ambos son impares

import random

print('\033[H\033[J')
print("Listas de números aleatorios\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

listaA = []
listaB = []
listaC = []

for i in range(10):
    numero = random.randint(1, 20)
    listaA.append(numero)

for i in range(10):
    numero = random.randint(1, 20)
    listaB.append(numero)

for i in range(10):
    if listaA[i] % 2 != 0 and listaB[i] % 2 != 0:
        resultado = listaA[i] + listaB[i]
    else:
        resultado = 0

    listaC.append(resultado)

print("--- Listas Generadas ---")
print(f"Lista A: {listaA}")
print(f"Lista B: {listaB}")

print("\n--- Resultados ---")
print(f"Lista C: {listaC}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")