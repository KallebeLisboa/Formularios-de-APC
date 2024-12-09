# Entrada de dados
n = int(input())

# Verificador de múltiplos
for c in range(n+1):
    if c%3 == 0 and c%7 == 0:
        print(c, end= " ")
