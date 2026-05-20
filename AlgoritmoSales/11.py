# matriz = [[],[]]
# for i in range (len(matriz)):
#     for j in range(3):
#         numero = int(input("Insira um número: "))
#         matriz[i].append(numero)
# print(matriz)

# matriz = []
# for i in range(3):
#     matriz.append([])
# for i in range(len(matriz)):
#     for j in range(3):
#         numero = int(input("Insira um número: "))
#         matriz[i].append(numero)
# for i in range(len(matriz)):
#     for j in range(3):
#         print(f"matriz[{i}][{j}]: {matriz[i][j]}")

# matriz = []
# for i in range (3):
#     matriz.append([])
# for i in range(len(matriz)):
#     for j in range(4):
#         numero = int(input("Insira um número: "))
#         matriz[i].append(numero)
# soma_total = 0
# for i in range(len(matriz)):
#     soma_total += sum(matriz[i])
# print(f"Soma total: {soma_total}")

# matriz = []
# coluna = 3
# linha = 3
# for i in range(linha):
#     matriz.append([])
# for i in range(len(matriz)):
#     for j in range(coluna):
#         numero = int(input("Insira um número: "))
#         matriz[i].append(numero)
# maior_valor = matriz[0][0]
# for i in range(len(matriz)):
#     for j in range(coluna):
#         if matriz[i][j] > maior_valor:
#             maior_valor = matriz[i][j]
# print(maior_valor)

# matriz = []
# linha = 3
# coluna = 4
# for i in range(linha):
#     matriz.append([])
# for i in range(linha):
#     for j in range(coluna):
#         numero = int(input("Insira um número: "))
#         matriz[i].append(numero)
# soma_linha = 0
# for i in range(linha):
#     soma_linha = sum(matriz[i])
#     print(f"Soma da linha {i}: {soma_linha}")
#     soma_linha = 0  

# matriz = []
# linha = 3
# coluna = 3
# for i in range(linha):
#     matriz.append([])
# for i in range(linha):
#     for j in range(coluna):
#         numero = int(input("Insira um número: "))
#         matriz[i].append(numero)
# for i in range(linha):
#     soma_coluna = 0
#     for j in range(coluna):
#         soma_coluna += matriz[j][i]
#     print(f"Soma da coluna {i}: {soma_coluna}")

# matriz = []
# linha = 4
# coluna = 4
# for i in range(linha):
#     matriz.append([])
# for i in range(linha):
#     for j in range(coluna):
#         numero = int(input("Insira um número: "))
#         matriz[i].append(numero)
# pares = []
# par = 0
# impares = []
# impar = 0
# for i in range(linha):
#     for j in range(coluna):
#         if j%2 == 0:
#             par += 1
#         else:
#             impar += 1
#     pares.append(par)
#     impares.append(impar)
#     par, impar = 0, 0
# print(pares, impares)