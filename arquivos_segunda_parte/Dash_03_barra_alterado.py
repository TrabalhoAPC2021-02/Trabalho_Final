# Importanto as bibliotecas
import plotly.graph_objects as go


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_barra(dataframe):
    # empresas que serao mostradas no grafico
    empresas_barra = ['Amazon', 'Apple', 'Dell', 'eBay', 'Facebook', 'Google', 'HP', 'Instagram', 'Intel', 'LinkedIn',
                      'Microsoft', 'Netflix', 'Nvidia', 'Twitter', 'YouTube']
    # variaveis que vao receber as medias calculadas
    media_female_empresa_barra = []
    media_male_empresa_barra = []
    # percorre empresa por empresa da lista
    for x in empresas_barra:
        # cria dataframe com dados da empresa em questao
        df_empresa_barra = dataframe[dataframe['Company'] == x]
        # transforma a coluna de percentual de mulheres em uma lista
        female_perc_barra = df_empresa_barra['Female%'].tolist()
        # transforma a coluna de percentual de homens em uma lista
        male_perc_barra = df_empresa_barra['Male%'].tolist()
        # acumula a soma dos percentuais femininos
        soma_female_perc_barra = 0
        for i in range(len(female_perc_barra)):
            soma_female_perc_barra = soma_female_perc_barra + female_perc_barra[i]
        # calcula a media se tiver dados
        if len(female_perc_barra) == 0:
            media_female_perc = 0
        else:
            media_female_perc = soma_female_perc_barra / len(female_perc_barra)
        # adiciona resultado na lista
        media_female_empresa_barra.append(media_female_perc)
        # acumula a soma dos percentuais masculinos
        soma_male_perc_barra = 0
        for i in range(len(male_perc_barra)):
            soma_male_perc_barra = soma_male_perc_barra + male_perc_barra[i]
        # calcula a media se tiver dados
        if len(male_perc_barra) == 0:
            media_male_perc_barra = 0
        else:
            media_male_perc_barra = soma_male_perc_barra / len(male_perc_barra)
        # adiciona resultado na lista
        media_male_empresa_barra.append(media_male_perc_barra)
    # gera o gráfico de barras horizontais
    figura_barra = go.Figure(data=[
        go.Bar(name='% Feminino', x=media_female_empresa_barra, y=empresas_barra, orientation='h'),
        go.Bar(name='% Masculino', x=media_male_empresa_barra, y=empresas_barra, orientation='h')
    ])
    figura_barra.update_layout(barmode='group')
    # retorna o gráfico gerado
    return figura_barra

