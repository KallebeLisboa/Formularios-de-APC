# Entrada
entrada = input().split()
N, M, f = int(entrada[0]), int(entrada[1]), int(entrada[2])

# Ler matriz de entrada
matriz = []
for _ in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Inicializar a matriz de saída
saida = []

# Iterar sobre as regiões f x f
for i in range(0, N, f):
    linha_saida = []
    for j in range(0, M, f):
        # Encontrar o maior valor na região f x f
        maior_valor = 0
        for x in range(i, i + f):
            for y in range(j, j + f):
                if matriz[x][y] > maior_valor:
                    maior_valor = matriz[x][y]
        linha_saida.append(maior_valor)
    saida.append(linha_saida)

# Imprimir a matriz de saída
for linha in saida:
    print(" ".join(map(str, linha)))
