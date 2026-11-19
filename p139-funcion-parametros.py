# p139-funcion-parametros.py

def saluda(apaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno}')

saluda('Perez', 'Juan')
# saluda('Juan') # Genera error (pocos)
# saluda('Pérez', 'Juan', 'Extra') # Error: demasiados argumentos