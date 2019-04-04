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
        """Region"""
        """进行数据的可视化展示,统计每个区二手房每平米的价格"""
        """统计各个区二手房子的数量"""
        df = self.addFeature()
        logging.info("对数据进行可视化展示")
        #对二手房区域分组对比二手房数量和每平方米房价
        df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
        print("打印分组之后的值")
        print(df_house_count)
        df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

        f,[ax1,ax2,ax3] = plt.subplots(3,1,figsize=(40,15))
        sns.barplot(x='Region',y='PerPrice',palette='Blues_d',data=df_house_mean,ax=ax1)
        ax1.set_title('北京各大区二手房每平方米单价对比',fontsize=15)
        ax1.set_xlabel('区域')
        ax1.set_ylabel('每平米单价')

        sns.barplot(x='Region',y='Price',palette='Greens_d',data=df_house_count,ax=ax2)
        ax2.set_title('北京各大区二手房数量对比',fontsize=15)
        ax2.set_xlabel('区域')
        ax2.set_ylabel('数量')

        sns.boxplot(x='Region',y='Price',data=df,ax=ax3)
        ax3.set_title('北京各大区二手房房屋总价',fontsize=15)
        ax3.set_xlabel('区域')
        ax3.set_ylabel('房屋总价')

        plt.show()

    def datavisual01(self):
        """特征值Size分析"""
        print("对Size特征进行分析")
        df = self.addFeature()
        print("去除掉错误的数据")
        df = df[(df['Layout'] != '叠拼别墅') & ( df['Size'] < 1000)]
        # data = df.loc[df['Size']<10]
        # print("打印房屋大小小于10平米")
        # print(data)
        # error_data = df.loc[df['Size']>1000]
        # print("打印错误的数据")
        # print(error_data)

        f,[ax1,ax2] = plt.subplots(1,2,figsize=(20,10))
        #建房时间的分布情况
        sns.distplot(df['Size'],bins=20,ax=ax1,color='r')
        sns.kdeplot(df['Size'],shade=True,ax=ax1)
        #建房时间和出售价格的关系
        sns.regplot(x='Size',y='Price',data=df,ax=ax2)
        plt.show()

    def datavisual02(self):
        """Layout特征分析"""
        df = self.addFeature()
        f,ax1 = plt.subplots(figsize=(20,20))
        sns.countplot(y='Layout',data=df,ax=ax1)
        ax1.set_title('房屋户型',fontsize=15)
        ax1.set_xlabel('数量')
        ax1.set_ylabel('户型')
        plt.show()

    def datavisual03(self):
        """对数据的装修方式进行特征分析"""
        df = self.addFeature()
        print("打印原始数据")
        print(df['Renovation'].value_counts())
        #去除掉一些脏的数据
        df['Renovation'] = df.loc[(df['Renovation'] != '南北'),'Renovation']

        #图画设置
        f,[ax1,ax2,ax3] = plt.subplots(3,1,figsize=(20,20))
        sns.countplot(df['Renovation'],ax=ax1)
        sns.barplot(x='Renovation',y='Price',data=df,ax=ax2)
        sns.boxplot(x='Renovation',y='Price',data=df,ax=ax3)
        plt.show()
if __name__ =="__main__":
    lianjia = LianjiaData("lianjia.csv")
    print("开始进行数据可视化")
    #
    lianjia.datavisual03()
    print("数据可视化结束")
