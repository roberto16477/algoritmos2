def ContaLinhas():
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        contagem = dominios.readlines()
        cont = 0

        for linha in contagem:
            cont += 1
        
        print("\nO arquivo dominios.csv possui ", cont, "linhas")
        print("Com as colunas:")
        print(Colunas())

        

def Colunas():
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        cabecalho = dominios.readline()
        return(cabecalho)



def AgrupaPorPalavra(palavra):
    with open("GovBR/dominios.csv","r", encoding="utf-8") as dominios:
        todos = dominios.readlines()
        existe = 0

    informacao = palavra

    for linha in todos:
        colunas = linha.split('|')
        if informacao in linha:
            print(colunas[1])
            existe += 1
        
    if existe < 1:
        print("Não existem domínios com a palavra: ", palavra)



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

           
def RegistrosHandle():
    regh = []
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        todos = dominios.readlines()

        for linha in todos:
            colunas = linha.split('|')

            if colunas[3] not in regh:
                regh.append(colunas[3])
                with open("GovBR/opcoes_handle.txt", "a", encoding="utf-8") as opcoeshandle:
                    opcoeshandle.write(f"{colunas[3]}\n")

            if colunas[4] not in regh:
                regh.append(colunas[4])
                with open("GovBR/opcoes_handle.txt", "a", encoding="utf-8") as opcoeshandle:
                    opcoeshandle.write(f"{colunas[4]}\n")

            if colunas[5] not in regh:
                regh.append(colunas[5])
                with open("GovBR/opcoes_handle.txt", "a", encoding="utf-8") as opcoeshandle:
                    opcoeshandle.write(f"{colunas[5]}\n")

        print("Foi gerado o arquivo opcoes_handle.txt com todas as opções usadas nas colunas Handle")



