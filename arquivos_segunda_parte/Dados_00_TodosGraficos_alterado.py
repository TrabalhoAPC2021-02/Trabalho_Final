# Importanto as bibliotecas
import Dash_01_mapa_alterado  # funcao que plota o grafico de mapa
import Dash_02_funil_alterado  # funcao que plota o grafico de funil
import Dash_03_barra_alterado  # funcao que plota o grafico de barra
import Dash_04_pizza_alterado  # funcao que plota o grafico de pizza
import Dash_05_linha_alterado  # funcao que plota o grafico de linha
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
from dash import Dash, html, dcc, Input, Output  # biblioteca para as funcoes do dash


if __name__ == '__main__':

    # =============================================================================================
    # Grafico de pizza - 15 Linguagens mais usadas no ano
    # =============================================================================================
    # lendo o arquivo csv do arquivo usando o pandas
    df_pizza = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    # criando a lista de opcoes (sem repeticao) para ser usada no dash core component (dcc)
    opcoes_pizza = list(df_pizza['Date'].unique())  # lista de anos sem repeticao
    opcoes_pizza.sort()  # ordenando a lista
    df_pizza_filtrado = df_pizza[df_pizza['Date'] == 2021]  # filtrando os dados para o primeiro gráfico
    # chamando a funcao q plota o grafico - parametro: dataframe ja filtrado por ano
    fig_pizza = Dash_04_pizza_alterado.funcao_pizza(df_pizza_filtrado)
    titulo1_pizza = 'As 15 linguagens de programação mais usadas no ano de 2021'  # titulo maior - padrão
    titulo2_pizza = '.'  # titulo menor
    # =============================================================================================
    # Grafico de linha - evolucao de uso da linguagem
    # =============================================================================================
    # segue a mesma linha de raciocinio do bloco anterior
    df_linha = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    nomes_colunas_linha = list(df_linha.columns)  # os nomes das colunas sao os nomes das linguagens
    opcoes_linha = nomes_colunas_linha[1:len(nomes_colunas_linha)]  # retira o nome da 1ª coluna - Data
    opcoes_linha.sort()
    # chamando a funcao q plota o grafico - parametro: dataframe inteiro e nome da linguagem padrão
    fig_linha = Dash_05_linha_alterado.funcao_linha(df_linha, 'Python')
    titulo1_linha = 'Evolução do uso da linguagem Python nos últimos 17 anos'
    titulo2_linha = 'Dados de 2005 a 2021'
    # =============================================================================================
    # Grafico de barras - Diversidade empresas
    # =============================================================================================
    # segue a mesma linha de raciocinio do primeiro bloco
    dados_csv_barra = pd.read_csv('03_Employee Diversity in Tech.csv', ';')
    opcoes_barra = list(dados_csv_barra['Date'].unique())  # lista de anos sem repeticao
    opcoes_barra.sort()
    df_barra_filtrado = dados_csv_barra[dados_csv_barra['Date'] == 2018]
    fig_barra = Dash_03_barra_alterado.funcao_barra(df_barra_filtrado)  # parametro: dataframe filtrado por ano
    titulo1_barra = 'Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia em 2018'
    titulo2_barra = '.'
    # =============================================================================================
    # Grafico de funil - Comparacao salarios CLT e terceirizados
    # =============================================================================================
    # segue a mesma linha de raciocinio do primeiro bloco
    df_funil = pd.read_excel('02.1_salarios_CLT_Terceirizado.xlsx')
    opcoes_funil = list(df_funil['Cargo'].unique())  # lista de cargos sem repeticao
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
    opcoes_mapa = list(df_mapa['Survey Year'].unique())  # lista de anos sem repeticao
    opcoes_mapa.append('2017 a 2021')
    fig_mapa = Dash_01_mapa_alterado.funcao_mapa(df_mapa)  # grafico padrao - dataframe inteiro
    titulo1_mapa = 'Média de salário anual dos profissionais de TI dos países do G12* de 2017 a 2021'
    titulo2_mapa = 'Média salarial em dólares.'
    titulo3_mapa = '*Exceto Japão e Coréia do Sul, ' \
                   'por não ter dados. No lugar desses foram adicionados Austrália e ' \
                   'África do Sul.'


    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app = Dash(__name__)

    # atualizando o layout do aplicativo flask
    app.layout = html.Div(children=[  # cria uma divisao nova
        html.Div(children=[
            html.Td(children=[  # cria uma coluna nova
                # titulos em html - H1 - letra maior ate H5 - letra menor
                html.H1(children='Mercado de TI', style={'color': 'black', 'font-family': 'cursive',
                                                         'font-size': '60px', 'font-weight': 'bold',
                                                         'text-shadow': '2px 2px 2px red',
                                                         'text-align': 'center', 'letter-spacing': '4px'})
            # formatacao CSS para cor de fundo, largura da coluna e estilo da borda da celula da tabela
            ], style={'background-color': 'rgb(209, 209, 209)', 'width': '1306px', 'border-style': 'outset'})
        ]),
        html.Div(children=[
            html.Td(children=[  # cria uma coluna nova
                # titulos em html - H1 - letra maior ate H5 - letra menor
                html.H2(children=titulo1_pizza, id='titulo1-pizza'),
                html.H4(children=titulo2_pizza),
                dcc.Slider(  # dcc = slider
                    df_pizza['Date'].min(),  # cria o range do slider
                    df_pizza['Date'].max(),
                    step=None,
                    value=df_pizza['Date'].max(),  # marca o valor maximo como padrão
                    # marcadores do slider - no caso, os anos do dataframe sem repeticao
                    marks={str(Date): str(Date) for Date in df_pizza['Date'].unique()},
                    id='slider-pizza'),
                # grafico plotado pela funcao que foi chamada
                dcc.Graph(id='grafico-pizza', figure=fig_pizza)
            ], style={'background-color': 'rgb(255, 255, 128)', 'width': '650px',
                      'border-style': 'outset'}),
            html.Td(children=[
                html.H2(children=titulo1_linha, id="titulo1-linha"),
                html.H4(children=titulo2_linha),
                # dcc = dropdown - lista de valores, value = valor padrão, id = nome do dcc
                dcc.Dropdown(opcoes_linha, value='Python', id='dropdown-linha'),
                dcc.Graph(id='grafico-linha', figure=fig_linha)
            ], style={'background-color': 'rgb(255, 174, 201)', 'width': '650px',
                      'border-style': 'outset'})
        ]),
        html.Div(children=[
            html.Td(children=[
                html.H2(children=titulo1_barra, id="titulo1-barra"),
                html.H4(children=titulo2_barra),
                # dcc = radioItems - lista de valores, valor padrão, id = nome, inline =
                dcc.RadioItems(opcoes_barra, 2018,
                               id='radioitems-barra'),
                dcc.Graph(id='grafico-barra', figure=fig_barra)
            ], style={'background-color': 'rgb(133, 211, 250)', 'width': '1306px',
                      'border-style': 'outset'})
        ]),
        html.Div(children=[
            html.Td(children=[
                html.H2(children=titulo1_funil),
                html.H3(children=titulo2_funil, id='titulo2-funil'),
                html.H5(children=titulo3_funil),
                # dcc = dropdown - lista de valores, value = valor padrão, id = nome do dcc
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
                # dcc = dropdown - lista de valores, value = valor padrão, id = nome do dcc
                dcc.Dropdown(opcoes_mapa, value='2017 a 2021', id='dropdown-mapa'),
                dcc.Graph(id='grafico-mapa', figure=fig_mapa)
            ], style={'background-color': 'rgb(128, 255, 128)', 'width': '1306px',
                      'border-style': 'outset'})
        ])
    ])


    # decorator - grafico pizza - para quando os valores do dcc for alterado
    @app.callback(
        # quem vai ser alterado? nome(id) e qual caracteristica
        Output('grafico-pizza', 'figure'),  # altera o grafico
        Output('titulo1-pizza', 'children'),  # altera o titulo1
        Input('slider-pizza', 'value'),  # value = informacao selecionada do dcc
    )
    def alterar_pizza(value):
        # altera o titulo1
        titulo1_pizza_alterado = f'As 15 linguagens de programação mais usadas no ano de {value}'
        # cria um novo dataframe filtrado pelo valor escolhido
        df_pizza_filtrado = df_pizza[df_pizza['Date'] == int(value)]
        # chama a funcao novamente para plotar o grafico com o dado escolhido
        fig_pizza_alterada = Dash_04_pizza_alterado.funcao_pizza(df_pizza_filtrado)
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
        figura_linha_alterada = Dash_05_linha_alterado.funcao_linha(df_linha, value)
        return figura_linha_alterada, titulo1_linha_alterado

    # decorator - grafico barra - segue o mesmo raciocinio do primeiro callback
    @app.callback(
        Output('grafico-barra', 'figure'),
        Output('titulo1-barra', 'children'),
        Input('radioitems-barra', 'value')  # dá a informacao selecionada
    )
    def alterar_barra(value):
        titulo1_barra = f'Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia em {value}'
        df_barra_filtrado = dados_csv_barra[dados_csv_barra['Date'] == int(value)]
        figura_barra_alterada = Dash_03_barra_alterado.funcao_barra(df_barra_filtrado)
        return figura_barra_alterada, titulo1_barra


    # decorator - grafico funil - segue o mesmo raciocinio do primeiro callback
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
