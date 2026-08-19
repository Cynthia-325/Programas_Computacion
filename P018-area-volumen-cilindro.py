#Crea un programa que calcule el área y volumen de un cilindro. Pide al usuario que ingrese el radio (R) y la altura
#(h) del cilindro. Las fórmulas para el cálculo de área y de volumen son:
#• Area = 2 π (R + h)
#• Volumen = π * R2 * h

import math

print('Calculando el área y volumen de un cilindro:\n')

print('Ingresa el radio: ')
R = float(input())

print('Ingresa la altura: ')
h = float(input())

A = 2 * math.pi * (R + h)
V = math.pi * (R**2) * h

print(f'El area del cilindro es de {A:.2f} y el volumen de {V:.2f}')