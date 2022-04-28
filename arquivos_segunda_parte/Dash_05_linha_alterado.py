# Importanto as bibliotecas
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
import plotly.express as px  # biclioteca responsável por plotar os gráficos
from dash import Dash, html, dcc, Input, Output


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_linha(dataframe, linguagem):
    lista_dados_linha = dataframe.values
    ano_linha: [str] = [0 for ff in range(204)]
    i = 0
    for x in lista_dados_linha:
        ano_linha[i] = x[0]
        i = i + 1
    anos_agrupados_linha: [str] = [0 for ff in range(17)]
    anos_agrupados_linha[0] = ano_linha[0]
    m = 0
    for z in ano_linha:
        if z != anos_agrupados_linha[m]:
            m = m + 1
            anos_agrupados_linha[m] = z
    valores_ling_linha = list(dataframe[linguagem])
    soma_ling_linha: [float] = [0 for hh in range(17)]
    media_ling_linha: [float] = [0 for ii in range(17)]
    j = 0
    for z in range(0, len(valores_ling_linha)):
        if ano_linha[z] == anos_agrupados_linha[j]:
            soma_ling_linha[j] = soma_ling_linha[j] + valores_ling_linha[z]
        else:
            media_ling_linha[j] = soma_ling_linha[j] / 12.0
            j = j + 1
            soma_ling_linha[j] = soma_ling_linha[j] + valores_ling_linha[z]
        media_ling_linha[j] = soma_ling_linha[j] / 12.0
    figura_linha = px.line(x=anos_agrupados_linha, y=media_ling_linha, markers=True)
    figura_linha.update_xaxes(title='Ano',  ticks='outside')
    figura_linha.update_yaxes(title='Percentual', ticks='outside')
    return figura_linha

'''
if __name__ == '__main__':

    df_linha = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    nomes_colunas_linha = list(df_linha.columns)
    opcoes_linha = nomes_colunas_linha[1:len(nomes_colunas_linha)]
    opcoes_linha.sort()
    fig_linha = funcao_linha(df_linha, 'Python')
    titulo1_linha = 'Evolução do uso da linguagem Python nos últimos 17 anos'
    titulo2_linha = 'Dados de 2005 a 2021'

    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app_linha = Dash(__name__)

    # atualizando o layout do aplicativo flask
    app_linha.layout = html.Div(children=[
        html.Td(children=[
            html.H2(children=titulo1_linha, id="titulo1-linha"),
            html.H4(children=titulo2_linha),
            dcc.Dropdown(opcoes_linha, value='Python', id='dropdown-linha'),
            dcc.Graph(id='grafico-linha', figure=fig_linha)
        ], style={'background-color': 'rgb(255, 174, 201)', 'width': '1306px',
                  'border-style': 'outset'})
    ])

    # decorator
    @app_linha.callback(
        Output('grafico-linha', 'figure'),
        Output('titulo1-linha', 'children'),
        Input('dropdown-linha', 'value')  # dá a informacao selecionada
    )
    def alterar_linha(value):
        titulo1_linha_alterado = f'Evolução do uso da linguagem {value} nos últimos 17 anos'
        figura_linha_alterada = funcao_linha(df_linha, value)
        return figura_linha_alterada, titulo1_linha_alterado

    # colocando o aplicativo no ar (servidor local)
    app_linha.run_server(debug=True)
'''