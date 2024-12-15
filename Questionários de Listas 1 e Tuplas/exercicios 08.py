# Lendo os 5 primeiros números e armazenando em lista1
lista1 = []
for i in range(5):
    numero = int(input())
    lista1.append(numero)

# Lendo os 5 próximos números e armazenando em lista2
lista2 = []
for i in range(5):
    numero = int(input())
    lista2.append(numero)

# Criando a lista de tuplas usando zip
list_tuple = list(zip(lista1, lista2))
print(list_tuple)

# Calculando as médias das tuplas
medias = []
for tupla in list_tuple:
    media = (tupla[0] + tupla[1]) / 2
    medias.append(media)

# Imprimindo a lista de médias
print(medias)
