maior = 0

# Lista infinita
while True:
    nomes, salarios = input().upper().split(",") # Lista de nomes
    if nomes == "FIM": # Final da lista
        break
    salarios = float(salarios)
# Comparador de salários
    if salarios > maior:
        maior = salarios
# Saida de dados
if maior == 0:
    print("Não tem")
else:
    print(f"{maior:.2f}")