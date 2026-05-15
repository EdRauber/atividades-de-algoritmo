numeros = []
x = 6

for i in range(x):
    num = float(input(""))
    numeros.append(num)

soma = sum(numeros)
media = soma / x

print(f"Soma: {soma}\nMédia: {media}")
