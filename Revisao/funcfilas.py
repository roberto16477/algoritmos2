def inserir(tam, lis):
    if tam == len(lis):
        print("A fila está cheia!")
    else:
        for i in range(tam):
            lis.append(input("Informe um valor para adicionar a lista: "))
    print(lis)

def remover(r, lis):
    if r in lis:
        lis.remove(r)
        print(f"o valor {r} foi removido da lista")
    else:
        print(f"O valor {r} não existe na lista")

def consultar(val, lis):
    if val in lis:
        print(f"O valor {val} está na lista!")
    else:
        print(f"Não existe '{val}' na lista")
