# Importanto as bibliotecas
import plotly.express as px # para plotar o grafico
import pandas as pd # para importar os dados da tabela excel ou .csv
from dash import Dash, html, dcc


"""
Nessa tabela nós trabalhamos com porcentagens.
São as porcentagens de uso das linguagens por mês em cada ano
A única coluna diferente é a "Date", a primeira, o resto das colunas são as linguagens
Nesse gráfico usamos para pegar pelas 15 mais usadas.
A célula abaixo carrega o arquivo .csv em um dataframe chamado df
A linha 2 puxa o arquivo de dados direto do github
A linha 3 só mostra o dataframe na tela
"""

# carrega a tabela para o dataframe df
#df_pizza = pd.read_csv('https://raw.githubusercontent.com/TrabalhoAPC2021-02/Trabalho_Final/main/arquivos/04e05_Most_Popular_Programming_Languages_from_2005_to_2021.csv', ';')
df_pizza = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
#df_pizza

"""
A próxima célula converte o dataframe em uma lista chamada lista_dados, 
ou seja, coloca os dados em uma matriz para facilitar o uso de indices 
no tratamento dos dados
"""

# converte os dados em uma lista chamada lista_dados
lista_dados_pizza = df_pizza.values
#print(lista_dados_pizza)
#print(len(lista_dados_pizza))

"""
Nesse grafico vao aparecer as linguagens e a totalizacao de cada uma delas do ano escolhido
assim, primeiro se coloca os nomes das colunas na lista nomes_colunas (29 itens)
depois em nomes_linguagens, despreza-se o primeiro nome, que nao e uma linguagem e so a data (28 itens)
"""

# carrega os nomes das colunas do dataframe para uma lista chamada nomes_colunas
nomes_colunas_pizza = list(df_pizza.columns)
#print(nomes_colunas_pizza)
#print(len(nomes_colunas_pizza))

# retira o nome da primeira coluna que nao e linguagem e so a data
nomes_linguagens_pizza = nomes_colunas_pizza[1:len(nomes_colunas_pizza)]
#print(nomes_linguagens_pizza)
#print(len(nomes_linguagens_pizza))

"""
A celula abaixo calcula o somatorio de cada coluna de linguagem do ano escolhido
no final tem-se 28 somatorios
"""

# faz o somatorio dos valores de cada linguagem apenas do ano em estudo
# cria uma lista para receber o somatorio dos valores de cada coluna (linguagem)
somatorio_pizza: [float] = [0 for aa in range(28)]
# determina um ano para filtrar os dados e plotar o grafico
ano_em_estudo_pizza = '2021'

for x in lista_dados_pizza: # percorre todas as linhas da lista_dados
    # salva em ano[i] so os 4 ultimos caracteres da string 'mes ano'
  ano_pizza = x[0][len(x[0]) - 4:len(x[0])]
  if ano_pizza == ano_em_estudo_pizza:
      # calcula o somatorio dos valores de cada coluna ou seja de cada linguagem
    for i in range(0, 28):
      somatorio_pizza[i] = somatorio_pizza[i] + x[i + 1]
      #print(x[i])
    #print('nova linha')

#print(len(somatorio_pizza))
#print(somatorio_pizza)

"""
Para cada somatorio agora se calcula a media
no final tem-se 28 medias, uma para cada linguagem
"""

# calcula a media de uso anual para cada linguagem
# cria uma lista para receber a media dos valores de cada coluna (linguagem)
media_pizza: [float] = [0 for aa in range(28)]

# calcula a media dos valores de cada coluna ou seja de cada linguagem
for i in range(0, 28):
      media_pizza[i] = somatorio_pizza[i] / 12
      #print(media[i])

#print(len(media_pizza))
#print(nomes_linguagens_pizza)
#print(media_pizza)

"""
O metodo de ordenacao abaixo e chamado metodo bolha, que consiste em 
percorrer a lista item a item (primeiro for) e comparar cada valor 
com todos os valores "a frente" deste (segundo for)
as variaveis auxiliares servem para armazenar o valor da media em 
questao temporariamente, enquanto se troca de lugar essa media com 
a outra que esta fora de ordem.
em seguida, volta o valor que estava armazenado na variavel aux para 
o lugar certo, o mesmo raciocinio se aplica a varaiavel que tem o 
nome da linguagem, porque essa precisa acompanhar o valor da sua media. 
Se a media muda de lugar, o nome da linguagem muda tambem, para 
acompanhar sua respectiva media e nao bagunçar tudo
"""

# ordena as linguagens pela media em ordem decrescente 
# inicializa a variavel auxiliar que vai receber o valor da media
# temporariamente enquanto troca de lugar as medias que estao fora de ordem
aux_media_pizza = 0
# a mesma coisa pra linguagem, para ela acompanhar sua respectiva media
aux_nomes_linguagens_pizza = ''

# percorre a lista media uma vez
for i in range(0, 27):
    # percorre a lista media novamente dali pra frente comparando os valores
    for j in range(i, 27):
        # se estiver fora de ordem usa a variavel aux para
        # trocar de lugar os valores e colocar na ordem
        if media_pizza[i]<media_pizza[j]:
            # ordena a media
            aux_media_pizza = media_pizza[i]
            media_pizza[i] = media_pizza[j]
            media_pizza[j] = aux_media_pizza
            # faz o nome da linguagem trocar de lugar tambem para
            # acompanhar sua respectiva media
            aux_nomes_linguagens_pizza = nomes_linguagens_pizza[i]
            nomes_linguagens_pizza[i] = nomes_linguagens_pizza[j]
            nomes_linguagens_pizza[j] = aux_nomes_linguagens_pizza

#print(len(nomes_linguagens_pizza), len(media_pizza))
#print(nomes_linguagens_pizza[0], media_pizza[0])
#print(nomes_linguagens_pizza[27], media_pizza[27])

"""
A celula abaixo pega as primeiras 15 linguagens da ordenacao 
feita anteriormente, ou seja, as 15 linguagens mais usadas
"""

# plota no gráfico apenas as 15 primeiras
# pega as linguagens de 0 a 14 - porque a 15 nao entra no fatiamento da lista
dados_x_pizza= nomes_linguagens_pizza[0:15]
# pega as medias de 0 a 14 - porque a 15 nao entra no fatiamento da lista
dados_y_pizza= media_pizza[0:15]

# usa o valor da variavel
fig_pizza = px.pie(names = dados_x_pizza, values=dados_y_pizza,
                   title=f'As 15 linguagens de programação mais usadas no ano de {ano_em_estudo_pizza}')
# mostra o grafico
#fig_pizza.show()

# criar o aplicativo do flask
# inicializacao do aplicativo
app_pizza = Dash(__name__)

# atualizando o layout do aplicativo flask
app_pizza.layout = html.Div(children=[
    html.H1(children='Gráfico de pizza'),

    html.Div(children='As 15 linguagens de programação mais usadas no ano de '),

    dcc.Graph(
        id='grafico-pizza',
        figure=fig_pizza
    )
])

if __name__ == '__main__':
    # colocando o aplicativo no ar (servidor local)
    app_pizza.run_server(debug=True)