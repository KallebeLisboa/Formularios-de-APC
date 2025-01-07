def ehPrimo(x):
    if x < 2:
        return 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0
    return 1

def divisoresPrimos(x):
    divisores_primos = set()
    for i in range(2, x): 
        if x % i == 0 and ehPrimo(i):
            divisores_primos.add(i)
    return len(divisores_primos)