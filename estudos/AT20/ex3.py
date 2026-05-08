from ex1 import pontuacao_jogadores as pontuacao
from ex2 import calcular_media as media

jogador = []
jogador = pontuacao(jogador)
media_partida = []
media_partida = media(jogador, media_partida)

for i in range(4):
    if i == 0 or maior < media_partida[i]:
        maior = media_partida[i]
        num_partida = i

print(f"A partida {num_partida+1} teve melhor desempenho em média. \n Desempenho médio = {maior}")
    