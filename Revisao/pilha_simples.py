def inicia(tam, arr):
    for i in range(tam):
        arr.append('')

def insere(tam, arr, t):
    global topo
    val = input("Informe um valor para inserir: ")
    if t < tam:
        arr[t] = val
        topo = t+1
    else:
        print("A pilha está cheia! Overflow!")

def tira(tam, arr, t):
    global topo
    for i in range(tam):
        if arr[(tam-1)-i] != '':
            arr[(tam-1)-i] = ''
            t -= 1
            topo = t
            break

fila = []
n = 5
base = 0
topo = 0
inicia(n, fila)
opcao = -1

while opcao != 0:
    print("Informe 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover um elemento da fila")
    opcao = int(input("Informe a opção que deseja: "))

    if opcao == 1:
        insere(n, fila, topo)
        print(f"\n {fila}")
        print(f"base: {base} Topo: {topo}")

    if opcao == 2:
        tira(n, fila, base)
        print(fila)
        print(f"base: {base} Topo: {topo}")