def troco(x):
    moedas_50 = 0
    moedas_25 = 0
    moedas_10 = 0
    moedas_5 = 0
    moedas_1 = 0

    moedas_50 = x // 50
    x = x % 50

    moedas_25 = x // 25
    x = x % 25

    moedas_10 = x // 10
    x = x % 10

    moedas_5 = x // 5
    x = x % 5

    moedas_1 = x

    print(f"{moedas_50} moedas de 50 centavos")
    print(f"{moedas_25} moedas de 25 centavos")
    print(f"{moedas_10} moedas de 10 centavos")
    print(f"{moedas_5} moedas de cinco centavos")
    print(f"{moedas_1} moedas de 1 centavo")