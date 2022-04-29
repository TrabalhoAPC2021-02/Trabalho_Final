# Importanto as bibliotecas
import plotly.graph_objects as go


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_barraHoriz(dataframe):
    # empresas que serao mostradas no grafico
    empresas_barraHoriz = ['Amazon', 'Apple', 'Dell', 'eBay', 'Facebook', 'Google', 'HP', 'Instagram', 'Intel', 'LinkedIn',
                      'Microsoft', 'Netflix', 'Nvidia', 'Twitter', 'YouTube']
    # variaveis que vao receber as medias calculadas
    media_female_empresa_barraHoriz = []
    media_male_empresa_barraHoriz = []
    # percorre empresa por empresa da lista
    for x in empresas_barraHoriz:
        # cria dataframe com dados da empresa em questao
        df_empresa_barraHoriz = dataframe[dataframe['Company'] == x]
        # transforma a coluna de percentual de mulheres em uma lista
        female_perc_barraHoriz = df_empresa_barraHoriz['Female%'].tolist()
        # transforma a coluna de percentual de homens em uma lista
        male_perc_barraHoriz = df_empresa_barraHoriz['Male%'].tolist()
        # acumula a soma dos percentuais femininos
        soma_female_perc_barraHoriz = 0
        for i in range(len(female_perc_barraHoriz)):
            soma_female_perc_barraHoriz = soma_female_perc_barraHoriz + female_perc_barraHoriz[i]
        # calcula a media se tiver dados
        if len(female_perc_barraHoriz) == 0:
            media_female_perc = 0
        else:
            media_female_perc = soma_female_perc_barraHoriz / len(female_perc_barraHoriz)
        # adiciona resultado na lista
        media_female_empresa_barraHoriz.append(media_female_perc)
        # acumula a soma dos percentuais masculinos
        soma_male_perc_barraHoriz = 0
        for i in range(len(male_perc_barraHoriz)):
            soma_male_perc_barraHoriz = soma_male_perc_barraHoriz + male_perc_barraHoriz[i]
        # calcula a media se tiver dados
        if len(male_perc_barraHoriz) == 0:
            media_male_perc_barraHoriz = 0
        else:
            media_male_perc_barraHoriz = soma_male_perc_barraHoriz / len(male_perc_barraHoriz)
        # adiciona resultado na lista
        media_male_empresa_barraHoriz.append(media_male_perc_barraHoriz)
    # gera o gráfico de barras horizontais
    figura_barraHoriz = go.Figure(data=[
        go.Bar(name='% Feminino', x=media_female_empresa_barraHoriz, y=empresas_barraHoriz, orientation='h'),
        go.Bar(name='% Masculino', x=media_male_empresa_barraHoriz, y=empresas_barraHoriz, orientation='h')
    ])
    figura_barraHoriz.update_layout(barmode='group', template='plotly_dark')
    # retorna o gráfico gerado
    return figura_barraHoriz

