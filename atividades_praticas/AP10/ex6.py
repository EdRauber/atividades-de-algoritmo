alunos = []
x = 10

for i in range(x):
    nota = float(input(""))
    alunos.append(nota)

soma = sum(alunos)
media = soma / x

acima_media = 0
lista_media = []

for i in alunos:
    if i > media:
        acima_media += 1
        lista_media.append(i)

print(f"Média da turma: {media}")
print(f"Quantidade acima da média: {acima_media}")
print(f"Notas acima da média: {lista_media}")