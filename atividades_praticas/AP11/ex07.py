matriz = []
for i in range(4):
    lista = []
    for j in range(4):
        lista.append(int(input("")))
    matriz.append(lista)


pares , impares = [] , []
for i in range(4):
    par , impar = 0 , 0
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            par += 1
        if matriz[j][i] % 2 != 0:
            impar += 1
    pares.append(par)
    impares.append(impar)
print(f"Pares: {pares}")
print(f"Impares: {impares}")
