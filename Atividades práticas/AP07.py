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

