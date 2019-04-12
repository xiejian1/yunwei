
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



if __name__ =="__main__":
    print("开始加载数据")
    dataHandle = DataHandle('lianjia.csv')
    # dataHandle.featureProject()
    # dataHandle.selectData()
    dataHandle.deleteData()
    print("处理数据结束")

