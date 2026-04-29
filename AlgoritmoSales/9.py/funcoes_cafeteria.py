def calcular_preco_cafe(preco_base, acrescimo=0):
    return preco_base + acrescimo

def calcular_acompanhamento(preco, desconto=0):
    return preco - (preco * desconto/100)

def resumo_item(nome, valor):
    return nome , f"R${valor :.2f}"

def calcular_totais(valor1, valor2, taxa_servico=10):
    return valor1 + valor2 , taxa_servico * (valor2 + valor1)/ 100 , (valor1 + valor2) + (taxa_servico * (valor2 + valor1)/ 100)