import pandas as pd  # biblioteca utilizada para arquivos em dataframe
import plotly.graph_objects as go # biblioteca que usaremos para criar os gráficos


def funcao_barraVert(dataframe, cargo):
    df_test = dataframe[dataframe['Cargo'] == cargo]
    figura_barraVert = go.Figure(data=[
        go.Bar(name='Terceiro', x=df_test['Especialidade'], y=df_test['Terceiro']),
        go.Bar(name='CLT', x=df_test['Especialidade'], y=df_test['CLT'])
    ])
    figura_barraVert.update_xaxes(title='Especialidade', ticks='outside')
    figura_barraVert.update_yaxes(title='Salario em reais', ticks='outside')

    figura_barraVert.update_layout(barmode='group', template='plotly_dark')
    return figura_barraVert
        