import pandas as pd

wb = pd.read_excel('E:\\student.xlsx')
temp = wb.iloc[:, [2, 3, 4]]

#按学生求和
wb['sum'] = temp.sum(axis=1)  #axis 0为列，1为行
#按学生求平均
wb['avg'] = temp.mean(axis=1)
print(wb)
print("=========================")
#算各科成绩平均
col_mean = wb.iloc[:, [2, 3, 4, 5, 6]].mean()
col_mean['name'] = "avg"
wb = wb.append(col_mean, ignore_index=True)
print(wb)

# wb.to_excel('E:\\student1.xlsx')
wb.to_excel('E:\\student1.xlsx', sheet_name='Sheet1', index=False, header=True)