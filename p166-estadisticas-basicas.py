# p166-estadisticas-basicas.py
# Calcula estadísticas poblacionales básicas para una lista de números enteros

import math

def leer_lista_enteros() -> list[int]:
    entrada = input('Dame números (separados por espacio): ').split()
    return [int(x) for x in entrada]

def numero_mayor(datos: list[int]) -> int:
    return max(datos)

def numero_menor(datos: list[int]) -> int:
    return min(datos)

def calcular_media(datos: list[int]) -> float:
    return sum(datos) / len(datos)

def calcular_varianza_poblacional(datos: list[int]) -> float:
    media = calcular_media(datos)
    return sum((x - media) ** 2 for x in datos) / len(datos)

def calcular_desviacion_estandar_poblacional(datos: list[int]) -> float:
    return math.sqrt(calcular_varianza_poblacional(datos))

def main() -> None:
    datos = leer_lista_enteros()
    if not datos:
        print('No se ingresaron números.')
        return

    media = calcular_media(datos)
    mayor = numero_mayor(datos)
    menor = numero_menor(datos)
    varianza = calcular_varianza_poblacional(datos)
    desviacion = calcular_desviacion_estandar_poblacional(datos)

    print(f'Lista de números: {datos}')
    print(f'La media: {media:.3f}')
    print(f'Mayor de los datos: {mayor}')
    print(f'Menor de los datos: {menor}')
    print(f'Varianza: {varianza:.3f}')
    print(f'Desviación estándar: {desviacion:.3f}')

if __name__ == "__main__":
    main()