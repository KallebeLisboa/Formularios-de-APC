n = int(input())

todos_corredores = []

for c in range(n):
    mercadorias = input().split()
    corredor = {}
    for i in range(0, len(mercadorias), 2):
        produto = mercadorias[i]
        preco = float(mercadorias[i+1])
        corredor[produto] = preco
    todos_corredores.append(corredor)




try:
    escolha = int(input())

    corredor_escolhido = todos_corredores[escolha-1]
    preco_medio_corredor = sum(corredor_escolhido.values())/len(corredor_escolhido)

    print(f"No corredor {escolha} encontramos:")
    print(*corredor_escolhido, sep=", ")
    print(f"E o preço médio é {preco_medio_corredor:.2f}.")
    
except IndexError:
    print("Esse corredor não existe no mercado.")
