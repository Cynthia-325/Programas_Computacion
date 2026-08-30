c = 0
suma = 0
print(" Meta de ahorro: $100. Empezando a sumar números...")
while c < 200:
    c += 1
    suma += c
    print(f" (+{c})", end="")
    if suma >= 100:
        print("\n\n ¡Meta alcanzada!")
        break

print(f"Se necesitaron los primeros {c} números para llegar a una suma de ${suma}.")