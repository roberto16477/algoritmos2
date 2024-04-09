def inicia(tam, arr):
    for i in range(tam):
        arr.append('')

def insere(arr, r):
    global re, volta
    elemento = input("Informe um elemento para adicionar a fila")
    for i in range(len(arr)):
        if ((volta < 1) or ((arr[r] == '')and(arr[(r+1) % len(arr)] == ''))or(arr[r] != '')):
            if arr[r] == '':
                arr[r] = elemento
                r = r+1
                re = r
                if re == len(arr):
                    re = 0
                    volta += 1
                    print(re)
                break
            else:
                 print("\nA fila está verdadeiramente cheia")
                 break
        else:
             print("Falso Overflow")
             break

def remover(arr, f, r):
    global frente
    if (r == f) and arr[f] == '':
            print("A fila está vazia")
    else:
        for i in range(len(arr)):
            if arr[f] != '':
                arr[f] = ''
                frente += 1
                if frente == len(arr):
                    frente = 0
                break
                    

n = 5
fila = []
frente = 0
re = 0
opcao = -1
volta = 0
inicia(n, fila)

while opcao != 0:
    print("\nInforme 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover da fila")
    opcao = int(input("Informe o número da operação que deseja: "))

    if opcao == 1:
        insere(fila, re)
        print(fila)
        print(f"frente: {frente}, re: {re}")

    if opcao == 2:
            remover(fila, frente, re)
            print(fila)
            print(f"frente: {frente}, re: {re}")