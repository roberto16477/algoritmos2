arquivo = open("manipulacao-arquivos/textos/variaslinhas.txt", "r", encoding="utf-8")

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
