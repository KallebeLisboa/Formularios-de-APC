#Entrada
txt = input()

#Contador
count = 0

#Verificação
for char in txt:
    if char.isnumeric():
        count += 1

#Saida de dados    
print(count)