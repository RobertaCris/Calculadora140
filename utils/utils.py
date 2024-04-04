import csv # biblioteca que sabe como çer e escrever em um arquivo com formato csv

def ler_csv(arquivo_csv):
    dados_csv = []                                      # cria uma lista em branco
    try:                                                # tentar / tratamento de erro
        with open(arquivo_csv, newline='') as massa:    # com o arquivo --> informa o nome e o apelido massa
                                                        # newline seria o caracter de final de linha
            tabela = csv.reader(massa, delimiter=',')   # com os dados do arquico, menos o cabeçalho
                                                        # informando que o separador é a vírgula
            next(tabela)                                # serve aqui para pular a linha de cabeçalho
            for linha in tabela:                        # para cada linha na tabela
                dados_csv.append(linha)                 # guardando os dados separados para usos
        return dados_csv                                # devolver os dados para serem usados no teste
    except FileNotFoundError:                           # tratamento de erro para arquivo não encontrado
        print(f'Arquivo não encontrado: {arquivo_csv}') # mensagem de erro de arquivo não encontrado
    except Exception as fail:                           # qualqer erro não previsto
        print(f'Falha imprevista:{fail}')               # mensagem de erro que voltará do sistema