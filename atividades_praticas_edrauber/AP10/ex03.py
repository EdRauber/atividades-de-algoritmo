numeros = []
x = 10

for i in range(x):
    inpute = int(input(""))
    numeros.append(inpute)

par = 0
pares = []
impar = 0
impares = []

for i in numeros:
    if i % 2 == 0:
        par += 1
        pares.append(i)
    elif i % 2 != 0:
        impar += 1
        impares.append(i)

print(f"Quantidade de pares: {par}")
print(f"Quantidade de ímpares: {impar}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")