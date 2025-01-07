menor = 1000000000
menor_salario = ""

# Lista infinita
while True:
    nomes, salarios = input().split(",") # Lista de nomes
    if nomes == "Fim": # Final da lista
        break
    salarios = float(salarios)
    nomes = str(nomes)
# Comparador de salários
    if salarios < menor:
        menor = salarios
        menor_salario = nomes
# Saida de dados
if menor_salario == "":
    print("Não tem")
else:
    print(menor_salario)