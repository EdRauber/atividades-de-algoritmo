def nota_valida(nota):
    if 0<=nota<=100:
        return True
    else:
        return False

def classificar_desempenho(nota):
    if 89<nota<=100:
        return "Excelente"
    elif 69<nota<90:
        return "Bom"
    elif 59<nota<70:
        return "Regular"
    else:
        return "Insuficiente"

def calcular_situacao(nota):
    if nota>=70:
        return "Aprovado"
    elif 50<=nota<70:
        return "Recuperação"
    else:
        return "Reprovado"
    
def gerar_resumo_correcao(nota):
    print(classificar_desempenho(nota))
    print(calcular_situacao(nota))




for aluno in range(1,4):
    print(f"aluno {aluno}")
    nota=int(input(f"Digite a nota do aluno {aluno}: "))
    if (nota_valida(nota)):
        gerar_resumo_correcao(nota)
    else:
        print("nota invalída")

