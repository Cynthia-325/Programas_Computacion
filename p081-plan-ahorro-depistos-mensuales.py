#El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, un depósito mensual fijo,
#una tasa de interés mensual (porcentaje), y el número total de meses del plan. El programa debe mostrar una
#tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, y el saldo final. El interés se
#calcula sobre el saldo inicial antes de sumar el nuevo depósito.


print("\033[H\033[J")
print("--- Plan de ahorro ---\n")
print("\n  🐱‍👤🐱‍👤🐱‍👤")


x = float(input("Monto inicial: "))
y = float(input("Deposito mensual fijo: "))
z = float(input("Porcentaje de interes mensual: "))
total = int(input("Total de meses del plan: "))
print("\n   🐱‍👤🐱‍👤🐱‍👤")


print(f"\n Plan de ahorro")
print("------------------------------------------")
   

for i in range(1, total + 1):
    inicial = x
    interes = inicial * (z/100)
    x = inicial + interes + y

    print(f"\n MES: {i}   |  SALDO INICIAL: {inicial}   |  INTERES{interes}    |  SALDO FINAL: {x}")

print(f"\n en {total} meses, tendrás ${inicial}")
