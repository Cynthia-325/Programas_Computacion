#Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. El
#usuario debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos,
#así como el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final
#indicar qué fondo generó un mayor rendimiento.

print("\033[H\033[J")
print("--- RENDIMIENTO DE INVERSION ---\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤")


x1 = float(input("Monto inicial del primer fondo: "))
n1 = int(input("Porcentaje de la tasa de interes anual: "))
print("\n   🐱‍👤🐱‍👤🐱‍👤")

x2 = float(input("Monto inicial del segundo fondo: "))
n2 = int(input("Porcentaje de la tasa de interes anual: "))
print("\n   🐱‍👤🐱‍👤🐱‍👤")

anos = int(input("Años a proyectar: "))

print(f"\n Comparacion de fondos")
print(f"\n AÑO   |   FONDO A    |   FONDO B")
print("------------------------------------------")
   

for i in range(1, anos + 1):
    x1 = x1 * (1 + n1/100)
    x2 = x2 * (1 + n2/100)
    print(f"\n {i}   |   {x1}   | {x2} ")
    print("------------------------------------------")

if x1 > x2: 
    print(f"\n Fondo A (${x1}) superó al Fondo B (${x2})") 
elif x2 > x1: 
    print(f"\n Fondo B (${x2}) superó al Fondo A (${x1})") 
else: 
    print(f"\n Ambos fondos son iguales")