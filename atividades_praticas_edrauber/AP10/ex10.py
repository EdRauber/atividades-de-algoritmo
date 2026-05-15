numeros = []
x = 8

for i in range(x):
    numeros.append(int(input("")))

ordem_crescente = True
primeiro = True

for i in numeros:
    if primeiro:
        anterior = i
        primeiro = False
    else:
        if i >= anterior and ordem_crescente:
            anterior = i
        elif ordem_crescente:
            ordem_crescente = False

if ordem_crescente:
    print("A lista está em ordem crescente.")
else:
    print("A lista não está em ordem crescente.")