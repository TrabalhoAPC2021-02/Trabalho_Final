# Importanto as bibliotecas
import plotly.graph_objects as go
import plotly.express as px # para plotar o grafico
import pandas as pd # para importar os dados da tabela excel ou .csv

import dash
#import dash_core_components as dcc
from dash import Dash, dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

# =============================================================================================
# =============================================================================================
# Grafico de pizza - 15 Linguagens mais usadas no ano
# =============================================================================================
# =============================================================================================

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

# =============================================================================================
# =============================================================================================
# Grafico de linha - evolucao de uso da linguagem
# =============================================================================================
# =============================================================================================

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
# df_linha = pd.read_csv('https://raw.githubusercontent.com/TrabalhoAPC2021-02/Trabalho_Final/main/arquivos/04e05_Most_Popular_Programming_Languages_from_2005_to_2021.csv', ';')
df_linha = pd.read_csv('04e05_Most Popular Programming Languages from 2005 to 2021.csv', ';')
# df_linha

"""A próxima célula converte o dataframe em uma lista chamada lista_dados, ou seja, coloca os dados em uma matriz para facilitar o uso de indices no tratamento dos dados"""

# converte os dados em uma lista chamada lista_dados
lista_dados_linha = df_linha.values
# print(lista_dados_linha)
# print(len(lista_dados_linha))

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

i = 0  # inicializa o contador que indexa a lista ano
# percorre todas as linhas da lista_dados
for x in lista_dados_linha:
    # salva em ano[i] so os 4 ultimos caracteres da string 'mes ano'
    ano_linha[i] = x[0][len(x[0]) - 4:len(x[0])]
    # print(ano[i])
    i = i + 1

# len(ano_linha)

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

# print(anos_agrupados_linha)
# len(anos_agrupados_linha)

"""
A celula abaixo carrega somente os dados da coluna python para tratamento
sintaxe: lista[linha,coluna] 
-> linha = : -> todas as linhas 
-> coluna = 20 -> coluna número 21 (começa em 0) com os dados de Python
"""

# carrega dados da linguagem python na lista valores_python
# sintaxe: lista[linha,coluna] -> linha = : todas as linhas -> coluna = 20 coluna de Python
valores_python_linha = lista_dados_linha[:, 20]
# print(valores_python_linha)

"""A celula abaixo calcula a soma e a media dos valores de python para cada ano_agrupado

no final teremos 17 somas e 17 medias, porque e o numero total de anos_agrupados
"""

# totalizar dados mensais em anos
soma_python_linha: [float] = [0 for hh in range(17)]  # cria uma lista para receber a soma dos valores da coluna Python
media_python_linha: [float] = [0 for ii in
                               range(17)]  # cria uma lista para receber a media dos valores da coluna Python

j = 0  # inicializa o contador que indexa a lista soma_python e media_python
for z in range(0, len(valores_python_linha)):  # de 0 ate quantidade total de valores de python
    if ano_linha[z] == anos_agrupados_linha[j]:  # soma enquanto o ano de lista_dados for igual ao ano agrupado
        soma_python_linha[j] = soma_python_linha[j] + valores_python_linha[z]  # acumula a soma
        # print(ano[z], soma_python[j], media_python[j])
    else:  # novo ano
        media_python_linha[j] = soma_python_linha[j] / 12.0  # ja calcula a media desse ano
        # print(anos_agrupados_linha[j], soma_python_linha[j], media_python_linha[j])
        j = j + 1  # incrementa o indice para começar a amular a soma do novo ano
        soma_python_linha[j] = soma_python_linha[j] + valores_python_linha[z]  # acumula a soma
    media_python_linha[j] = soma_python_linha[j] / 12.0  # calcula a media do ultimo ano acumulado

# print(anos_agrupados_linha[j], soma_python_linha[j], media_python_linha[j])

"""
A celula abaixo usa a biblioteca plotly express para configurar e traçar o grafico de linhas
Linha 2 -> # markers -> pontinhos na curva
linha 3 -> configura o eixo x: titulo do eixo e de que lado esses tracinhos (ticks) que acompanham o numero vao ficar
linha 4 -> o mesmo para o eixo y
"""

# plotar grafico de linhas com os dados totalizados por ano da linguagem python
# markers -> pontos na curva
fig_linha = px.line(x=anos_agrupados_linha, y=media_python_linha,
                    title="Evolução do uso da linguagem Python nos últimos 17 anos", markers=True)
# ticks -> tracinhos que acompanham os numeros
fig_linha.update_xaxes(title='Ano', ticks='outside')
fig_linha.update_yaxes(title='Percentual', ticks='outside')
# mostra o grafico na tela
# fig_linha.show()

# =============================================================================================
# =============================================================================================
# Grafico de barras - Diversidade empresas
# =============================================================================================
# =============================================================================================

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

# dados_csv_barra = pd.read_csv('https://raw.githubusercontent.com/TrabalhoAPC2021-02/Trabalho_Final/main/arquivos/03_Employee_Diversity_in_Tech.csv', ';')
dados_csv_barra = pd.read_csv('03_Employee Diversity in Tech.csv', ';')
# dados_csv_barra

"""
Separamos o nosso dataframe principal, pegando somente os dados do ano de 
2018 e atribuimos isso a 'df_2018'
"""

df_2018_barra = dados_csv_barra[dados_csv_barra['Date'] == 2018]
# df_2018_barra

"""
Criamos uma lista com as 15 empresas mais conhecidas da nossa tabela
Logo depois criamos duas listas para receber as médias do percentual masculino e feminino
"""

# criando as listas para receber os dados

# lista das empresas escolhidas
empresas_barra = ['Amazon', 'Apple', 'Dell', 'eBay', 'Facebook', 'Google', 'HP', 'Instagram', 'Intel', 'LinkedIn',
                  'Microsoft', 'Netflix', 'Nvidia', 'Twitter', 'YouTube']

# lista que receberá as medias do percentual da presenca feminina nas empresas
media_female_empresa_barra = []
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

# Selecionando os dados de cada empresa

for x in empresas_barra:
    df_2018_empresa_barra = df_2018_barra[df_2018_barra['Company'] == x]
    female_perc_barra = df_2018_empresa_barra[
        'Female%'].tolist()  # tranformando o dataframe do percentual feminino em lista.
    male_perc_barra = df_2018_empresa_barra[
        'Male%'].tolist()  # tranformando o dataframe do percentual feminino em lista.

    # utilização de um laço for para calcular a média dos percentuais
    soma_female_perc_barra = 0
    for i in range(len(female_perc_barra)):
        soma_female_perc_barra = soma_female_perc_barra + female_perc_barra[i]
    media_female_perc = soma_female_perc_barra / len(female_perc_barra)
    media_female_empresa_barra.append(media_female_perc)

    # utilização de um laço for para calcular a média dos percentuais
    soma_male_perc_barra = 0
    for i in range(len(male_perc_barra)):
        soma_male_perc_barra = soma_male_perc_barra + male_perc_barra[i]
    media_male_perc_barra = soma_male_perc_barra / len(male_perc_barra)
    media_male_empresa_barra.append(media_male_perc_barra)

# print(empresas_barra)
# print(media_female_empresa_barra)
# print(media_male_empresa_barra)

"""# 
Criando a figura
Usamos o comando go.Figure para iniciar nossa figura, 
passamos para ele no parâmetro "data=" dois gráficos de barra 
para que seja possivel fazermos as barras duplas.
Para que o gráfico realmente saio como barras duplas, usamos o 
comando .update_layout() e colocamos o barmode='group'
"""

fig_barra = go.Figure(data=[
    go.Bar(name='% Feminino', x=media_female_empresa_barra, y=empresas_barra, orientation='h'),
    # orientation='h' é para dizer que queremos na horizontal
    go.Bar(name='% Masculino', x=media_male_empresa_barra, y=empresas_barra, orientation='h')
])
# mudando o layout parra barras duplas
fig_barra.update_layout(barmode='group',
                        title='Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia')
# fig_barra.show()

# =============================================================================================
# =============================================================================================
# Grafico de funil - Comparacao salarios CLT e terceirizados
# =============================================================================================
# =============================================================================================


"""
# Explicando a tabela
Essa tabela mostra os salários de CLT: que são contratados com carteira assinada.
E salários de terceirizados de acordo com o google terceirizado é : "O contrato 
de trabalho terceirizado nada mais é que a execução das atividades de uma empresa, 
realizada por outra empresa."
Mostram os cargos e as especialidades
Os valores nas Tabelas estão em reais
"""

# definindo um dataframe a partir da url do arquivo que puxamos do github
# url_funil = 'https://raw.githubusercontent.com/TrabalhoAPC2021-02/Trabalho_Final/main/arquivos/02.1_salarios_CLT_Terceirizado.xlsx'
url_funil = '02.1_salarios_CLT_Terceirizado.xlsx'

# atribuindo uma variável 'df' para especificar nosso data frame
# usamos o comando pd.read_excel para ler o excel que atribuimos a variável "url"
df_funil = pd.read_excel(url_funil)
#f_funil # mostrar a tabela

# vendo valores repetidos
#df_funil['Cargo'].value_counts() # usamos o value.counts() para contar os valores da tabela na coluna cargo
                           # assim poderemos ver quantas vezes cada Cargo se repete

"""
Os colchetes[] no caso do código abaixo está servindo para localizar uma 
coluna no data frame especificado antes
Df é o dataframe que definimos lá em cima, o ['Cargo'] é especificando a 
coluna do dataframe
"""

# criando um data frame para os cargos mais repetidos
# separamos aqui o nosso dataframe principal "df" em quatro outros
# cada um atriubuido para cada cargo que mais se repetiu

# aqui por exemplo criei um dataframe puxando os dados aonde na
# na coluna cargo seria == a programador
# a mesma coisa foi feita nos itens seguintes
programador_funil = df_funil[df_funil['Cargo'] == 'Programador']

anpro_funil = df_funil[df_funil['Cargo'] == 'Analista Programador']
ansup_funil = df_funil[df_funil['Cargo'] == 'Analista de Suporte']
ansis_funil = df_funil[df_funil['Cargo'] == 'Analista de sistemas']

"""
# Mostrando cada DATA FRAME criado nas celulas anteriores
"""
# programador_funil
# anpro_funil
# ansup_funil
# ansis_funil

"""
# Serve para o código do terceirizados e dos clt pois eles usam a mesma lógica
Fazendo uma média para os contratados por CLT e pelo contratados que são Terceirizados:
Passo 1- Transformação dos valores das colunas para lista, colunas "terceirizado" e "clt"
Passo 2- Usamos o comando de repetição "for" para fazer uma soma de todos os valores 
que criamos nas listas do passo 1, fora do comando "for" fazemos uma média dessa soma 
total que fizemos usando a estrutura de repetição dividindo pelo tamanho da lista, 
lembrando que é uma lista para cada cargo e uma soma total para cada cargo, as variaveis 
explicam bem isso, como por exemplo "soma_t_pro".
# Atenção!!! A próxima celula é somente para o salário de terceirizados
# Terceirizados
"""

# tratando os dados para calcular a soma e a media
# para terceirizado
# PASSO 1
# criamos uma lista para cada dataframe que separamos, lembrando que aqui é
# somente da coluna terceiro, então transformamos somente elas em listas

t_programador_funil = programador_funil['Terceiro'].tolist() # comando .tolist() usado para transformar a coluna numa lista
t_anpro_funil = anpro_funil['Terceiro'].tolist()
t_ansup_funil =ansup_funil['Terceiro'].tolist()
t_ansis_funil = ansis_funil['Terceiro'].tolist()

#PASSO 2
# usando o for para criar uma média para cada cargo
# atribuimos um 0 aqui nessa variável para que seja possivel ser somado na nossa estrutura
# de repetição
soma_t_pro_funil = 0


# usamos o for para criar nossa somatória total dos valores das nossas listas
# len(t_programador) é o tamanho da nossa lista
# o comando " for i in range (len(t_programador)" é para a cada repetição ele atribuir
# uma posição da lista ao comando i, por exemplo, na primeira repetição o "i" será o 0, na segunda
# será 1, e assim até chegar a ultima posição da lista
# no comando a baixo usamos essa repetição para fazer a soma
# então na primeira repetição nosso soma_t_pro é igual a 0
# ai ele vai somar 0 mais o primeiro valor da nossa lista
# por exemplo, vamos dizer que nosso valor é 6000, ele vai somar 6000 + 0
# então na segunda repetição ele não será mais 0, será 6000, ai ele vai somar o 6000
# mais o segundo valor da lista e assim por diante até o final
# usamos a mesma logica para as outras listas

for i in range (len(t_programador_funil)):
  soma_t_pro_funil = soma_t_pro_funil + t_programador_funil[i]
media_pro_funil = soma_t_pro_funil / len(t_programador_funil)
#print('Terc_programador',soma_t_pro, media_pro)

#mesma logica da explicação de cima

soma_t_anpro_funil = 0
for i in range (len(t_anpro_funil)):
  soma_t_anpro_funil = soma_t_anpro_funil + t_anpro_funil[i]
media_anpro_funil = soma_t_anpro_funil / len(t_anpro_funil)
#print('Terc_analista_programador', soma_t_anpro_funil, media_anpro_funil)

soma_t_ansup_funil = 0
for i in range (len(t_ansup_funil)):
  soma_t_ansup_funil = soma_t_ansup_funil + t_ansup_funil[i]
media_ansup_funil = soma_t_ansup_funil / len(t_ansup_funil)
#print('Terc_analista_suporte', soma_t_ansup_funil, media_ansup_funil)

soma_t_ansis_funil = 0
for i in range (len(t_ansis_funil)):
  soma_t_ansis_funil = soma_t_ansis_funil + t_ansis_funil[i]
media_ansis_funil = soma_t_ansis_funil / len(t_ansis_funil)
# os prints foram usados para podermos visualizar a
# somatória total de cada cargo e suas respecitivas médias
# print('Terc_analista_sistemas', soma_t_ansis_funil, media_ansis_funil)


"""
Abaixo iremos criar um novo dataframe a partir dos dados que 
conseguimos com o código explicado acima
Usamos a biblioteca Pandas, com o seu comando pd.Dataframe 
Como funciona esse comando?
Aqui está um link para vocês darem uma olhada na documentação dele:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
Explicando: o comando pd.DataFrame pela sua documentação pede para, 
primeiro indicarmos nossa "data" o que seria isso? São os dados do 
dataframe que queremos criar, logo após ele pede um index, e o que 
seria isso? Index é, de acordo com a documentação é o nosso indice 
bem simples, nossas linhas
Isso é um indice:
1.
2.
3.
4.
Então passaremos um index para ele, dizendo quantas linhas temos no nosso dataframe, 
também podemos falar que indicaremos um indice para o nosso dataframe.
Pela documentação também pede o comando "columns" que é para especificar nossas colunas
Como usamos esses comandos que expliquei
Vocês podem ver que especifiquei uma variável "columns" certo? Dentro dela está 
['Cargo', 'Terceiro'] porque é o nome das colunas que queremos, poderiámos colocar 
qualquer nome nelas, então tentem trocar ai e coloque qualquer nome e vcs vão poder ver melhor.
Logo depois temos a variável "line" ela servirá para o nosso indice, o nosso index 
no comando pd.dataframe, dentro deles entre colchetes podemos ver que estão entre aspas 
vazias, pois eu quero só 4 linhas que não mostrem nada, experimentem colocar os numeros 
1, 2, 3 e 4 dentro dessas aspas e rodem o código vocês conseguiram entender melhor a lógica
logo após nós passamos a variável dados, para? Para usarmos no comando data que expliquei 
lá em cima, os dados são feitos da seguinte maneira, abrimos um colchetes e especificamos 
primeiro o nome ou o dado que será passado na nossa primeira coluna, como sabemos qual vai 
ser nossa primeira coluna? Olhem para a variável column a primeira, o primeiro nome que 
passamos é 'cargo', e o segundo terceiro, então vocês iram seguir essa ordem.
Exemplo:
Na primeira parte da nossa variável "dados" temos ['Analista de suporte', media_ansup] 
que serão atribuidads respecitvamentes para a coluna 'cargo' e 'terceiro'
"""

# criando um novo dataframe
# para terceirizado

column_funil = 'Cargo', 'Terceiro'
line_funil = '', '', '', ''
dados_funil = [['Analista de Suporte', media_ansup_funil], ['Programador', media_pro_funil]
         , ['Analista programador', media_anpro_funil], ['Analista de sistemas', media_ansis_funil]]
# tb_terceiro é o nome do nosso novo dataframe
tb_terceiro_funil = pd.DataFrame(data=dados_funil, index=line_funil, columns=column_funil)
#print(tb_terceiro_funil)

"""
A próxima célula usa a mesma lógica do terceiro lá de cima é igual creio 
que não precise de explicação
Mas se precisar é só olhar a primeira explicação que dei para o comando 
for dos terceiros lá em cima, só que aqui usamos para a o salários de clt
"""

# tratando os dados para calcular a soma e a media
# para o CLT
clt_programador_funil = programador_funil['CLT'].tolist()
clt_anpro_funil = anpro_funil['CLT'].tolist()
clt_ansup_funil =ansup_funil['CLT'].tolist()
clt_ansis_funil = ansis_funil['CLT'].tolist()

soma_clt_pro_funil = 0
for i in range (len(clt_programador_funil)):
  soma_clt_pro_funil = soma_clt_pro_funil + clt_programador_funil[i]
media_clt_pro_funil = soma_clt_pro_funil / len(clt_programador_funil)
#print('CLT_programador', soma_clt_pro_funil, media_clt_pro_funil)

soma_clt_anpro_funil = 0
for i in range (len(clt_anpro_funil)):
  soma_clt_anpro_funil = soma_clt_anpro_funil + clt_anpro_funil[i]
media_clt_anpro_funil = soma_clt_anpro_funil / len(clt_anpro_funil)
#print('CLT_analista_programador', soma_clt_anpro_funil, media_clt_anpro_funil)

soma_clt_ansup_funil = 0
for i in range (len(clt_ansup_funil)):
  soma_clt_ansup_funil = soma_clt_ansup_funil + clt_ansup_funil[i]
media_clt_ansup_funil = soma_clt_ansup_funil / len(clt_ansup_funil)
#print('CLT_analista_suporte', soma_clt_ansup_funil, media_clt_ansup_funil)

soma_clt_ansis_funil = 0
for i in range (len(clt_ansis_funil)):
  soma_clt_ansis_funil = soma_clt_ansis_funil + clt_ansis_funil[i]
media_clt_ansis_funil = soma_clt_ansis_funil / len(clt_ansis_funil)
#print('CLT_analista_sistemas', soma_clt_ansis_funil, media_clt_ansis_funil)

"""
A ideia de dataframe é a mesma de lá de cima
"""

# criando um novo dataframe
# para o CLT
column_funil = ['Cargo', 'CLT']
line_funil = ['', '', '', '']
dados_funil = [['Analista de Suporte', media_clt_ansup_funil], ['Programador', media_clt_pro_funil]
         , ['Analista programador', media_clt_anpro_funil], ['Analista de sistemas', media_clt_ansis_funil]]
# mesma lógica do dataframe do terceiro, porém para o clt
# só atribuimos o nome tb_clt para o nosso novo dataframe
tb_clt_funil = pd.DataFrame(data=dados_funil, index=line_funil, columns=column_funil)

#print(tb_clt_funil)

"""
# Criando nosso gráfico
Como criamos nosso gráfico? Primeiro a gente criou a variável "fig" lembrando ela 
poderia ser qualquer coisa,poderia ser "grafico" também, mas fig remete a figura né, 
creio que isso deu pra entender, dentro dela jogamos o comando da plotly.graph_objects, 
que é o go.Figure() e pra que ele serve? Para criar uma figura, só isso
Logo apos usamos o comando .add_trace, alguns podem estar se perguntando mas porque 
tem esse "fig" antes? Pq ele é a figura que iniciamos, então ai está dizendo que iremos 
adicionar um traço, um gráfico nessa figura.
Usamos o comando go.Funnel() para criar um gráfico de funil, de acordo com a documentação, 
passamos qual será o nome do nosso primeiro traço para ele ficar identificado no gráfico, 
ent colocamos name='Terceiro', no eixo y queremos os valores da tabela terceiro na coluna 
cargo, então fica tb_terceiro['Cargo'], já no eixo x queremos a mesma tabela mas na coluna 
Terciro assim ficando tb_terceiro['Terceiro']
Usamos a mesma lógica para criar um segundo traço, esse sendo usado os dados da tb_clt. 
É a mesma lógica
o .update_layout() é por pura estetica, só definimos um titulo e um background para o gráfico
O fig.show() é para mostrar o gráfico
"""

fig_funil = go.Figure()

fig_funil.add_trace(go.Funnel(name='Terceiro', y=tb_terceiro_funil['Cargo'], x=tb_terceiro_funil['Terceiro']))

fig_funil.add_trace(go.Funnel(name='CLT', y=tb_clt_funil['Cargo'], x=tb_clt_funil['CLT']))


fig_funil.update_layout(title='Comparação entre salários de contratados pela CLT e salários de terceirizados R$', template='plotly_dark')
# fig_funil.show()

# =============================================================================================
# =============================================================================================
# Grafico de mapa - Medias salarias G12
# =============================================================================================
# =============================================================================================


"""
# Criando as listas para receber os dados do gráfico
"""
# vetor que receberá as médias salariais
s_av_mapa =[]
# vetor para receber o nome do país
country_mapa = []

"""
# Explicando a tabela
Essa tabela mostra os salários mundiais dos profissionais de TI por país
Os valores nas Tabelas estão em dólares
"""

#Criando dataframe através da leitura da planilha em excel
#df_mapa = pd.read_excel('https://raw.githubusercontent.com/TrabalhoAPC2021-02/Trabalho_Final/main/arquivos/01_Data_Professional_full.xlsx')
df_mapa = pd.read_excel('01_Data_Professional_full.xlsx')
#df_mapa.head() # mostra apenas as primeiras linhas do dataframe

"""
# Lógica utilizada
Para os maiores doze países foi calculada a média salarial e cada valor 
foi adicionado ("append") nas listas criadas no início do código
Essa lógica foi repetida para cada país separadamente
"""

#Selecionando os dados dos USA com slários de 2017 a 2021

df_usa_mapa = df_mapa[df_mapa['Country'] == 'United States'] #Esse dataframe escolhe os dados apenas dos USA
salary_usa_mapa = df_usa_mapa['SalaryUSD'].tolist() # tranformando o dataframe dos usa  com salarios de 2017 a 2021 em lista para poder usar laços iterativos.

#utilização de um laço for para calcular média dos salários dos USA

soma_sal_usa_mapa = 0   # contador = 0, para somar todos os salários declarados referente aos USA

for i in range (len(salary_usa_mapa)):  # o laço vai percorrer todas as linhas refernte aos USA
    soma_sal_usa_mapa = soma_sal_usa_mapa + salary_usa_mapa[i]  # Aqui o contador vai começar a acmular linha por linha cada salário declarado
av_usa_mapa = soma_sal_usa_mapa / len(salary_usa_mapa) #fora do laço a variável av_usa recebe a média dos salários, onde divide o salário acumulado pela quantidade de salários declarados

s_av_mapa.append(av_usa_mapa)    # recebendo a media salarial na lista s_av (anteriormente vazia)
country_mapa.append('USA')  # recebendo o código do país na lista s_av (anteriormente vazia)

#Selecionando os dados dq China com slários de 2017 a 2021

df_china_mapa = df_mapa[df_mapa['Country'] == 'China']
salary_china_mapa = df_china_mapa['SalaryUSD'].tolist() # tranformando o dataframe da china com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários da china

soma_sal_china_mapa = 0

for i in range (len(salary_china_mapa)):
    soma_sal_china_mapa = soma_sal_china_mapa + salary_china_mapa[i]
av_china_mapa = soma_sal_china_mapa / len(salary_china_mapa)
s_av_mapa.append(av_china_mapa)
country_mapa.append('CHN')

#Selecionando os dados da Alemanha com slários de 2017 a 2021

df_alemanha_mapa = df_mapa[df_mapa['Country'] == 'Germany']
salary_alemanha_mapa = df_alemanha_mapa['SalaryUSD'].tolist() # tranformando o dataframe da Alemanha com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários da Alemanha

soma_sal_alemanha_mapa = 0

for i in range (len(salary_alemanha_mapa)):
    soma_sal_alemanha_mapa = soma_sal_alemanha_mapa + salary_alemanha_mapa[i]
av_alemanha_mapa = soma_sal_alemanha_mapa / len(salary_alemanha_mapa)
s_av_mapa.append(av_alemanha_mapa)
country_mapa.append('DEU')

#Selecionando os dados do Reino unido com slários de 2017 a 2021

df_uk_mapa = df_mapa[df_mapa['Country'] == 'United Kingdom']
salary_uk_mapa = df_uk_mapa['SalaryUSD'].tolist() # tranformando o dataframe do reino unido com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários do Reino Unido.

soma_sal_uk_mapa = 0

for i in range (len(salary_uk_mapa)):
    soma_sal_uk_mapa = soma_sal_uk_mapa + salary_uk_mapa[i]
av_uk_mapa = soma_sal_uk_mapa / len(salary_uk_mapa)
s_av_mapa.append(av_uk_mapa)
country_mapa.append('GBR')

#Selecionando os dados da Índia com slários de 2017 a 2021

df_india_mapa = df_mapa[df_mapa['Country'] == 'India']
salary_india_mapa = df_india_mapa['SalaryUSD'].tolist() # tranformando o dataframe da India com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários da India.

soma_sal_india_mapa = 0

for i in range (len(salary_india_mapa)):
    soma_sal_india_mapa = soma_sal_india_mapa + salary_india_mapa[i]
av_india_mapa = soma_sal_india_mapa / len(salary_india_mapa)
s_av_mapa.append(av_india_mapa)
country_mapa.append('IND')

#Selecionando os dados da França com slários de 2017 a 2021

df_france_mapa = df_mapa[df_mapa['Country'] == 'France']
salary_france_mapa = df_france_mapa['SalaryUSD'].tolist() # tranformando o dataframe da França com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários da França.

soma_sal_france_mapa = 0

for i in range (len(salary_france_mapa)):
    soma_sal_france_mapa = soma_sal_france_mapa + salary_france_mapa[i]
av_france_mapa = soma_sal_france_mapa / len(salary_france_mapa)
s_av_mapa.append(av_france_mapa)
country_mapa.append('FRA')

#Selecionando os dados da Itália com slários de 2017 a 2021

df_italia_mapa = df_mapa[df_mapa['Country'] == 'Italy']
salary_italia_mapa = df_italia_mapa['SalaryUSD'].tolist() # tranformando o dataframe da Itália com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários da Itália.

soma_sal_italia_mapa = 0

for i in range (len(salary_italia_mapa)):
    soma_sal_italia_mapa = soma_sal_italia_mapa + salary_italia_mapa[i]
av_italia_mapa = soma_sal_italia_mapa / len(salary_italia_mapa)
s_av_mapa.append(av_italia_mapa)
country_mapa.append('ITA')

#Selecionando os dados da Canadá com slários de 2017 a 2021

df_canada_mapa = df_mapa[df_mapa['Country'] == 'Canada']
salary_canada_mapa = df_canada_mapa['SalaryUSD'].tolist() # tranformando o dataframe do Canadá com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários do Canadá.

soma_sal_canada_mapa = 0

for i in range (len(salary_canada_mapa)):
    soma_sal_canada_mapa = soma_sal_canada_mapa + salary_canada_mapa[i]
av_canada_mapa = soma_sal_canada_mapa / len(salary_canada_mapa)
s_av_mapa.append(av_canada_mapa)
country_mapa.append('CAN')

#Selecionando os dados da Russia com slários de 2017 a 2021

df_russia_mapa = df_mapa[df_mapa['Country'] == 'Russia']
salary_russia_mapa = df_russia_mapa['SalaryUSD'].tolist() # tranformando o dataframe do Russia com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários do Russia.

soma_sal_russia_mapa = 0

for i in range (len(salary_russia_mapa)):
    soma_sal_russia_mapa = soma_sal_russia_mapa + salary_russia_mapa[i]
av_russia_mapa = soma_sal_russia_mapa / len(salary_russia_mapa)
s_av_mapa.append(av_russia_mapa)
country_mapa.append('RUS')

#Selecionando os dados do Brasil com slários de 2017 a 2021

df_br_mapa = df_mapa[df_mapa['Country'] == 'Brazil']
salary_br_mapa = df_br_mapa['SalaryUSD'].tolist() # tranformando o dataframe do Brasil com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários do Brasil.

soma_sal_br_mapa = 0

for i in range (len(salary_br_mapa)):
    soma_sal_br_mapa = soma_sal_br_mapa + salary_br_mapa[i]
av_br_mapa = soma_sal_br_mapa / len(salary_br_mapa)
s_av_mapa.append(av_br_mapa)
country_mapa.append('BRA')

#Selecionando os dados da Austrália com slários de 2017 a 2021

df_australia_mapa = df_mapa[df_mapa['Country'] == 'Australia']
salary_australia_mapa = df_australia_mapa['SalaryUSD'].tolist() # tranformando o dataframe do Austrália com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários da Austrália.

soma_sal_australia_mapa = 0

for i in range (len(salary_australia_mapa)):
    soma_sal_australia_mapa = soma_sal_australia_mapa + salary_australia_mapa[i]
av_australia_mapa = soma_sal_australia_mapa / len(salary_australia_mapa)
s_av_mapa.append(av_australia_mapa)
country_mapa.append('AUS')

#Selecionando os dados da Africa do sul com slários de 2017 a 2021

df_africasul_mapa = df_mapa[df_mapa['Country'] == 'South Africa']
salary_africasul_mapa = df_africasul_mapa['SalaryUSD'].tolist() # tranformando o dataframe da Africa do Sul com salarios de 2017 a 2021 em lista.

#utilização de um laço for para calcular média dos salários da africa do sul.

soma_sal_africasul_mapa = 0

for i in range (len(salary_africasul_mapa)):
    soma_sal_africasul_mapa = soma_sal_africasul_mapa + salary_africasul_mapa[i]
av_africasul_mapa = soma_sal_africasul_mapa / len(salary_africasul_mapa)
s_av_mapa.append(av_africasul_mapa)
country_mapa.append('ZAF')

#print(s_av_mapa)    # mostra como ficou a lista que recebe as médias salariais
#print(country_mapa)  # mostra como ficou a lista que recebe os códigos dos países.

"""
# Vamos criar dois gráficos com os mesmos dados, um de barra e outro através de um mapa mundi. 
Ambos os gráficos utilizam a bblioteca do plotly express e mostram a média saalrial de cada país.
"""

#Método para criar o gráfico de barra. através da combinação das listas s_av e country.
#fig_mapa = px.bar(x=country_mapa, y=s_av_mapa, title='Average')  # no eeixo x ploto os nomes dos países, no eixo y a média salarial
#fig_mapa.update_xaxes(title='Country') #título do eixo x
#fig_mapa.update_yaxes(title='Average annual salary [USD]') #título do eixo y
#fig_mapa.show()  # mostra o gráfico de barras

"""
# Gráfico de dispersão geográfica
zip ????
locations = codigos das coordenadas dos países
size = "ajusta" o tamanho da bolinha de acordo com o valor da média salarial,
maiores salários, maiores bolinhas.
projection = tipo de mapa mundi
"""

#Criando o gráfico através do mapa mundi.
#estrutura para criar um dataframe tendo duas listas, s_av (media salarial) e country (código dos países)
df_sv_mapa = pd.DataFrame(list(zip(country_mapa, s_av_mapa)), columns = ['Country', 'Average annual salary [USD]'])
#print(df_sv_mapa)  #print do dataframe

# para esse utiliza a função scatter_geo do plotely express. Os países ficam alocados em location, e a média salarial em size.
fig_mapa = px.scatter_geo(df_sv_mapa, locations='Country', size='Average annual salary [USD]', color=country_mapa, projection="natural earth", title='Média de salário anual dos profissionais de TI dos paises do G12*')
#fig_mapa.show()


# =============================================================================================
# =============================================================================================
# Colocando os graficos no dash
# =============================================================================================
# =============================================================================================


# criar o aplicativo do flask
# inicializacao do aplicativo
app = Dash(__name__)

# atualizando o layout do aplicativo flask
app.layout = html.Div(children=[
        html.H1(children='Gráfico de pizza'),
        html.Div(children='As 15 linguagens de programação mais usadas no ano de '),
        dcc.Graph(
            id='grafico-pizza',
            figure=fig_pizza
        ),
        html.H1(children='Gráfico de linha'),
        html.Div(children='Evolução do uso da linguagem Python nos últimos 17 anos'),
        dcc.Graph(
            id='grafico-linha',
            figure=fig_linha
        ),
        html.H1(children='Gráfico de barra'),
        html.Div(children='Distribuição entre homens e mulheres contratados pelas principais empresas de tecnologia'),
        dcc.Graph(
            id='grafico-barra',
            figure=fig_barra
        ),
        html.H1(children='Gráfico de funil'),
        html.Div(children='Comparação entre salários de contratados pela CLT e salários de terceirizados R$'),
        dcc.Graph(
            id='grafico-funil',
            figure=fig_funil
        ),
        html.H1(children='Gráfico de mapa'),
        html.Div(children='Media Salarial do G12'),
        dcc.Graph(
            id='grafico-mapa',
            figure=fig_mapa
        )
    ])

if __name__ == '__main__':
    # colocando o aplicativo no ar (servidor local)
    app.run_server(debug=True)

