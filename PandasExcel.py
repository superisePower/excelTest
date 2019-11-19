import pandas as pd
import numpy as np

# pandas操作Excel的行列 == https://www.cnblogs.com/liulinghua90/p/9935642.html
# Pandas 操作多个列进行运算，并生成新列的方法 == https://blog.csdn.net/weixin_42493346/article/details/80744159


filePath = 'E:\\HRP1908.xls'
wb = pd.read_excel(filePath, sheet_name=0)  # 可以通过表单索引来指定读取的表单
data = wb.head()  # 读取前五行
# data = wb.values #读取所有


# 指定区间均匀分布的数值创建数组
arr = np.arange(7, 42, 1, int)

data = wb.iloc[:, arr].values   #读所有行的区间列的值，这里需要嵌套列表


expression = ''
for i in arr:
    expression += '+'
    expression += str(i)
wb.eval('sum = '+expression, inplace=True)

print(format(data))

