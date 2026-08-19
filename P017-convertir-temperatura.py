#Desarrolla un programa que convierta una temperatura de grados Celsius a grados Fahrenheit. El programa debe
#solicitar al usuario una temperatura en Celsius y luego mostrar el resultado en Fahrenheit. La fórmula para la
#conversión es:
#• farenheit = (celcius × 9/5) + 32

import math

print("Conversor de Temperatura de Celsius a Fahrenheit:\n")

celsius = float(input("Temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")