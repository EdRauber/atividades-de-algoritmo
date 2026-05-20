matriz = []
soma_linhas = []
for i in range(3):
    lista = []
    soma = 0
    for j in range(4):
        num = int(input(""))
        lista.append(num)
        soma += num 
    soma_linhas.append(soma)
    matriz.append(lista)

for i in range(len(soma_linhas)):
    print(f"Soma da linha: [{i}] : {soma_linhas[i]}")