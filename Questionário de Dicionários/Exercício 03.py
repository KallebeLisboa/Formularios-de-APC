estoque = {}

itens = input().split()

for i in range(0, len(itens), 2):
    item = itens[i]
    preço = float(itens[i+1])
    estoque[item] = preço


compra = {}
quantidade = input().split()

for c in range(0, len(quantidade), 2):
    item_2 = quantidade[c]
    quant = int(quantidade[c + 1])
    compra[item_2] = quant

valor_total = 00.00

for item, quant in compra.items():
    if item in estoque:
        valor_total += estoque[item] * quant


print(f"R$ {valor_total:.2f}")