import pandas as pd  # biblioteca utilizada para arquivos em dataframe
import plotly.graph_objects as go # biblioteca que usaremos para criar os gráficos


def funcao_barras(dataframe, cargo):
    df_test = dataframe[dataframe['Cargo'] == cargo]
    figura_barra = go.Figure(data=[
        go.Bar(name='Terceiro', x=df_test['Especialidade'], y=df_test['Terceiro']),
        go.Bar(name='CLT', x=df_test['Especialidade'], y=df_test['CLT'])
    ])

    figura_barra.update_layout(barmode='group')
    return figura_barra
        