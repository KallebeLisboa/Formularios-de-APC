# Lendo os valores de entrada
m, n = map(int, input().split())  # Número de fileiras e cadeiras
sala = []
for _ in range(m):
    sala.append(list(map(int, input().split())))

# Encontrando a maior distância em todas as fileiras
maior_distancia_possivel = 0
for fileira in sala:
    indices_ocupados = []
    for i in range(len(fileira)):
        if fileira[i] == 1:
            indices_ocupados.append(i)

    max_dist = 0

    # Verificar distâncias entre os ocupados
    for i in range(len(indices_ocupados) - 1):
        dist = (indices_ocupados[i + 1] - indices_ocupados[i]) // 2
        if dist > max_dist:
            max_dist = dist

    # Verificar distância no início e no fim da fileira
    inicio = indices_ocupados[0]
    fim = len(fileira) - 1 - indices_ocupados[-1]

    if inicio > max_dist:
        max_dist = inicio
    if fim > max_dist:
        max_dist = fim

    if max_dist > maior_distancia_possivel:
        maior_distancia_possivel = max_dist

# Exibindo a saída
print(maior_distancia_possivel)
