def inicia(tam):
    return ['' for _ in range(tam)]

def insere(arr, elemento, re):
    global volta
    if arr[re] == '':
        arr[re] = elemento
        re = (re + 1) % len(arr)
        if re == 0:
            volta += 1
        print(f"Elemento '{elemento}' inserido com sucesso.")
    else:
        print("\nA fila está verdadeiramente cheia")

def remover(arr, frente):
    if arr[frente] == '':
        print("A fila está vazia")
    else:
        elemento = arr[frente]
        arr[frente] = ''
        print(f"Elemento '{elemento}' removido com sucesso.")

n = 5
fila = inicia(n)
frente = 0
re = 0
volta = 0
opcao = -1

while opcao != 0:
    print("\nInforme 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover da fila")
    opcao = int(input("Informe o número da operação que deseja: "))

    if opcao == 1:
        elemento = input("Informe um elemento para adicionar à fila: ")
        insere(fila, elemento, re)
        print(f"Fila: {fila}")

    elif opcao == 2:
        remover(fila, frente)
        print(f"Fila: {fila}")

print("Programa encerrado.")