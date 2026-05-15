treino = []
x = 10

for i in range(x):
    treino.append(int(input("")))

contador = 0
quantidade_pico = 0
posicao_maior = []
valor_maior = []

for i in treino:
    if contador != 0 and contador != x - 1:
        if i > treino[contador - 1] and i > treino[contador + 1]:
            quantidade_pico += 1
            posicao_maior.append(contador)
            valor_maior.append(i)
    contador += 1

print(f"Quantidade de picos: {quantidade_pico}")
print(f"Posições dos picos: {posicao_maior}")
print(f"Valores dos picos: {valor_maior}")