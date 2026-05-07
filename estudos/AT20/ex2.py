from ex1 import pontuacao_jogadores as funcao

jogador=[]
jogador = funcao(jogador)
media_partida = []

for i in range(4):
    soma = 0
    for j in range(3):
        soma += jogador[j][i]
    media = soma / 3
    media_partida.append(media)
    print(f"media da partida {i+1}: {media}")