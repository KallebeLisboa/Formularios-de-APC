# Entrada de Dados
n = int(input())

for c in range(n):
    codigo = input()
    resultado = []
    i = 0
    while i < len(codigo):
        caractere = codigo[i]
        i += 1
        numero = ""
        while i < len(codigo) and codigo[i].isdigit():
            numero += codigo[i]
            i += 1
        resultado.append(caractere * int(numero))
        final = ''.join(resultado)
    print(final)