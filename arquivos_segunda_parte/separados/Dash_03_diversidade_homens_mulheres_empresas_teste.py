# Importando as bibliotecas
# para a criação dos nossos gráficos
import plotly.graph_objects as go
# para ler nossa tabela
import pandas as pd
from dash import Dash, html, dcc

"""
Abaixo faremos o processo de ler nossa tabela, dando o nome de dados_csv
Usamos o comando do pandas "pd.read_csv"
Passamos o link do nosso arquivo que está no github
# Explicando a tabela
O assunto da tabela é a diversidade de contratação por empresas, os dados estão em porcentagem
Temos as colunas "Date" para os anos
"Type" é o cargo ocupado dentro da empresa
"Company" são as empresas
O resto está bem autoexplicativo e podemos ver que todos estão em porcentagem, 
as próprias colunas nos dizem isso
Nós usamos a tabela para pegar apenas os valores de porcentagem feminina e masculina
"""

#dados_csv_barra = pd.read_csv('https://raw.githubusercontent.com/TrabalhoAPC2021-02/Trabalho_Final/main/arquivos/03_Employee_Diversity_in_Tech.csv', ';')
dados_csv_barra = pd.read_csv('03_Employee Diversity in Tech.csv', ';')
#dados_csv_barra

"""
Separamos o nosso dataframe principal, pegando somente os dados do ano de 
2018 e atribuimos isso a 'df_2018'
"""

df_2018_barra = dados_csv_barra[dados_csv_barra['Date'] == 2018]
#df_2018_barra

"""
Criamos uma lista com as 15 empresas mais conhecidas da nossa tabela
Logo depois criamos duas listas para receber as médias do percentual masculino e feminino
"""

# criando as listas para receber os dados

# lista das empresas escolhidas
empresas_barra = ['Amazon', 'Apple', 'Dell', 'eBay', 'Facebook', 'Google', 'HP', 'Instagram', 'Intel', 'LinkedIn', 'Microsoft', 'Netflix', 'Nvidia', 'Twitter', 'YouTube']

# lista que receberá as medias do percentual da presenca feminina nas empresas
media_female_empresa_barra =[]
# lista que receberá as medias do percentual da presenca masculina nas empresas
media_male_empresa_barra = []

"""
Criamos um laço de repetição para cada empresa que escolhemos lá em cima
na linha -> df_2018_empresa = df_2018[df_2018['Company'] == x] o "x" será 
cada empresa da nossa lista "empresas" que criamos lá em cima, então na 
primeira repetição o nome será 'Amazon', então ele vai puxar os dados das 
colunas 'Female%' e 'Male% para transformar em uma lista mas somente aonde 
os dados forem da empresa Amazon, logo depois ele irá fazer uma média dos 
percentuais femininos e masculinos  e usar o comando .append para jogar 
esse valor na nossa lista vazia que criamos lá em cima
Após tudo isso o comando vai voltar para o primeiro "for" e repetirá o 
mesmo processo mas com outra empresa.
# Comandos
.append() usamos ele no nosso código para jogar os valores das nossas 
médias naquelas listas vazias que criamos lá em cima
"""

#Selecionando os dados de cada empresa

for x in empresas_barra:
  df_2018_empresa_barra = df_2018_barra[df_2018_barra['Company'] == x]
  female_perc_barra = df_2018_empresa_barra['Female%'].tolist() # tranformando o dataframe do percentual feminino em lista.
  male_perc_barra = df_2018_empresa_barra['Male%'].tolist() # tranformando o dataframe do percentual feminino em lista.
  
  # utilização de um laço for para calcular a média dos percentuais
  soma_female_perc_barra = 0
  for i in range (len(female_perc_barra)):
    soma_female_perc_barra = soma_female_perc_barra + female_perc_barra[i]
  media_female_perc = soma_female_perc_barra / len(female_perc_barra)
  media_female_empresa_barra.append(media_female_perc)

  # utilização de um laço for para calcular a média dos percentuais
  soma_male_perc_barra = 0
  for i in range (len(male_perc_barra)):
    soma_male_perc_barra = soma_male_perc_barra + male_perc_barra[i]
  media_male_perc_barra = soma_male_perc_barra / len(male_perc_barra)
  media_male_empresa_barra.append(media_male_perc_barra)

#print(empresas_barra)
#print(media_female_empresa_barra)
#print(media_male_empresa_barra)

"""# 
Criando a figura
Usamos o comando go.Figure para iniciar nossa figura, 
passamos para ele no parâmetro "data=" dois gráficos de barra 
para que seja possivel fazermos as barras duplas.
Para que o gráfico realmente saio como barras duplas, usamos o 
comando .update_layout() e colocamos o barmode='group'
"""

fig_barra = go.Figure(data=[
    go.Bar(name='% Feminino', x=media_female_empresa_barra, y=empresas_barra, orientation='h'), # orientation='h' é para dizer que queremos na horizontal
    go.Bar(name='% Masculino', x=media_male_empresa_barra, y=empresas_barra, orientation='h')
])
# mudando o layout parra barras duplas
fig_barra.update_layout(barmode='group', title='Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia')
#fig_barra.show()

# criar o aplicativo do flask
# inicializacao do aplicativo
app_barra = Dash(__name__)

# atualizando o layout do aplicativo flask
app_barra.layout = html.Div(children=[
    html.H1(children='Gráfico de barra'),

    html.Div(children='Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia'),

    dcc.Graph(
        id='grafico-barra',
        figure=fig_barra
    )
])

if __name__ == '__main__':
    # colocando o aplicativo no ar (servidor local)
    app_barra.run_server(debug=True)