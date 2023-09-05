lista = [1, 'a', 3, 'b', 5, 'c', 7]

print("A lista inicial é:")
print(lista)

print("Número de elementos da lista inicial: ", len(lista))

it = int(input("Digite um número para incerir na lista: "))
lista.append(it)

print("Lista atual: ", lista)

x = int(input("Digite o índice de um valor para removê-lo: "))
del lista[x]

print("A lista final é: ", lista)
