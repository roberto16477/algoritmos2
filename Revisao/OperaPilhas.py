pilha = []
n = 5

def insere():
    cont = 0
    while cont < n:
        item = input("Informe um valor: ")
        pilha.append(item)
        cont +=1


insere()
print(pilha)