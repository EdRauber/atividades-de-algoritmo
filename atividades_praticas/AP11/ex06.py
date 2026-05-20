matriz = []
for i in range(3):
    lista = []
    for i in range(3):
        lista.append(int(input("")))
    matriz.append(lista)

for i in range(3):
    soma_coluna = 0
    for j in range(3):
        soma_coluna += matriz[j][i]
    print(f"Soma da coluna {i}: {soma_coluna}")