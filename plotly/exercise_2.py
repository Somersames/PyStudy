import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
def fun_1():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
    trace = go.Table(
        header=dict(values=df.columns,
                    fill = dict(color='#C2D4FF'),
                    align = ['left'] * 5),
        cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
                   fill = dict(color='#F5F8FF'),
                   align = ['left'] * 5))

    data = [trace]
    py.iplot(data, filename = 'pandas_table.html')
fun_1()