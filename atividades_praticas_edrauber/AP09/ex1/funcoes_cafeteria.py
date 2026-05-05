
def calcular_preco_cafe(preco_base, acrescimo=0):
    return preco_base + acrescimo

def calcular_acompanhamento(preco, desconto=0):
    return preco - (preco / (100 / desconto))

def resumo_item(nome, valor):
    return str(nome) , f"R${valor:.2f}"

def calcular_totais(valor1, valor2, taxa_servico=10):
    return valor1 + valor2 , (valor1 + valor2) * (taxa_servico / 100), (valor1 + valor2)+(valor1 + valor2) * (taxa_servico / 100)