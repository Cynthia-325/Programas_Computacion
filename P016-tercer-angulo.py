#Escribe un programa que determine el tercer ángulo de un triángulo. El programa debe pedir al usuario que ingrese
#las medidas de dos ángulos del triángulo. Utiliza la siguiente fórmula para encontrar el ángulo faltante:
#• angulo3 = 180 – (angulo1 + angulo2)

import math

print('Calculando el tercer ángulo de un triángulo:\n')

print('Dame el primer angulo: ')
A1 = float(input())

print('Dame el segundo angulo: ')
A2 = float(input())

#area = math.pi * radio**2
A3 = 180 -(A1 + A2)

print(f'El tercer ángulo de un triángulo con angulos {A1:.2f} y {A2:.2f} es de: {A3:.2f}')