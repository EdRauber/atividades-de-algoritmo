def ex1():
    for apple in range(1, 11):
        print(apple)

def ex2():
    for apple in range(10,0,-1):
        print(apple)
    print("Fim da contagem")

def ex3():
    n=int(input("Digite o número n: "))
    m=int(input("Digite o número m: "))
    resultado=m
    resultado_string=""
    for apple in range (n,m):
        resultado+=apple
        resultado_string+=" "+str(apple)+" +" 
    print(f"{resultado_string} {m} = {resultado}")

def ex4():
    vogais=0
    word=input("Digite a palavra: ")
    for letter in word:
        if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
            vogais+=1
    print(f"número de vogais: {vogais}")

def ex5():
    contador=0
    word=input("Digite a palavra: ")
    caracter=input("Digite uma letra: ")
    for letter in word:
        if caracter==letter:
            contador+=1
    print(contador)

def ex6():
    num_maior=0
    for number in range(1,6):
        num=int(input("Digite o número: "))
        if num>num_maior:
            num_maior=num
    print(num_maior)

def ex7():
    eh_pal=True
    word=input("Digite a palavra: ")
    for letter in range(0,len(word)):
        if word[letter] != word[len(word)-1-letter]:
            eh_pal=False
    if eh_pal==False:
        print("Não é palindromo")
    else:
        print("É palindromo")

def ex8():
    # Sem for alininhado

    # n=int(input("Digite o número n: "))
    # for linha in range(1,n+1):
    #     if linha==1 or linha==n:
    #         print("1"*n)
    #     else:
    #         print("1"+(str(0)*(n-2))+"1")

    n=int(input("Digite o número n: "))
    for coluna in range(n):
        tabela=""
        for linha in range(n):
            if coluna==0 or coluna==n-1 or linha==0 or linha==n-1:
                tabela+="1"
            else:
                tabela+="0"
        print(tabela)

def ex9():
    prefixo=""
    eh_palindromo="sim"
    word=input("Digite a palavra: ")
    for letter in range(len(word)):
        prefixo+=word[letter]
        eh_palindromo="sim"
        for letter2 in range(len(prefixo)):
            if prefixo[letter2] != prefixo[len(prefixo) - letter2 - 1]:
                eh_palindromo="não"
        print(f"{prefixo} - {eh_palindromo}")

def ex10():
    caracteres=0
    maisculo=0
    minusculo=0
    num=0
    especial=0
    senha=input("Digite a senha: ")
    for digito in senha:
        # caracteres+=1  no lugar disso eu posso fzr um len para ser um código mais economico
        if "A" <= digito <= "Z":
            maisculo+=1
        elif "a" <= digito <= "z":
            minusculo+=1
        elif "1" <= digito <= "9":
            num+=1
        else:
            especial+=1
    caracteres=len(senha) #mais economico pq só roda uma vez no lugar de varias no for
    if caracteres>=8 and maisculo>0 and minusculo>0 and num>0 and especial>0:
        forca_senha="sim"
    else:
        forca_senha="não"
    print(f"Quantidade de caracteres: {caracteres}")  
    print(f"Letras maiusculas: {maisculo}")
    print(f"Letras minusculas: {minusculo}")
    print(f"Digitos: {num}")
    print(f"Caracteres especiais: {especial}")
    print(f"Senha forte: {forca_senha}")

def ex11():
    palavra=0
    dentro_de_palavra=False
    frase=input("Digite o texto: ")
    for letra in frase:
        if letra!=" "and not dentro_de_palavra:
            palavra+=1
            dentro_de_palavra=True
        elif letra==" " and dentro_de_palavra:
            dentro_de_palavra=False

    print(f"Quantidade de palavras: {palavra}")

def ex12():
    menu=""
    config=False
    exec=False
    while menu!="0":
        print("1 - Configurar simulação")
        print("2 - Executar simulação")
        print("3 - Mostrar relatório geral")
        print("4 - Mostrar evolução mês a mês")
        print("0 - Encerrar sistema")
        menu=input("")

        if menu=="1":
            valor_inical=int(input("Valor inicial: "))
            aporte_mensal=int(input("Aporte mensal: "))
            taxa_de_juros=int(input("Taxa de juros mensal (em porcentagem): "))/100
            tempo=int(input("Meses: "))
            historico=[0] * tempo
            print("____________________")
            print("Valores Configurados")
            print("____________________")
            config=True
        
        elif menu=="2":
            if not config:
                print("________________________________________")
                print("ERRO")
                print("Primeiro configure valores para a simulação")
                print("________________________________________")
            else:
                investimento=valor_inical
                saldo_maior, saldo_total=0, 0
                saldo=valor_inical
                for mes in range(tempo):
                    investimento+=aporte_mensal
                    saldo+=aporte_mensal
                    saldo*=(1+taxa_de_juros)
                    saldo_total+=saldo
                    if saldo>saldo_maior:
                        saldo_maior=saldo
                        mes_maior=mes+1
                    historico[mes] = saldo

                lucro=saldo-investimento
                saldo_medio=saldo_total/tempo
                config=False
                exec=True
                print("_________________________________")
                print("Simulação executada com sucesso.")
                print("_________________________________")

        
        elif menu=="3":
            if not exec:
                print("________________________________________")
                print("ERRO")
                print("primeiro configure e execute a simulação")
                print("________________________________________")
            else:
                print("Relatório Geral")
                print(f"Valor inicial: {valor_inical}")
                print(f"Aporte mensal: {aporte_mensal}")
                print(f"Taxa de juros mensal: {taxa_de_juros *100}%")
                print(f"Meses simulados: {tempo}")
                print(f"Total investido: {investimento}")
                print(f"Saldo final: {saldo:.2f}")
                print(f"Lucro total: {lucro:.2f}")
                print(f"Saldo médio na simulação: {saldo_medio:.2f}")
                print(f"Maior saldo registrado: {saldo_maior:.2f}")
                print(f"Mês do maior saldo: {mes_maior}")

        elif menu=="4":
            if exec:
                print("Evolução mês a mês")
                for mes in range(tempo):
                    print(f"Mês {mes+1}: {historico[mes]:.2f}")
            else:
                print("________________________________________")
                print("ERRO")
                print("primeiro configure e execute a simulação")
                print("________________________________________")

        elif menu=="0":
            if exec:
                print("Resumo final")
                print(f"total investido: {investimento}")
                print(f"Saldo final: {saldo:.2f}")
                print(f"Lucro total: {lucro:.2f}")
        
        else:
            print("______________________________")
            print("ERRO")
            print("Escolha Inválida - tente novamente")
            print("______________________________")

ex12()