# input para adicionar os números da seqência
a = int(input())
b = int(input())
c = int(input())

# input para adicionar os letras da seqência
p1 = str(input())
p2 = str(input())

# Concatenação
c1 = (a+b)*(p1)
c2 = (b+c)*(p2)
c3 = c1+c2
c4 = c3*(a+c)

# Print final da concatenação
print(c4)