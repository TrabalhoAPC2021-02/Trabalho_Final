# Importanto as bibliotecas
import Dash_01_mapa_alterado as D_mapa  # funcao que plota o grafico de mapa
import Dash_02_funil_alterado as D_funil  # funcao que plota o grafico de funil
import Dash_03_barraHoriz_alterado as D_barraH  # funcao que plota o grafico de barra horizontal
import Dash_04_pizza_alterado as D_pizza  # funcao que plota o grafico de pizza
import Dash_05_linha_alterado as D_linha  # funcao que plota o grafico de linha
import Dash_06_barraVert_alterado as D_barraV  # funcao que plota o grafico de barra vertical
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
from dash import Dash, html, dcc, Input, Output  # biblioteca para as funcoes do dash
import dash_bootstrap_components as dbc  # biblioteca para o tema dark do dash


def funcao_filtrar_ano(dataframe, coluna_a_ser_filtrada, valor_filtro):
    lista_dados_filtrados = []
    nomes_colunas_filtrados = list(dataframe.columns)
    for x in dataframe.values:
        if x[coluna_a_ser_filtrada] == valor_filtro:
            lista_dados_filtrados.append(x)
    dataframe_filtrado = pd.DataFrame(lista_dados_filtrados, columns=nomes_colunas_filtrados)
    #  print(dataframe_filtrado)
    return dataframe_filtrado


if __name__ == '__main__':

    # =============================================================================================
    # Grafico de pizza - 15 Linguagens mais usadas no ano
    # =============================================================================================
    # lendo o arquivo csv do arquivo usando o pandas
    df_pizza = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    # criando a lista de opcoes (sem repeticao) para ser usada no dash core component (dcc)
    opcoes_pizza = list(df_pizza['Date'].unique())  # lista de anos sem repeticao
    opcoes_pizza.sort()  # ordenando a lista
    df_pizza_filtrado = funcao_filtrar_ano(df_pizza, 0, 2021)
    #df_pizza_filtrado = df_pizza[df_pizza['Date'] == 2021]  # filtrando os dados para o primeiro gráfico
    # chamando a funcao que plota o grafico - parametro: dataframe ja filtrado por ano
    fig_pizza = D_pizza.funcao_pizza(df_pizza_filtrado)
    titulo1_pizza = 'As 15 linguagens de programação mais usadas no ano de 2021'  # titulo maior - padrão
    titulo2_pizza = '.'  # titulo menor
    texto_fonte_pizza = 'Fonte: kaggle - disponível em: https://www.kaggle.com/datasets/muhammadkhalid/most-popular-programming-languages-since-2004'
    # =============================================================================================
    # Grafico de linha - evolucao de uso da linguagem
    # =============================================================================================
    # segue a mesma linha de raciocinio do bloco anterior
    df_linha = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    nomes_colunas_linha = list(df_linha.columns)  # os nomes das colunas sao os nomes das linguagens
    opcoes_linha = nomes_colunas_linha[1:len(nomes_colunas_linha)]  # retira o nome da 1ª coluna - Data
    opcoes_linha.sort()
    # chamando a funcao q plota o grafico - parametro: dataframe inteiro e nome da linguagem padrão
    fig_linha = D_linha.funcao_linha(df_linha, 'Python')
    titulo1_linha = 'Evolução do uso da linguagem Python nos últimos 17 anos'
    titulo2_linha = 'Dados de 2005 a 2021'
    texto_fonte_linha = 'Fonte: kaggle - disponível em: https://www.kaggle.com/datasets/muhammadkhalid/most-popular-programming-languages-since-2004'
    # =============================================================================================
    # Grafico de barras horizontais - Diversidade empresas
    # =============================================================================================
    # segue a mesma linha de raciocinio do primeiro bloco
    dados_csv_barraHoriz = pd.read_csv('03_Employee Diversity in Tech.csv', ';')
    opcoes_barraHoriz = list(dados_csv_barraHoriz['Date'].unique())  # lista de anos sem repeticao
    opcoes_barraHoriz.sort()
    df_barraHoriz_filtrado = funcao_filtrar_ano(dados_csv_barraHoriz, 0, 2018)
    #df_barraHoriz_filtrado = dados_csv_barraHoriz[dados_csv_barraHoriz['Date'] == 2018]
    fig_barraHoriz = D_barraH.funcao_barraHoriz(df_barraHoriz_filtrado)  # parametro: dataframe filtrado por ano
    titulo1_barraHoriz = 'Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia em 2018'
    titulo2_barraHoriz = '.'
    texto_fonte_barraHoriz = 'Fonte: Data.world - disponível em: https://data.world/makeovermonday/2018w46'
    # =============================================================================================
    # Grafico de funil - Comparacao salarios CLT e terceirizados
    # =============================================================================================
    # segue a mesma linha de raciocinio do primeiro bloco
    df_funil = pd.read_excel('02.1_salarios_CLT_Terceirizado.xlsx')
    opcoes_funil = list(df_funil['Cargo'].unique())
    opcoes_funil.sort()
    fig_funil = D_funil.funcao_funil_gerargrafico(df_funil, opcoes_funil)
    titulo1_funil = 'Comparação entre salários de contratados pela CLT e salários de terceirizados.'
    titulo2_funil = 'Valores em reais.'
    texto_fonte_funil = 'Fonte: APINFO - disponível em: https://www.apinfo2.com/apinfo/informacao/p21sal-br.cfm'
    # =============================================================================================
    # Grafico de barra vertical - Comparacao salarios CLT e terceirizados por especialidade
    # =============================================================================================
    # segue a mesma linha de raciocinio do primeiro bloco
    df_barraVert = pd.read_excel('02.1_salarios_CLT_Terceirizado.xlsx')
    opcoes_barraVert = ['Programador', 'Analista Programador', 'Analista de Suporte', 'Analista de sistemas']
    opcoes_barraVert.sort()
    fig_barraVert = D_barraV.funcao_barraVert(df_barraVert, 'Programador')
    titulo1_barraVert = 'Comparação entre salários de contratados pela CLT e salários de terceirizados por especialidade'
    titulo2_barraVert = 'Cargo: Programador'
    texto_fonte_barraVert = 'Fonte: APINFO - disponível em: https://www.apinfo2.com/apinfo/informacao/p21sal-br.cfm'
    # =============================================================================================
    # Grafico de mapa - Medias salariais G12
    # =============================================================================================
    df_mapa = pd.read_excel('01_Data_Professional_full.xlsx')
    opcoes_mapa = list(df_mapa['Survey Year'].unique())  # lista de anos sem repeticao
    opcoes_mapa.append('2017 a 2021')
    fig_mapa = D_mapa.funcao_mapa(df_mapa)  # grafico padrao - dataframe inteiro
    titulo1_mapa = 'Média de salário anual dos profissionais de TI dos países do G12* de 2017 a 2021'
    titulo2_mapa = 'Média salarial em dólares.'
    titulo3_mapa = '*Exceto Japão e Coréia do Sul, por não ter dados. No lugar desses foram adicionados Austrália e África do Sul.'
    texto_fonte_mapa = 'Fonte: Data.world - disponível em: https://data.world/finance/data-professional-salary-survey'
    # =============================================================================================

    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

    # atualizando o layout do aplicativo flask
    app.layout = html.Div(children=[  # cria uma divisao nova
        html.Div(children=[
            html.Td(children=[  # cria uma coluna nova
                # titulos em html - H1 - letra maior ate H5 - letra menor
                html.H1(children='Mercado de TI', style={'color': 'white', 'font-family': 'cursive',
                                                         'font-size': '60px', 'font-weight': 'bold',
                                                         'text-shadow': '2px 2px 2px red',
                                                         'text-align': 'center', 'letter-spacing': '4px'})
                # formatacao CSS para cor de fundo, largura da coluna e estilo da borda da celula da tabela
                ], style={'background-color': 'rgb(23, 23, 23)',  'width': '1300px'})
        ]),
        html.Br(),
        html.Br(),
        html.Div(children=[
            html.Td(children=[  # cria uma coluna nova
                # titulos em html - H1 - letra maior ate H5 - letra menor
                html.H3(children=titulo1_pizza, id='titulo1-pizza'),
                html.H5(children=titulo2_pizza),
                dcc.Slider(  # dcc = slider
                    df_pizza['Date'].min(),  # cria o range do slider
                    df_pizza['Date'].max(),
                    step=None,
                    value=df_pizza['Date'].max(),  # marca o valor maximo como padrão
                    # marcadores do slider - no caso, os anos do dataframe sem repeticao
                    marks={str(Date): str(Date) for Date in df_pizza['Date'].unique()},
                    id='slider-pizza'),
                # grafico plotado pela funcao que foi chamada
                dcc.Graph(id='grafico-pizza', figure=fig_pizza),
                html.H5(children=texto_fonte_pizza, style={'font-size': '12px'}),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '650px'}),
            html.Td(children=[
                html.H3(children=titulo1_linha, id="titulo1-linha"),
                html.H5(children=titulo2_linha),
                # dcc = dropdown - lista de valores, value = valor padrão, id = nome do dcc
                dcc.Dropdown(opcoes_linha, value='Python', id='dropdown-linha',
                             style={'color': 'black'}),
                dcc.Graph(id='grafico-linha', figure=fig_linha),
                html.H5(children=texto_fonte_linha, style={'font-size': '12px'}),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '650px'})
        ]),
        html.Br(),
        html.Div(children=[
            html.Td(children=[
                html.H3(children=titulo1_barraHoriz, id="titulo1-barraHoriz"),
                html.H5(children=titulo2_barraHoriz),
                # dcc = radioItems - lista de valores, valor padrão, id = nome, inline =
                dcc.RadioItems(opcoes_barraHoriz, 2018,
                               id='radioitems-barraHoriz',
                               style={'background-color': 'rgb(23, 23, 23)'}),
                dcc.Graph(id='grafico-barraHoriz', figure=fig_barraHoriz),
                html.H5(children=texto_fonte_barraHoriz, style={'font-size': '12px'}),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '1300px'})
        ]),
        html.Br(),
        html.Div(children=[
            html.Td(children=[
                html.H3(children=titulo1_funil),
                html.H5(children=titulo2_funil),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '1300px',
                      'vertical-align': 'top'}),
        ]),
        html.Div(children=[
            html.Td(children=[
                dcc.Checklist(opcoes_funil,
                              ['Analista de Suporte', 'Programador', 'Analista Programador', 'Analista de sistemas'],
                              id='checklist-funil', inline=True,
                              style={'display': 'block', 'background-color': 'rgb(23, 23, 23)',
                                     'font-size': '14px'}),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '500px',
                      'columns': '2'}),
            html.Td(children=[
                dcc.Graph(id='grafico-funil', figure=fig_funil),
                html.H5(children=texto_fonte_funil, style={'font-size': '12px'}),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '800px',
                      'vertical-align': 'top'})
        ]),
        html.Br(),
        html.Div(children=[
            html.Td(children=[
                html.H3(children=titulo1_barraVert, id="titulo1-barraVert"),
                html.H5(children=titulo2_barraVert, id="titulo2-barraVert"),
                dcc.Dropdown(opcoes_barraVert, value='Programador', id='dropdown-barraVert',
                             style={'color': 'black'}),
                dcc.Graph(id='grafico-barraVert', figure=fig_barraVert),
                html.H5(children=texto_fonte_barraVert, style={'font-size': '12px'}),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '1300px',
                      'vertical-align': 'top'})
        ]),
        html.Br(),
        html.Div(children=[
            html.Td(children=[
                html.H3(children=titulo1_mapa, id="titulo1-mapa"),
                html.H5(children=titulo2_mapa),
                html.H5(children=titulo3_mapa, style={'font-size': '13px'}),
                # dcc = dropdown - lista de valores, value = valor padrão, id = nome do dcc
                dcc.Dropdown(opcoes_mapa, value='2017 a 2021', id='dropdown-mapa',
                             style={'color': 'black'}),
                dcc.Graph(id='grafico-mapa', figure=fig_mapa),
                html.H5(children=texto_fonte_mapa, style={'font-size': '12px'}),
            ], style={'background-color': 'rgb(23, 23, 23)', 'width': '1300px'})
        ])
    ])

    # decorator - grafico pizza - para quando os valores do dcc for alterado
    @app.callback(
        # quem vai ser alterado - nome(id) e qual caracteristica
        Output('grafico-pizza', 'figure'),  # altera o grafico
        Output('titulo1-pizza', 'children'),  # altera o titulo1
        Input('slider-pizza', 'value'),  # value = informacao selecionada do dcc
    )
    def alterar_pizza(value):
        # altera o titulo1
        titulo1_pizza_alterado = f'As 15 linguagens de programação mais usadas no ano de {value}'
        # cria um dataframe filtrado pelo valor escolhido
        # df_pizza_filtrado_alterado = df_pizza[df_pizza['Date'] == int(value)]
        df_pizza_filtrado_alterado = funcao_filtrar_ano(df_pizza, 0, int(value))
        # chama a funcao novamente para plotar o grafico com o dado escolhido
        fig_pizza_alterada = D_pizza.funcao_pizza(df_pizza_filtrado_alterado)
        # retorna o que foi alterado, na ordem dos Outputs
        return fig_pizza_alterada, titulo1_pizza_alterado

    # decorator - grafico linha - segue o mesmo raciocinio do primeiro callback
    @app.callback(
        Output('grafico-linha', 'figure'),
        Output('titulo1-linha', 'children'),
        Input('dropdown-linha', 'value')  # dá a informacao selecionada
    )
    def alterar_linha(value):
        titulo1_linha_alterado = f'Evolução do uso da linguagem {value} nos últimos 17 anos'
        # chama a funcao novamente para plotar o grafico com a linguagem escolhido
        figura_linha_alterada = D_linha.funcao_linha(df_linha, value)
        return figura_linha_alterada, titulo1_linha_alterado

    # decorator - grafico barra - segue o mesmo raciocinio do primeiro callback
    @app.callback(
        Output('grafico-barraHoriz', 'figure'),
        Output('titulo1-barraHoriz', 'children'),
        Input('radioitems-barraHoriz', 'value')  # dá a informacao selecionada
    )
    def alterar_barraHoriz(value):
        titulo1_barraHoriz_alterado = f'Distribuição entre homens e mulheres contratados ' \
                        f'pelas principais empresas de tecnologia em {value}'
        df_barraHoriz_filtrado = funcao_filtrar_ano(dados_csv_barraHoriz, 0, int(value))
        # df_barraHoriz_filtrado = dados_csv_barraHoriz[dados_csv_barraHoriz['Date'] == int(value)]
        figura_barraHoriz_alterada = D_barraH.funcao_barraHoriz(df_barraHoriz_filtrado)
        return figura_barraHoriz_alterada, titulo1_barraHoriz_alterado

    # decorator - grafico funil - segue o mesmo raciocinio do primeiro callback
    @app.callback(
        Output('grafico-funil', 'figure'),
        Input('checklist-funil', 'value')
    )
    def alterar_funil(value):
        figura_funil_alterada = D_funil.funcao_funil_gerargrafico(df_funil, value)
        return figura_funil_alterada

    # decorator - grafico barra vertical - segue o mesmo raciocinio do primeiro callback
    @app.callback(
        Output('grafico-barraVert', 'figure'),
        Output('titulo2-barraVert', 'children'),
        Input('dropdown-barraVert', 'value')
    )
    def alterar_barraVert(value):
        titulo2_barraVert_alterada = f'Cargo: {value}'
        figura_barraVert_alterada = D_barraV.funcao_barraVert(df_barraVert, value)
        return figura_barraVert_alterada, titulo2_barraVert_alterada

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
            fig_mapa_alterada = D_mapa.funcao_mapa(df_mapa)
        else:
            # usa a base de dados filtrada pelo ano escolhido
            titulo1_mapa_alterado = f'Média de salário anual dos profissionais de TI dos países do G12* de {value}'
            df_mapa_filtrado = funcao_filtrar_ano(df_mapa, 0, int(value))
            # df_mapa_filtrado = df_mapa[df_mapa['Survey Year'] == value]
            fig_mapa_alterada = D_mapa.funcao_mapa(df_mapa_filtrado)
        return fig_mapa_alterada, titulo1_mapa_alterado

    # colocando o aplicativo no ar (servidor local)
    app.run_server(debug=True)
