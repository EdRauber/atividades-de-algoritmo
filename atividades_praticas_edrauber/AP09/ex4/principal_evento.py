import atividades_praticas_edrauber.AP09.ex4.funcoes_evento as funcoes

for i in range (3):
    print(f"participante {i+1}")
    nome = input("Digite seu nome: ")
    tipo_ingresso = input("Digite o tipo do ingresso (regular / vip /estudante): ")
    oficinas = int(input("Digite quantas oficinas deseja participar: "))
    material_extra = funcoes.intencao(sim_nao = int(input("Deseja materia extra (sim = 1/não = 0)? ")))
    cupom = int(input("Digite o valor (em %) do desconto: "))
    valor_base , valor_oficinas , valor_extra , valor_desconto , valor_taxa_adm , total_final , inscricao = funcoes.gerar_relatorio_participante(nome, tipo_ingresso, valor_padrao=120, oficinas=oficinas, material_extra=material_extra, cupom=cupom)

    print("__________________________________")
    print(f"Nome: {nome}")
    print(f"Tipo do ingresso: {tipo_ingresso}")
    print(f"Valor base do ingresso: {valor_base}")
    print(f"Valor das oficinas extras: {valor_oficinas}")
    print(f"Valor do materia extra: {valor_extra}")
    print(f"Valor do desconto aplicado: {valor_desconto}")
    print(f"valor da taxa admistrativa: {valor_taxa_adm}")
    print(f"valor final da inscrição: {total_final}")
    print(f"Status da inscrição: {inscricao}")

    print("_____________")