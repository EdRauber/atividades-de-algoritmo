def calcular_calorias(calorias_base, bonus=0):
    return calorias_base+bonus

def calcular_tempo_treino(tempo_principal, aquecimento=10):
    return tempo_principal+aquecimento

def analisar_desempenho(total_minutos):
    return total_minutos // 60 , total_minutos % 60

def consolidar_treino(calorias, meta=300):
    if calorias>=meta:
        return calorias-meta , calorias>=meta , "Meta atingida"
    else:
        return meta-calorias , calorias>=meta , "Meta não atingida"

