#Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. El
#programa deberá dibujar el rombo utilizando el carácter que el usuario elija.

print("\033[H\033[J")
print("--- ENTERO IMPAR---\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤")

n = int(input("NUMERO IMPAR: "))

for i in range(1, n + 1, 2): 
    espacios = (n - i) // 2 
    print(" " * espacios + "°" * i) 
for i in range(n - 2, 0, -2): 
    espacios = (n - i) // 2 
    print(" " * espacios + "°" * i)