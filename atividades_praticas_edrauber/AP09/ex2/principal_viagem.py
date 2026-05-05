import atividades_praticas_edrauber.AP09.ex2.funcoes_viagem as funcoes

valor_base = int(input("Digite o valor base da passagem: "))
bagagem = int(input("Digite a taxa da bagagem: "))
passagem = funcoes.calcular_passagem(valor_base , bagagem)

valor_diarias = int(input("Digite o valor da diária: "))
dias = int(input("Digite a quantidade de dias: "))
taxa_extra = int(input("Digite o valor da taxa extra da hospedagem: "))
hospedagem = funcoes.calcular_hospedagem( valor_diarias , dias , taxa_extra)

total_horas = int(input("Digite a duração total (em horas) da viagem: "))
total_dias , sobra_horas = funcoes.converter_duracao(total_horas)

alimentacao = int(input("Digite o gasto com alimentação: "))
orcamento_total = funcoes.calcular_orcamento(passagem , hospedagem , alimentacao)

print(f"Valor final da passagem: R$ {passagem}.")
print(f"Valor final da hospedagem: R$ {hospedagem}.")
print(f"A viagem dura {total_dias} dias e {sobra_horas} horas.")
print(f"A viagem tem um custo fixo de R$ {orcamento_total[0]}.")
print(f"A viagem tem um custo extra de R$ {orcamento_total[1]}.")
print(f"A viagem tem um custo total de R$ {orcamento_total[3]}.")