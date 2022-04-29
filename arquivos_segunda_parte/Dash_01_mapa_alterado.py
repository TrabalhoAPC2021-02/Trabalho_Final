# Importanto as bibliotecas
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
import plotly.express as px  # biclioteca responsável por plotar os gráficos


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_mapa(dataframe):
    # variaveis que irao receber a media salarial e o codigo do pais para plotar no mapa
    s_av_mapa = []
    country_mapa = []
    # paise do G12 escolhidos - com excecao de Japao e Coreia do Sul
    paises_mapa = ['United States', 'China', 'Germany', 'United Kingdom', 'India', 'France',
                   'Italy', 'Canada', 'Russia', 'Brazil', 'Australia', 'South Africa']
    codigos_mapa = ['USA', 'CHN', 'DEU', 'GBR', 'IND', 'FRA', 'ITA', 'CAN', 'RUS', 'BRA', 'AUS', 'ZAF']
    # para cada país calcula e guarda a média em 'sv_av_mapa' e guarda código do país em 'country_mapa'
    for x in paises_mapa:
        # cria um dataframe com o pais em questao
        df_pais_mapa = dataframe[dataframe['Country'] == x]
        # transforma a coluna de salario em uma lista
        salary_pais_mapa = df_pais_mapa['SalaryUSD'].tolist()
        # acumula a soma dos salarios
        soma_sal_pais_mapa = 0
        for i in range(len(salary_pais_mapa)):
            soma_sal_pais_mapa = soma_sal_pais_mapa + salary_pais_mapa[i]
        # calcula a media se tiver dados
        if len(salary_pais_mapa) == 0:
            av_pais_mapa = 0
        else:
            av_pais_mapa = soma_sal_pais_mapa / len(salary_pais_mapa)
        # guarda o valor calculado e o codigo correspondente ao pais em questao
        s_av_mapa.append(av_pais_mapa)
        country_mapa.append(codigos_mapa[paises_mapa.index(x)])
    # cria dataframe com os valores armazenados
    df_sv_mapa = pd.DataFrame(list(zip(country_mapa, s_av_mapa)),
                              columns=['Country', 'Average annual salary [USD]'])
    # gera o gráfico de dispersão geografica
    figura_mapa = px.scatter_geo(df_sv_mapa, locations='Country',
                                 size='Average annual salary [USD]', color=country_mapa,
                                 projection="natural earth")
    # retorna o gráfico gerado
    return figura_mapa



