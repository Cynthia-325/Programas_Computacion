#Escribe un programa que reciba tres números enteros y determine si son consecutivos. Si lo son,
#muestra un mensaje de confirmación; de lo contrario, informa que no lo son.

print(" NUMEROS ENTEROS CONSECUTIVOS ")
print("Ingresa NUMEROS 🥞")

a = float(input("Ingresa primer numero: "))
b = float(input("Ingresa segundo numero: "))
c = float(input("Ingresa tercer numero: "))

if a < b and b < c:
    print(f" SON CONSECUTIVOS")
elif a == b+1 and b == c+1 :
    print(f" SON CONSECUTIVOS")
else:
    print(f" No son consecutivos 🐱‍👤")
