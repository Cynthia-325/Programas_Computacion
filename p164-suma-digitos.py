# p164-suma-digitos.py
# Calcula la suma de los dígitos de cada número en una lista

def leer_lista_enteros() -> list[int]:
    entrada = input('Dame los números (separados por espacio): ').split()
    return [int(x) for x in entrada]

def suma_digitos_numero(numero: int) -> int:
    n = abs(numero)
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

def procesar_lista_digitos(numeros: list[int]) -> list[int]:
    return [suma_digitos_numero(num) for num in numeros]

def main() -> None:
    numeros = leer_lista_enteros()
    sumas = procesar_lista_digitos(numeros)
    print('La lista de números original')
    print(numeros)
    print('La lista con las suma de dígitos de los números:')
    print(sumas)

if __name__ == "__main__":
    main()