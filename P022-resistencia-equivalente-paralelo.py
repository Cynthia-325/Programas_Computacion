#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.
#El programa debe solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias (R1, R2, R3 y R4).
#Luego, debe calcular la resistencia total usando la siguiente fórmula:

import math

print('Calcular resistencia total para 4 resistencias en paralelo')

print('Ingresa resistencias:')
print('R1: ')
r1 = int(input())

print('R2: ')
r2 = int(input())

print('R3: ')
r3 = int(input())

print('R4: ')
r4 = int(input())

total = 1 / ((1/r1) + (1/r2) + (1/r3) + (1/r4))

print(f'Resistencia total: {total : .2f}')