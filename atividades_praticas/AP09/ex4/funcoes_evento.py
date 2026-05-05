def intencao(sim_nao):
    if sim_nao == 1:
        return True
    else:
        return False 

def calcular_valor_base(tipo_ingresso, valor_padrao=120):
    if tipo_ingresso == "regular":
        return valor_padrao
    elif tipo_ingresso == "vip":
        return valor_padrao+(valor_padrao/2)
    elif tipo_ingresso == "estudante":
        return valor_padrao - ((valor_padrao * 2) / 5)

def calcular_extras(valor_base, oficinas=0, material_extra=False):
    if material_extra:
        return 30*oficinas , 20 , valor_base+(30*oficinas)+20
    elif not material_extra:
        return 30*oficinas , 0 , valor_base+(30*oficinas)

def aplicar_desconto(valor_parcial, cupom=0, taxa_admin=5):
    return valor_parcial * (cupom / 100) , valor_parcial * (taxa_admin/100) , (valor_parcial - (valor_parcial * (cupom / 100))) + (valor_parcial * (taxa_admin/100))

def classificar_participacao(oficinas, material_extra, total_final):
    if oficinas>=2 and material_extra:
        return "Inscrição completa"
    elif oficinas>=1:
        return "Inscrição intermediária"
    else:
        return "Inscrição básica"

def gerar_relatorio_participante(nome, tipo_ingresso, valor_padrao, oficinas, material_extra, cupom=0):
    valor_base = calcular_valor_base (tipo_ingresso , valor_padrao)
    valor_oficinas , valor_extra , valor_parcial = calcular_extras(valor_base , oficinas , material_extra)
    valor_desconto , valor_taxa_adm , total_final = aplicar_desconto(valor_parcial , cupom, taxa_admin=5)
    return valor_base , valor_oficinas , valor_extra , valor_desconto , valor_taxa_adm , total_final , classificar_participacao(oficinas, material_extra , total_final)
