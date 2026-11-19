# p160-numero-menor.py
# Solicita tres números enteros y devuelve el menor

def numero_menor() -> int:
    n1 = int(input('Introduce el primer número: '))
    n2 = int(input('Introduce el segundo número: '))
    n3 = int(input('Introduce el tercer número: '))
    return min(n1, n2, n3)

def main() -> None:
    menor = numero_menor()
    print(f'El número menor es: {menor}')

if __name__ == "__main__":
    main()