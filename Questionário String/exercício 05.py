#Entrada de dados
txt = str(input())
palavras = txt.split()

#dicionáerio
numeros_extensos = {
    "zero": 0, "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5,
    "seis": 6, "sete": 7, "oito": 8, "nove": 9
}

#Troca de palavra pro número
for i in range(len(palavras)):
    palavra = palavras[i]
    if palavra in numeros_extensos:
        palavras[i] = str(numeros_extensos[palavra])
    else: # Verifica palaras escritas juntas ex: zeroum / quatrozero etc
        for j in range(1, len(palavra)):
            parte1 = palavra[:j]  
            parte2 = palavra[j:] 
            if parte1 in numeros_extensos and parte2 in numeros_extensos:
                palavras[i] = str(numeros_extensos[parte1]) + str(numeros_extensos[parte2])
                txtFinal = ' '.join(palavras)
                break
    # Junção das palavras em uma única string
    txtFinal = ' '.join(palavras)
# Saida de dados
print(txtFinal)