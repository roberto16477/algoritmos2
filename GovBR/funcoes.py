def AgrupaPorPalavra(palavra):
    with open("GovBR/dominios.csv","r", encoding="utf-8") as dominios:
        todos = dominios.readlines()

    informacao = palavra

    for linha in todos:
        colunas = linha.split('|')
        if informacao in linha:
            print(colunas[1])
