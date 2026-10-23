# p131-conjunto-numeros.py
# Operaciones entre conjuntos de números

# 1. Crear conjuntos A, B y C a partir de las listas
A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
print("--- Conjuntos Base ---")
print(f"A: {A}\nB: {B}\nC: {C}")

# 2. Calcular y mostrar operaciones
print("\n--- Unión ( | ) ---")
print(f"A union B: {A | B}")
print(f"B union C: {B | C}")

print("\n--- Diferencia ( - ) ---")
print(f"A diferencia C (Elementos en A, no en C): {A - C}")

print("\n--- Diferencia Simétrica ( ^ ) ---")
print(f"B dif. simétrica C (Elementos en B o C, no en ambos): {B ^ C}")

print("\n--- Intersección ( & ) ---")
print(f"B intersección C: {B & C}")

# 3. Verificar y mostrar preguntas (Verdadero/Falso)
print("\n--- Subconjuntos ( <= ) ---")
print(f"¿Es A subconjunto de B? : {A <= B}")
print(f"¿Es C subconjunto de A? : {C <= A}")

print("\n--- Pertenencia ( in / not in ) ---")
print(f"¿Está el número 100 en A? : {100 in A}")
print(f"¿Está el número 60 en A, B y C? : {60 in A and 60 in B and 60 in C}")
print(f"¿No está el número 900 en C? : {900 not in C}")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")