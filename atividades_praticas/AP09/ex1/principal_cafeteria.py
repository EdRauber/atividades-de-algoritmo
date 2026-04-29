import funcoes_cafeteria

nome_cafe=(input("Digite o nome do café: "))
preco_base=float(input("Preço base do café: "))
acrescimo=float(input("Digite o valor do acréscimo (0 para nenhum): "))

total_cafe=funcoes_cafeteria.calcular_preco_cafe(preco_base , acrescimo)
print(funcoes_cafeteria.resumo_item(nome=nome_cafe , valor=total_cafe))


nome_acompanhamento=input("Digite o nome do acompanhamento: ")
preco=float(input("Digite o preço do acompanhamento: "))
desconto=float(input("Digite o valor do desconto em % (0 para nenhum): "))

total_acompanhamento=funcoes_cafeteria.calcular_acompanhamento(preco, desconto)
print(funcoes_cafeteria.resumo_item(nome=nome_acompanhamento , valor=total_acompanhamento))

subtotal , taxa_servico , total_pedido = funcoes_cafeteria.calcular_totais(valor1=total_cafe, valor2=total_acompanhamento, taxa_servico=float(input("Digite a taxa do serviço: ")))

print(f"Subtotal: R${subtotal}")
print(f"Taxa de servico: R${taxa_servico:.2f}")
print(f"Total Final: R${total_pedido}")