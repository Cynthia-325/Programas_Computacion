print('La Suma de los dos primeros números igual al tercero? ')
print('-' * 60) 

print('Por favor, proporciona tres números enteros.')
n1 = int(input('Dame el primer número : '))
n2 = int(input('Dame el segundo número: '))
n3 = int(input('Dame el tercer número : '))

# --- Proceso y Salida ---
suma = n1 + n2
if suma == n3:
    print(f"\n ¡Correcto! La suma de {n1} + {n2} es igual a {n3}.")
else:
    print(f"\n No coincide. La suma de {n1} + {n2} es {suma}, lo cual es distinto de {n3}.")
print('-' * 60)