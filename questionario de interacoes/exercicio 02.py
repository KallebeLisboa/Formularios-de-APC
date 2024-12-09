count = 0
media = 0

while True:
    entrada = input()  # Lê a entrada
    nome, salario = entrada.upper().split(",")  # Divide a entrada pelo separador ","
    
    if nome == "FIM":  # Verifica a condição de parada
        break

    salario = float(salario)  # Converte o salário para float
    media += salario  # Soma o salário à variável acumuladora
    count += 1  # Incrementa o contador de funcionários

# Calcula a média salarial
if count > 0:
    media_final = media / count
    print(f"{media_final:.2f}")  # Imprime com duas casas decimais
else:
    print("0.00")