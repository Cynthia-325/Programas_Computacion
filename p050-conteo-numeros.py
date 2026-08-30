cuenta = 0
suma = 0
cuenta_positivos = 0
cuenta_negativos = 0
cuenta_ceros = 0
print(" Analizador de Números (escribe 999 para finalizar) ")
while True:
    num = int(input('Introduce un número entero: '))
    if num == 999: # Condición de salida
        print("Detectado código de salida (999)")
    break # Rompe el ciclo infinito.
    cuenta += 1
    suma += num
    if num > 0:
        cuenta_positivos += 1
    elif num < 0:
        cuenta_negativos += 1
    else:
        cuenta_ceros += 1