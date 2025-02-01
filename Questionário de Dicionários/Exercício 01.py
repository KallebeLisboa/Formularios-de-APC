frase = str(input().lower())
count_D = 0
count_T = 0
count_V = 0

dicionario = {}

for palava in frase:
    for letra in palava:
        if letra == "d":
            count_D += 1
        elif letra == "t":
            count_T += 1
        elif letra == "v":
            count_V +=1

dicionario["d"] = count_D
dicionario["t"] = count_T
dicionario["v"] = count_V


if dicionario["d"] != 0:
    print(f"d {count_D}")
if dicionario["t"] != 0:
    print(f"t {count_T}")
if dicionario["v"] != 0:
    print(f"v {count_V}")