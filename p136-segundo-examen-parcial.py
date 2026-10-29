# p136-segundo-examen-parcial.py
# Procesamiento del registro de vuelos de la aerolínea "AeroRegistro"
# Manejo de Listas, Diccionarios, Conjuntos (Sets) y Tuplas

# Limpiar la pantalla de la consola e imprimir el encabezado del sistema
print('\033[H\033[J')
print("\n  🐱‍👤🐱‍👤🐱‍👤 ")
print("AeroRegistro - Sistema de Vuelos")
print("Captura de datos de los vuelos (* para terminar):\n")

# ==============================================================================
# FASE 1: ESTRUCTURA Y CAPTURA DE DATOS
# ==============================================================================

# Lista principal que representará el inventario almacenando los diccionarios de vuelos
vuelos = []

# Ciclo infinito para capturar registros hasta que el usuario indique el fin
while True:
    # Captura del identificador del vuelo eliminando espacios en blanco adicionales
    numero_vuelo = input("Número de vuelo: ").strip()
    
    # Condición de paro: termina la captura si se ingresa '*' o una cadena vacía
    if numero_vuelo == "*" or numero_vuelo == "":
        break
        
    # Captura de las cadenas de texto para origen, destino y aerolínea
    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    aerolinea = input("Aerolínea: ").strip()
    
    # Captura y conversión explícita de datos numéricos (entero y flotante)
    pasajeros = int(input("Pasajeros: "))
    tarifa = float(input("Tarifa: "))
    print("-" * 35)
    
    # Creación del diccionario que agrupa los atributos del vuelo actual
    vuelo = {
        'numero_vuelo': numero_vuelo,
        'origen': origen,
        'destino': destino,
        'aerolinea': aerolinea,
        'pasajeros': pasajeros,
        'tarifa': tarifa
    }
    
    # Inserción del diccionario en la lista principal de inventario
    vuelos.append(vuelo)

# ==============================================================================
# FASE 2: EXTRACCIÓN DE COLECCIONES ESPECIALES
# ==============================================================================

# Inicialización del conjunto (set) para destinos sin duplicados y lista para tuplas
destinos_unicos = set()
registro_inmutable = []

# Recorrido del inventario para poblar las colecciones secundarias
for v in vuelos:
    # Se añade el destino al set (las ciudades repetidas se descartan automáticamente)
    destinos_unicos.add(v['destino'])
    
    # Creación de la tupla inmutable con (numero_vuelo, aerolinea, destino)
    tupla_vuelo = (v['numero_vuelo'], v['aerolinea'], v['destino'])
    registro_inmutable.append(tupla_vuelo)

# ==============================================================================
# FASE 3: FORMATEO Y VISUALIZACIÓN
# ==============================================================================

# 1. Impresión de los datos crudos tal como se almacenaron en la lista de diccionarios
print("\nDatos (Lista de diccionarios):")
print(vuelos)

# 2. Impresión del conjunto resultante de ciudades de destino únicas
print("\nDestinos Únicos (Conjunto):")
print(destinos_unicos)

# 3. Impresión del registro histórico inmutable (lista de tuplas)
print("\nRegistro Inmutable (Tuplas):")
print(registro_inmutable)

# 4. Impresión de los vuelos en formato tabular con alineación de columnas
print("\nTabla de datos:")
print(f"{'No. Vuelo':<10} | {'Origen':<15} | {'Destino':<15} | {'Aerolínea':<12} | {'Pasajeros':>9} | {'Tarifa':>10}")
print("-" * 86)

# Recorrido para imprimir cada fila alineando texto a la izquierda (<) y números a la derecha (>)
for v in vuelos:
    print(f"{v['numero_vuelo']:<10} | {v['origen']:<15} | {v['destino']:<15} | {v['aerolinea']:<12} | {v['pasajeros']:>9} | {v['tarifa']:>10,.2f}")

# ==============================================================================
# FASE 4: ANALÍTICA Y CÁLCULOS MATEMÁTICOS
# ==============================================================================

print("\nResumen:")
# Obtención del total de vuelos registrados mediante la longitud de la lista principal
total_vuelos = len(vuelos)
print(f"Vuelos totales: {total_vuelos}")

# Validación para ejecutar cálculos estadísticos solo si existe al menos un vuelo registrado
if total_vuelos > 0:
    # Diccionarios auxiliares para contabilizar frecuencias por aerolínea y por destino
    conteo_aerolineas = {}
    conteo_destinos = {}
    
    for v in vuelos:
        aero = v['aerolinea']
        dest = v['destino']
        
        # Si la clave existe suma 1 a su valor actual; si no existe, la inicializa en 0 y suma 1
        conteo_aerolineas[aero] = conteo_aerolineas.get(aero, 0) + 1
        conteo_destinos[dest] = conteo_destinos.get(dest, 0) + 1

    # Impresión del desglose de vuelos por aerolínea
    print("\nAerolíneas:")
    for aero, cant in conteo_aerolineas.items():
        print(f"{aero}: {cant}")

    # Impresión del desglose de vuelos por ciudad de destino
    print("\nDestinos:")
    for dest, cant in conteo_destinos.items():
        print(f"{dest}: {cant}")

    # Cálculo de la suma total y promedio de pasajeros por vuelo
    suma_pasajeros = sum(v['pasajeros'] for v in vuelos)
    promedio_pasajeros = suma_pasajeros / total_vuelos

    # Cálculo de la suma total de tarifas y tarifa promedio
    suma_tarifas = sum(v['tarifa'] for v in vuelos)
    promedio_tarifas = suma_tarifas / total_vuelos

    # Impresión de métricas de pasajeros y tarifas formateadas a dos decimales
    print(f"\nPasajeros -> Suma: {suma_pasajeros}, Promedio: {promedio_pasajeros:.2f}")
    print(f"Tarifa -> Suma: {suma_tarifas:,.2f}, Promedio: {promedio_tarifas:,.2f}")

    # Búsqueda de los diccionarios con la tarifa máxima y mínima usando funciones lambda
    vuelo_caro = max(vuelos, key=lambda x: x['tarifa'])
    vuelo_barato = min(vuelos, key=lambda x: x['tarifa'])

    # Impresión comparativa del vuelo más caro y el más barato
    print(f"{vuelo_caro['numero_vuelo']} de ${vuelo_caro['tarifa']:,.2f} es el más caro, "
          f"{vuelo_barato['numero_vuelo']} de ${vuelo_barato['tarifa']:,.2f} es el más barato.")
else:
    print("No se registraron vuelos para calcular estadísticas.")

print("\n  🐱‍👤🐱‍👤🐱‍👤 ")