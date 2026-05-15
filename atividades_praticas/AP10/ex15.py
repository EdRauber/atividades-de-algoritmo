palavras = []
x = 10

for i in range(x):
    palavras.append(input(""))

primero = True
comeca_a = 0
muitos_caracteres = [] 

for i in palavras:
    if primero:
        maior = i
        menor = i
        primero = False
    else:
        if len(i) > len(maior):
            maior = i
        elif len(i) < len(menor):
            menor = i
    if i[0] == "a":
       comeca_a += 1
    if  len(i) > 5:
        muitos_caracteres.append(i)

print(f"Maior palavra: {maior}")
print(f"Menor palavra: {menor}")
print(f"Quantidade de palavras que começam com a: {comeca_a}")
print(f"Palavras com mais de 5 caracteres: {muitos_caracteres}")