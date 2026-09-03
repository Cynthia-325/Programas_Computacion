while(True):
    print('\033[H\033[J')
    print('Tablas de Multiplicar')
    while True:
        n = int(input('Hasta que tabla quieres ? '))
        m = int(input('Hasta donde la quieres ? '))
        if n>0 and m>0:
            break
        print('Error, los números deben ser mayores que 0')
    t = 1
    while t <= n:
        c=1
        print(f'\nTabla del {t} \n')
        while( c <= m ):
            print(f'{t} x {c} = {t*c}')
            c+=1
        t+=1
    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N':
        break

print("\n\nGracias por utilizar este programa...")