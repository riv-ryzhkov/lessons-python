# pip install plotly
# pip install matplotlib
# pip install pandas
# pip install numpy


import plotly
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd
import json


x = np.arange(-1, 1, 0.2)
# print(x, type(x))
# print(*dir(x), sep='\n')
# x1 = list(x)
# print(x1, type(x1))


def f(x):
    return x**2


def h(x):
    return np.sin(x)


def k(x):
    return np.cos(x)


def m(x):
    return np.tan(x)




#========================================== Простой график 1 и 2 функций
# fig = go.Figure()
# print(*dir(fig), sep='\n')
# print(fig.to_dict())
#
#
# print(json.dumps(fig.to_dict(), indent=4))
# print('='*80)
#
# print(fig.to_dict()['data'])
# print('='*80)
#
# fig.add_trace(go.Scatter(x=x, y=f(x)))
# fig.add_trace(go.Scatter(x=x, y=5*x))
# fig.add_trace(go.Scatter(x=x, y=-4*x))
# #
# print(fig.to_dict()['data'])
# #
# fig.show()

#==================================== Легенда и подписи осей
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=f(x), name='<b>f(x)=x<sup>2</sup></b>'))
# fig.add_trace(go.Scatter(x=x, y=x, name='g(x)=x'))
# # fig.update_layout(legend_orientation="h")
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   title="<b>Plot Title<b>",
#                   xaxis_title="<b>x Axis Title</b>",
#                   yaxis_title="<b><i>y Axis Title</i></b>",
#                   margin=dict(l=100, r=100, t=100, b=100))
# fig.show()
#============================ Маркеры и подписи к данным

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'))
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x'))
# fig.update_layout(legend_orientation="h",
#                   hovermode="x",
#                   # hovermode="x unified",
#                   legend=dict(x=.5, xanchor="center"),
#                   margin=dict(l=50, r=50, t=50, b=50))
# # fig.update_traces(hoverinfo="x+y")
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#============== Управление маркерами, масштаб фрагмента, добавление графиков

# fig = go.Figure()
# # # Масштабирование
# # fig.update_yaxes(range=[-0.5, 1.5])
# # fig.update_xaxes(range=[-0.5, 1.5])
# fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=5, zerolinecolor='Red')
# fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=5, zerolinecolor='#00ff00') # RGB
# # #
# # # # Добавление графиков (нужно включить)
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=h(x),  name='h(x)=sin(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=k(x),  name='k(x)=cos(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=m(x),  name='m(x)=tg(x)'))
# # #
# # #
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'))
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='Red', size=20, line=dict(color='MediumPurple', width=3))))
#
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#============== Несколько графиков

# # fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"))
# fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"), column_widths=[2, 1])
# # #
# fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='#008000', col=2)
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightGreen', col=1)
# fig.update_xaxes(range=[-2, 2], zeroline=True, zerolinewidth=2, zerolinecolor='#000080', col=1)
# # #
# # #
# fig.add_trace(go.Scatter(x=x, y=h(x),  name='h(x)=sin(x)'), 1, 1)
# fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'), 1, 1)
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=m(x),  name='m(x)=tg(x)'), 1, 1)
#
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 1, 2)
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='LightSkyBlue', size=20, line=dict(color='MediumPurple', width=3))), 1, 2)
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   hovermode="x",
#                   margin=dict(l=50, r=50, t=50, b=50))
# fig.update_layout(title="Plot Title")
# fig.update_xaxes(title='Ось X графика 1', row=1, col=1)
# fig.update_xaxes(title='Ось X графика 2', col=2, row=1)
# fig.update_yaxes(title='Ось Y графика 1', col=1, row=1)
# fig.update_yaxes(title='Ось Y графика 2', col=2, row=1)
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#========== Разные размеры графиков и функций (столбец)
# fig = make_subplots(rows=3, cols=2,
#                     specs=[[{"rowspan": 3}, {}], [None, {}], [None, {}]])
# # # # Объединяет "секции" матрицы графиков и "подавляет" графики
# # #
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-2, 2], zeroline=True, zerolinewidth=2, zerolinecolor='#008000', col=2)
# #
# fig.add_trace(go.Scatter(x=x, y=h(x),  name='h(x)=sin(x)'), 2, 2)
# fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'), 3, 2)
# fig.add_trace(go.Scatter(x=x, y=m(x),  name='m(x)=tg(x)'), 1, 1)
# # #
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 1, 2)
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='LightSkyBlue', size=10, line=dict(color='MediumPurple', width=3))), 1, 2)
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   hovermode="x",
#                   # hovermode="x unified",
#                   margin=dict(l=50, r=50, t=50, b=50))
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#========== Разные размеры графиков и функций (строка)
# x = np.arange(-5, 10, 0.2)
# fig = make_subplots(rows=2, cols=3,
#                     specs=[[{"colspan": 3}, None, None], [{}, {}, {}]])
#
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='#008000', col=2)
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=3)
# fig.update_xaxes(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='#25f3aa', col=3) # 000000 ffffff
# #
# fig.add_trace(go.Scatter(x=x, y=h(x),  name='h(x)=sin(x)'), 2, 2)
# fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'), 2, 3)
# fig.add_trace(go.Scatter(x=x, y=m(x),  name='m(x)=tg(x)'), 1, 1)
# #
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 2, 1)
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='LightSkyBlue', size=5, line=dict(color='MediumPurple', width=2))), 2, 1)
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   hovermode="x",
#                   margin=dict(l=40, r=40, t=40, b=40),
#                   # height=1500,
#                   # width=1600
#                   )
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()


#========Тепловая карта
# aggrnyl     agsunset    blackbody   bluered     blues       blugrn      bluyl       brwnyl
# bugn        bupu        burg        burgyl      cividis     darkmint    electric    emrld
# gnbu        greens      greys       hot         inferno     jet         magenta     magma
# mint        orrd        oranges     oryel       peach       pinkyl      plasma      plotly3
# pubu        pubugn      purd        purp        purples     purpor      rainbow     rdbu
# rdpu        redor       reds        sunset      sunsetdark  teal        tealgrn     turbo
# viridis     ylgn        ylgnbu      ylorbr      ylorrd      algae       amp         deep
# dense       gray        haline      ice         matter      solar       speed       tempo
# thermal     turbid      armyrose    brbg        earth       fall        geyser      prgn
# piyg        picnic      portland    puor        rdgy        rdylbu      rdylgn      spectral
# tealrose    temps       tropic      balance     curl        delta       oxy         edge
# hsv         icefire     phase       twilight    mrybm       mygbm



# x = np.arange(-5, 10, 0.3)
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>',
#                          marker=dict(color=h(x), colorbar=dict(title="h(x)=sin(x)"),
#                                      colorscale='Inferno',
#                                      # colorscale='Oryel',
#                                      # colorscale='earth',
#                                      size=50 * abs(h(x))
#                                      )
#                         ))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=h(x),  name='h(x)=sin(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=k(x),  name='k(x)=cos(x)'))
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   margin=dict(l=30, r=30, t=30, b=30))
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#========= Анимация 1
x = np.arange(-7, 15, 0.2)
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=[x[0]], y=[f(x)[0]], mode='lines+markers',  name='f(x)=x<sup>2</sup>',
#                          marker=dict(color=h(x[0]), colorbar=dict(title="h(x)=sin(x)"), colorscale='Inferno', size=50*abs(h(x[0])))
#                         ))
#
# frames = []
# for i in range(1, len(x)):
#     frames.append(go.Frame(data=[go.Scatter(x=x[:i+1], y=f(x[:i+1]), marker=dict(color=h(x[:i+1]), size=50*abs(h(x[:i+1]))))]))
#
# fig.frames = frames
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   updatemenus=[dict(type="buttons", buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
#                                                              dict(label="❚❚", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False},
#                                                                                                                "mode": "immediate",
#                                                                                                                "transition": {"duration": 0}}])])],
#                   margin=dict(l=0, r=0, t=0, b=0))
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()
#========= Анимация 2
# num_steps = len(x)
# fig = go.Figure(data=[go.Scatter(x=[x[0]], y=[h(x)[0]], mode='lines+markers', name='h(x)=sin(x)',
#                                  marker=dict(color=[f(x[0])], colorbar=dict(yanchor='top', y=0.8, title="f(x)=x<sup>2</sup>"), colorscale='Inferno', size=[50*abs(h(x[0]))])),
#                       go.Scatter(x=[x[0]], y=[k(x)[0]], mode='lines+markers', name='k(x)=cos(x)',
#                                  marker=dict(color=[f(x[0])], colorscale='Inferno', size=[50*abs(k(x[0]))]))])
#
# frames=[]
# for i in range(0, len(x)):
#     frames.append(go.Frame(name=str(i),
#                            data=[go.Scatter(x=x[:i+1], y=h(x[:i+1]), mode='lines+markers', name='h(x)=sin(x)',
#                                             marker=dict(color=f(x[:i+1]), colorscale='Inferno', size=50*abs(h(x[:i+1])))),
#                                  go.Scatter(x=x[:i+1], y=k(x[:i+1]), mode='lines+markers', name='k(x)=cos(x)',
#                                             marker=dict(color=f(x[:i+1]), colorscale='Inferno', size=50*abs(k(x[:i+1]))))]))
#
# steps = []
# for i in range(num_steps):
#     step = dict(
#         label = str(i),
#         method = "animate",
#         args = [[str(i)]]
#     )
#     steps.append(step)
#
# sliders = [dict(
#     steps = steps,
# )]
#
# fig.update_layout(updatemenus=[dict(direction="left",
#                                     x=0.5,
#                                     xanchor="center",
#                                     y=0,
#                                     showactive=False,
#                                     type="buttons",
#                                     buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
#                                              dict(label="❚❚", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False},
#                                                                                                "mode": "immediate",
#                                                                                                "transition": {"duration": 0}}])])],
#                   )
#
#
# fig.layout.sliders = sliders
# fig.frames = frames
#
# fig.show()

#================ Диаграммы (круговая)
# dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(10000, 2)), columns=('Кость 1', 'Кость 2'))
# #
# dices['Сумма'] = dices['Кость 1'] + dices['Кость 2']
# # # Первые 5 бросков игральных костей
# # # display(dices.head())
# # print(dices.head())
# # print('====== Статистика ===========')
# #
# sum_counts = dices['Сумма'].value_counts().sort_index()
# # # количество выпавших сумм
# # # display(sum_counts)
# # print(sum_counts)
# #
# fig = go.Figure()
# pull = [0]*len(sum_counts)
# # print(pull)
#
# # fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, sort=False))
#
# pull[sum_counts.tolist().index(sum_counts.max())] = 0.2 # Сдвиг
# # fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, sort=False, pull=pull))
# fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, sort=False, pull=pull, hole=0.5))
# fig.update_layout(
#     title="Пример кольцевой/круговой диаграммы",
#     title_x=0.5,
#     margin=dict(l=0, r=0, t=30, b=0),
#     legend_orientation="h",
#     annotations=[dict(text='Суммы очков<br>при броске<br>2 игральных костей', x=0.5, y=0.5, font_size=20, showarrow=False)])
# fig.show()

#========= Диаграмма "Солнечные лучи"

# dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(100000, 2)), columns=('Кость 1', 'Кость 2'))
# dices['Сумма'] = dices['Кость 1'] + dices['Кость 2']
# sum_counts = dices['Сумма'].value_counts().sort_index()
sum_counts = 3
level2_count = 8


# 1-й уровень, центр диаграммы
# labels = ["Діяльність\nЦентру\nфранкомовних\nпрограм"]
labels = ["<b>Центр<br>франкомовних<br>програм</b>"]
parents = ['']
values = [level2_count * 2]
# 2-й уровень, "промежуточный"
# second_level_dict = {x:'Событий: ' + str(sum_counts[x]) + '<br>Σ = ' + str(x) for x in sum_counts.index}
# labels += map(lambda x: second_level_dict[x], sum_counts.index)
labels += [
    'Міжнародне<br>партнерство',
    'AUF',
    'Гранти',
    'Медійні ресурси',
    'Мовна підготовка',
    'Профорієнтеція',
    'Стажування',
    'Курси'
]
# parents += [labels[0]]*len(sum_counts)
parents += [labels[0]]*level2_count
# values += sum_counts.tolist()
values += [2]*level2_count
#
# # Готовим DataFrame для 3 уровня (группируем )
# third_level = dices.groupby(['Кость 1', 'Кость 2']).count().reset_index()
third_level = {}
# third_level.rename(columns={'Сумма':'Value'}, inplace=True)
# third_level['Сумма'] = third_level['Кость 1'] + third_level['Кость 2']
# third_level['Сумма'] =
# third_level['Label'] = third_level['Кость 1'].map(str) + ' + ' + third_level['Кость 2'].map(str)
third_level['Label'] = [
    'Міжнародне<br>партнерство',
    'AUF',
    'Гранти',
    'Медійні ресурси',
    'Мовна підготовка',
    'Профорієнтеція',
    'Стажування',
    'Курси'
]
# third_level['Parent'] = third_level['Сумма'].map(lambda x: second_level_dict[x])
third_level['Parent'] = third_level['Label']
# # 3-й уровень, "лепестки" диаграммы
# values += third_level['Value'].tolist()
# parents += third_level['Parent'].tolist()
# labels += third_level['Label'].tolist()
labels += third_level['Label']
# parents += [labels[0]]*len(sum_counts)
parents += [labels[0]]*level2_count*2
# parents += third_level['Parent']
# values += sum_counts.tolist()
values += [2]*level2_count*2




fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total"
))
fig.update_layout(margin=dict(t=30, l=30, r=30, b=30))

fig.show()

#============== Диаграмма "Гистограмма"
# #
# dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(100, 2)), columns=('Кость 1', 'Кость 2'))
# dices['Сумма'] = dices['Кость 1'] + dices['Кость 2']
#
# dices2 = pd.DataFrame(np.random.randint(low=1, high=7, size=(100, 2)), columns=('Кость 1', 'Кость 2'))
# dices2['Сумма'] = dices2['Кость 1'] + dices2['Кость 2']
#
# dices3 = pd.DataFrame(np.random.randint(low=1, high=7, size=(1000, 2)), columns=('Кость 1', 'Кость 2'))
# dices3['Сумма'] = dices3['Кость 1'] + dices3['Кость 2']
#
#
# fig = go.Figure()
#
# fig.add_trace(go.Histogram(x=dices['Сумма'], histnorm='probability density', name='100 бросков v.1'))
# fig.add_trace(go.Histogram(x=dices2['Сумма'], histnorm='probability density', name='100 бросков v.2'))
# fig.add_trace(go.Histogram(x=dices3['Сумма'], histnorm='probability density', name='1000 бросков'))
#
# fig.update_layout(
#     title="Пример гистограммы на основе бросков пары игральных костей",
#     title_x=0.5,
#     xaxis_title="<b>сумма очков</b>",
#     yaxis_title="<b>Плотность вероятности</b>",
#     legend=dict(x=.5, xanchor="center", orientation="h"),
#     margin=dict(l=30, r=30, t=30, b=30))
#
# fig.show()




#  END !!!!!





#========== ??????????????????????? Map Rail (((((((((
# def to_int_year(value):
#     try:
#         return int(value)
#     except:
#         return None
#
# def to_int_size(value):
#     try:
#         return np.log10(int(value))
#     except:
#         return np.log10(int(value.split('[')[0]))
#
#
#
# # ========= 1
# fig = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))
# fig.update_layout(mapbox_style="open-street-map")
# fig.show()

#========== 2
# fig = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))
# capital = cities[cities['region']=='Москва']
# map_center = go.layout.mapbox.Center(lat=capital['geo_lat'].values[0], lon=capital['geo_lon'].values[0])
# fig.update_layout(mapbox_style="open-street-map",
#                   mapbox=dict(center=map_center, zoom=2))
# fig.show()


#======= Map
# train_russia = pd.read_csv('https://gist.githubusercontent.com/lexnekr/2da07b5fc12b5be24068e4d68ed47ca5/raw/d6256765a3223282fbfec7e0b040cbfb21593fff/train_russia.scv')
#
# fig = go.Figure(go.Scattermapbox(legendgroup="group",
#                                  name='Города России',
#                                  lat=cities['geo_lat'],
#                                  lon=cities['geo_lon'],
#                                  text=cities['city'],
#                                  marker=dict(colorbar=dict(title="Год основания"),
#                                              color=cities['foundation_year'].map(to_int_year),
#                                              size=cities['population'].map(to_int_size))))
#
# for df_for_today in train_russia.groupby(['day number']):
#     fig.add_trace(go.Scattermapbox(name='День {}'.format(df_for_today[0]),
#                                    mode = "lines",
#                                    hoverinfo='skip',
#                                    lat=df_for_today[1]['geo_lat'],
#                                    lon=df_for_today[1]['geo_lon']))
#
# map_center = go.layout.mapbox.Center(lat=(cities['geo_lat'].max()+cities['geo_lat'].min())/2,
#                                      lon=(cities['geo_lon'].max()+cities['geo_lon'].min())/2)
# fig.update_layout(title='По России на поезде',
#                   legend_orientation="h",
#                   mapbox_style="open-street-map",
#                   mapbox=dict(center=map_center, zoom=2))
#
# fig.show()



#========= Animation

# cities = pd.read_csv('https://raw.githubusercontent.com/hflabs/city/master/city.csv')
# train_russia = pd.read_csv('https://gist.githubusercontent.com/lexnekr/2da07b5fc12b5be24068e4d68ed47ca5/raw/d6256765a3223282fbfec7e0b040cbfb21593fff/train_russia.scv')
# #
#
# data = [go.Scattermapbox(legendgroup="group",
#                          name='Города России',
#                          lat=cities['geo_lat'],
#                          lon=cities['geo_lon'],
#                          text=cities['city'],
#                          marker=dict(colorbar=dict(title="Год основания"),
#                                      color=cities['foundation_year'].map(to_int_year),
#                                      size=cities['population'].map(to_int_size)))]
# for df_for_today in train_russia.groupby(['day number']):
#     data.append(go.Scattermapbox(visible=False,
#                                  name='День {}'.format(df_for_today[0]),
#                                  mode="lines",
#                                  hoverinfo='skip',
#                                  lat=df_for_today[1]['geo_lat'],
#                                  lon=df_for_today[1]['geo_lon']))
#
# fig = go.Figure(data)
#
# frames = []
# for i in range(len(data) + 1):
#     temp_frame = go.Frame(name=str(i), data=data)
#
#     for j in range(1, i):
#         temp_frame['data'][j]['visible'] = True
#
#     frames.append(temp_frame)
#
# steps = []
# for i in range(len(data)):
#     step = dict(
#         label=str(i),
#         method="animate",
#         args=[[str(i + 1)]]
#     )
#     steps.append(step)
#
# sliders = [dict(
#     currentvalue={"prefix": "День №", "font": {"size": 20}},
#     len=0.9,
#     x=0.1,
#     pad={"b": 10, "t": 50},
#     steps=steps,
# )]
#
# map_center = go.layout.mapbox.Center(lat=(cities['geo_lat'].max() + cities['geo_lat'].min()) / 2,
#                                      lon=(cities['geo_lon'].max() + cities['geo_lon'].min()) / 2)
# fig.update_layout(title='По России на поезде',
#                   legend_orientation="h",
#                   mapbox_style="open-street-map",
#                   mapbox=dict(center=map_center, zoom=2),
#                   updatemenus=[dict(direction="left",
#                                     pad={"r": 10, "t": 80},
#                                     x=0.1,
#                                     xanchor="right",
#                                     y=0,
#                                     yanchor="top",
#                                     showactive=False,
#                                     type="buttons",
#                                     buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
#                                              dict(label="❚❚", method="animate",
#                                                   args=[[None], {"frame": {"duration": 0, "redraw": False},
#                                                                  "mode": "immediate",
#                                                                  "transition": {"duration": 0}}])])],
#                   )
#
# fig.layout.sliders = sliders
# fig.frames = frames
#
# fig.show()





