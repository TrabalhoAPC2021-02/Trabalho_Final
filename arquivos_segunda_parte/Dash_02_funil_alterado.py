# Importanto as bibliotecas
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
import plotly.graph_objects as go # biblioteca que usaremos para criar os gráficos


# funcao que gera o grafico
def funcao_funil_gerargrafico(dataframe, lista_cargos):
    # cria as listas que vao receber os valores calculados
    lista_cargo = []
    lista_media_t = []
    lista_media_clt = []
    # para cada cargo que consta na lista, chama a funcao de calcular a media
    for x in lista_cargos:
        cargo, media_t, media_clt = funcao_funil_media(dataframe, x)
        lista_cargo.append(cargo)
        lista_media_t.append(media_t)
        lista_media_clt.append(media_clt)
    # cria os dataframes com as medias calaculadas
    tb_terceiro_funil = pd.DataFrame(list(zip(lista_cargo, lista_media_t)), columns=['Cargo', 'Terceiro'])
    tb_clt_funil = pd.DataFrame(list(zip(lista_cargo, lista_media_clt)), columns=['Cargo', 'CLT'])
    # cria os dataframes ordenado para usar no grafico
    tb_terceiro_ordenado = tb_terceiro_funil.sort_values(by=['Terceiro'], ascending=False)
    tb_clt_ordenado = tb_clt_funil.sort_values(by=['CLT'], ascending=False)
    # gera o grafico
    figura_funil = go.Figure()
    figura_funil.add_trace(go.Funnel(name='Terceiro', y=tb_terceiro_ordenado['Cargo'], x=tb_terceiro_ordenado['Terceiro']))
    figura_funil.add_trace(go.Funnel(name='CLT', y=tb_clt_ordenado['Cargo'], x=tb_clt_ordenado['CLT']))
    figura_funil.update_layout(template='plotly_dark')
    # retorna o grafico
    return figura_funil


# recebe como parametro a base de dados e o cargo que vai ser calculado
def funcao_funil_media(dataframe, cargo):
    # filtra a base de dados so com o cargo em questao
    cargo_funil = dataframe[dataframe['Cargo'] == cargo]
    # transforma a coluna "Terceiro" em uma lista
    t_cargo_funil = cargo_funil['Terceiro'].tolist()  # comando .tolist() usado para transformar a coluna numa lista
    # acumula a soma dos salarios de terceirizados
    soma_t_cargo_funil = 0
    for i in range(len(t_cargo_funil)):
        soma_t_cargo_funil = soma_t_cargo_funil + t_cargo_funil[i]
    # calcula a media dos salarios de terceirizados - se tiver valores
    if len(t_cargo_funil) == 0:
        media_t_cargo_funil = 0
    else:
        media_t_cargo_funil = soma_t_cargo_funil / len(t_cargo_funil)
    # faz tudo de novo para CLT
    # transforma a coluna "CLT" em uma lista
    clt_cargo_funil = cargo_funil['CLT'].tolist()
    # acumula a soma dos salarios de CLT
    soma_clt_cargo_funil = 0
    for i in range(len(clt_cargo_funil)):
        soma_clt_cargo_funil = soma_clt_cargo_funil + clt_cargo_funil[i]
    # calcula a media dos salarios de CLT - se tiver valores
    if len(clt_cargo_funil) == 0:
        media_clt_cargo_funil = 0
    else:
        media_clt_cargo_funil = soma_clt_cargo_funil / len(clt_cargo_funil)
    # retorna o calculo da media CLT e da media Terceirizado do cargo especifico
    return cargo, media_t_cargo_funil, media_clt_cargo_funil

