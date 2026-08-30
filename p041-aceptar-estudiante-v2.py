#La "Universidad Kitty Kat SA" solo acepta estudiantes que cumplan con los siguientes requisitos: ser
#mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5.
#Escribe un programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. El programa
#debe evaluar los datos y mostrar un mensaje claro que indique si el estudiante fue aceptado. Si no es aceptado, el
#mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promedio
#requerido).

print(" UNIVERSIDAD KITTY KAY SA ")
print(" 🥞")

a = str(input("Ingresa NOMBRE: "))
b = str(input("Ingresa SEXO (h/m): "))
c = float(input("Ingresa edad: "))
d = float(input("Ingresa una calificacion: "))
e = float(input("Ingresa segunda calificacion: "))
f = float(input("Ingresa tercera calificacion: "))

calif = (d + e + f)/3

if b=='h':
    print(f" No lo podemos aceptar ya que es HOMBRE")
elif c < 21 :
    print(f" No es aceptado ya que no tiene la EDAD suficiente")
elif calif < 8 :
    print(f" No es aceptado ya que no cumple con el PROMEDIO")
else:
    print(f" {a} USTED ES ACEPTADA 🐱‍👤")