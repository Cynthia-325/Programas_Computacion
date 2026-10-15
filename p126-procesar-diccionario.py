# p126-procesar-diccionario.py
# Procesar y combinar listas en un diccionario

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
print('Diccionario de nómina:')
print(nomina)

print('\n--- Iterando Llaves (keys) ---')
for k in nomina.keys():
    print(k)

print('\n--- Iterando Valores (values) ---')
print(*nomina.values(), sep='\n')

print('\n--- Iterando Llave y Valor (accediendo por llave) ---')
for k in nomina:
    print(f'{k} -> {nomina[k]}')

print('\n--- Iterando Llave y Valor (items) ---')
for item in nomina.items():
    print(item)


suma = sum(nomina.values())
promedio = suma / len(nomina)

print('\n--- Cálculos ---')
print(f'Suma total de sueldos: {suma:.2f}')
print(f'Promedio de sueldos: {promedio:.2f}')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
