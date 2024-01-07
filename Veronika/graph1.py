import plotly
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd
import json



x = np.arange(-1, 1, 0.2)



def f(x):
    return 2*x + 5 - x**2


def h(x):
    return np.sin(x) * 3


def k(x):
    return np.cos(x) * 5


def m(x):
    return np.arctan(x)


fig = go.Figure()
# # Масштабирование
# fig.update_yaxes(range=[-0.5, 1.5])
# fig.update_xaxes(range=[-0.5, 1.5])
fig.update_yaxes(range=[-10.5, 12.5], zeroline=True, zerolinewidth=5, zerolinecolor='Red')
fig.update_xaxes(range=[-10.5, 12.5], zeroline=True, zerolinewidth=5, zerolinecolor='#00ff00') # RGB
# #
# # # Добавление графиков (нужно включить)
fig.add_trace(go.Scatter(visible='legendonly', x=x, y=h(x),  name='h(x)=sin(x)'))
fig.add_trace(go.Scatter(visible='legendonly', x=x, y=k(x),  name='k(x)=cos(x)'))
fig.add_trace(go.Scatter(visible='legendonly', x=x, y=m(x),  name='m(x)=tg(x)'))
# #
# #
fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'))
fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
                         marker=dict(color='Red', size=20, line=dict(color='MediumPurple', width=3))))

fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
fig.show()
