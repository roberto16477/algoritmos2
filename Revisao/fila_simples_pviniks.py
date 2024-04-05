# - Declarar uma lista;
# - Inserir um elemento na lista;
# - Remover um elemento da lista;
# - Consultar um elemento específico da lista;
# - Determinar o tamanho da lista;
# - Inserir um elemento em uma posição específica da lista;

print("\nExercício:")

n = 5
lista = []

def inserir():
    if len(lista) < n:
        lista.append(input(f"Insira um elemento na lista: "))
    else:
        print("A lista está cheia!")

def remover():
    if lista:
        escolha = input("Você gostaria de remover o último elemento da lista (1) ou algum elemento específico (2)? ")
        
        if escolha == '1':
            elemento_removido = lista.pop()
            print(f"O elemento {elemento_removido} foi removido!\n{lista}")
        elif escolha == '2':
            x = input(f"Qual elemento da lista ({lista}) você gostaria de remover? ")
            if x in lista:
                lista.remove(x)
                print(f"O elemento {x} foi removido!\n{lista}")
            else:
                print(f"O elemento {x} não existe na lista.")
        else:
            print("Escolha inválida! Por favor, digite '1' ou '2'.")
    else:
        print("A lista está vazia!")

def consulta():
    x = input(f"Qual elemento da lista você quer consultar? ")
    if x in lista:
        print(f"O elemento {x} está na {(lista.index(x))+1}ª posição.")
    else:
        print(f"O elemento {x} não existe na lista.")

def tamanho():
    print(f"O tamanho da lista é {len(lista)}.")

def inserir_especifico():
    x = (int(input("Em qual posição (1-5) você gostaria de adicionar um elemento? ")))-1
    if x < len(lista) & len(lista) < n:
        lista.insert(x,input(f"Insira um elemento para a {x+1}ª posição da lista: "))
    elif x > len(lista) & len(lista) < n:
        lista.append(input(f"Não é possível inserir na {x+1}ª posição. Insira um elemento na {(len(lista))+1}ª posição da lista: "))
    elif len(lista) == n:
        print("A lista está cheia!")
    elif x >= n:
        print("Não é possível inserir nessa posição.")

while True:
    print("""
MENU DA LISTA

Você gostaria de:
1. Inserir um elemento na lista;
2. Remover um elemento da lista;
3. Consultar um elemento específico da lista;
4. Determinar o tamanho da lista;
5. Inserir um elemento em uma posição específica da lista
6. Visualizar a lista;
""")
    x = input("")
    print("")

    if x == "1":
        inserir()
    elif x == "2":
        remover()
    elif x == "3":
        consulta()
    elif x == "4":
        tamanho()
    elif x == "5":
        inserir_especifico()
    elif x == "6":
        print(f"{lista}")
    else:
        print("O número informado não existe.")