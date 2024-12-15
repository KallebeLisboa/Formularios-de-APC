numeros = input().split()
n  = int(input())
multiplos = list()

for numero in numeros:
    if int(numero) % n ==0:
        multiplos.append(int(numero))
print(*multiplos)