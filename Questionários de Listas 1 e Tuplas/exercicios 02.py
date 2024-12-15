n = int(input())
jogadores = list()

crewmates = list()

for jogardor in range(n):
    username = str(input())
    jogadores.append(username)

impostores =  set(input().strip().split())

for jogador in jogadores:
    if jogador not in impostores:
        crewmates.append(jogador)
print(*crewmates)
