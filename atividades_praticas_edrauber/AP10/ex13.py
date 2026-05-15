numeros = []
x = 10

for i in range(x):
    numeros.append(int(input("")))

primeiro = True

for i in numeros:
    if primeiro:
        maior_valor = i
        segundo_maior = i
        primeiro = False
    else:
        if i > segundo_maior:
            if i >= maior_valor:
                maior_valor = i
            else:
                segundo_maior = i

if maior_valor == segundo_maior:
    print("Não existe segundo maior valor distinto.")
else:
    print(f"Maior valor: {maior_valor}")
    print(f"Segundo maior valor: {segundo_maior}")