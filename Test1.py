import pandas as pd
import numpy as np

# 1: build
s = pd.Series([1, 3, 5, np.nan, 6, 8])  #S1 基本
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])  #S2 指定索引
s3 = s1[[1,3,5]] #S3 指定索引
s4 = s1[:7]
s5 = s1[4:]
s6 = s1[s1 > s1.median()]
s7 =pd.Series(np.random.randn(5))
s8 = pd.Series(np.arange(10))
print('-------------------------------------')
print(s1)
print('-------------------------------------')
print(s7)
print('-------------------------------------')
print(s7+s1)
print('-------------------------------------')
print(s7*2)
print('-------------------------------------')
dates = pd.date_range('20130101', periods=6)
print(dates)
print('-------------------------------------')
print(s8)
div, rem = divmod(s8, 3)
print(div)
print(rem)