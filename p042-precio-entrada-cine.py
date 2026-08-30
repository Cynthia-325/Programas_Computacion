#Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del
#cliente. El programa debe solicitar la edad y mostrar el precio correspondiente, siguiendo estas reglas:
#● Menores de 5 años: Entran gratis.
#● Niños (5 a 12 años): Pagan $5.
#● Adultos (13 a 64 años): Pagan $10.
#● Tercera edad (65 años o más): Pagan $7.

print(" ENTRADA AL CINE ")
print(" 🥞")

a = float(input("Ingresa edad: "))

if a < 5:
    print(f" ENTRA GRATIS")
elif a >= 5 and total < 12 :
    print(f" paga $5")
elif total >= 13 and total < 64 :
    print(f" Pagan $10")
else:
    print(f"  Pagan $7 🐱‍👤")
