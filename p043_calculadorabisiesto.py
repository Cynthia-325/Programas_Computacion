#Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto. Un año es bisiesto
#si cumple una de las siguientes condiciones:
#1. Es divisible por 4, pero no es divisible por 100.
#2. Es divisible por 400.
#El programa debe indicar claramente si el año es bisiesto o no.

print(" Ano bisiesto ")
print(" 🥞")

a = float(input("Ingresa ano: "))

if a%4 == 0 and a%100 != 0:
    print(f" es bisiesto")
elif a %400 == 0 :
    print(f"  es bisiesto")
else:
    print(f" NO ES BISIESTO 🐱‍👤")
