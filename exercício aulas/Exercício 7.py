n1, n2, n3 = map(float, input().split()) # Os valores são colocados e já transformados para Float e Separados pelo Split()
p1, p2, p3 = map(int, input().split()) # Os valores são colocados e já transformados para int e Separados pelo Split()

m = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3) # Fórmula para média ponderada

print(f"{m:.6f}") # Print de m (média) com as 6 casa decimais 