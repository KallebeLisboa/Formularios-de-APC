n = int(input())

dados = {}
lista_alunos = list()

for _ in range(n):
    aluno, nota = input().split(",")
    nota = float(nota)
    dados[aluno] = nota
    

busca = float(input())

for chave, valor in dados.items():
        if valor == busca:
            lista_alunos.append(chave)

lista_alunos.sort()

if len(lista_alunos) != 0:
    print(*lista_alunos, sep="/")
else:
    print("Você foi o único aluno com essa nota.")