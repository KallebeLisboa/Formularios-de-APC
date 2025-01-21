def erase(lista):
    # Criar uma nova lista para armazenar as tuplas não vazias
    lista_sem_tuplas_vazias = []
    
    # Iterar sobre cada elemento da lista original
    for tupla in lista:
        # Verificar se a tupla não é vazia
        if tupla:
            # Adicionar a tupla não vazia à nova lista
            lista_sem_tuplas_vazias.append(tupla)
    
    # Retornar a nova lista sem tuplas vazias
    return lista_sem_tuplas_vazias


erase
