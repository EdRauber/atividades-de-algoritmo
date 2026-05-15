numeros = []
x = 7

for i in range(x):
    numeros.append(int(input("")))

palindromo = True

for i in range(len(numeros)):
    if numeros[i] != numeros[len(numeros) - 1 - i]:
        if palindromo:
            palindromo = False

if palindromo:
    print("A lista é palíndromo.")
else:
    print("A lista não é palíndromo.")