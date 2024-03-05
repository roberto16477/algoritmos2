lista = []
n = int(input("Quantos valores terá a lista? "))

for i in range(n):
    lista.append(input("Informe um valor para adicionar a lista: "))

print(lista)

remove = input("Informe um valor para ser removido da lista: ")
lista.remove(remove)

print(lista)
