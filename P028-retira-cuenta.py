print("Bienvenido al Cajero Automático \n")
saldo_actual = 1500.50
print(f"Tu saldo actual es: ${saldo_actual:,.2f}")
cantidad_retiro = float(input("Ingresa la cantidad a retirar: $"))
if cantidad_retiro > 0:
    if cantidad_retiro <= saldo_actual:
        nuevo_saldo = saldo_actual - cantidad_retiro
        print("\n Retiro exitoso.")
        print(f"Tu nuevo saldo es: ${nuevo_saldo:,.2f}")
    else:
        print("\n Fondos insuficientes. No se puede completar la transacción.")
else:
    print("\n La cantidad a retirar debe ser un número positivo.")