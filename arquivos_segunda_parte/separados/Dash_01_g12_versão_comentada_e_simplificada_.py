# Importanto as bibliotecas
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
import plotly.express as px # biclioteca responsável por plotar os gráficos
from dash import Dash, html, dcc

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

# criar o aplicativo do flask
# inicializacao do aplicativo
app_mapa = Dash(__name__)

# atualizando o layout do aplicativo flask
app_mapa.layout = html.Div(children=[
    html.H1(children='Gráfico de mapa'),

    html.Div(children='Media Salarial do G12'),

    dcc.Graph(
        id='grafico-mapa',
        figure=fig_mapa
    )
])

if __name__ == '__main__':
    # colocando o aplicativo no ar (servidor local)
    app_mapa.run_server(debug=True)