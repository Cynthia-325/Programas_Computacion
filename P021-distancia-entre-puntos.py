#Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano. El programa debe pedir al usuario
#que ingrese las coordenadas del punto A (x1,y1) y las coordenadas del punto B (x2,y2). Utiliza la siguiente fórmula
#para calcular la distancia:

import math

print('Ingresa cordenadas:')
print('X1: ')
x1 = int(input())

print('X2: ')
x2 = int(input())

print('Y1: ')
y1 = int(input())

print('Y2: ')
y2 = int(input())

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'Distancia: {distancia : .2f}')