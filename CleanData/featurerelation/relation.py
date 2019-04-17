
import os
import pandas as pd
import logging
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Relationship():

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

    def relation(self):
        """"数据的相关性"""
        df = self.addFeature()
        colormap = plt.cm.RdBu
        plt.figure(figsize=(20, 20))
        # plt.title('Pearson Correlation of Features', y=1.05, size=15)
        sns.heatmap(df.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
        plt.show()


if __name__ == "__main__":
    relationship = Relationship('lianjia.csv')
    print("打印数据之间的相关性")
    relationship.relation()