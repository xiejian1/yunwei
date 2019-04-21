import numpy as np

employment = np.array([
 55.70000076,  51.40000153,  50.5       ,  75.69999695,
 58.40000153,  40.09999847,  61.5       ,  57.09999847,
 60.90000153,  66.59999847,  60.40000153,  68.09999847,
 66.90000153,  53.40000153,  48.59999847,  56.79999924,
 71.59999847,  58.40000153,  70.40000153,  41.20000076
])

mean = employment.mean()         #计算平均数
deviation = employment.std()     #计算标准差
# 标准化数据的公式: (数据值 - 平均数) / 标准差
standardized_employment = (employment - mean) / deviation
print ("得到标准化的数据",standardized_employment)