#Se requiere desarrollar un sistema interactivo de consola para la gestión de una
#estación de servicio (gasolinera). El programa debe permitir a los operadores
#realizar cálculos de ventas, proyecciones de rendimiento y categorización de
#clientes mediante un flujo lógico robusto.

#MENU 
while True:

    print("========================================")
    print("       SIMULADOR DE GASOLINERA")
    print("========================================")
    print("1. Venta de Combustible")
    print("2. Simulación de Rendimiento")
    print("3. Clasificador de Cliente")
    print("4. Salir")
    print("========================================")

    opcion = int(input("Seleccione una opción: "))

#COMPORTAMIENTO DEL MENU

    if opcion == 1:

        print()
        print("Tipos de combustible:")
        print("1. Gasolina Regular")
        print("2. Gasolina Premium")
        print("3. Diésel")

        tipo_combustible = int(input("Seleccione el tipo de combustible: "))

        if tipo_combustible == 1:
            combustible = "Gasolina Regular"

        elif tipo_combustible == 2:
            combustible = "Gasolina Premium"

        elif tipo_combustible == 3:
            combustible = "Diésel"

        else:
            print("Opción de combustible inválida.")
            continue

        precio = float(input("Introduce el precio por litro: "))
        litros = float(input("Introduce la cantidad de litros: "))

        if precio <= 0 or litros <= 0:
            print("Error: el precio y los litros deben ser positivos.")
            continue

        total = precio * litros

        print()
        print("========== RESUMEN DE VENTA ==========")
        print(f"Combustible:       {combustible}")
        print(f"Precio por litro:  ${precio:>10.2f}")
        print(f"Litros:            {litros:>10.2f}")
        print(f"Total de venta:    ${total:>10.2f}")
        
    elif opcion == 2:

        kilometraje = int(input("Introduce el kilometraje inicial: "))
        rendimiento = float(input("Introduce el rendimiento (km por litro): "))

        if kilometraje < 0 or rendimiento <= 0:
            print("Error: los datos deben ser válidos.")
            continue

        print()
        print(f"{'KM':>10} {'Litros estimados':>20}")
        print("--------------------------------")

        for km in range(0, 1001, 100):
            kilometraje_actual = kilometraje + km
            litros_consumidos = km / rendimiento

            print(f"{kilometraje_actual:>10} {litros_consumidos:>20.2f}")

    elif opcion == 3:

        litros_mensuales = float(input("Introduce los litros comprados este mes: "))

        if litros_mensuales < 0:
            print("Error: los litros no pueden ser negativos.")
            continue

        if litros_mensuales < 100:
            categoria = "Regular"

        elif litros_mensuales <= 500:
            categoria = "Premium"

        else:
            categoria = "Flotilla"

        print(f"Volumen mensual: {litros_mensuales:.2f} L")
        print(f"Clasificación: {categoria}")

    elif opcion == 4:
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
        continue





