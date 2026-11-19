# p161-dia-semana.py
# Devuelve el nombre del día de la semana según un número del 1 al 7

def dia_de_la_semana(dia: int) -> str:
    dias = {
        1: 'Lunes',
        2: 'Martes',
        3: 'Miércoles',
        4: 'Jueves',
        5: 'Viernes',
        6: 'Sábado',
        7: 'Domingo'
    }
    if dia in dias:
        return f'El día es: {dias[dia]}'
    return 'Error: El número debe estar entre 1 y 7.'

def main() -> None:
    numero = int(input('Introduce un número del 1 al 7: '))
    print(dia_de_la_semana(numero))

if __name__ == "__main__":
    main()