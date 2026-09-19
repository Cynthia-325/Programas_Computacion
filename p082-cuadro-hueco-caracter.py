#El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se
#dibujará. Luego, deberá imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar
#el contorno del mismo.

print("\033[H\033[J")
print("--- CUADRADO ---\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤")

lado1 = int(input("Tamaño del lado: "))

for i in range (1, lado1 + 1):
    if i == 1 or i == lado1:
        print("°"*lado1)
    else: print( "°" + " " * (lado1 - 2) + "°")
