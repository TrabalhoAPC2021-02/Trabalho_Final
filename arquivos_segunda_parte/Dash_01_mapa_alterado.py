# Importanto as bibliotecas
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
import plotly.express as px  # biclioteca responsável por plotar os gráficos
from dash import Dash, html, dcc, Input, Output


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_mapa(dataframe):
    s_av_mapa = []
    country_mapa = []
    paises_mapa = ['United States', 'China', 'Germany', 'United Kingdom', 'India', 'France',
                   'Italy', 'Canada', 'Russia', 'Brazil', 'Australia', 'South Africa']
    codigos_mapa = ['USA', 'CHN', 'DEU', 'GBR', 'IND', 'FRA', 'ITA', 'CAN', 'RUS', 'BRA', 'AUS', 'ZAF']
    # para cada país calcula e guarda a média em 'sv_av_mapa' e guarda código do país em 'country_mapa'
    for x in paises_mapa:
        df_pais_mapa = dataframe[dataframe['Country'] == x]
        salary_pais_mapa = df_pais_mapa['SalaryUSD'].tolist()
        soma_sal_pais_mapa = 0
        for i in range(len(salary_pais_mapa)):
            soma_sal_pais_mapa = soma_sal_pais_mapa + salary_pais_mapa[i]
        if len(salary_pais_mapa) == 0:
            av_pais_mapa = 0
        else:
            av_pais_mapa = soma_sal_pais_mapa / len(salary_pais_mapa)
        s_av_mapa.append(av_pais_mapa)
        country_mapa.append(codigos_mapa[paises_mapa.index(x)])
    # cria dataframe com os valores armazenados e gera o gráfico
    df_sv_mapa = pd.DataFrame(list(zip(country_mapa, s_av_mapa)), columns=['Country', 'Average annual salary [USD]'])
    figura_mapa = px.scatter_geo(df_sv_mapa, locations='Country',
                                 size='Average annual salary [USD]', color=country_mapa,
                                 projection="natural earth")
    # retorna o gráfico gerado
    return figura_mapa

'''
if __name__ == '__main__':

    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app_mapa = Dash(__name__)

    df_mapa = pd.read_excel('01_Data_Professional_full.xlsx')
    opcoes_mapa = list(df_mapa['Survey Year'].unique())
    opcoes_mapa.append('2017 a 2021')
    fig_mapa = funcao_mapa(df_mapa)
    titulo1_mapa = 'Média de salário anual dos profissionais de TI dos países do G12* de 2017 a 2021'
    titulo2_mapa = 'Média salarial em dólares.'
    titulo3_mapa = '*Exceto Japão e Coréia do Sul, ' \
                   'por não ter dados. No lugar desses foram adicionados Austrália e ' \
                   'África do Sul.'

    # atualizando o layout do aplicativo flask
    app_mapa.layout = html.Div(children=[
            html.Td(children=[
                html.H2(children=titulo1_mapa, id="titulo1-mapa"),
                html.H4(children=titulo2_mapa),
                html.H5(children=titulo3_mapa),
                dcc.Dropdown(opcoes_mapa, value='2017 a 2021', id='dropdown-mapa'),
                dcc.Graph(id='grafico-mapa', figure=fig_mapa)
            ], style={'background-color': 'rgb(128, 255, 128)', 'width': '1306px',
                      'border-style': 'outset'})
    ])

    # decorator
    @app_mapa.callback(
        Output('grafico-mapa', 'figure'),
        Output('titulo1-mapa', 'children'),
        Input('dropdown-mapa', 'value')  # dá a informacao selecionada
    )
    def alterar_mapa(value):
        titulo1_mapa_alterado = f'Média de salário anual dos profissionais de TI dos países do G12* de {value}'
        if value == '2017 a 2021':
            # usa a base de dados toda
            fig_mapa_alterada = funcao_mapa(df_mapa)
        else:
            # usa a base de dados filtrada pelo ano escolhido
            df_mapa_filtrado = df_mapa[df_mapa['Survey Year'] == value]
            fig_mapa_alterada = funcao_mapa(df_mapa_filtrado)
        return fig_mapa_alterada, titulo1_mapa_alterado

    # colocando o aplicativo no ar (servidor local)
    app_mapa.run_server(debug=True)
'''

