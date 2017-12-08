##--encoding=utf-8
import pandas as pd
import numpy as  np
import plotly.plotly as py
import cufflinks as cf
import pandas as pd
class Exercise_1:
    def __init__(self):
        pass
    @classmethod
    def run(self):
        df_1=pd.DataFrame(data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})
        df_2=pd.DataFrame(data={'A':[11,12,13],'C':[14,15,16],'D':[17,18,19]})
        df_3=pd.concat([df_1,df_2],ignore_index=True)
        series = df_3['A'].value_counts()[:4]
        series.head(3)
        #
        # series.iplot(kind='bar', yTitle='Number of Complaints', title='NYC 311 Complaints',
        #              filename='categorical-bar-chart.html')
        series.iplot(kind='bar', yTitle='Number of Complaints', title='NYC 311 Complaints',
                     filename='-bar-chart.html')
if __name__ == '__main__':
    Exercise_1.run()