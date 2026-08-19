#Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos. A partir
#de este dato, el programa debe:
#• Mostrar cada uno de los dígitos individuales del año. Por ejemplo, si el año es 1995, debe mostrar "1", "9",
#"9", "5".
#• Calcular y mostrar la suma de los dígitos individuales del año. Siguiendo el ejemplo anterior, la suma sería
#1 + 9 + 9 + 5 = 24.

import math

print('Ingresa AÑO de nacimiento: ')
ano = float(input())

uno = ano // 1000
dos = (ano // 100) % 10
tres = (ano // 10) % 10
cuatro = (ano % 10)
total = uno + dos + tres + cuatro
print(f'{uno : }')
print(f'{dos : }')
print(f'{tres : }')
print(f'{cuatro : }')
print(f'Total: {total : }')
