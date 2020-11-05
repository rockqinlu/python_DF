import pandas as pd
import numpy as np

index = pd.date_range('1/1/2020', periods=8)
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame(np.random.randn(8, 3), index=index,columns=['A', 'B', 'C'])
print('--------------------------------------------------------------')
print(df)
print('-----------------------预览 头部 和 尾部，默认5---------------------------------------')
long_series = pd.Series(np.random.randn(1000))
print('----------------------------头部----------------------------------')
print(long_series.head())
print('----------------------------尾部----------------------------------')
print(long_series.tail())
print('--------------------------------------------------------------')
print(df[:2])
df.columns = [x.lower() for x in df.columns]
print('--------------------------------------------------------------')
print(df)