# Calcular la paga total de un trabajador
print('Calculando la paga')

#entrada
print('Nombre : ')
nombre = input()

print('Horas : ')
horas = int(input())

print('Paga p/ hora : ')
paga = float(input())

tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

#salida
print('Resumen de pagos:\n')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%')
print(f'Paga bruta {pagabruta}')
print(f'Impuesto {impuesto}')
print(f'Paga neta {paganeta}')