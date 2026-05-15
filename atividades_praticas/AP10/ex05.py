numeros = []
x = 7

for i in range(x):
    captura = int(input(""))
    numeros.append(captura)

contador = 0 

for i in numeros:
    if contador == 0:
        maior = i
        menor = i
    elif i > maior:
        maior = i
        posicao_maior = contador
    elif i < menor:
        menor = i
        posicao_menor = contador
    contador += 1

print(f"Maior valor: {maior}")
print(f"Posição do maior valor: {posicao_maior}")
print(f"Menor valor: {menor}")
print(f"Posição do menor valor: {posicao_menor}")