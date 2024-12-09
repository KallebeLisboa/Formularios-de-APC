n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
operacao = input().strip().upper()

if operacao == 'A':
    print("Aritmetica")
    resultado = (n1 + n2 + n3)/3
    print(f"{resultado:.2f}")
elif operacao == 'P':
    # Entrada dos pesos
    p1, p2, p3 = input().split()
    p1 = int(p1)
    p2 = int(p2)
    p3 = int(p3)
    resultado = ((n1*p1) + (n2*p2) + (n3*p3))/(p1+p2+p3)
    print("Ponderada")
    print(f"{resultado:.2f}")
elif operacao == 'H':
    resultado = 3/((1/n1)+(1/n2)+(1/n3))
    print("Harmonica")
    print(f"{resultado:.2f}")
else:
    print("Operacao inexistente")