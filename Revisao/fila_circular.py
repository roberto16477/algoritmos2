def inicia(tam, arr):
    for i in range(tam):
        arr.append('')

def insere(arr):
    elemento = input("Informe um elemento para adicionar a fila")
    for i in range(len(arr)):
        if arr[i] == '':
            arr[i] = elemento
            re = re+1
            break

def remover(arr):
       if frente == re:
           print("A fila está vazia")
       else:
            for i in range(len(arr)):
                if arr[i] != '':
                    arr[i] = ''
                    frente = frente+1
                    break

n = 5
fila = []
frente = 0
re = 0
opcao = -1
inicia(n, fila)

while opcao != 0:
    print("\nInforme 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover da fila")
    opcao = int(input("Informe o número da operação que deseja: "))

    if opcao == 1:
        insere(fila)
        print(fila)
        print(f"frente: {frente}, re: {re}")

    if opcao == 2:
        remover(fila)
        print(fila)
        print(f"frente: {frente}, re: {re}")