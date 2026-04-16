def ex8():

    #valores padrões
    contador=0
    soma_num=0

    #número inicial
    num=int(input("Digite um número (0 para encerrar): "))

    #repetição com quebra
    while num!=0:
        soma_num+=num
        contador+=1
        num=int(input("Digite um número (0 para encerrar): "))

    #Resultado final
    print(f"Você digitou {contador} números, somando a {soma_num}")

def ex9():

    #valores padrões
    quantidade=0
    valor_total=0

    #venda inicial
    venda=int(input("Digite o valor da venda (0 para encerrar): "))

    #repetição
    while venda!=0:
        quantidade+=1
        valor_total+=venda
        venda=int(input("Digite o valor da venda (0 para encerrar): "))
    
    #Processar média
    media=valor_total/quantidade

    #Resultado final
    print(f"O valor total vendido foi: {valor_total}R$. Dando em média {media:.0f}R$ por venda, com um total de {quantidade} itens vendidos.")

def ex10():
    
    #valores padrões
    quantidade=0
    plus80temp=0
    temp_total=0

    #Temperatura inicial
    temp=int(input("Digite a temperatura (-1 para encerrar): "))

    #repetição
    while temp!=-1:
        quantidade+=1
        temp_total+=temp

        #Def de mais alta e baixa na primeira repetição
        if quantidade==1:
            temp_maior=temp
            temp_menor=temp

        #Def de mais alta e baixa nas demais repetições
        if temp>temp_maior:
            temp_maior=temp
        if temp_menor>temp:
            temp_menor=temp

        #Def de 80+
        if temp>80:
            plus80temp+=1

        temp=int(input("Digite a temperatura (-1 para encerrar): "))
   
   #Calculo da média
    media_temp=temp_total/quantidade

    #Print dos resultados finais
    print(f"{quantidade} temperaturas foram registradas, {temp_maior}° foi a maior temperatura registrada, enquanto {temp_menor}° foi a menor.")
    print(f"A média de temperaturas registradas foi {media_temp}°, com {plus80temp} acima dos 80°.")

def ex11():

    #valores padrões
    contador=0

    #Def do numero para tabuada
    num=int(input("Digite o número: "))
    print(f"Tabuada do {num}")

    #Repetiçaõ tabuada
    while contador!=10:
        contador+=1
        produto=num*contador
        print(f"{num} x {contador} = {produto}")

def ex12():

    #Def de parâmetros para o retângulo
    linhas=int(input("Digite o número de linhas: "))
    colunas=int(input("Digite o número de colunas: "))


    #Jeito fácil (mas eu preciso fzr com dois whiles)
    # texto_C="*"*colunas
    # while linhas!=contador:
    #     print(texto_C)
    #     contador+=1

    #Repetição de linhas
    contador_L=0
    while linhas!=contador_L:
        contador_C=0
        linha=""

        #repetição de coluna
        while colunas!=contador_C:
            linha+="*"
            contador_C+=1

    #Repetição de linha parte 2
        print(linha)
        contador_L+=1

def ex13():
    num=int(input("Digite o número: "))
    contador=0
    coluna=""
    num_coluna=""

    while contador!=num:
        contador+=1
        num_coluna=str(contador)
        coluna+=num_coluna
        print (coluna)

def ex14():
    
    tempo=0
    massa_inicial=float(input("Digite a massa: "))
    massa=massa_inicial

    while massa>=0.5:
        massa=massa/2
        tempo+=50

    massa_final=massa
    print(f"Massa inicial: {massa_inicial}g")
    print(f"Massa final: {massa_final:.4f}g")
    print(f"tempo necessário: {tempo}s")

def ex15():
    s=float(1)
    sharmonica="1"
    contador=1
    num=int(input("Digite o número: "))
    while contador!=num:
        contador+=1
        div_str=str(contador)
        sharmonica+=" + 1/"+div_str
        div_int=1/contador
        s+=div_int
    print(f"S = {sharmonica}")
    print(f"S = {s:.2f}")

def ex16():
    resultado=float(1)
    soma="1"
    contador=1
    num=int(input("Digite o número: "))

    while contador!=num:
        contador+=1
        div_str=str(contador)
        div_float=1/contador
        if contador%2==0:
            soma+=" - 1/"+div_str
            resultado-=div_float
        else:
            soma+=" + 1/"+div_str
            resultado+=div_float
    
    print(f"S = {soma}")
    print(f"S = {resultado:.2f}")

def ex17():
    resultado=0
    soma=""
    contador=0
    divisor=1
    num=int(input("Digite o número: "))
    
    while num!=contador:
        contador+=1
        con_str=str(contador)
        div_str=str(divisor)
        if contador<num:
            soma+=(f" {con_str}/{div_str} +")
        else:
            soma+=(f" {con_str}/{div_str}")
        resultado+=contador/divisor
        divisor+=contador+1
    
    print(f"S = {soma}")
    print(f"S = {resultado:.2f}")

def ex18():

    #valores padrões
    valor_medio=0
    lanche,bebida,sobremesa=0,0,0
    valor_total,quantidade=0,0
    num=""

    #repetição de programa
    while num!=0:
        print("_________________")
        print("1 - Registrar venda")
        print("2 - Mostrar total vendido")
        print("3 - Mostrar quantidade de vendas")
        print("4 - Mostrar valor médio das vendas")
        print("5 - Mostrar quantidade vendida por tipo de produto")
        print("0 - Encerrar sistema")
        print("_________________")
        num=int(input())

    #Registro de venda
        if num==1:

            #Código
            code=int(input("Código do produto: "))

            #Número informado incorreto
            while code!=1 and code!=2 and code!=3:
                print("Código do produto inválido, por favor, tente novamente.")
                print("1 - Lanche")
                print("2 - Bebida")
                print("3 - Sobremesa")
                code=int(input("Código do produto: "))

            #associação de código com produto
            if code==1:
                lanche+=1
                print("produto:Lanche")
            if code==2:
                bebida+=1
                print("produto:Bebida")
            if code==3:
                sobremesa+=1
                print("produto:Sobremesa")

            #Preço
            preco=int(input("Preço do produto: "))
            
            #Preço incorreto
            while preco<0:
                print("preço de produto inválido, por favor, tente novamente (valor do produto deve ser acima de zero)")
                preco=int(input("Preço do produto: "))

            #Informações extra do produto
            valor_total+=preco
            quantidade+=1


        #Total vendido
        if num==2:
            print(f"valor total vendido: {valor_total}R$")

        #Quantidade vendido
        if num==3:
            print(f"quantidade total de itens vendidos: {quantidade}")

        #Valor médio vendido
        if num==4:
            valor_medio=valor_total/quantidade
            print(f"o valor médio por venda é: {valor_medio:.2f}R$")
        
        #Quantidade de cada tipo de produto vendido
        if num==5:
            print(f"Foram registradas {lanche} vendas de lanches, {bebida} vendas de bebidas e {sobremesa} vendas de sobremesas")

        #Número informado incorreto
        if num!=1 and num!=2 and num!=3 and num!=4 and num!=5 and num!=0:
            print("ERRO: número digitado inválido, por favor, tente novamente.")

        #Finalização da operação
        if num==0:
            valor_medio=valor_total/quantidade
            print(f"- {valor_total}R$ foram ganhos")
            print(f"- {quantidade} itens foram vendidos.")
            print(f"- O valor médio de cada venda foi: {valor_medio:.2f}R$")
            print(f"- {lanche} Lanches foram vendidos")
            print(f"- {bebida} Bebidas foram vendidas")
            print(f"- {sobremesa} Sobremesas foram vendidas")
    print("_________________")
    print("fim da operação")

ex18()