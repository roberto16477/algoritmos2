arquivo = open("manipulacao-arquivos/textos/nome.txt", "w", encoding="utf-8")

nome = input("Informe o nome a ser escrito: ")

arquivo.write(f"{nome}")

print(nome)

arquivo.close()
