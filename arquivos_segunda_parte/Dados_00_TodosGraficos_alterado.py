import Dash_01_mapa_alterado
import Dash_02_funil_alterado
import Dash_03_barra_alterado
import Dash_04_pizza_alterado
import Dash_05_linha_alterado
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
from dash import Dash, html, dcc, Input, Output


if __name__ == '__main__':

    # =============================================================================================
    # Grafico de pizza - 15 Linguagens mais usadas no ano
    # =============================================================================================
    df_pizza = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    opcoes_pizza = list(df_pizza['Date'].unique())
    opcoes_pizza.sort()
    df_dados_pizza = df_pizza[df_pizza['Date'] == 2021]
    fig_pizza = Dash_04_pizza_alterado.funcao_pizza(df_dados_pizza)
    titulo1_pizza = 'As 15 linguagens de programação mais usadas no ano de 2021'
    titulo2_pizza = '.'
    # =============================================================================================
    # Grafico de linha - evolucao de uso da linguagem
    # =============================================================================================
    df_linha = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    nomes_colunas_linha = list(df_linha.columns)
    opcoes_linha = nomes_colunas_linha[1:len(nomes_colunas_linha)]
    opcoes_linha.sort()
    fig_linha = Dash_05_linha_alterado.funcao_linha(df_linha, 'Python')
    titulo1_linha = 'Evolução do uso da linguagem Python nos últimos 17 anos'
    titulo2_linha = 'Dados de 2005 a 2021'
    # =============================================================================================
    # Grafico de barras - Diversidade empresas
    # =============================================================================================
    dados_csv_barra = pd.read_csv('03_Employee Diversity in Tech.csv', ';')
    df_barra = dados_csv_barra[dados_csv_barra['Date'] == 2018]
    opcoes_barra = list(dados_csv_barra['Date'].unique())
    opcoes_barra.sort()
    fig_barra = Dash_03_barra_alterado.funcao_barra(df_barra)
    titulo1_barra = 'Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia em 2018'
    titulo2_barra = '.'
    # =============================================================================================
    # Grafico de funil - Comparacao salarios CLT e terceirizados
    # =============================================================================================
    df_funil = pd.read_excel('02.1_salarios_CLT_Terceirizado.xlsx')
    opcoes_funil = list(df_funil['Cargo'].unique())
    opcoes_funil.append(' Programador, Analista Programador, Analista de Suporte e Analista de sistemas')
    opcoes_funil.sort()
    fig_funil = Dash_02_funil_alterado.funcao_funil_quatro_cargos(df_funil)
    titulo1_funil = 'Comparação entre salários de contratados pela CLT e salários de terceirizados'
    titulo2_funil = 'Cargos: Programador, Analista Programador, Analista de Suporte e Analista de sistemas'
    titulo3_funil = 'Média salarial em reais.'
    # =============================================================================================
    # Grafico de mapa - Medias salariais G12
    # =============================================================================================
    df_mapa = pd.read_excel('01_Data_Professional_full.xlsx')
    opcoes_mapa = list(df_mapa['Survey Year'].unique())
    opcoes_mapa.append('2017 a 2021')
    fig_mapa = Dash_01_mapa_alterado.funcao_mapa(df_mapa)
    titulo1_mapa = 'Média de salário anual dos profissionais de TI dos países do G12* de 2017 a 2021'
    titulo2_mapa = 'Média salarial em dólares.'
    titulo3_mapa = '*Exceto Japão e Coréia do Sul, ' \
                   'por não ter dados. No lugar desses foram adicionados Austrália e ' \
                   'África do Sul.'


    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app = Dash(__name__)

    # atualizando o layout do aplicativo flask
    app.layout = html.Div(children=[
        html.Div(children=[
            html.Td(children=[
                html.H2(children=titulo1_pizza, id='titulo1-pizza'),
                html.H4(children=titulo2_pizza),
                dcc.Slider(
                    df_pizza['Date'].min(),
                    df_pizza['Date'].max(),
                    step=None,
                    value=df_pizza['Date'].max(),
                    marks={str(Date): str(Date) for Date in df_pizza['Date'].unique()},
                    id='slider-pizza'),
                # dcc.Dropdown(opcoes_pizza, value='2021', id='dropdown-pizza'),
                dcc.Graph(id='grafico-pizza', figure=fig_pizza)
            ], style={'background-color': 'rgb(255, 255, 128)', 'width': '650px',
                      'border-style': 'outset'}),
            html.Td(children=[
                html.H2(children=titulo1_linha, id="titulo1-linha"),
                html.H4(children=titulo2_linha),
                dcc.Dropdown(opcoes_linha, value='Python', id='dropdown-linha'),
                dcc.Graph(id='grafico-linha', figure=fig_linha)
            ], style={'background-color': 'rgb(255, 174, 201)', 'width': '650px',
                      'border-style': 'outset'})
        ]),
        html.Div(children=[
            html.Td(children=[
                html.H2(children=titulo1_barra, id="titulo1-barra"),
                html.H4(children=titulo2_barra),
                # dcc.Dropdown(opcoes_barra, value='2018', id='dropdown-barra'),
                dcc.RadioItems(opcoes_barra, 2018,
                               id='radioitems-barra', inline=True),
                dcc.Graph(id='grafico-barra', figure=fig_barra)
            ], style={'background-color': 'rgb(133, 211, 250)', 'width': '1306px',
                      'border-style': 'outset'})
        ]),
        html.Div(children=[
            html.Td(children=[
                html.H2(children=titulo1_funil),
                html.H3(children=titulo2_funil, id='titulo2-funil'),
                html.H5(children=titulo3_funil),
                dcc.Dropdown(opcoes_funil, value=' Programador, Analista Programador, '
                                                 'Analista de Suporte e Analista de sistemas',
                             id='dropdown-funil'),
                dcc.Graph(id='grafico-funil', figure=fig_funil)
            ], style={'background-color': 'rgb(248, 180, 135)', 'width': '1306px',
                      'border-style': 'outset'})
        ]),
        html.Div(children=[
            html.Td(children=[
                html.H2(children=titulo1_mapa, id="titulo1-mapa"),
                html.H4(children=titulo2_mapa),
                html.H5(children=titulo3_mapa),
                dcc.Dropdown(opcoes_mapa, value='2017 a 2021', id='dropdown-mapa'),
                dcc.Graph(id='grafico-mapa', figure=fig_mapa)
            ], style={'background-color': 'rgb(128, 255, 128)', 'width': '1306px',
                      'border-style': 'outset'})
        ])
    ])


    # decorator - grafico pizza
    @app.callback(
        Output('grafico-pizza', 'figure'),
        Output('titulo1-pizza', 'children'),
        Input('slider-pizza', 'value'),  # dá a informacao selecionada
        # Input('dropdown-pizza', 'value'),  # dá a informacao selecionada
    )
    def alterar_pizza(value):
        titulo1_pizza_alterado = f'As 15 linguagens de programação mais usadas no ano de {value}'
        df_dados_pizza = df_pizza[df_pizza['Date'] == int(value)]
        fig_pizza_alterada = Dash_04_pizza_alterado.funcao_pizza(df_dados_pizza)
        return fig_pizza_alterada, titulo1_pizza_alterado

    # decorator - grafico linha
    @app.callback(
        Output('grafico-linha', 'figure'),
        Output('titulo1-linha', 'children'),
        Input('dropdown-linha', 'value')  # dá a informacao selecionada
    )
    def alterar_linha(value):
        titulo1_linha_alterado = f'Evolução do uso da linguagem {value} nos últimos 17 anos'
        figura_linha_alterada = Dash_05_linha_alterado.funcao_linha(df_linha, value)
        return figura_linha_alterada, titulo1_linha_alterado

    # decorator - grafico barra
    @app.callback(
        Output('grafico-barra', 'figure'),
        Output('titulo1-barra', 'children'),
        Input('radioitems-barra', 'value')  # dá a informacao selecionada
        # Input('dropdown-barra', 'value')  # dá a informacao selecionada
    )
    def alterar_barra(value):
        titulo1_barra = f'Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia em {value}'
        df_barra_filtrado = dados_csv_barra[dados_csv_barra['Date'] == int(value)]
        figura_barra_alterada = Dash_03_barra_alterado.funcao_barra(df_barra_filtrado)
        return figura_barra_alterada, titulo1_barra


    # decorator - grafico funil
    @app.callback(
        Output('grafico-funil', 'figure'),
        Output('titulo2-funil', 'children'),
        Input('dropdown-funil', 'value')  # dá a informacao selecionada
    )
    def alterar_funil(value):
        titulo2_funil = f'Cargos: {value}'
        if value == ' Programador, Analista Programador, Analista de Suporte e Analista de sistemas':
            figura_funil_alterada = Dash_02_funil_alterado.funcao_funil_quatro_cargos(df_funil)
        else:
            figura_funil_alterada = Dash_02_funil_alterado.funcao_funil(df_funil, value)
        return figura_funil_alterada, titulo2_funil

    # decorator - grafico mapa
    @app.callback(
        Output('grafico-mapa', 'figure'),
        Output('titulo1-mapa', 'children'),
        Input('dropdown-mapa', 'value')  # dá a informacao selecionada
    )
    def alterar_mapa(value):
        if value == '2017 a 2021':
            # usa a base de dados toda
            titulo1_mapa_alterado = f'Média de salário anual dos profissionais de TI dos países do G12* de {value}'
            fig_mapa_alterada = Dash_01_mapa_alterado.funcao_mapa(df_mapa)
        else:
            # usa a base de dados filtrada pelo ano escolhido
            titulo1_mapa_alterado = f'Média de salário anual dos profissionais de TI dos países do G12* de {value}'
            df_mapa_filtrado = df_mapa[df_mapa['Survey Year'] == value]
            fig_mapa_alterada = Dash_01_mapa_alterado.funcao_mapa(df_mapa_filtrado)
        return fig_mapa_alterada, titulo1_mapa_alterado

    # colocando o aplicativo no ar (servidor local)
    app.run_server(debug=True)
