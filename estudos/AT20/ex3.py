import ex2 as funcoes

for i in range(4):
    if i == 0 or maior < media_partida[i]:
        maior = media_partida[i]
        num_partida = i

print(f"A partida {num_partida+1} teve melhor desempenho em média. /n Desempenho médio = {maior}")
    