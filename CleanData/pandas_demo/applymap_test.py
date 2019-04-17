import pandas as pd

class ApplyMapTest():
    """Dataframe测试"""
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })


    def add_one(x):
        return x + 1

    def shuchu(self):
        """打印测试的结果"""
        df = self.df.applymap(self.add_one)
        print("打印相加之后的值",df)

class GradesTest():
    """对成绩进行等级的转换"""
    grades_df = pd.DataFrame(
        data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
              'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
        index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
               'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
    )

    def convert_to_letter(self,score):

        if (score >= 90):
            return 'A'
        elif (score >= 80):
            return 'B'
        elif (score >= 70):
            return 'C'
        elif (score >= 60):
            return 'D'
        else:
            return 'F'

    def convert_grades(self,grades):
        return grades.applymap(self.convert_to_letter)



if __name__ =="__main__":
    # applymap = ApplyMapTest()
    # applymap.shuchu()
    grade = GradesTest()
    df = grade.convert_grades(grade.grades_df)
    print("打印成绩等级",df)