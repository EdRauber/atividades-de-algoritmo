matriz = []
maior = 0
for i in range(3):
    lista = []
    for j in range(3):
        num = int(input(""))
        lista.append(num)
        if num > maior:
            maior = num
    matriz.append(lista)

print(maior)