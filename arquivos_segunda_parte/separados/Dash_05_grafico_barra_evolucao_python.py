# Importanto as bibliotecas
import plotly.express as px # para plotar o grafico
import pandas as pd # para importar os dados da tabela excel ou .csv
from dash import Dash, html, dcc

"""
Nessa tabela nós trabalhamos com porcentagens.
São as porcentagens de uso das linguagens por mês em cada ano
A única coluna diferente é a "Date", a primeira, o resto das colunas são as linguagens
Nesse gráfico usamos a tabela para ver a evolução do uso da linguagem Python
A célula abaixo carrega o arquivo .csv em um dataframe chamado df
A linha 2 puxa o arquivo de dados direto do github
A linha 3 só mostra o dataframe na tela
"""

# carrega a tabela para o dataframe df
#df_linha = pd.read_csv('https://raw.githubusercontent.com/TrabalhoAPC2021-02/Trabalho_Final/main/arquivos/04e05_Most_Popular_Programming_Languages_from_2005_to_2021.csv', ';')
df_linha = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
#df_linha

"""A próxima célula converte o dataframe em uma lista chamada lista_dados, ou seja, coloca os dados em uma matriz para facilitar o uso de indices no tratamento dos dados"""

# converte os dados em uma lista chamada lista_dados
lista_dados_linha = df_linha.values
#print(lista_dados_linha)
#print(len(lista_dados_linha))

"""
Na matriz acima, observa-se que a data vem no formato de mes e ano, 
mas so queremos tratar os dados anuais, entao vamos criar uma lista 
para receber so os quatro ultimos caracteres da data , ou seja, o ano
A linha 6 particiona a string que contem a data 
ano[i] -> vai receber o ano da string particionada
x[0] -> e a coluna 0 da lista_dados
[len(x[0])-4:len(x[0])] -> [inicio da string:final da string + 1 posicao]
len(x[0])-4 -> inicio no caracter 2 do ano
len(x[0]) -> vai até o final, lembrando que ultrapassa um (começa do zero)
"""

# separa ano do mês
# cria uma lista para receber a parte da string de data que se refere ao ano
ano_linha: [str] = [0 for ff in range(204)]

i = 0 # inicializa o contador que indexa a lista ano
# percorre todas as linhas da lista_dados
for x in lista_dados_linha:
  # salva em ano[i] so os 4 ultimos caracteres da string 'mes ano'
  ano_linha[i] = x[0][len(x[0]) - 4:len(x[0])]
  #print(ano[i])
  i = i + 1

#len(ano_linha)

"""
A lista ano tem todos os anos do dataframe, mas muitos sao repetidos (204 itens)
entao a celula abaixo agrupa na lista anos_agrupados so os nao repetidos
assim anos tem 204 itens enquanto anos_agrupados tem somente 17 itens
"""

# agrupar os anos repetidos
# cria uma lista para receber os anos que nao forem repetidos
anos_agrupados_linha: [str] = [0 for ff in range(17)]

# incializa o primeiro ano a ser comparado
anos_agrupados_linha[0] = ano_linha[0]

# inicializa o contador que indexa a lista anos_agrupados
m = 0
# percorre todas as linhas da lista ano
for z in ano_linha:
  # compara o ano do atual da lista_dados com o utlimo ano_agrupado armazenado
  if z != anos_agrupados_linha[m]:
    # como sao anos diferentes, incremeta o indice para armazenar o novo ano em uma nova posicao da lista
    m = m + 1
    anos_agrupados_linha[m] = z
    
#print(anos_agrupados_linha)
#len(anos_agrupados_linha)

"""
A celula abaixo carrega somente os dados da coluna python para tratamento
sintaxe: lista[linha,coluna] 
-> linha = : -> todas as linhas 
-> coluna = 20 -> coluna número 21 (começa em 0) com os dados de Python
"""

# carrega dados da linguagem python na lista valores_python
# sintaxe: lista[linha,coluna] -> linha = : todas as linhas -> coluna = 20 coluna de Python
valores_python_linha = lista_dados_linha[:, 20]
#print(valores_python_linha)

"""A celula abaixo calcula a soma e a media dos valores de python para cada ano_agrupado

no final teremos 17 somas e 17 medias, porque e o numero total de anos_agrupados
"""

# totalizar dados mensais em anos
soma_python_linha: [float] = [0 for hh in range(17)] # cria uma lista para receber a soma dos valores da coluna Python
media_python_linha: [float] = [0 for ii in range(17)] # cria uma lista para receber a media dos valores da coluna Python

j = 0 # inicializa o contador que indexa a lista soma_python e media_python
for z in range(0, len(valores_python_linha)): # de 0 ate quantidade total de valores de python
    if ano_linha[z] == anos_agrupados_linha[j]: # soma enquanto o ano de lista_dados for igual ao ano agrupado
        soma_python_linha[j] = soma_python_linha[j] + valores_python_linha[z]  # acumula a soma
        #print(ano[z], soma_python[j], media_python[j])
    else: # novo ano
        media_python_linha[j] = soma_python_linha[j] / 12.0 # ja calcula a media desse ano
        #print(anos_agrupados_linha[j], soma_python_linha[j], media_python_linha[j])
        j = j + 1 # incrementa o indice para começar a amular a soma do novo ano
        soma_python_linha[j] = soma_python_linha[j] + valores_python_linha[z] # acumula a soma
    media_python_linha[j] = soma_python_linha[j] / 12.0 # calcula a media do ultimo ano acumulado
    
#print(anos_agrupados_linha[j], soma_python_linha[j], media_python_linha[j])

"""
A celula abaixo usa a biblioteca plotly express para configurar e traçar o grafico de linhas
Linha 2 -> # markers -> pontinhos na curva
linha 3 -> configura o eixo x: titulo do eixo e de que lado esses tracinhos (ticks) que acompanham o numero vao ficar
linha 4 -> o mesmo para o eixo y
"""

# plotar grafico de linhas com os dados totalizados por ano da linguagem python
# markers -> pontos na curva
fig_linha = px.line(x=anos_agrupados_linha, y=media_python_linha, title="Evolução do uso da linguagem Python nos últimos 17 anos", markers=True)
# ticks -> tracinhos que acompanham os numeros
fig_linha.update_xaxes(title='Ano', ticks='outside')
fig_linha.update_yaxes(title='Percentual', ticks='outside')
# mostra o grafico na tela
#fig_linha.show()

# criar o aplicativo do flask
# inicializacao do aplicativo
app_linha = Dash(__name__)

# atualizando o layout do aplicativo flask
app_linha.layout = html.Div(children=[
    html.H1(children='Gráfico de linha'),

    html.Div(children='Evolução do uso da linguagem Python nos últimos 17 anos'),

    dcc.Graph(
        id='grafico-linha',
        figure=fig_linha
    )
])

if __name__ == '__main__':
    # colocando o aplicativo no ar (servidor local)
    app_linha.run_server(debug=True)