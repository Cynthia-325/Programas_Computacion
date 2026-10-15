# p124-agregar-diccionario.py
# Agregar elementos a un diccionario

ventas = {
    'Juan': 1550, 
    'Jose': 2600, 
    'Maria': 2220
}

print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
print('Ventas iniciales:')
print(ventas)

# Agregando elementos
ventas['Rocio'] = 2500
ventas['Mateo'] = 1567
ventas.update({'Andrea': 9567})
ventas.update({'Miguel': 1234})

print('\nVentas actualizadas:')
print(ventas)
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
