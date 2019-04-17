
import os
import pandas as pd
import logging
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class LianjiaData():

    def __init__(self,filepath):
        self.datapath = os.path.join(BASE_DIR,"datafiles\\"+filepath)

    def addFeature(self):
        """根据以前的值，填充新的特征值"""
        df = pd.read_csv(self.datapath)
        #对数据进行copy,添加新特征PerPrice
        lianjia_df = df.copy()
        lianjia_df['PerPrice'] = df['Price']/df['Size']
        #重新摆放位置列
        column = ['Region','District','Garden','Layout','Floor','Year','Size','Elevator','Direction','Renovation','PerPrice','Price']
        df = pd.DataFrame(lianjia_df,columns = column)
        print("重新显示数据",df.head(n=2))
        return df

    #对布局进行原始数据的查看
    def LayoutData(self):
        df =self.addFeature()
        data = df['Layout'].value_counts()
        print("打印各布局的数量",data[:6])

    def gainData(self):
        # 只考虑“室”和“厅”，将其它少数“房间”和“卫”移除
        df = self.addFeature()
        df = df.loc[df['Layout'].str.extract('^\d(.*?)\d.*?') == '室']
        print("打印移除之后的新数据",df[:6])

    def createFeature(self):
        """提取“室”和“厅”创建新特征"""
        df = self.addFeature()
        # data = df['Layout']
        # print("打印数据为空的数据",data)
        # df = df[df['Layout'] != 'nan']
        df = df.loc[(df['Layout'].str.extract('^\d(.*?)\d.*?') == '室')[0]]
        df['Layout_room_num'] = df['Layout'].str.extract('(^\d).*', expand=False).astype('int64')
        df['Layout_hall_num'] = df['Layout'].str.extract('^\d.*?(\d).*', expand=False).astype('int64')
        #
        print("打印新生成的数据",df['Layout_room_num'][:6])

    def discretYear(self):
        """离散化做分箱处理"""
        df = self.addFeature()
        df['Year'] = pd.qcut(df['Year'],8).astype('object')
        print("打印时间年限",df['Year'][:6])

    def cleanDirection(self):
        """对朝向的数据进行清洗"""
        df =self.addFeature()
        d_list_one = ['东', '西', '南', '北']
        d_list_two = ['东西', '东南', '东北', '西南', '西北', '南北']
        d_list_three = ['东西南', '东西北', '东南北', '西南北']
        d_list_four = ['东西南北']

if __name__ =="__main__":
    meta = LianjiaData('lianjia.csv')
    print("打入数据")
    meta.discretYear()
    print("打印数据结束")
