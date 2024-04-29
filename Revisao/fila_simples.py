'''def insere(tam, arr):
    val = input("Informe um valor para inserir: ")
    for i in range(tam):
        if arr[i] == '':
            arr[i] = val
            break'''


'''def insere(l):
    val = input("Informe o valor de deseja inserir: ")
    l.append(val)'''

'''def tira(l):
    if len(l) > 0:
        l.pop(0)
    else:
        print("A fila já está vazia!")'''

'''def tira(tam, arr):
    for i in range(tam):
        if arr[i] != '':
            arr[i] = ''
            break'''

def inicia(tam, arr):
    for i in range(tam):
        arr.append('')

def insere(tam, arr, r):
    global re
    val = input("Informe um valor para inserir: ")
    if r < tam:
        arr[r] = val
        re = r+1
    else:
        if arr[0] != '':
            print("A fila está cheia! Overflow!")
        else:
            print("Falso Overflow!")

def tira(tam, arr, f):
    global frente, re
    if arr[f] != '':
        arr[f] = ''
        frente = f+1
        #if (frente == re)and(frente != 0):
        if frente == tam:
            frente = 0
            re = 0
    else:
        print("A fila já está vazia! Underflow!")

fila = []
n = 5
frente = 0
re = 0
inicia(n, fila)
opcao = -1

while opcao != 0:
    print("Informe 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover um elemento da fila")
    opcao = int(input("Informe a opção que deseja: "))

    if opcao == 1:
        insere(n, fila, re)
        print(f"\n {fila}")
        print(f"Frente: {frente} Ré: {re}")

    if opcao == 2:
        tira(n, fila, frente)
        print(fila)
        print(f"Frente: {frente} Ré: {re}")
