# p135-alumnos-tuplas.py
# Registro escolar con tuplas anidadas

alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Mar", "ISC", (10, 9, 10, 10)),
)

print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
print("--- Registro escolar ---")

# 1. Mostrar la tupla externa y el total de alumnos
print("Registros de alumnos:", alumnos)
print("Total de alumnos:", len(alumnos))

# 2. Recorrer mediante desempaquetado y mostrar promedio con dos decimales
print()
for nombre, carrera, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")

# 3. Construir tupla de pares (nombre, promedio) y obtener el mejor promedio
promedios = tuple(
    (nombre, sum(notas) / len(notas))
    for nombre, _, notas in alumnos
)
print("\nPares (nombre, promedio):", promedios)
mejor = max(promedios, key=lambda x: x[1])
print(f"Alumno con mejor promedio: {mejor[0]} con {mejor[1]:.2f}")

# 4. Consultar calificaciones usando índices de tuplas anidadas, count() e index()
print()
for i in range(len(alumnos)):
    nombre_al = alumnos[i][0]
    califs = alumnos[i][2]
    conteo_10 = califs.count(10)
    indice_primera = califs.index(califs[0])
    print(f"{nombre_al} -> Conteo de 10s: {conteo_10}, Índice de primera calificación: {indice_primera}")

# 5. Ordenar los pares (nombre, promedio) de menor a mayor con sorted()
ordenados = tuple(sorted(promedios, key=lambda x: x[1]))
print("\nOrdenados por promedio:", ordenados)

# 6. Formar tupla nueva agregando a "Eva" sin modificar la original
alumnos_con_eva = alumnos + (("Eva", "ISC", (9, 9, 10)),)
print("\nTupla original intacta:", alumnos)
print("Nueva tupla con Eva:", alumnos_con_eva)
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")