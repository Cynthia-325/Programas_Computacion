# p102-aplanar-matriz.py
# Recorre una matriz con ciclos anidados
print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤")
matriz = [[4, -2, 8], [0, 5, -1], [7, 3, -6]]
valores = [numero for fila in matriz for numero in fila]
positivos = [numero for fila in matriz
    for numero in fila if numero > 0]
print(f'Matriz: {matriz}')
print(f'Lista plana: {valores}')
print(f'Valores positivos: {positivos}')
print("\n  🐱‍👤🐱‍👤🐱‍👤")
