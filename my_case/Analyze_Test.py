import pandas as pd
import matplotlib.pyplot as plt
from numpy import *

# 1.st : read a .xls file T18_TASK_FACT.xls
xls_file = pd.ExcelFile('G:\\Temp\\yw\\T18_TASK_FACT.xls')
df = pd.read_excel(xls_file, 'Sheet1', index_col='序号')
print(df['USETIME'].describe())
# last ： save file
# df.to_excel('G:\\Temp\\yw\\path_to_file.xlsx', sheet_name='Sheet1')
df['USETIME'].plot.hist()
# df['USETIME'].plot.density()
plt.show()