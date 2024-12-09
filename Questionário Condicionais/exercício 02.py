# Cada P é uma pergunta

P1 = str(input("O programa funciona?\n"))
P1 = P1.upper()

if P1 == "SIM":
    P2 = str(input("Você entende o que fez?\n"))
    P2 = P2.upper()
    if P2 == "SIM":
        print("Ótimo. Então não mexe!\n")
    else:
        P3 = str(input("Já foi na tutoria?\n"))
        P3 = P3.upper()
        if P3 == "SIM":
            print("Choremos!")
        else: 
            print("Temos um time a disposição!\n")
else: 
    P2 = str(input("Você sabe onde está o erro?\n"))
    P2 = P2.upper()
    if P2 == "SIM":
        P3 = str(input("Acha que pode solucionar sozinho?\n"))
        P3 = P3.upper()
        if P3 == "SIM":
            print("Então mão na massa!\n")
        else: 
            P4 = str(input("Já pesquisou no Google?\n"))
            P4 = P4.upper()
            if P4 == "SIM":
                P5 = P5 = str(input("Já foi na tutoria?\n"))
                P5 = P5.upper()
                if P5 == "SIM":
                    print("Choremos!\n")
                else: 
                    print("Temos um time a disposição!\n")
            else:   
                print("Corre lá então!\n")
    else:
        P4 = str(input("Já foi na tutoria?\n"))
        P4 = P4.upper()
        if P4 == "SIM":
            print("Choremos!\n")
        else: 
            print("Temos um time a disposição!\n")