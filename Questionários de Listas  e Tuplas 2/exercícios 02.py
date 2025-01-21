# Leitura do número de listas e índice de ordenação
n = int(input())
t = int(input())

# Leitura das listas de inteiros
listas = []
for _ in range(n):
    linha = input("Digite os elementos da lista separados por espaço: ").split()
    linha = [int(x) for x in linha]  # Convertendo para inteiros
    listas.append(linha)

# Ordenação das listas diretamente no sort
listas.sort(key=lambda lista: (lista[t], -sum(lista)))

# Impressão das listas ordenadas
print("\nListas ordenadas:")
for lista in listas:
    print(*lista)
