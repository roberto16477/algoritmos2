arquivo = open("manipulacao-arquivos/textos/variaslinhas.txt", "w", encoding="utf-8")

for linha in range(1, 101):
    arquivo.write(linha)

arquivo.close()
