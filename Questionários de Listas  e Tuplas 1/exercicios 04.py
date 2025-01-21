numeros = input().split()
soma_2 = numeros[0]
count = 1
soma = 0.00

if numeros == '0' :    
    print("0.00")
else:
    for numero in numeros[0:len(numeros) -1]:
        multiplicacao = (float(soma_2) * 2)
        multiplicacao_2 = (float(numeros[count]) *  0.5)
        if count < len(numeros) -1:
            count += 1 
        soma = multiplicacao + multiplicacao_2
        soma_2 = soma

    print(f"{soma:.2f}")
