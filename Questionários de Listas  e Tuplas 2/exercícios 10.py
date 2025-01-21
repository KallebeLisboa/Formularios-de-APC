N, M, K = map(int, input().split())  # Número de mercearias, mangos disponíveis, quantidade mínima de produtos por mercearia
q = list(map(int, input().split()))  # Lista com a quantidade de produtos em cada mercearia

produtos = []
for i in range(N):
    produtos.append(sorted(map(int, input().split())))  # Para cada mercearia, armazenamos os preços dos produtos ordenados

# Verificar se é possível comprar pelo menos K produtos em cada mercearia
for i in range(N):
    if q[i] < K:
        print("Nao")
        break
else:
    mangos = M
    while True:
        # Verificar se há mangos suficientes para comprar pelo menos K produtos em cada mercearia
        total_gasto = 0
        for i in range(N):
            if len(produtos[i]) >= K:  # Se há pelo menos K produtos na mercearia
                total_gasto += sum(produtos[i][:K])  # Adiciona o valor dos K produtos mais baratos
            else:
                total_gasto = M + 1  # Fazendo total_gasto maior que o número de mangos se não houver produtos suficientes
                break

        if total_gasto > mangos:  # Se o total gasto exceder o número de mangos
            print("Nao")
            break
        else:
            mangos -= total_gasto  # Subtrai o total de mangos gastos

        if mangos < 0:
            print("Nao")
            break
        elif mangos >= 0:  # Se o número de mangos for suficiente, continua comprando
            print("Sim")
            break
