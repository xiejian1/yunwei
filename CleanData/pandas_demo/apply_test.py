import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grades_curve(exam_grades):
    """自定义函数，对dataframe的每一列进行操作，返回一个新的值"""
    return pd.qcut(exam_grades,[0,0.1,0.2,0.5,0.8,1],labels=['E','D','C','B','A'])

print('对整个dataframe应用apply函数')
df = grades_df.apply(convert_grades_curve)
print(df)