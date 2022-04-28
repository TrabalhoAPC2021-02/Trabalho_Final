# Importanto as bibliotecas
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
import plotly.express as px  # biclioteca responsável por plotar os gráficos
from dash import Dash, html, dcc, Input, Output


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_pizza(dataframe):
    lista_dados_pizza = dataframe.values
    nomes_colunas_pizza = list(dataframe.columns)
    nomes_linguagens_pizza = nomes_colunas_pizza[1:len(nomes_colunas_pizza)]
    somatorio_pizza: [float] = [0 for aa in range(28)]
    for x in lista_dados_pizza:  # percorre todas as linhas da lista_dados
        for i in range(0, 28):
            somatorio_pizza[i] = somatorio_pizza[i] + x[i + 1]
    media_pizza: [float] = [0 for aa in range(28)]
    for i in range(0, 28):
        media_pizza[i] = somatorio_pizza[i] / 12
    aux_media_pizza = 0
    aux_nomes_linguagens_pizza = ''
    for i in range(0, 27):
        for j in range(i, 27):
            if media_pizza[i] < media_pizza[j]:
                aux_media_pizza = media_pizza[i]
                media_pizza[i] = media_pizza[j]
                media_pizza[j] = aux_media_pizza
                aux_nomes_linguagens_pizza = nomes_linguagens_pizza[i]
                nomes_linguagens_pizza[i] = nomes_linguagens_pizza[j]
                nomes_linguagens_pizza[j] = aux_nomes_linguagens_pizza
    dados_x_pizza = nomes_linguagens_pizza[0:15]
    dados_y_pizza = media_pizza[0:15]
    figura_pizza = px.pie(names=dados_x_pizza, values=dados_y_pizza)
    # retorna o gráfico gerado
    return figura_pizza

'''
if __name__ == '__main__':

    df_pizza = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
    opcoes_pizza = list(df_pizza['Date'].unique())
    opcoes_pizza.sort()
    df_dados_pizza = df_pizza[df_pizza['Date'] == 2021]
    fig_pizza = funcao_pizza(df_dados_pizza)
    titulo1_pizza = 'As 15 linguagens de programação mais usadas no ano de 2021'
    titulo2_pizza = '.'

    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app_pizza = Dash(__name__)

    # atualizando o layout do aplicativo flask
    app_pizza.layout = html.Div(children=[
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
                #dcc.Dropdown(opcoes_pizza, value='2021', id='dropdown-pizza'),
                dcc.Graph(id='grafico-pizza', figure=fig_pizza)
            ], style={'background-color': 'rgb(255, 255, 128)', 'width': '1306px',
                      'border-style': 'outset'})
    ])

    # decorator
    @app_pizza.callback(
        Output('grafico-pizza', 'figure'),
        Output('titulo1-pizza', 'children'),
        Input('slider-pizza', 'value'),  # dá a informacao selecionada
        #Input('dropdown-pizza', 'value'),  # dá a informacao selecionada
    )
    def alterar_pizza(value):
        titulo1_pizza_alterado = f'As 15 linguagens de programação mais usadas no ano de {value}'
        df_dados_pizza = df_pizza[df_pizza['Date'] == int(value)]
        fig_pizza_alterada = funcao_pizza(df_dados_pizza)
        return fig_pizza_alterada, titulo1_pizza_alterado

    # colocando o aplicativo no ar (servidor local)
    app_pizza.run_server(debug=True)
'''