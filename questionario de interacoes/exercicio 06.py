import math

# Entrada de dados
amigos, valor_ingressos = input().split()
amigos = int(amigos)
valor_ingressos = float(valor_ingressos)

media = 0

# Média dos ingressos e quantidade de dinheiro
for c in range(amigos):
    dinheiros_amigos = float(input())
    media += dinheiros_amigos
media_final = media/amigos

# Saida de dados
media_arredondada = math.floor(media_final)
print(f"media: {media_arredondada:.0f}")
if media_final > valor_ingressos:
    print("o rock reinara mais uma vez")
else:
    print("rockeiros trabalhando ja")