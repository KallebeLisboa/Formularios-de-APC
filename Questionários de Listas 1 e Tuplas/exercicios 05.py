numeros = input().split()
inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)

numeros_inteiros = list(map(int, numeros))

print(numeros_inteiros[inicio:fim:1])