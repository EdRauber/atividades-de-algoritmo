txt=input()
txt = txt.lower()

def eh_palindromo(txt, inicio, fim):
    t = len(txt)

    if inicio in [" ", ".", ",", ":", ";", "!", "?"]:
        if inicio != t:
            inicio += 1

    if fim in [" ", ".", ",", ":", ";", "!", "?"]:
        if fim != -t:
            fim -= 1
    

    if txt[inicio] != txt[fim]:
        return False
    
    return eh_palindromo(txt, inicio + 1, fim - 1)

resultado = eh_palindromo(txt, 0, -1)
print(resultado)