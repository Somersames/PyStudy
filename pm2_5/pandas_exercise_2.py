#--encoding=utf-8

import pandas as pd
import numpy as np
class Exercise2:
    def __init__(self):
        pass
    @classmethod
    def run(cls,path):
        df_20170101 =pd.read_csv(path,sep=',',decimal=',',usecols=[0,1,2,3,4,5,6,7,8,9])
        print df_20170101
        df_20170101=df_20170101.loc[~df_20170101['dongfour'].isnull()]
        print df_20170101
        print df_20170101.index
        # df_20170101['mean']=df_20170101.groupby('type').apply(lambda x : pd.Series(data=np.mean(x['dongfour']),index=x.index))
        df_20170101['mean']=df_20170101.groupby('type')['dongfour'].apply(lambda x : pd.Series(data=np.mean(x),index=x.index))
        # df_20170101['mean']=df_20170101.groupby('type').apply(lambda x : pd.Series(data=x.sum()))
        print df_20170101
        df_20170101['avg']=0
        df_20170101=df_20170101.T
        print df_20170101
        print df_20170101.ix[3:9]
        list1=list(df_20170101.ix[3:9][0])
        # df_20170101 = df_20170101.reset_index(drop=True)
        # print df_20170101.index
        df_20170101.loc['avg'][0]=np.mean(list1)
        print df_20170101.T
        print df_20170101.groupby('type').apply(lambda x : x.sum(axis=1))
        # df_20170101['mean']=df_20170101.groupby('type').apply(lambda x : x.sum(axis=1))
        print df_20170101
if __name__ =='__main__':
    Exercise2.run('D:\\PM2.5\\beijing_20170101-20171125\\beijing_all_20170101.csv')