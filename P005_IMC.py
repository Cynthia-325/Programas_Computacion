# Calcular el IMC de una persona
print(" Índice de Masa Corporal (IMC)\n")
peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))
imc = peso_kg / (altura_m ** 2)
print(f"IMC: {imc:.2f}")