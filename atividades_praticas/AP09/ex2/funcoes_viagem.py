def calcular_passagem(valor_base, bagagem=0):
    return valor_base + bagagem

def calcular_hospedagem(valor_diaria, dias=1, taxa_extra=0):
    return (valor_diaria*dias) + taxa_extra

def converter_duracao(total_horas):
    return total_horas//24 , total_horas%24

def calcular_orcamento(passagem, hospedagem, alimentacao=0):
    return passagem + hospedagem , alimentacao , passagem + hospedagem + alimentacao
