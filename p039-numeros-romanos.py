#Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en
#números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.

print("NUMEROS ROMANOS")
a = int(input("Ingresa NUMERO (1-10): "))

if a == 1:
    print(f" 1 ES I")
elif a == 2:
    print(f" 2 II")
elif a == 3:
    print(f" 3 ES III")
elif a == 4:
    print(f" 4 ES IV")
elif a == 5:
    print(f" 5 ES V")
elif a == 6:
    print(f" 6 ES VI")
elif a == 7:
    print(f" 7 ES VII")
elif a == 8:
    print(f" 8 ES VIII")
elif a == 9:
    print(f" 9 ES IX")
elif a == 10:
    print(f" 10 ES X")
else:
    print(f" NUMERO INVALIDO")
