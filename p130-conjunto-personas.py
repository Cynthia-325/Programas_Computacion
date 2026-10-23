# p130-conjunto-personas.py
# Operaciones entre conjuntos de nombres de personas

# 1. Crear conjuntos A y B basados en las listas
A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
print("--- Conjuntos Base ---")
print(f"A: {A}\nB: {B}")

# 2. Calcular y mostrar operaciones
print("\n--- Unión ( | ) ---")
print(f"A union B: {A | B}")

print("\n--- Intersección ( & ) ---")
print(f"A intersección B: {A & B}")

print("\n--- Diferencia ( - ) ---")
print(f"A diferencia B (Elementos en A, no en B): {A - B}")

print("\n--- Diferencia Simétrica ( ^ ) ---")
print(f"A dif. simétrica B (Elementos en A o B, no en ambos): {A ^ B}")

# 3. Verificar y mostrar afirmaciones (Verdadero/Falso)
print("\n--- Subconjuntos ( <= ) ---")
print(f"¿Es {{'Pablo', 'Mateo'}} un subconjunto de B? : {{'Pablo', 'Mateo'} <= B}")

print("\n--- Superconjuntos ( >= ) ---")
print(f"¿Es A un superconjunto de {{'Reynaldo', 'Angelica'}}? : {A >= {'Reynaldo', 'Angelica'}}")

print("\n--- Pertenencia ( in / not in ) ---")
print(f"¿Está 'Pedro' en el conjunto A? : {'Pedro' in A}")
print(f"¿No está 'Lilia' en el conjunto B? : {'Lilia' not in B}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")