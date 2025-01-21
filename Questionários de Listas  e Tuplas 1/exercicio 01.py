n = int(input())
classe = list()


for alunos in range(n):
    estudantes = str(input())
    classe.append(estudantes)
classe_inversa = classe[::-1]

for alunos in classe_inversa:
    print(alunos)