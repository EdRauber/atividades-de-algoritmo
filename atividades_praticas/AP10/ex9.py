temp = [ ]
x = 10

for i in range(x):
	instancia = int(input(""))
	temp.append(instancia)

primeira_contagem = True

for i in temp:
	if primeira_contagem:
		aumentou = 0
		diminui = 0
		igual = 0
		anterior = i
		primeira_contagem = False
	elif i > anterior:
		aumentou += 1
	elif i < anterior:
		diminui += 1
	elif i == anterior:
		igual += 1
	anterior = i

print(f"aumentou: {aumentou} vezes")
print(f"diminuiu: {diminui} vezes")
print(f"Permaneceu igual: {igual} vezes")	