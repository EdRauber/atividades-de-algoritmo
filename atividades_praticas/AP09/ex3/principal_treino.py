import funcoes_treino as funcoes

calorias_base = int(input("Digite a quantidade base de calorias gastas no treino: "))
bonus = int(input("Digite a quantidade de calorias gastas a mais: "))
calorias = funcoes.calcular_calorias(calorias_base , bonus)

tempo_principal = int(input("Digite o tempo do treino principal: "))
aquecimento = int(input("Digite o tempo gasto nos aquecimentos: "))
total_minutos = funcoes.calcular_tempo_treino (tempo_principal , aquecimento)
tempo_horas , tempo_minutos = funcoes.analisar_desempenho (total_minutos)

meta = int(input("Digite a meta de calorias gastas no treino: "))
resultados = funcoes.consolidar_treino(calorias , meta)

print(f"Total de calorias gatas: {calorias} kcal.")
print(f"O tempo total gasto no treino foi {tempo_horas} horas e {tempo_minutos} minutos.")
print(f"A diferença de calorias gastas a sua meta são de {resultados[0]}kcal")
print(resultados[2])
print("____________________________________________________________")
print("Resumo:")
print(f"Tempo gasto: {tempo_horas}h e {tempo_minutos}m \n Calorias gastas: {calorias}kcal \n Diferença com a meta: {resultados[0]}kcal \n {resultados[2]}")