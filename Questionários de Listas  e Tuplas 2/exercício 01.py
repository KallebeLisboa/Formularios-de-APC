n = int(input()) 

matriz = []

for i in range(n):
    linha = input().split()  # Lê a linha como uma string
     # Divide a linha em uma lista de elementos
    matriz.append(linha)  # Adiciona essa lista como uma linha da matriz

def verifica_poneglifo(matriz, n):
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 'X':
                # Deve estar na diagonal principal ou secundária
                if i != j and i + j != n - 1:
                    return False
            else:
                # Não deve estar na diagonal principal ou secundária
                if i == j or i + j == n - 1:
                    return False
    return True

if verifica_poneglifo(matriz, n):
    print("O one piece eh real!")
else:
    print("Talvez o tesouro seja os amigos que fizemos no caminho")
