numeros = []
x = 12

for i in range(x):
    numeros.append(int(input("")))

sequencia , maior_sequencia = 0 , 0

for i in numeros:
    if sequencia == 0:
        anterior = i
    else:
        if i > anterior:
            anterior = i
        else:
            if sequencia > maior_sequencia:
                maior_sequencia = sequencia + 1
            sequencia = -1
    sequencia += 1

print(f"Maior sequência crescente: {maior_sequencia}")