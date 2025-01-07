# Contador para determinar o número de nomes
count = 0

# Lista infinita
while True:
    nomes = str(input()).upper() # Lista de nomes
    if nomes == "FIM": # Final da lista
        break
    count += 1 # Contador de nomes
print(count)