#Diseña un programa que tome una cantidad de horas como un número entero. El programa debe calcular y mostrar
#el equivalente de ese tiempo en:
#• Días (considerando que 1 día tiene 24 horas)
#• Minutos (considerando que 1 hora tiene 60 minutos)
#• Segundos (considerando que 1 minuto tiene 60 segundos)

import math

print('Calculando el tercer ángulo de un triángulo:\n')

print('Dame cantidad de horas: ')
horas = float(input())

dias = horas/24
minutos = horas * 60
segundos = minutos * 60

print(f'Cantidad de dias: {dias:.2f} ')
print(f'Cantidad de minutos: {minutos:.2f} ')
print(f'Cantidad de segundos: {segundos:.2f} ')