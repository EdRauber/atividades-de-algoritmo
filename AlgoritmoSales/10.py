# lista = []
# for i in range (5):
#     numero = int(input("Digite um número: "))
#     lista.append(numero)

# print(lista)
# for n in lista:
#     print(n)



# lista = []
# for i in range (6):
#     numero = float(input("Digite um número: "))
#     lista.append(numero)
# media = (sum(lista))/6

# print(f"Soma: {sum(lista)}")
# print(f"Média: {media}")



# numeros = []
# pares = []
# par = 0
# impares = []
# impar = 0
# for i in range ((10)):
#     numero = int(input("Digite um núero: "))
#     numeros.append(numero)

#     if numero%2 == 0:
#         par += 1
#         pares.append(numero)
#     elif numero%2 != 0:
#         impar += 1
#         impares.append(numero)

# print(f"Quantidade de pares: {par}")
# print(f"Quantidade de impares: {impar}")
# print(f"Pares: {pares}")
# print(f"Imares: {impares}")



# palavras = []
# for i in range (8):
#     texto = input("Digite uma palavra: ")
#     palavras.append(texto)

# for palavra in range (len(palavras)):
#     print(palavras[len(palavras) - 1 - palavra])



numeros = []
maior = int(input("Digite um número: "))
numeros.append(maior)
menor = maior
posicao = 1
for i in range (6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

for indice in range (len(numeros) - 1):
    if numeros[indice] == maior:
        posicao_maior = indice
    elif numeros[indice] == menor:
        posicao_menor = indice

print(f"Maior valor: {maior}")
print(f"Posição do maior valor: {posicao_maior}")
print(f"Menor valor: {menor}")
print(f"Posição do menor valor: {posicao_menor}")
