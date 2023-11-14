def ContaLinhas():
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        contagem = dominios.readlines()
        cont = 0

        for linha in contagem:
            cont += 1
        
        print("O arquivo dominios.csv possui ", cont, "linhas")
        print("Com as colunas:")
        print(Colunas())

        

def Colunas():
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        cabecalho = dominios.readline()
        return(cabecalho)



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

           
