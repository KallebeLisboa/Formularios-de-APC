import math
# Entrada de Dados

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Cálculo

dist = (x1 - x2)**2 + (y1 - y2)**2
dist2 = math.sqrt(dist)

# Condicionais
if dist2 <= 100:
    print("É o amor da minha vida!")
elif 100 < dist2 <= 200:
    print("Talvez dê certo")
else: 
    print("Não vale a pena investir")