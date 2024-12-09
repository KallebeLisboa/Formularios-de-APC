# Entrada de dados - Idade
n = int(input("Qual sua idade? "))

# verificação de condicional da idade
if n < 16:
    print(f"Você possui {n} anos, por isso NÃO pode votar e nem beber bebidas alcoólicas")
elif 16 < n < 18:
    print(f"Você possui {n} anos, por isso PODE votar, mas NÃO pode beber bebidas alcoólicas")
else:
    print(f"Você possui {n} anos, por isso PODE votar e PODE beber bebidas alcoólicas")