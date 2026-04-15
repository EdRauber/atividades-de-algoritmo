#QUESTÃO-1
# numero_a = int(input("Insira um número: "))
# numero_b = int(input("Insira o segundo número: "))
# for i in range (numero_a, numero_b + 1):
#     print(f"Número {i}")
#     for numero in range (1, 1 + i):
#         if numero%3 == 0 and numero%5 == 0:
#             print(f"{numero} - múltiplo de ambos")
#         elif numero%3 == 0:
#             print(f"{numero} - múltiplo de 3")
#         elif numero%5 == 0:
#             print(f"{numero} - múltiplo de 5")
#         else:
#             print(f"{numero} - nenhum")
#     print("______________________")

#QUESTÃO-2
numero1 = int(input("Insira o número de linhas: "))
numero2 = int(input("Insira o número de colunas: "))
par_ou_impar = ""
numero = ""
for linha in range (1, numero1 + 1):
    for coluna in range (1, numero2 + 1):
        resultado = linha * coluna
        if resultado%2 == 0:
            par_ou_impar = "par"
        else:
            par_ou_impar = "ímpar"
        if resultado <= 10:
            tamanho = "pequeno"
        elif resultado > 20:
            tamanho = "grande"
        else:
            tamanho = "médio"
        print(f"linha {linha}, coluna {coluna} → {resultado}, {par_ou_impar}, {tamanho}")

#QUESTÃO-3
