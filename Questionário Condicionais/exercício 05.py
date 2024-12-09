# Entrada de dados
indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

# Cálculo do índice com base nas reclamações
if percentReclamResolPrim >= 60:
    indice = indiceReclamacao - 5
else:
    indice = indiceReclamacao + 15
print(indice)

# Cálculo do índice considerando os cancelamentos
if percentCliCancel >= 10:  
    if canceladoPorProblema == 1:  
        indice += 80
    else:  
        indice -= 30
else:  
    if canceladoPorProblema == 1: 
        indice += 50
    else:  
        indice -= 10
print(indice)

# Cálculo do índice considerando a indisponibilidade
if indiceIndisponibilidade >= 10:  
    indice += 70
else:  
    indice -= 20
print(indice)
