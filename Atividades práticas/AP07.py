def ex1():
    #CT-1: entrada: 1,6 saida: 3/3 5/5 6/3
    #CT-2: entrada: 0,0: saida: ambos
    #CT-3: entrada: -1,-5 saida: -5/-5
    #CT-4: entrada: -1,5 saida: 0/ambos 3/3 5/5
    n_inicial=int(input("Número Inicial: "))
    n_final=int(input("Número Final: "))
    if n_final>n_inicial:
        for i in range(n_inicial, n_final+1):
            print("Número:"+ str(i))
            for j in range(n_inicial, i+1):
                if j%3==0 and j%5==0:
                    divisivel="múltiplo de ambos"
                elif j%3==0:
                    divisivel="múltiplo de 3"
                elif j%5==0:
                    divisivel="múltiplo de 5"
                else:
                    divisivel="nenhum"
                print(f"{j} - {divisivel}")
    else:
        for i in range(n_inicial, n_final-1,-1):
            print("Número:"+ str(i))
            for j in range(n_inicial, i-1, -1):
                if j%3==0 and j%5==0:
                    divisivel="múltiplo de ambos"
                elif j%3==0:
                    divisivel="múltiplo de 3"
                elif j%5==0:
                    divisivel="múltiplo de 5"
                else:
                    divisivel="nenhum"
                print(f"{j} - {divisivel}")

def ex2():
    #CT1: entrada: 3,5 saída final: 15 impar, médio
    #CT2: entrada: 0,1 saída final: null
    #CT3: entrada: -1,-5 saída final null
    line=int(input("Digite o número de linhas: "))
    colum=int(input("Digite o número de colunas: "))
    for linha in range(1,line+1):
        for coluna in range(1, colum+1):
            num=linha*coluna
            if num%2==0:
                paridade="par"
            else:
                paridade="impar"
            if num<10:
                tamanho="pequeno"
            elif num>20:
                tamanho="grande"
            else:
                tamanho="médio"
            if num>20:
                print(f"linha {linha} e coluna {coluna} → produto = {num} → {paridade}, Maior do que 20, {tamanho};")
            else:
                print(f"linha {linha} e coluna {coluna} → produto = {num} → {paridade}, {tamanho};")
        print("_________________________")

def ex3():
    #CT1: entrada: N=4 Saida: 7 8 9 10
    #CT2: entrada: N=0 Saida: null
    n = int(input("Digite o número de N: "))
    contador=1
    for linha in range(1, n+1):
        valores_c=""
        soma_c=0
        divisores_c=0
        for coluna in range(contador, contador+linha):
            valores_c+=str(coluna)+" "
            soma_c+=coluna
            if coluna==1:
                maior_c=coluna
            else:
                if coluna>maior_c:
                    maior_c=coluna
            if coluna%3==0:
                divisores_c+=1
        contador=coluna+1
        print(f"{valores_c}| soma = {soma_c} | maior = {maior_c} | multiplos de 3 = {divisores_c}")

def ex4():
    turma=int(input("Digite a quantidade de turmas: "))
    for i in range(1, turma+1):
        aluno=int(input(f"Digite a quantidade de alunos na turma {i}: "))
        aprovados=0
        reprovados=0
        recuperação=0
        nota_geral=0
        for j in range(1, aluno+1):
            nota_1=float(input(f"Digite a nota 1 do aluno {j}: "))
            nota_2=float(input(f"Digite a nota 2 do aluno {j}: "))
            nota_media=(nota_1+nota_2)/2
            nota_geral+=nota_media
            if nota_media>7:
                estado="aprovado"
                aprovados+=1
            elif nota_media<5:
                estado="reprovado"
                reprovados+=1
            else:
                estado="recuperação"
                recuperação+=1
            print(f"Aluno {j} teve uma média de {nota_media:.1f} e por isso está {estado}.")
        nota_geral/=aluno
        print(f"Na turma {i} a nota média foi {nota_geral:.1f}, com {aprovados} aprovado(s), {recuperação} em recuperação, e {reprovados} reprovado(s).")

def ex5():
    mesas = int(input("Digite a quantidade de mesas atendidas: "))
    faturamento_total,hamburger,refrigerante,sobremesa=0,0,0,0
    for i in range(1 , mesas + 1):
        pedidos = int(input(f"Digite a quantidade de pedidos feitos na mesa {i}: "))
        quantia_pedidos=0
        conta_mesa=0
        for j in range(1 , pedidos + 1):
            codigo = int(input(f"Digite o código do pedido {j}: "))
            status=True
            if codigo==1:
                valor=18
            elif codigo==2:
                valor=6
            elif codigo==3:
                valor=9
            else:
                print("código de produto inválido, desconsiderando item.")
                status=False
            if status:
                qnt = int(input("Digite a quantidade de itens pedidos: "))
                if qnt<=0:
                    print("quantia de produto inválida, desconsiderando item.")
                else:
                    if codigo==1:
                        hamburger+=qnt
                    elif codigo==2:
                        refrigerante+=qnt
                    elif codigo==3:
                        sobremesa+=qnt
            if status:
                conta_mesa+=valor*qnt
                quantia_pedidos+=qnt
        print(f"A mesa {i} gastou um total de R${conta_mesa} com um total de {quantia_pedidos} itens pedidos.")
        faturamento_total+=conta_mesa

    print(f"O dia de hoje faturou um total de R${faturamento_total} vendendo {hamburger} hambúrgeres, {refrigerante} refrigerantes, e {sobremesa} sobremesas.")

ex5()