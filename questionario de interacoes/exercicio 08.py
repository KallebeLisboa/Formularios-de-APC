# Leitura da entrada
cidadeA, cidadeB, crescimentoA, crescimentoB = input().split()
cidadeA = int(cidadeA)
cidadeB = int(cidadeB)
crescimentoA = float(crescimentoA)
crescimentoB = float(crescimentoB)
soma = 0

# Verificar se A nunca alcançará B
if crescimentoA > crescimentoB:
    while cidadeA < cidadeB:
        cidadeA += (cidadeA * crescimentoA)/100
        cidadeB += (cidadeB * crescimentoB)/100
        soma = soma + 1
    if soma <= 1000:
        print(f"Vai alcançar em {soma} ano(s).")
    else: 
        print("Mais de um milenio.")
else:
    print("A nunca alcancara B.")