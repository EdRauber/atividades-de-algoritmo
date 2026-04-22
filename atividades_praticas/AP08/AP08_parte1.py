def exibir_cabecalho():
    print(f"Sistema de atendimento: Laerte Empire")

def exibir_cliente(nome):
    print(f"Cliente: {nome}")

def calcular_valor_final(valor_produto, desconto):
    valor_final = valor_produto-(valor_produto * (desconto/100))
    print(f"R${valor_final}")
    return valor_final

def calcular_comissao(valor_final):
    comissao = valor_final * 0.05
    print(f"{comissao:.2f}")

exibir_cabecalho()
nome=input("Digite seu nome: ")
exibir_cliente(nome)
valor_produto=int(input("Digite o valor do produto: "))
desconto=int(input("Digite o valor em porcentagem do desconto: "))
valor_final=calcular_valor_final(valor_produto, desconto)
calcular_comissao(valor_final)
