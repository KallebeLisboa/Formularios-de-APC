# Entradad de dados
txt= str(input())
censura = str(input())
palavras = txt.split()

# Troca de Palavras
if censura in txt:
    for i in range(len(palavras)):
        palavra = palavras[i]
        if palavra in censura:
            palavras[i] = str("*")
        txtFinal = " ".join(palavras)
    print(txtFinal)
else: 
    print("tudo certo :)")