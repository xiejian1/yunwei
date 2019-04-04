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

    def getdata(self):
        """加载数据，并且返回数据"""
        df = pd.read_csv(self.datapath)
        logging.info("读取文件!")
        print("初步的显示数据,查看数据的特征值")
        display(df.head(n=2))
        print("\n")
        print("查看数据的缺失情况")
        print(df.info())
        print("\n")
        print("查看特征值是数值的一些基本统计值")
        print(df.describe())
        return df

    def addFeature(self):
        """根据以前的值，填充新的特征值"""
        df = self.getdata()
        #对数据进行copy,添加新特征PerPrice
        lianjia_df = df.copy()
        lianjia_df['PerPrice'] = df['Price']/df['Size']
        #重新摆放位置列
        column = ['Region','District','Garden','Layout','Floor','Year','Size','Elevator','Direction','Renovation','PerPrice','Price']
        df = pd.DataFrame(lianjia_df,columns = column)
        print("重新显示数据",df.head(n=2))
        return df

    def dataVisual(self):

        """Elevator"""
        """进行数据的可视化展示"""
        """统计各个区二手房子的数量"""
        df = self.addFeature()
        print("对数据进行可视化展示")
        misn = len(df.loc[df['Elevator'].isnull()])
        # misn = len(df.loc[(df['Elevator'].isnull()), 'Elevator'])
        print("打印数据缺失的部分",str(misn))
        #由于存在个别类型错误,如简装和精装，特征值错位，故需要移除
        df['Elevator'] = df.loc[(df['Elevator'] == '有电梯') | (df['Elevator'] == '无电梯'),'Elevator']
        df.loc[(df['Floor'] > 6) & (df['Elevator'].isnull()),'Elevator'] = '有电梯'
        df.loc[(df['Floor'] <= 6) & (df['Elevator'].isnull()),'Elevator'] = '无电梯'

        f,[ax1,ax2] = plt.subplots(1,2,figsize=(20,20))
        sns.countplot(df['Elevator'],ax=ax1)
        ax1.set_title('有无电梯数量对比',fontsize=15)
        ax1.set_xlabel('是否有电梯')
        ax1.set_ylabel('数量')
        sns.barplot(x='Elevator',y='Price',data=df,ax=ax2)
        ax2.set_title('有无电梯房价对比')
        ax2.set_xlabel('是否有电梯')
        ax2.set_ylabel('价格')
        plt.show()
        #对二手房区域分组对比二手房数量和每平方米房价

    def dataVisual01(self):
        """使用FacetGrid进行数据的可视化"""
        df = self.addFeature()
        print("根据独立的图形生成散点图")
        grid = sns.FacetGrid(df,row='Elevator',col='Renovation',palette='seismic',height=4)
        grid.map(plt.scatter,'Year','Price')
        grid.add_legend()

    def dataVisual02(self):
        """对二手房楼层进行数据分析"""
        df = self.addFeature()
        f,ax1 = plt.subplots(figsize=(20,5))
        sns.countplot(x='Floor',data=df,ax=ax1)
        ax1.set_title('房屋户型',fontsize=15)
        ax1.set_xlabel('数量')
        ax1.set_ylabel('户型')
        plt.show()



if __name__ =="__main__":
    lianjia = LianjiaData("lianjia.csv")
    print("开始进行数据可视化")
    #
    lianjia.dataVisual02()
    print("数据可视化结束")
