# Importanto as bibliotecas
import plotly.express as px  # biblioteca responsável por plotar os gráficos


# funcao que gera o grafico
# recebe como parametro a base de dados ja filtrada pela opcao escolhida
def funcao_pizza(dataframe):
    # transforma em lista o dataframe inteiro
    lista_dados_pizza = dataframe.values
    # guarda os nomes das colunas em uma lista
    nomes_colunas_pizza = list(dataframe.columns)
    # retira o primeiro nome que nao é nome de linguagem (é a data)
    nomes_linguagens_pizza = nomes_colunas_pizza[1:len(nomes_colunas_pizza)]
    # define o vetor que recebera o somatorio de uso das linguagens
    somatorio_pizza: [float] = [0 for aa in range(28)]
    # acumula o somatorio de uso das linguagens
    for x in lista_dados_pizza:  # percorre todas as linhas da lista_dados
        for i in range(0, 28):
            somatorio_pizza[i] = somatorio_pizza[i] + x[i + 1]
    # define o vetor que recebera a media de uso das linguagens
    media_pizza: [float] = [0 for aa in range(28)]
    # calcula a media de uso das linguagens (sao 28 linguagens ao todo)
    for i in range(0, 28):
        media_pizza[i] = somatorio_pizza[i] / 12
    # utiliza o metodo bolha para ordenar as medias de forma decrescente e suas respectivas linguagens
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
    # define o vetor do eixo x do grafico - apenas as 15 primeiras linguagens
    dados_x_pizza = nomes_linguagens_pizza[0:15]
    # define o vetor do eixo y do grafico - apenas as 15 primeiras linguagens
    dados_y_pizza = media_pizza[0:15]
    # gera o gráfico de pizza
    figura_pizza = px.pie(names=dados_x_pizza, values=dados_y_pizza)
    figura_pizza.update_layout(template='plotly_dark')
    # retorna o gráfico gerado
    return figura_pizza

