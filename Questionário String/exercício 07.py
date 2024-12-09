# Entrada de Dados
txt = str(input())
count = 0

tamanho = len(txt)

# Verificação
for c in range(tamanho // 2):
    if txt[c] != txt[tamanho - c - 1]:
        count += 1

# Condição e saida de dados
if count == 1 or (count == 0 and tamanho % 2 == 1):
    print("ON")
else:
    print("OFF")