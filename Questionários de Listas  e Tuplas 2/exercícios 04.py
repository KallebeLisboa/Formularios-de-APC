# Definir os horários para cada turno
horarios = {
    'M': [(14, 0), (14, 55), (15, 50), (16, 45), (17, 40)],
    'T': [(14, 0), (14, 55), (15, 50), (16, 45), (17, 40)],
    'N': [(20, 0), (20, 50), (21, 40), (22, 30)],
}

# Grade horária inicial (dias da semana: Seg, Ter, Qua, Qui, Sex, Sab)
grade = { 'Seg': [None, None, None, None, None], 'Ter': [None, None, None, None, None], 'Qua': [None, None, None, None, None], 
          'Qui': [None, None, None, None, None], 'Sex': [None, None, None, None, None], 'Sab': [None, None, None, None, None] }

# Função para exibir a grade horária
def exibir_grade():
    dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
    print("+---------------+----------+----------+----------+----------+----------+----------+")
    print("|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |")
    print("+---------------+----------+----------+----------+----------+----------+----------+")
    for i in range(5):  # 5 horários
        print(f"| {horarios['M'][i][0]}:{horarios['M'][i][1]:02d} - {horarios['M'][i][0]+1}:{horarios['M'][i][1]:02d} | ", end="")
        for dia in dias:
            if grade[dia][i] is not None:
                print(f"{grade[dia][i]:<10} | ", end="")
            else:
                print("          | ", end="")
        print("\n+---------------+----------+----------+----------+----------+----------+----------+")

# Função para adicionar uma disciplina
def adicionar_disciplinas(disciplina, horarios_list):
    for horario in horarios_list:
        dia, turno, hora = horario[0], horario[1], horario[2]
        if grade[dia][hora] is not None:
            print(f'!(+ {disciplina})')  # Exemplo de erro de adição
            return
        grade[dia][hora] = disciplina

# Função para remover uma disciplina
def remover_disciplinas(disciplina, horarios_list):
    for horario in horarios_list:
        dia, turno, hora = horario[0], horario[1], horario[2]
        if grade[dia][hora] != disciplina:
            print(f'!( - {disciplina})')  # Erro de remoção
            return
        grade[dia][hora] = None

# Função principal que vai fazer o loop da execução
def executar_comando(comando):
    comando_partes = comando.split()
    instrucao = comando_partes[0]
    
    if instrucao == '+':
        disciplina = comando_partes[1]
        horarios_list = [(comando_partes[i][0], comando_partes[i][1], int(comando_partes[i][2])) for i in range(2, len(comando_partes))]
        adicionar_disciplinas(disciplina, horarios_list)
    elif instrucao == '-':
        disciplina = comando_partes[1]
        horarios_list = [(comando_partes[i][0], comando_partes[i][1], int(comando_partes[i][2])) for i in range(2, len(comando_partes))]
        remover_disciplinas(disciplina, horarios_list)
    elif instrucao == '?':
        exibir_grade()
    elif instrucao == "Hasta la vista, beibe!":
        print("Programa encerrado")
    else:
        print("Comando desconhecido.")

# Função para ler múltiplos comandos (para testes automatizados)
def ler_comandos():
    while True:
        comando = input().strip()
        if comando == "Hasta la vista, beibe!":
            break
        executar_comando(comando)
