arquivo = open("manipulacao-arquivos/textos/nome.txt", "a", encoding="utf-8")

nome = input("Informe o nome a ser escrito: ")

arquivo.write(f"\n{nome}")

print(nome)

arquivo.close()
