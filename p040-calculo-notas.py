#Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en
#el promedio, el programa deberá mostrar uno de los siguientes mensajes:
#● Menor a 6: "Quedas reprobado"
#● Desde 6 hasta menos de 7: "Pasas de panzazo"
#● Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
#● Desde 8 hasta menos de 9: "Excelente, sigue así"
#● Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"

print(" CALIFICACIONES ")
print("Ingresa 5 CALIFICACIONES 🥞")

a = float(input("Ingresa primer numero: "))
b = float(input("Ingresa segundo numero: "))
c = float(input("Ingresa tercer numero: "))
d = float(input("Ingresa cuarto numero: "))
e = float(input("Ingresa quinto numero: "))

total = (a + b + c + d + e)/5

if total < 6:
    print(f" REPROBADO")
elif total >= 6 and total < 7 :
    print(f" Pasas de panzazo")
elif total >= 7 and total < 8 :
    print(f" Muy bien, puedes mejorar")
elif total >= 8 and total < 9 :
    print(f" Excelente, sigue así")
elif total >= 9 and total <= 10 :
    print(f" Perfecto, tu esfuerzo valió la pena")
else:
    print(f" Invalido, ingresa correctamente las calificaciones 🐱‍👤")
