#--encoding=utf-8
# import pandas as pd
# import numpy as  np
# # import plotly.plotly as py
# import cufflinks as cf
# import plotly.offline as pltoff
# import plotly.graph_objs as go
# import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.offline as pltoff
import plotly.graph_objs as go
import pandas as pd
import numpy as np
def fun_1(name='bar_charts.html'):
    df_1 = pd.DataFrame(data={'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df_2 = pd.DataFrame(data={'A': [11, 12, 13], 'C': [14, 15, 16], 'D': [17, 18, 19]})
    df_3 = pd.concat([df_1, df_2], ignore_index=True)
    # ase=go.Scatter(
    #     x=df_3['A'],
    #     y=df_3['C'],
    #     mode='markers',
    #     marker=dict(
    #         color=df_3['A'],
    #         size= 5,
    #         colorscale= 'Viridis',
    #         showscale= True
    #     )
    # )
    ase=go.Bar(

    )
    print ase
    pltoff.plot([ase],filename=name)
    # df = pd.read_csv('E:\MySelf_2\\file_5\\userSubjectInfo.csv')
    # print df_1
    # data = [go.Scatter(x=df['userId'], y=df['userNum'])]
    # layout = go.Layout(
    #     title='<b>Monthly Transactions</b>',
    #     xaxis=dict(title='userId'),
    #     yaxis=dict(title='userNum')
    # )
    # fig = go.Figure(data=data, layout=layout)
    # py.iplot(fig, filename='InteractiveGraph_2')
fun_1()