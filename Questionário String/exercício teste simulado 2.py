# Entrada de Dados
n1, n2 = input().split(",")
n1 = int(n1)
n2 = int(n2)

# Backups dos valores
count1 = n1
count2 = n2

# Laço principal
while n1 >= n2:
    # Sequência decrescente
    for i in range(count1, count2 - 1, -1):
        print(i, end=" ")
    print()  # Quebra de linha após sequência decrescente

    # Atualizar valores para a sequência crescente
    n1 -= 1
    count1 -= 1
    if n1 >= n2:  # Evitar repetir o último número
        for i in range(count2, count1 + 1):
            print(i, end=" ")
        n1 -= 1
        count2 +=1
        print()  # Quebra de linha após sequência crescente