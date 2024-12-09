# Entrada de dados - Notas das provas, projetos e questionário

prova1 = float(input("Digite a nota da primeira prova: "))
prova2= float(input("Digite a nota da segunda prova: "))

proj1 = float(input("Digite a nota do primeiro projeto: "))
proj2 = float(input("Digite a nota do segundo projeto: "))

quest1 = float(input("Digite a nota do questionário: "))

# Calculo de média

MPP =  (prova1 + 2*prova2)/3 
MPProj = (proj1 + 2*proj2)/3 
NF = 0.5*MPP + 0.4*MPProj + 0.1*quest1

# Mensão final  

if 90 <= NF <= 100:
    print(f"Sua nota final é {NF}, você ficou com SS")
elif 70 <= NF <=89:
    print(f"Sua nota final é {NF}, você ficou com MS")
elif 50 <= NF <= 69:
    print(f"Sua nota final é {NF}, você ficou com MM")
elif 30 <= NF <= 49:
    print(f"Sua nota final é {NF}, você ficou com MI")
elif 0 <= NF <= 2:
    print(f"Sua nota final é {NF}, você ficou com II")