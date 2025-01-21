def convert(l):
    # Inicializamos um dicionário vazio para armazenar as chaves e os valores
    dicionario = {}
    
    # Iteramos sobre cada tupla na lista
    for chave, valor in l:
        # Se a chave já existe no dicionário, adicionamos o valor à lista
        if chave in dicionario:
            dicionario[chave].append(valor)
        else:
            # Se a chave não existe, criamos uma nova chave com o valor em uma lista
            dicionario[chave] = [valor]
    
    # Retornamos o dicionário com as chaves e seus valores acumulados
    return dicionario

convert
