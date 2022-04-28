# Importanto as bibliotecas
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_barra(dataframe):
    empresas_barra = ['Amazon', 'Apple', 'Dell', 'eBay', 'Facebook', 'Google', 'HP', 'Instagram', 'Intel', 'LinkedIn',
                      'Microsoft', 'Netflix', 'Nvidia', 'Twitter', 'YouTube']
    media_female_empresa_barra = []
    media_male_empresa_barra = []
    for x in empresas_barra:
        df_empresa_barra = dataframe[dataframe['Company'] == x]
        female_perc_barra = df_empresa_barra['Female%'].tolist()
        male_perc_barra = df_empresa_barra['Male%'].tolist()
        soma_female_perc_barra = 0
        for i in range(len(female_perc_barra)):
            soma_female_perc_barra = soma_female_perc_barra + female_perc_barra[i]
        if len(female_perc_barra) == 0:
            media_female_perc = 0
        else:
            media_female_perc = soma_female_perc_barra / len(female_perc_barra)
        media_female_empresa_barra.append(media_female_perc)
        soma_male_perc_barra = 0
        for i in range(len(male_perc_barra)):
            soma_male_perc_barra = soma_male_perc_barra + male_perc_barra[i]
        if len(male_perc_barra) == 0:
            media_male_perc_barra = 0
        else:
            media_male_perc_barra = soma_male_perc_barra / len(male_perc_barra)
        media_male_empresa_barra.append(media_male_perc_barra)
    figura_barra = go.Figure(data=[
        go.Bar(name='% Feminino', x=media_female_empresa_barra, y=empresas_barra, orientation='h'),
        go.Bar(name='% Masculino', x=media_male_empresa_barra, y=empresas_barra, orientation='h')
    ])
    figura_barra.update_layout(barmode='group')
    return figura_barra

'''
if __name__ == '__main__':

    dados_csv_barra = pd.read_csv('03_Employee Diversity in Tech.csv', ';')
    opcoes_barra = list(dados_csv_barra['Date'].unique())
    opcoes_barra.sort()
    df_barra = dados_csv_barra[dados_csv_barra['Date'] == 2018]
    fig_barra = funcao_barra(df_barra)
    titulo1_barra = 'Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia em 2018'
    titulo2_barra = '.'

    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app_barra = Dash(__name__)

    # atualizando o layout do aplicativo flask
    app_barra.layout = html.Div(children=[
        html.Td(children=[
            html.H2(children=titulo1_barra, id="titulo1-barra"),
            html.H4(children=titulo2_barra),
            #dcc.Dropdown(opcoes_barra, value='2018', id='dropdown-barra'),
            dcc.RadioItems(opcoes_barra, 2018,
                id='radioitems-barra', inline=True),
            dcc.Graph(id='grafico-barra', figure=fig_barra)
        ], style={'background-color': 'rgb(133, 211, 250)', 'width': '1306px',
                  'border-style': 'outset'})
    ])

    # decorator
    @app_barra.callback(
        Output('grafico-barra', 'figure'),
        Output('titulo1-barra', 'children'),
        Input('radioitems-barra', 'value')  # dá a informacao selecionada
        #Input('dropdown-barra', 'value')  # dá a informacao selecionada
    )
    def alterar_barra(value):
        titulo1_barra = f'Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia em {value}'
        df_barra_filtrado = dados_csv_barra[dados_csv_barra['Date'] == int(value)]
        figura_barra_alterada = funcao_barra(df_barra_filtrado)
        return figura_barra_alterada, titulo1_barra

    # colocando o aplicativo no ar (servidor local)
    app_barra.run_server(debug=True)
'''