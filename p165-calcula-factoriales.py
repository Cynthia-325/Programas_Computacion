# p165-calcula-factoriales.py
# Calcula el factorial de cada número entero en una lista

def leer_lista_enteros() -> list[int]:
    entrada = input('Dame los números (separados por espacio): ').split()
    return [int(x) for x in entrada]

def factorial_numero(numero: int) -> int:
    if numero < 0:
        raise ValueError('El factorial no está definido para números negativos.')
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

def procesar_lista_factoriales(numeros: list[int]) -> list[int]:
    return [factorial_numero(num) for num in numeros]

def main() -> None:
    numeros = leer_lista_enteros()
    factoriales = procesar_lista_factoriales(numeros)
    print(f'La lista de números originales: {numeros}')
    print(f'La lista con los factoriales: {factoriales}')

if __name__ == "__main__":
    main()