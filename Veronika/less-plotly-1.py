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
# # #
# # print(fig.to_dict()['data'])
# # #
# fig.show()

#==================================== Легенда и подписи осей
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=f(x), name='<b>f(x)=x<sup>2</sup></b>'))
# fig.add_trace(go.Scatter(x=x, y=x, name='<i>g(x)=x</i>'))
# # fig.update_layout(legend_orientation="h")
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   title="<b>Plot Title</b>",
#                   xaxis_title="<b>x Axis Title</b>",
#                   yaxis_title="<b><i>y Axis Title</i></b>",
#                   margin=dict(l=100, r=100, t=100, b=100))
# fig.show()
#============================ Маркеры и подписи к данным
#
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'))
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x'))
# fig.update_layout(legend_orientation="h",
#                   # hovermode="x",
#                   hovermode="x unified",
#                   legend=dict(x=.5, xanchor="center"),
#                   margin=dict(l=50, r=50, t=50, b=50))
# # fig.update_traces(hoverinfo="x+y")
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#============== Управление маркерами, масштаб фрагмента, добавление графиков
#
# fig = go.Figure()
# # # Масштабирование
# # fig.update_yaxes(range=[-0.5, 1.5])
# # fig.update_xaxes(range=[-0.5, 1.5])
# fig.update_yaxes(range=[-2.5, 2.5], zeroline=True, zerolinewidth=5, zerolinecolor='Red')
# fig.update_xaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=5, zerolinecolor='#00ff00') # RGB
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
#
# # fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"))
# fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"), column_widths=[3, 1])
# # #
# fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='#2980B9', col=2)
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightGreen', col=1)
# fig.update_xaxes(range=[-1, 1], zeroline=True, zerolinewidth=2, zerolinecolor='#F4D03F', col=1)
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
#                   # hovermode="x",
#                   hovermode="x unified",
#                   margin=dict(l=50, r=50, t=50, b=50))
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()


################ Veronika !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
