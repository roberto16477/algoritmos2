def inserir(tam, lis):
    if tam == len(lis):
        print("A fila está cheia!")
    else:
        for i in range(tam):
            lis.append(input("Informe um valor para adicionar a lista: "))
    print(lis)

def remover(lis):
        if len(lis) != 0:
            r = lis.pop()
            print(f"o valor {r} foi removido da lista")
            print("Lista atual: ", lis)
        else:
            print("A fila está vazia")

def consultar(val, lis):
    if val in lis:
        print(f"O valor {val} está na lista!")
    else:
        print(f"Não existe '{val}' na lista")
