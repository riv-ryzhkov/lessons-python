# import dash
# from dash import dcc
# from dash import html
# import plotly.express as px
# import pandas as pd
#
# #---------------------------------------------------------------------------------------
# #КЛАСС ДЛЯ ПОИСКА СЛОВ С ПОЗИТИВНОЙ ТОНАЛЬНОСТЬЮ(создается ссылка на график)
# #!!!перед запуском этого класса, надо остановить ВСЕ остальные!!!
#
# '''
#     Модуль dash не создает два разных графика одновременно.
#     Сначала запускается один график, после просмотра графика закрывается вкладка в браузере,
#     останавливается программа и тогда запускается второй.
# '''
# #----------------------------------------------------------------------------------------
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# df = pd.DataFrame({
#     "Слова": ["good", "awesome", "great", "cool", "fun", "like", "amazing", "interesting", "beautiful", "nice", "best", "perfect", "enjoy", "happy"],
#     "Частота": [6192, 493, 6470, 437, 2063, 6867, 580, 936, 599, 985, 2614, 875, 1800, 557]
# })
#
# fig = px.bar(df, x="Слова", y="Частота", height=900) #, barmode="group"
#
# app.layout = html.Div(children=[
#     html.H1(children='Графік №1 '),
#
#     html.Div(children='''
#         Кількість слів з позитивною тональністю
#     '''),
#
#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
#=========================================================================
#
# import dash
# from dash import dcc
# from dash import html
# import plotly.express as px
# import pandas as pd
#
# #---------------------------------------------------------------------------------------
# #
# # '''
# #     Модуль dash не создает два разных графика одновременно.
# #     Сначала запускается один график, после просмотра графика закрывается вкладка в браузере,
# #     останавливается программа и тогда запускается второй.
# # '''
# #----------------------------------------------------------------------------------------
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# df = pd.DataFrame({
#     "Статистика по месяцам": ["январь", "февраль", "март", "апрель", "май", "июнь", "июль",
#                   "август", "сентябрь", "октябрь", "ноябрь", "декабрь"],
#     "Среднемесячные показатели": [123, 154, 205, 142, 96, 193, 28, 215, 188, 107, 201, 133]
# })
#
# fig = px.bar(df, x="Статистика по месяцам", y="Среднемесячные показатели", height=500) #, barmode="group"
#
# app.layout = html.Div(children=[
#     html.H1(children='Графік №1 '),
#
#     html.Div(children='''
#         Таблица значений, выводимая в виде графа.
#     '''),
#
#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
#===================================================================
# import plotly
# import plotly.graph_objs as go
# import plotly.express as px
# from plotly.subplots import make_subplots
#
# import numpy as np
# import pandas as pd
#
#
#
#
# x = np.arange(0, 5, 0.1)
# def f(x):
#     return x**2
#
# # px.scatter(x=x, y=f(x)).show()
#
# fig = px.scatter(x=x, y=f(x))
# fig.show()
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd


#======== 1
# x = np.arange(-5, 10, 0.1)
# print(x, type(x))
#
# def f(x):
#     return x**2
#
# def h(x):
#     return np.sin(x)
#
# def k(x):
#     return np.cos(x)
#
# def m(x):
#     return np.tan(x)
#
# # fig = px.scatter(x=x, y=f(x))
# # fig.show()
#
# fig = go.Figure()
# fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
# fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='#008000')
#
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=h(x),  name='h(x)=sin(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=k(x),  name='k(x)=cos(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=m(x),  name='m(x)=tg(x)'))
#
#
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers', name='<b>функция</b> f(x)=x<sup>2</sup>'))  # Отделные графики
# fig.add_trace(go.Scatter(x=x, y=x, mode='lines+markers',
#                          name='<i>график</i> g(x)=x',
#               marker=dict(color='LightSkyBlue', size=10,
#               line=dict(color='MediumPurple', width=3))))     # Отделные графики
# fig.update_layout(legend_orientation="h", # легенду вниз
#                   margin=dict(l=40, r=40, t=40, b=40), # отступы по краям
#                   legend=dict(x=.45, xanchor="center"), # легенда сдвинута по центру
#                   hovermode="x", # сравнение двух графиков
#                   title="<b>График двух функций</b>",  # Заголовок графика
#                   xaxis_title="<i>Значения аргумента Х</i>", # Подпись оси Х
#                   yaxis_title="<i>Значения функции Y</i>", # Подпись оси Y
#                   )
# # fig.update_traces(hoverinfo="x+y") # подпись возле указателя мышки
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()
# # ===== Несколько графиков ========================================
#
# x = np.arange(-5, 10, 0.1)
# def f(x):
#     return x**2
#
# def h(x):
#     return np.sin(x)
#
# def k(x):
#     return np.cos(x)
#
# def m(x):
#     return np.tan(x)
#
# # fig = px.scatter(x=x, y=f(x))
# # fig.show()
#
# fig = go.Figure()
#
# fig = make_subplots(rows=1, cols=2) #  указатель разбивки экрана на окна
#
# fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='#008000', col=2)
#
#
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=h(x),  name='h(x)=sin(x)'), 1, 1)
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=k(x),  name='k(x)=cos(x)'), 1, 1)
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=m(x),  name='m(x)=tg(x)'), 1, 2)
#
#
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',
#                 name='<b>функция</b> f(x)=x<sup>2</sup>'), 1, 2)  # Отделные графики
# fig.add_trace(go.Scatter(x=x, y=x, mode='lines+markers',
#                          name='<i>график</i> g(x)=x',
#               marker=dict(color='LightSkyBlue', size=10,
#               line=dict(color='MediumPurple', width=3))), 1, 2)     # Отделные графики
# fig.update_layout(legend_orientation="h", # легенду вниз
#                   margin=dict(l=40, r=40, t=40, b=40), # отступы по краям
#                   legend=dict(x=.45, xanchor="center"), # легенда сдвинута по центру
#                   hovermode="x", # сравнение двух графиков
#                   title="<b>График двух функций</b>",  # Заголовок графика
#                   # xaxis_title="<i>Значения аргумента Х</i>", # Подпись оси Х
#                   # yaxis_title="<i>Значения функции Y</i>", # Подпись оси Y
#                   )
# fig.update_xaxes(title='Ось X графика 1', col=1, row=1) # Подписи к графикам по колонкам
# fig.update_xaxes(title='Ось X графика 2', col=2, row=1) # Подписи к графикам по колонкам
# fig.update_yaxes(title='Ось Y графика 1', col=1, row=1) # Подписи к графикам по колонкам
# fig.update_yaxes(title='Ось Y графика 2', col=2, row=1) # Подписи к графикам по колонкам
#
#
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()
#
# # ================== Графики разного размера ========================
x = np.arange(-2, 5, 0.1)
def f(x):
    return x**2

def h(x):
    return np.sin(x)

def k(x):
    return np.cos(x)

def m(x):
    return np.tan(x)


fig = make_subplots(rows=2, cols=2,
                    specs=[[{"colspan": 2}, None], [{}, {}]])


fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='#008000', col=2)

fig.add_trace(go.Scatter(x=x, y=h(x),  name='h(x)=sin(x)'), 2, 2)
fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'), 2, 2)
fig.add_trace(go.Scatter(x=x, y=m(x),  name='m(x)=tg(x)'), 1, 1)

fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 2, 1)
fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
                         marker=dict(color='LightSkyBlue', size=10,
                                     line=dict(color='MediumPurple', width=3))), 2, 1)
fig.update_layout(legend_orientation="h",
                  legend=dict(x=.5, xanchor="center"),
                  hovermode="x",
                  margin=dict(l=20, r=20, t=30, b=30),
                  height=1000,
                  width=1300,
                  title="<b>График нескольких функций</b>")  # Заголовок графика
fig.update_xaxes(title='Ось X графика 1', col=1, row=1) # Подписи к графикам по колонкам
fig.update_xaxes(title='Ось X графика 2', col=1, row=2) # Подписи к графикам по колонкам
fig.update_yaxes(title='Ось Y графика 1', col=1, row=1) # Подписи к графикам по колонкам
fig.update_yaxes(title='Ось Y графика 2', col=1, row=2)
fig.update_xaxes(title='Ось X графика 3', col=2, row=2) # Подписи к графикам по колонкам
fig.update_yaxes(title='Ось Y графика 3', col=2, row=2)
fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
fig.show()
# ======================================================
# ============= тепловая карта =========================
# ======================================================
# x = np.arange(-2, 5, 0.1)
#
#
# def f(x):
#     return x**2
#
# def h(x):
#     return np.sin(x)
#
# def k(x):
#     return np.cos(x)
#
# def m(x):
#     return np.tan(x)
#
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>',
#                          marker=dict(size=10, color=f(x), colorbar=dict(title="f(x)=x"))
#                         ))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=h(x),  name='h(x)=sin(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=k(x),  name='k(x)=cos(x)'))
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   margin=dict(l=30, r=30, t=30, b=30))
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()