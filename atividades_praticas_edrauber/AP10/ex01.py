numeros = []
x = 5

for i in range(x):
    num = int(input("Digite um número: "))
    numeros.append(num)

print(f"Lista Completa: {numeros}")
for i in numeros:
    print(i)