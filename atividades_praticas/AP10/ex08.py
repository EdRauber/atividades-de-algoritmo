pessoas = []
x = 8

for i in range(x):
    nome = input("")
    pessoas.append(nome)

nombre = input("Digite um nome: ")
ocorrencias = 0
encontrado = False

for i in pessoas:
    if nombre == i :
        ocorrencias += 1
        encontrado = True

if encontrado:
    print("Nome encontrado.")
else:
    print("Nome não encontrado.")
print(f"Quantidade de ocorrências: {ocorrencias}")