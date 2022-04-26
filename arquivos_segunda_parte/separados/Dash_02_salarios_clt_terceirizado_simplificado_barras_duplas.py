# Importanto as bibliotecas
import pandas as pd # importando a biblioteca pandas para leitura de dados
import plotly.graph_objects as go # biblioteca que usaremos para criar os gráficos
from dash import Dash, html, dcc

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

# criar o aplicativo do flask
# inicializacao do aplicativo
app_funil = Dash(__name__)

# atualizando o layout do aplicativo flask
app_funil.layout = html.Div(children=[
    html.H1(children='Gráfico de funil'),

    html.Div(children='Comparação entre salários de contratados pela CLT e salários de terceirizados R$'),

    dcc.Graph(
        id='grafico-funil',
        figure=fig_funil
    )
])

if __name__ == '__main__':
    # colocando o aplicativo no ar (servidor local)
    app_funil.run_server(debug=True)