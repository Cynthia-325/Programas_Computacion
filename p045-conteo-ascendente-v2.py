print("Iniciando secuencia de conteo ascendente")
print(" 🥞")

n = int(input("Hasta donde ? "))
m = int(input("De cuanto en cuanto ? "))
c = 1
while c <= n:
    print(f" {c}", end="")
    c += m
print("\n Secuencia completada")