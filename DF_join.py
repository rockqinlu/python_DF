import pandas as pd

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print('-------------------------- begin -----------------------------------------')
result = left.join(right)
print(left)
print(right)
print(result)
print('-------------------------- how= outer -----------------------------------------')
result = left.join(right, how='outer')
print(result)
print('-------------------------- how= inner -----------------------------------------')
result = left.join(right, how='inner')
print(result)
