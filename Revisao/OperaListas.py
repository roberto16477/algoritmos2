from funcfilas import *

opcao = -1
lista = []
n = int(input("Quantos valores terá a lista? "))
inserir(n, lista)

while opcao != 0:
    print("\nInforme 0 para sair")
    print("Informe 1 para inserir na fila")
    print("Informe 2 para remover da lista")
    print("Informe 3 para consultar um valor na fila")
    opcao = int(input("Informe o número da operação que deseja: "))


    if opcao == 1:
        
        inserir(n, lista)

    if opcao == 2:
        tirar = input("Informe um valor para ser removido da lista: ")
        remover(tirar, lista)

    if opcao == 3:
        vc = input("Informe o valor que deseja consultar: ") # VC = Valor Consulta
        consultar(vc, lista)

print(lista)
