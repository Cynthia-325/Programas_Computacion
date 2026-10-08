# p115-conversor-unidades.py
# Conversor de unidades de longitud usando diccionarios
print('\033[H\033[J')
print('Conversor de unidades de longitud usando diccionarios\n')
print("\n  🐱‍👤🐱‍👤🐱‍👤")
conversiones = {
'km': 1000,
'm': 1,
'cm': 0.01,
'mm': 0.001
}

longitud = float(input("Dame la longitud ?"))
while True:
    unidad = input("Unidad (km, m, cm ,mm) ? ")
    if unidad in conversiones:
        break
    else:
        print("Unidad no válida. Intente de nuevo.")

resultado = longitud * conversiones[unidad]
print(f"{longitud:,.2f} {unidad} son {resultado:,.2f} metros")
print("\n  🐱‍👤🐱‍👤🐱‍👤")