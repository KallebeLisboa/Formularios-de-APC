base  = float(input()) # transformei em float para possibilitar números decimais
altura = float(input()) # transformei em float para possibilitar números decimais
                        # Apaguei a linha desnecessária
area = (base * altura)/2 # Adicionei a divisão por 2 que estava faltando
print(f'{area:.2f}') # troquei o 3 pelo 2 para corrigir o número de casa decimais