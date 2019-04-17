

import  pandas as pd
import numpy as np
class AxisTest():
    """对pandas的坐标轴进行相应的统计"""
    ridership_df = pd.DataFrame(
        data=[[0, 0, 2, 5, 0],
              [1478, 3877, 3674, 2328, 2539],
              [1613, 4088, 3991, 6461, 2691],
              [1560, 3392, 3826, 4787, 2613],
              [1608, 4802, 3932, 4477, 2705],
              [1576, 3933, 3909, 4979, 2685],
              [95, 229, 255, 496, 201],
              [2, 0, 1, 27, 0],
              [1438, 3785, 3589, 4174, 2215],
              [1342, 4043, 4009, 4665, 3033]],
        index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
               '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
        columns=['R003', 'R004', 'R005', 'R006', 'R007']
    )

    def everyday_station(self):
        """计算每天各站的平均客流"""
        df = self.ridership_df.mean(axis=1)
        print("打印每天各站的平均客流")
        print(df[:6])

    def station_everyday(self):
        """计算每个站台各天的平均气流"""
        df = self.ridership_df.mean(axis=0)
        print("打印各站台各天的平均气流")
        print(df[:6])

class NumpyTest():
    """对numpy进行简单的求和操作"""
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    def allsum(self):
        """对所有的进行求和"""
        print("进行求和",self.a.sum())
    def indexsum(self):
        """对行进行求和"""
        print(self.a.sum(axis=0))

    def columnssum(self):
        """对列进行求和"""
        print(self.a.sum(axis=1))


if __name__ =="__main__":
    # axistest = AxisTest()
    # axistest.everyday_station()
    numpyTest = NumpyTest()
    numpyTest.indexsum()