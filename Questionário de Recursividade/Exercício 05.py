def JaChegou(n, frase, count = 0):
    
    if count >= n:
        return
    
    print(frase)
    JaChegou(n, frase, count + 1)