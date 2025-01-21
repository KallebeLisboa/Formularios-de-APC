linha,coluna = input().split()
linha,coluna = int(linha),int(coluna)
mat =[]
for i in range(linha):
    mat_linha =[]
    for j in range(coluna):
        mat_linha +=[0]
    mat +=[mat_linha]       
n = int(input())
for l in range(n):
    x,y = input().split()
    x,y = int(x)-1,int(y)-1
    for m in range(linha):
        mat[m][y] += 1
    for n in range(coluna):
        mat[x][n] += 1
    mat[x][y] -= 1


cont = 0
maximo = 0
for i in range(linha):
    for j in range(coluna):
        if mat[i][j] > maximo:
            maximo = mat[i][j]
            cont = 1
        elif mat[i][j] == maximo:
            cont += 1
        else:
            continue
print(cont)
    