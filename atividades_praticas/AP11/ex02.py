matriz = []
for i in range(3):
    lista = []
    for j in range(3):
        lista.append(int(input("")))
    matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")