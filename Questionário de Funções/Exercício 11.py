def stockmarket(stock):
    # Dicionário para armazenar o valor total das ações por data
    total_by_date = {}

    # Itera sobre a lista de tuplas fornecida
    for data, preco, quantidade, simbolo in stock:
        # Calcula o valor total para a data específica
        valor_total = preco * quantidade
        
        # Adiciona o valor total ao dicionário
        total_by_date[data] = valor_total

    # Retorna o dicionário sumarizado
    return total_by_date