#lista de gastos


print("\n  🐱‍👤🐱‍👤🐱‍👤")

gastos = []

while True:

    print("\n===== CONTROL DE GASTOS =====")
    print("1. Ver Gastos")
    print("2. Agregar Gasto")
    print("3. Modificar Gasto")
    print("4. Eliminar Gasto")
    print("5. Ver Total")
    print("6. Salir")
    print("\n  🐱‍👤🐱‍👤🐱‍👤")


    opcion = input("Selecciona una opción: ")

    # 1. Ver gastos
    if opcion == "1":
        print("\nGastos actuales:")

        if len(gastos) == 0:
            print("No hay gastos registrados.")
        else:
            for i in range(len(gastos)):
                print(i, ":", gastos[i])

    # 2. Agregar gasto
    elif opcion == "2":
        try:
            gasto = float(input("Ingresa el monto del gasto: "))
            gastos.append(gasto)
            print("Gasto agregado correctamente.")

        except:
            print("Error: debes introducir un número.")

    # 3. Modificar gasto
    elif opcion == "3":
        try:
            indice = int(input("Ingresa el índice del gasto que deseas modificar: "))

            if indice >= 0 and indice < len(gastos):
                nuevo_gasto = float(input("Ingresa el nuevo valor: "))
                gastos[indice] = nuevo_gasto
                print("Gasto modificado correctamente.")
            else:
                print("Error: índice fuera de rango.")

        except:
            print("Error: debes introducir un número.")

    # 4. Eliminar gasto
    elif opcion == "4":
        try:
            indice = int(input("Ingresa el índice del gasto que deseas eliminar: "))

            if indice >= 0 and indice < len(gastos):
                gastos.pop(indice)
                print("Gasto eliminado correctamente.")
            else:
                print("Error: índice fuera de rango.")

        except:
            print("Error: debes introducir un número.")

    # 5. Ver total
    elif opcion == "5":
        total = sum(gastos)
        print("El total de gastos es:", total)

    # 6. Salir
    elif opcion == "6":
        print("Programa terminado.")
        break

    # Opción incorrecta
    else:
        print("Opción no válida.")