#Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana
#correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango,
#debe mostrar un mensaje de error.

print("DIA DE LA SEMANA")
a = int(input("Ingresa NUMERO (1-7): "))

if a == 1:
    print(f" ES DOMINGO")
elif a == 2:
    print(f" ES LUNES")
elif a == 3:
    print(f" ES MARTES")
elif a == 4:
    print(f" ES MIERCOLES")
elif a == 5:
    print(f" ES JUEVES")
elif a == 6:
    print(f" ES VIERNES")
elif a == 7:
    print(f" ES SABADO")
else:
    print(f" NUMERO INVALIDO")
