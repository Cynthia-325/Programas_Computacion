# p154-lista-pares.py
# Función para obtener los números pares de una lista
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
def lista_pares(lista: list[int]) -> list[int]:
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)

return pares

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = lista_pares(numeros)
print(f"Los números pares de la lista son: {resultado}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
