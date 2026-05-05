def calcular_inscricao(valor_base, taxa):
    valor_final = valor_base + (valor_base * taxa / 100)
    return valor_final

def converter_tempo(total_segundos):
    sobra_segundos = total_segundos % 60
    minutos = total_segundos // 60
    horas = minutos // 60
    minutos %= 60
    return f"{horas} hora(s), {minutos} minuto(s) e {sobra_segundos} segundo(s)."

def gerar_resumo_tempo(nome, total_segundos):
    return f"Participante {nome}: {converter_tempo(total_segundos)}"

def eh_par(numero):
    return numero % 2 == 0

def contar_pares_faixa(inicio, fim):
    num_par=0
    for numero in range(inicio,fim+1):
        if eh_par(numero):
            num_par+=1
    return num_par

nome=input("Digite o nome do participante: ")
valor_base = int(input("Digite o valor base da inscrição: "))
taxa = 0
print(f"Valor base: {calcular_inscricao(valor_base,taxa)}")
taxa = 10
print(f"Valor taxado: {calcular_inscricao(valor_base, taxa)}")
total_segundos = int(input("Digite o tempo total de prova em segundos: "))
print(gerar_resumo_tempo(nome, total_segundos))
inicio=int(input("Digite o início da faixa: "))
fim=int(input("Digite o fim da faixa: "))
print(f"{contar_pares_faixa(inicio,fim)} números pares")