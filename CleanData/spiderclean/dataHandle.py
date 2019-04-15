
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DataHandle():
    """数据的处理与清洗"""

    def __init__(self,filepath):
        self.file_path = os.path.join(BASE_DIR,'datafiles\\'+filepath)

    def featureProject(self):
        """特征工程"""
        print("数据的加载")
        df = pd.read_csv(self.file_path)
        print("数据加载完成，打印一下初始的数据")
        print(df.head(n=2))

        return df

    def cleanData(self):
        """对数据进行清洗"""
        df = self.featureProject()
        #移除结构类型异常值和房屋大小异常
        #条件判断，对数据进行选择
        df = df[(df['Layout'] != '叠拼别墅') & (df['Size'] < 1000)]
        print("打印一下过滤后的数据")
        print(df.head(n=2))

    def selectData(self):
        """对数据进行选择"""
        df = self.featureProject()
        print("对数据进行选择")
        df['Renovation'] = df.loc[(df['Renovation'] != '南北'),'Renovation']
        print('打印帅选的数据')
        print(df['Renovation'])

    def deleteData(self):
        """对数据进行删除"""
        df = self.featureProject()
        #移除一些错误的数据
        df['Elevator'] = df.loc[(df['Elevator'] == '有电梯')|(df['Elevator'] == '无电梯'),'Elevator']
        print('打印删除脏数据之后的数据')
        print(df['Elevator'][:11])

    def fillData(self):
        """数据的填充，对缺失的值进行补充"""
        df = self.featureProject()
        df.loc[(df['Floor']>6)&(df['Elevator'].isnull()),'Elevator'] = '有电梯'
        df.loc[(df['Floor']<=6)&(df['Elevator'].isnull()),'Elevator'] = '无电梯'

    def findData(self):
        """只考虑室和厅的数据，得到新的dataframe数据结构"""
        df = self.featureProject()
        #只考虑“室和厅”，将其他少数“房间”和“卫”移除
        df = df.loc[df['Layout'].str.extract('^\d(.*?)\d.*?') == '室']
        print("打印获得的值",df)

    def getData(self):
        """提取数值，创建新的特征"""
        df = self.featureProject()
        #提取“室”和“厅”创建新的特征
        df['Layout_room_num'] = df['Layout'].str.extract('(^\d).*',expand=False).astype('int64')
        df['Layout_hall_num'] = df['Layout'].str.extract('^\d .*?(\d).*',expand=False).astype('int64')

    def splitData(self):
        """按中位数对year特征进行分析"""
        df = self.featureProject()
        #按中位数对“Year”特征进行分箱
        df['Year'] = pd.qcut(df['Year'],8).astype('object')
        print("打印获取的值",df['Year'])
    def defineData(self):
        """Direction进行重新定义"""
        df = self.featureProject()
        d_list_one  = ['东','西','南','北']
        d_list_two = ['东西','东南','东北','西南','西北','南北']
        d_list_three = ['东西南','东西北','东南北','西南北']
        d_list_four = ['东西南北']

        df['Direction'] = df.loc[(df['Direction']!='no')&(df['Direction']!='nan')]

    def createData(self):
        """创建新的特征"""
        df = self.featureProject()
        df['Layout_total_num'] = df['Layout_room_num'] + df['Layout_hall_num']
        df['Size_room_ration'] = df['Size']/df['Layout_total_num']

    def dropData(self):
        """删除无用的特征"""
        df = self.featureProject()
        df = df.drop(['Layout','PerPrice','Garden'],axis=1)
    def encodeData(self):
        """对于object特征进行编码"""
        df = self.featureProject()
        # df,df_cat = one_hot_encoder(df)

if __name__ =="__main__":
    print("开始加载数据")
    dataHandle = DataHandle('lianjia.csv')
    # dataHandle.featureProject()
    # dataHandle.selectData()
    dataHandle.splitData()
    print("处理数据结束")

