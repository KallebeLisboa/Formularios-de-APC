n = int(input())
dados = {}
emails = {}

for i in range(n):
    informacoes_aluno = input().split()
    nome = informacoes_aluno[0]
    email = informacoes_aluno[1]
    nota_1 = float(informacoes_aluno[2])
    nota_2 = float(informacoes_aluno[3])
    nota_3 = float(informacoes_aluno[4])
    nota_4 = float(informacoes_aluno[5])
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    dados[nome] = media
    emails[nome] = email


aluno_escolhido = input()

if aluno_escolhido in dados:
    print(f"Destinatário: {emails[aluno_escolhido]}")
    if dados[aluno_escolhido] >= 5:
        print(f"O aluno {aluno_escolhido} foi aprovado com média {dados[aluno_escolhido]:.2f}.")
    else:
        print(f"O aluno {aluno_escolhido} foi reprovado com média {dados[aluno_escolhido]:.2f}.")
else:
    print(f"O aluno {aluno_escolhido} não está na turma.")
