#--encoding=utf-8

import pandas as pd
import numpy as np

class Exercise_3:
    def __init__(self):
        pass
    @classmethod
    def run(cls,path1,path2):
        df_1=pd.read_csv(path1,sep=',',decimal=',',usecols=[0,1,2,3,4,5])
        df_2=pd.read_csv(path2,sep=',',decimal=',',usecols=[0,1,2,3,4,5])
        df_1=df_1.loc[~df_1['dongfour'].isnull()]
        df_2 = df_2.loc[~df_2['dongfour'].isnull()]
        # print df_1
        """
        df_3=df_1.merge(df_2, on=['hour','type'],how='left')  #进行左连接
        df_3['total']=df_3.groupby('type')['dongfour_x'].apply(lambda x : pd.Series(np.mean(x),index=x.index))
        print df_3
        """
        df_1.reset_index(drop=True, inplace=True)
        cols = [0, 1, 2, 3, 4, 5, 6,7]
        df_temp=pd.DataFrame(data=None,columns=['date','hour','type','dongfour','天坛','官园'],index=cols)
        df_temp['date']='20170101'
        print df_temp
        df_2.reset_index(drop=True, inplace=True)
        # df_3 =pd.concat([df_1,df_2],axis=0,ignore_index=True)
        df_3=df_temp.update(df_1)
        # print df_1
        print df_temp.fillna(df_1) #可以将df_temp的值替换成df_1 ,根据名称推测其是finalna
        print pd.merge(df_temp, df_1, left_index=True, right_index=True, how='left', on=['date','hour','type','dongfour','天坛','官园']) #只有on的才会出现一次
if __name__=='__main__':
    path1='D:\\PM2.5\\beijing_20170101-20171125\\beijing_all_20170101.csv'
    path2='D:\\PM2.5\\beijing_20170101-20171125\\beijing_all_20170102.csv'
    Exercise_3.run(path1,path2)