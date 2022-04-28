# Importanto as bibliotecas
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
import plotly.graph_objects as go # biblioteca que usaremos para criar os gráficos
from dash import Dash, html, dcc, Input, Output


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_funil(dataframe, cargo):
    cargo_funil = dataframe[dataframe['Cargo'] == cargo]
    t_cargo_funil = cargo_funil['Terceiro'].tolist()  # comando .tolist() usado para transformar a coluna numa lista
    soma_t_cargo_funil = 0
    for i in range(len(t_cargo_funil)):
        soma_t_cargo_funil = soma_t_cargo_funil + t_cargo_funil[i]
    if len(t_cargo_funil) == 0:
        media_t_cargo_funil = 0
    else:
        media_t_cargo_funil = soma_t_cargo_funil / len(t_cargo_funil)
    column_t_funil = ['Cargo', 'Terceiro']
    line_t_funil = ['']
    dados_t_funil = [['cargo', media_t_cargo_funil]]
    tb_terceiro_funil = pd.DataFrame(data=dados_t_funil, index=line_t_funil, columns=column_t_funil)
    clt_cargo_funil = cargo_funil['CLT'].tolist()
    soma_clt_cargo_funil = 0
    for i in range(len(clt_cargo_funil)):
        soma_clt_cargo_funil = soma_clt_cargo_funil + clt_cargo_funil[i]
    if len(clt_cargo_funil) == 0:
        media_clt_cargo_funil = 0
    else:
        media_clt_cargo_funil = soma_clt_cargo_funil / len(clt_cargo_funil)
    column_clt_funil = ['Cargo', 'CLT']
    line_clt_funil = ['']
    dados_clt_funil = [['cargo', media_clt_cargo_funil]]
    tb_clt_funil = pd.DataFrame(data=dados_clt_funil, index=line_clt_funil, columns=column_clt_funil)
    figura_funil = go.Figure()
    figura_funil.add_trace(go.Funnel(name='Terceiro', y=tb_terceiro_funil['Cargo'], x=tb_terceiro_funil['Terceiro']))
    figura_funil.add_trace(go.Funnel(name='CLT', y=tb_clt_funil['Cargo'], x=tb_clt_funil['CLT']))
    return figura_funil

def funcao_funil_quatro_cargos(dataframe):
    programador_funil = dataframe[dataframe['Cargo'] == 'Programador']
    anpro_funil = dataframe[dataframe['Cargo'] == 'Analista Programador']
    ansup_funil = dataframe[dataframe['Cargo'] == 'Analista de Suporte']
    ansis_funil = dataframe[dataframe['Cargo'] == 'Analista de sistemas']
    t_programador_funil = programador_funil['Terceiro'].tolist()  # comando .tolist() usado para transformar a coluna numa lista
    t_anpro_funil = anpro_funil['Terceiro'].tolist()
    t_ansup_funil = ansup_funil['Terceiro'].tolist()
    t_ansis_funil = ansis_funil['Terceiro'].tolist()
    soma_t_pro_funil = 0
    for i in range(len(t_programador_funil)):
        soma_t_pro_funil = soma_t_pro_funil + t_programador_funil[i]
    media_pro_funil = soma_t_pro_funil / len(t_programador_funil)
    soma_t_anpro_funil = 0
    for i in range(len(t_anpro_funil)):
        soma_t_anpro_funil = soma_t_anpro_funil + t_anpro_funil[i]
    media_anpro_funil = soma_t_anpro_funil / len(t_anpro_funil)
    soma_t_ansup_funil = 0
    for i in range(len(t_ansup_funil)):
        soma_t_ansup_funil = soma_t_ansup_funil + t_ansup_funil[i]
    media_ansup_funil = soma_t_ansup_funil / len(t_ansup_funil)
    soma_t_ansis_funil = 0
    for i in range(len(t_ansis_funil)):
        soma_t_ansis_funil = soma_t_ansis_funil + t_ansis_funil[i]
    media_ansis_funil = soma_t_ansis_funil / len(t_ansis_funil)
    column_funil = ['Cargo', 'Terceiro']
    line_funil = ['', '', '', '']
    dados_funil = [['Analista de Suporte', media_ansup_funil], ['Programador', media_pro_funil]
        , ['Analista programador', media_anpro_funil], ['Analista de sistemas', media_ansis_funil]]
    # tb_terceiro é o nome do nosso novo dataframe
    tb_terceiro_funil = pd.DataFrame(data=dados_funil, index=line_funil, columns=column_funil)
    clt_programador_funil = programador_funil['CLT'].tolist()
    clt_anpro_funil = anpro_funil['CLT'].tolist()
    clt_ansup_funil = ansup_funil['CLT'].tolist()
    clt_ansis_funil = ansis_funil['CLT'].tolist()
    soma_clt_pro_funil = 0
    for i in range(len(clt_programador_funil)):
        soma_clt_pro_funil = soma_clt_pro_funil + clt_programador_funil[i]
    media_clt_pro_funil = soma_clt_pro_funil / len(clt_programador_funil)
    soma_clt_anpro_funil = 0
    for i in range(len(clt_anpro_funil)):
        soma_clt_anpro_funil = soma_clt_anpro_funil + clt_anpro_funil[i]
    media_clt_anpro_funil = soma_clt_anpro_funil / len(clt_anpro_funil)
    soma_clt_ansup_funil = 0
    for i in range(len(clt_ansup_funil)):
        soma_clt_ansup_funil = soma_clt_ansup_funil + clt_ansup_funil[i]
    media_clt_ansup_funil = soma_clt_ansup_funil / len(clt_ansup_funil)
    soma_clt_ansis_funil = 0
    for i in range(len(clt_ansis_funil)):
        soma_clt_ansis_funil = soma_clt_ansis_funil + clt_ansis_funil[i]
    media_clt_ansis_funil = soma_clt_ansis_funil / len(clt_ansis_funil)
    column_funil = ['Cargo', 'CLT']
    line_funil = ['', '', '', '']
    dados_funil = [['Analista de Suporte', media_clt_ansup_funil], ['Programador', media_clt_pro_funil]
        , ['Analista programador', media_clt_anpro_funil], ['Analista de sistemas', media_clt_ansis_funil]]
    tb_clt_funil = pd.DataFrame(data=dados_funil, index=line_funil, columns=column_funil)
    figura_funil = go.Figure()
    figura_funil.add_trace(go.Funnel(name='Terceiro', y=tb_terceiro_funil['Cargo'], x=tb_terceiro_funil['Terceiro']))
    figura_funil.add_trace(go.Funnel(name='CLT', y=tb_clt_funil['Cargo'], x=tb_clt_funil['CLT']))
    return figura_funil

'''
if __name__ == '__main__':

    df_funil = pd.read_excel('02.1_salarios_CLT_Terceirizado.xlsx')
    opcoes_funil = list(df_funil['Cargo'].unique())
    opcoes_funil.append(' Programador, Analista Programador, Analista de Suporte e Analista de sistemas')
    opcoes_funil.sort()
    fig_funil = funcao_funil_quatro_cargos(df_funil)
    titulo1_funil = 'Comparação entre salários de contratados pela CLT e salários de terceirizados'
    titulo2_funil = 'Cargos: Programador, Analista Programador, Analista de Suporte e Analista de sistemas'
    titulo3_funil = 'Média salarial em reais.'

    # criar o aplicativo do flask
    # inicializacao do aplicativo
    app_funil = Dash(__name__)

    # atualizando o layout do aplicativo flask
    app_funil.layout = html.Div(children=[
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
    ])


    # decorator
    @app_funil.callback(
        Output('grafico-funil', 'figure'),
        Output('titulo2-funil', 'children'),
        Input('dropdown-funil', 'value')  # dá a informacao selecionada
    )
    def alterar_funil(value):
        titulo2_funil = f'Cargos: {value}'
        if value == ' Programador, Analista Programador, Analista de Suporte e Analista de sistemas':
            figura_funil_alterada = funcao_funil_quatro_cargos(df_funil)
        else:
            figura_funil_alterada = funcao_funil(df_funil, value)
        return figura_funil_alterada, titulo2_funil

    # colocando o aplicativo no ar (servidor local)
    app_funil.run_server(debug=True)
'''