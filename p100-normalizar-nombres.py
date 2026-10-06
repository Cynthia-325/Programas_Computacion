# p100-normalizar-nombres.py
# Limpia nombres mediante una comprensión
print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤")
nombres = [' ana', 'LUIS ', '', ' maría josé ', 'Pedro']
normalizados = [ nombre.strip().title() for nombre in nombres if nombre.strip() ]
print(f'Datos originales: {nombres}')
print(f'Nombres normalizados: {normalizados}')
print("\n  🐱‍👤🐱‍👤🐱‍👤")
