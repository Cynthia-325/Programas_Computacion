# p134-coordenadas-tuplas.py
# Coordenadas de ciudades mediante tuplas

print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
print("--- Coordenadas con Tuplas ---")

# 1. Crear y mostrar las tuplas, tipo e índices positivos y negativos
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

print(f"Tupla Zacatecas: {zacatecas}, Tipo: {type(zacatecas)}")
print(f"Tupla Guadalupe: {guadalupe}, Tipo: {type(guadalupe)}")

print("\nAcceso por índices (Zacatecas):")
print(f"Positivos -> Nombre: {zacatecas[0]}, Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}")
print(f"Negativos -> Nombre: {zacatecas[-3]}, Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}")

# 2. Desempaquetar cada tupla en variables e imprimir con formato
nom_z, lat_z, lon_z = zacatecas
nom_g, lat_g, lon_g = guadalupe
print(f"\n{nom_z}: ({lat_z}, {lon_z})")
print(f"{nom_g}: ({lat_g}, {lon_g})")

# 3. Recorrer ambas ubicaciones con un ciclo y mostrar coordenadas con slicing
print()
ubicaciones = (zacatecas, guadalupe)
for ubicacion in ubicaciones:
    print(f"Ubicación: {ubicacion[0]}, Coordenadas: {ubicacion[1:]}")

# 4. Calcular e imprimir el punto medio aproximado
punto_medio = (round((lat_z + lat_g) / 2, 2), round((lon_z + lon_g) / 2, 2))
print(f"\nPunto medio aproximado: {punto_medio}")

# 5. Crear nueva tupla para Zacatecas con el código "ZAC" y comprobar la original
zacatecas_nueva = zacatecas + ("ZAC",)
print(f"\nNueva tupla Zacatecas: {zacatecas_nueva}")
print(f"Original sin cambios: {zacatecas}")

# 6. Verificar pertenencia y comentario sobre inmutabilidad
print(f"\n'Zacatecas' pertenece a la tupla: {'Zacatecas' in zacatecas}")
# Nota: Intentar modificar un elemento directamente arroja TypeError (las tuplas son inmutables).
print("# Nota: Intentar modificar un elemento directamente arroja TypeError (las tuplas son inmutables).")
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")