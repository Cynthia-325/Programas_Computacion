# p127-contar-caracteres.py
# Contar la frecuencia de caracteres en una cadena

print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
cadena = input('Ingrese una cadena : ')

caracteres = {}

for car in cadena:
    if car not in caracteres:
        caracteres[car] = 1
    else:
        caracteres[car] += 1

print('Resultado:')
print(caracteres)
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")