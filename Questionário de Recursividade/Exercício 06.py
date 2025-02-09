def corrida(a, b, c):
    if a == 0:
        print("A corrida chegou ao fim.")
        return
    if b == 0:
        print(f"Faltam {a} voltas, hora de trocar os pneus.")
        b = c
    corrida(a - 1, b - 1, c)


