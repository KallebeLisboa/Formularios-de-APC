# Dicionário para armazenar o número de chamadas de cada valor de fibonacci
chamadas = {}

def fibonacci(n):
    # Inicializando as contagens no dicionário
    if n not in chamadas:
        chamadas[n] = 0
    chamadas[n] += 1

    # Caso base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Chamadas recursivas
        return fibonacci(n-1) + fibonacci(n-2)

def main(n):
    termo = fibonacci(n)
    print(f"Termo: {termo}")
    print("Quantidades:")
    for i in range(n + 1):
        print(f"fibonacci({i}) - {chamadas.get(i, 0)}")

n = int(input())
main(n)