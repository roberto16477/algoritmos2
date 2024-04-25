def inicia(tam, arr):
    for i in range(tam):
        arr.append('')

def insere(tam, arr):
    val = input("Informe um valor para inserir: ")
    for i in range(tam):
        if arr[i] == '':
            arr[i] = val
            break


'''def insere(l):
    val = input("Informe o valor de deseja inserir: ")
    l.append(val)'''

'''def tira(l):
    if len(l) > 0:
        l.pop(0)
    else:
        print("A fila já está vazia!")'''

def tira(tam, arr):
    for i in range(tam):
        if arr[i] != '':
            arr[i] = ''
            break

fila = []
n = 5
inicia(n, fila)
opcao = -1

while opcao != 0:
    print("Informe 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover um elemento da fila")
    opcao = int(input("Informe a opção que deseja: "))

    if opcao == 1:
        insere(n, fila)
        print(f"\n {fila}")

    if opcao == 2:
        tira(n, fila)
        print(fila)
