produtos = []
x = 8

for i in range(x):
    item = float(input(""))
    produtos.append(item)

precos_ajustados = []

for i in produtos:
    if i < 100:
        ajuste = i + (i/10)
    elif i >= 100:
        ajuste = i + (i/20)
    precos_ajustados.append(ajuste)

print(f"Preços originais: {produtos}")
print(f"Preços reajustados: {precos_ajustados}")