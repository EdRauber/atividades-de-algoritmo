def exibir_cabecalho():
    print("Laerte Store: Sistema de Atendimento")

def exibir_cliente(nome):
    print(f"Cliente: {nome}")

def calcular_comissao(valor_final):
    comissao = valor_final * 5/100
    print(f"Comissão: {comissao}")

def calcular_valor_final(valor_produto, desconto):
    valor_final = valor_produto - (valor_produto * desconto / 100)
    print(f"Valor final do produto: R${valor_final}")
    return valor_final

# exibir_cabecalho()
# nome = input("Digite seu nome: ")
# exibir_cliente(nome)
# valor_produto = int(input("Insira o valor do produto: "))
# desconto = int(input("Insira o percentual do desconto: "))
# valor_final = calcular_valor_final(valor_produto, desconto)
# calcular_comissao(valor_final)


def nota_valida(nota):
    if nota < 0 or nota > 100:
        return False
    else:
        return True

def classificar_desempenho(nota):
    if 89<nota<=100:
        return "Excelente"
    elif 69<nota<=89:
        return "Bom"
    elif 59<nota<=69:
        return "Regular"
    else:
        return "Insuficiente"

def calcular_situacao(nota):
    if nota >= 70:
        return "Aprovado"
    elif 50<=nota<=69:
        return "Recuperação"
    else:
        return "Reprovado"

def gerar_resumo_correcao(nota):
    print(classificar_desempenho(nota))
    print(calcular_situacao(nota))

# for aluno in range(1,4):
#     print("________________")
#     print(f"Aluno {aluno}:")
#     nota = int(input("Digite sua nota: "))
#     if (nota_valida(nota)):
#         gerar_resumo_correcao(nota)