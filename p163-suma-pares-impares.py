# p163-suma-pares-impares.py
# Suma números pares o impares dentro de un rango especificado

def sumar_rango(inicio: int, fin: int, tipo: str) -> int:
    tipo = tipo.strip().upper()
    total = 0
    for num in range(inicio, fin + 1):
        if tipo == 'P' and num % 2 == 0:
            total += num
        elif tipo == 'I' and num % 2 != 0:
            total += num
    return total

def main() -> None:
    print('***')
    print('Suma en Rango')
    print('***')
    inicio = int(input('Introduce el número inicial: '))
    fin = int(input('Introduce el número final: '))
    tipo = input('¿Qué deseas sumar? (P)ares o (I)mpares: ').strip().upper()

    if tipo not in ('P', 'I'):
        print('Opción inválida. Elige P o I.')
        return

    resultado = sumar_rango(inicio, fin, tipo)
    etiqueta = 'pares' if tipo == 'P' else 'impares'
    print(f'La suma de los números {etiqueta} entre {inicio} y {fin} es: {resultado}')

if __name__ == "__main__":
    main()