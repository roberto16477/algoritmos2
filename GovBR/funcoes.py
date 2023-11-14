def AgrupaPorPalavra(palavra):
    with open("GovBR/dominios.csv","r", encoding="utf-8") as dominios:
        todos = dominios.readlines()

    informacao = palavra

    for linha in todos:
        colunas = linha.split('|')
        if informacao in linha:
            print(colunas[1])



def ConsultaDominio(dominio):
    with open("GovBR/dominios.csv","r", encoding="utf-8") as dominios:
        todos = dominios.readlines()

        busca = (dominio + ".gov.br")
        existe = 0

        for linha in todos:
            if busca in linha:
                print(f"O domínio {busca} já existe!")
                print(linha)
                existe += 1
        
        if existe < 1:
            print(f"O domínio {busca} está livre!")

           
