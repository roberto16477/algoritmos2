from funcfilas import *

opcao = -1
lista = []
n = 5

while opcao != 0:
    print("\nInforme 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover da fila")
    print("Informe 3 para consultar um valor na fila")
    print("Informe 4 para verificar o tamanho da fila")
    opcao = int(input("Informe o número da operação que deseja: "))


    if opcao == 1:
        inserir(n, lista)

    if opcao == 2:
        remover(lista)

    if opcao == 3:
        vc = input("Informe o valor que deseja consultar: ") # VC = Valor Consulta
        consultar(vc, lista)

    if opcao == 4:
        tamanho(lista)

