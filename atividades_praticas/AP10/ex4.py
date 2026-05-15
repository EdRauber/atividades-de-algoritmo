palavras = []
x = 8

for i in range(x):
    captura = input("")
    palavras.append(captura)

print("_________________________________")
for i in range((len(palavras)-1) , -1 , -1):
    print(palavras[i])