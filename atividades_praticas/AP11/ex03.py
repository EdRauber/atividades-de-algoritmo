matriz = []
soma = 0
for i in range(3):
    lista = []
    for j in range(4):
        lista.append(int(input("")))
    matriz.append(lista)
    soma += sum(lista)


print(soma)