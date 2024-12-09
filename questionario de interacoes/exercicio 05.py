# Definições de variáveis
count = 0
media = 0
n = int(input())
menor = 1000000000
menor_salario = ""
maior_salario = ""
maior = 0

if n > 0:
    for c in range(n):
        entrada = input()  # Lê a entrada
        nome, salario = entrada.split(",")  # Divide a entrada pelo separador ","
        
        if nome == "Fim":  # Verifica a condição de parada
            break

        salario = float(salario)  # Converte o salário para float
        media += salario  # Soma o salário à variável acumuladora
        count += 1  # Incrementa o contador de funcionários
        # Maior salário
        if salario > maior:
            maior = salario
            maior_salario = nome
        # menor salário
        if salario < menor:
                menor = salario
                menor_salario = nome
    # Calcula a média salarial
    if count > 0:
        media_final = media / count
        print(f"{media_final:.2f}")  # Imprime com duas casas decimais
    else:
        print("0.00")
    # Saida de dados maior salário
    if maior == 0:
        print("Não tem")
    else:
        print(f"{maior_salario} {maior:.2f}")
    # Saida de dados menor salário
    if menor_salario == "":
        print("Não tem")
    else:
        print(f"{menor_salario} {menor:.2f}")
else:
    print("Não tem média")
    print("Não tem")
    print("Não tem")