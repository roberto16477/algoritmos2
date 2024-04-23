def inicia(tam, arr):
    for i in range(tam):
        arr.append('')

def insere(tam, arr):
    val = input("Informe um valor para inserir: ")
    for i in range(tam):
        if arr[i] == '':
            arr[i] = val
        
fila = []
n = 5