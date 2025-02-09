def controle(n,c):
    for i in range(n, c, -1):
        if n-i != 0:
            print(f"Voce ja tomou {n-i} comprimidos, restam {i}.")
    print(f"Parabens Julie! Voce tomou todos os {n} comprimidos!")