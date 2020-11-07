import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])
frames = [df1, df2, df3]

result = pd.concat(frames)
result2 = pd.concat(frames, keys=['x', 'y', 'z'])
result3 = pd.concat([df1, df4], axis=1)
result4 = pd.concat([df1, df4], axis=1, join='inner')
result5 = df1.append(df3)
result6 = df1.append(df4)
result7 = df1.append(df4, ignore_index=True)
print('----------------- Begin def--------------------')
print(result)
print('----------------- + keys --------------------')
print(result2)
print('----------------- use keys --------------------')
print(result2.loc['y'])
print('----------------- + join : def --------------------')
print(result3)
print('----------------- join= ''inner'' --------------------')
print(result4)
print('----------------- .append() --------------------')
print(result5)
print(result6)
print(result7)
print(result7.iloc[2])