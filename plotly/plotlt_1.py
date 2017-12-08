#--encoding=utf-8
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.offline as pltoff
import plotly.graph_objs as go
import pandas as pd
import numpy as np
def fun_1():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y})
    df.head()

    data = [
        go.Bar(
            x=df['x'],  # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    layout = go.Layout(title="bar charts",
                       xaxis={'title': 'x'}, yaxis={'title': 'value'})
    fig = go.Figure(data=data, layout=layout)
    pltoff.plot(fig, filename="bar_charts.html")
    py.plot(data, filename='pandas-bar-chart')
def bar_charts(name="bar_charts.html"):
    dataset = {'x':['man', 'woman'],
               'y1':[35, 26,30],
               'y2':[33, 30,35]}
    data_g = []
    tr_y1 = go.Bar(
        x = dataset['x'],
        y = dataset['y1'],
        name = '2016'

    )
    data_g.append(tr_y1)

    tr_y2 = go.Bar(
    x = dataset['x'],
    y = dataset['y2'],
    name = '2017'

    )
    data_g.append(tr_y2)
    layout = go.Layout(title="bar charts",
        xaxis={'title':'x'}, yaxis={'title':'value'})
    fig = go.Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)
bar_charts()
# fun_1()