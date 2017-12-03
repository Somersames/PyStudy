#--encoding=utf-8
import xlwt
"""
若pycharm把py文件当成一个txt，有时候rename下就可以了
UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal return self._engine.get_value(s, k)这个错误解决办法目前是在csv
文件中将文件中文改成英文解决的
#读取指定的列
"""
import  pandas as pd

class Projecr_Run:
    def __init__(self):
        pass
    @classmethod
    def run(cls,path1,path2):
        df_20170101=pd.read_csv(path1,sep=',', decimal=',',usecols=[0,1,2,3,4,5,6])
        df_20170101=df_20170101.set_index('type')
        df_20170101['type']=df_20170101.index
        # print list(set(df_20170101.index))
        df_20170102=pd.read_csv(path2,sep=',', decimal=',',usecols=[0,1,2,3,4,5,6,7])
        df_20170102=df_20170102.set_index('type')
        print df_20170101
        # print df_20170102
        df_20170101=df_20170101.merge(df_20170102.loc[:,['type','aoti']],how='left',on='type')

        print df_20170101
        df_20170101=df_20170101.loc[~df_20170101['dongfour'].isnull()]
        print df_20170101
        df_20170101_gr=df_20170101.groupby('hour')
        # df_20170101_gr1=df_20170101['hour'].groupby.num()
        print  df_20170101_gr['dongfour'].sum()
        index=0
        # for k in  range(0,len(df_20170101_gr)):
        #     index+=1
        # df_20170101['new_col'] = df_20170101_gr['dongfour'].apply(lambda x :pd.Series(data=x.sum(),index=x.index))
        df_20170101['new_col'] = df_20170101_gr['dongfour'].apply(lambda x :pd.Series(data=x.sum(),index=x.index))
        # print df_20170101_gr.first()
        print df_20170101
        for k in df_20170101_gr.__iter__():
            print k
        # # print df_20170101['dongfour']
        # # df_20170101=df_20170101.drop(df_20170101.columns[[0,1,3]],axis=1)
        # df_gr=df_20170101.groupby('type')
        # print df_gr
        # print  df_20170101
if __name__ == '__main__':
    Projecr_Run.run('D:\\PM2.5\\beijing_20170101-20171125\\beijing_all_20170101.csv','D:\\PM2.5\\beijing_20170101-20171125\\beijing_all_20170102.csv')
