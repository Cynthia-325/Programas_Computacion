# p110-comprension-filtra-palabras.py
# Filtrar palabras usando comprensión de listas

print('\033[H\033[J')
print("Filtrar palabras\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")

texto = input("Introduzca palabras separadas por espacios: ")

palabras = texto.split()

filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 4]

print("\n--- Resultados ---")
print(f"Lista original: {palabras}")
print(f"Lista filtrada (>4 caracteres en mayúsculas): {filtradas}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")