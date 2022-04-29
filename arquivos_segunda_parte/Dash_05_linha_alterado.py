# Importanto as bibliotecas
import plotly.express as px  # biblioteca responsável por plotar os gráficos


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_linha(dataframe, linguagem):
    # transforma em lista o dataframe inteiro
    lista_dados_linha = dataframe.values
    # define o vetor que recebera o ano de cada linha do dataframe
    ano_linha: [str] = [0 for ff in range(204)]
    i = 0
    for x in lista_dados_linha:
        ano_linha[i] = x[0]
        i = i + 1
    # define o vetor que recebera os anos agrupados sem repeticao
    anos_agrupados_linha: [str] = [0 for ff in range(17)]
    anos_agrupados_linha[0] = ano_linha[0]
    m = 0
    for z in ano_linha:
        if z != anos_agrupados_linha[m]:
            m = m + 1
            anos_agrupados_linha[m] = z
    # transforma em lista a coluna da linguagem escolhida
    valores_ling_linha = list(dataframe[linguagem])
    # define os vetores que receberao a soma e a media de uso da linguagem por ano
    soma_ling_linha: [float] = [0 for hh in range(17)]
    media_ling_linha: [float] = [0 for ii in range(17)]
    j = 0
    for z in range(0, len(valores_ling_linha)):
        # acumula a soma dos 12 meses
        if ano_linha[z] == anos_agrupados_linha[j]:
            soma_ling_linha[j] = soma_ling_linha[j] + valores_ling_linha[z]
        else:
            media_ling_linha[j] = soma_ling_linha[j] / 12.0
            j = j + 1
            soma_ling_linha[j] = soma_ling_linha[j] + valores_ling_linha[z]
        # calcula a media dos 12 meses
        media_ling_linha[j] = soma_ling_linha[j] / 12.0
    # gera o gráfico de linha
    figura_linha = px.line(x=anos_agrupados_linha, y=media_ling_linha, markers=True)
    figura_linha.update_xaxes(title='Ano',  ticks='outside')
    figura_linha.update_yaxes(title='Percentual', ticks='outside')
    # retorna o gráfico gerado
    return figura_linha

