#Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.

print("NUMERO MAYOR ")
print("Ingresa NUMEROS 🐱‍👓🐱‍👓🐱‍🐉")

a = float(input("Ingresa primer numero: "))
b = float(input("Ingresa segundo numero: "))
c = float(input("Ingresa tercer numero: "))

if a > b and a > c:
    print(f" {a} es mayor")
elif b > a and b > c:
    print(f" {b} es mayor")
elif c > a and c > b:
    print(f" {c} es mayor")
else:
    print(f" Son todos los numeros iguales")
