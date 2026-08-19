#Crea un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo. El programa debe solicitar
#al usuario que ingrese la longitud de los dos lados (catetos) del triángulo. Para el cálculo, utiliza la siguiente
#fórmula:
#• hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

import math

print('Calculando la longitud de la hipotenusa de un triángulo rectángulo.:\n')

print('Dame el cateto 1: ')
cateto1 = float(input())

print('Dame el cateto 2: ')
cateto2 = float(input())

#area = math.pi * radio**2
Hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f'La hipotenusa con los lados {cateto1:.2f} y {cateto2:.2f} es de: {Hipotenusa:.2f}')