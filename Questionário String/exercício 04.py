# Entrada de Dados
txt = str(input())

# Verificação
result = ""
for i in range(len(txt)):
    if i % 2 != 0 and txt[i] != " ": 
        result += txt[i]
print(result)