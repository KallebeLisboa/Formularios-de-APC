def paron(lista):
    lista_final = []
    for palavra in lista:
        count = 0
        for letra in palavra:
            if letra in "aeiouAEIOU":
                count += 1
        if count % 2 == 0: 
            lista_final.append(palavra)
    return lista_final