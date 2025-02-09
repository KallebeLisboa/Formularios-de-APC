n = int(input())
p = int(input())

if n == 0:
    print("Cabum!!!! Explodiu")

for i in range(n, -1, -1):
    if i == 5:
        print("Seu tempo está acabando!")
    if i > 1 and i != 5:
        print(f"Atenção faltam {i} segundos...")
    elif i == 1 and p < n:
        print(f"Seja rápido. Falta 1 segundo")
    elif i == 1 and p > n:
        print("Bomba desativada automaticamente!")
    elif i == 0 and p < n:
        print("Cabum!!!! Explodiu")
    elif i == 1 and p == n:
        print("Bomba desativada automaticamente!")