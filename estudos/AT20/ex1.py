jogador = []

def pontuacao_jogadores(jogador):
    for i in range(3):
        pontuacao = []
        print("Jogador" , i+1)
        for j in range(4):
            partida = int(input(""))
            pontuacao.append(partida)
        jogador.append(pontuacao)
    return jogador

if __name__ == "__main__":
    jogador = pontuacao_jogadores(jogador)
    for i in range(3):
        for j in range(4):
            valor = jogador[i][j]
            if j == 0:
                maior = 0
            if valor > maior:
                maior = valor
        print(f"Maior do jogador {i+1}: {maior}")