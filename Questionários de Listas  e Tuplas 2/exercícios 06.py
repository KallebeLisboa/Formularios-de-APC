# Entrada
N, M, K = map(int, input().split())
equipes_jogadores = list(map(int, input().split()))
jogadores_por_empresario = list(map(int, input().split()))

# Lista para armazenar os jogadores agenciados por cada empresário
empresarios = []
for _ in range(M):
    empresarios.append(list(map(int, input().split())))

# Inicializar a lista de empresários com potencial
empresarios_com_potencial = []

# Iterar sobre cada empresário
for i in range(M):
    jogadores_agenciados = empresarios[i]
    
    # Conjunto de equipes cobertas pelo empresário
    equipes_cobertas = set()
    
    for jogador in jogadores_agenciados:
        equipe = equipes_jogadores[jogador - 1]  # Encontrar a equipe do jogador
        equipes_cobertas.add(equipe)
    
    # Verificar se o empresário cobre todas as equipes
    if len(equipes_cobertas) == K:
        empresarios_com_potencial.append(i + 1)

# Imprimir resultado
if empresarios_com_potencial:
    print(" ".join(map(str, sorted(empresarios_com_potencial))))
else:
    print("-1")
